from time import time
from typing import Optional

import numpy as np
from numpy.typing import ArrayLike, NDArray
from numba import get_num_threads
from scipy.optimize import minimize

from mumott.output_handling.live_view_handler import LiveViewHandler
from .optimization_parameters import OptimizationParameters
from .optimization_timer import OptimizationTimer
from .regularizer import Regularizer


class Optimizer:
    """
    Wrapper class for executing optimization.

    Parameters
    ----------
    optimization_parameters : OptimizationParameters
        Instance of an :class:`OptimizationParameters <mumott.optimization_parameters.OptimizationParameters>`
        object, containing most of the parameters related to the reconstruction.
    regularizer : Regularizer
        An instance of a :class:`Regularizer <mumott.regularizer.Regularizer>` object, containing parameters
        related to regularization of the optimization.
    optimization_timer: OptimizationTimer, optional
        An instance of an :class:`OptimizationTimer <mumott.optimization_timer.OptimizationTimer` object,
        timing the reconstruction.
    live_view_handler: LiveViewHandler, optional
        An instance of a :class:`LiveViewHandler <mumott.live_view_handler.LiveViewHandler` object,
        which visualizes the reconstruction.
    """
    def __init__(self,
                 optimization_parameters: OptimizationParameters,
                 regularizer: Regularizer = None,
                 optimization_timer: Optional[OptimizationTimer] = None,
                 live_view_handler: Optional[LiveViewHandler] = None):
        print('Initializing optimizer...')

        self._optimization_parameters = optimization_parameters
        self._reconstruction_parameters = optimization_parameters.reconstruction_parameters

        self._recon_in = self._reconstruction_parameters.reconstruction_input
        self._recon_out = self._reconstruction_parameters.reconstruction_output
        self._proj_params = self._reconstruction_parameters.projection_parameters
        self._sph_params = self._reconstruction_parameters.spherical_harmonic_parameters
        self._regularizer = regularizer
        if optimization_timer is None:
            optimization_timer = OptimizationTimer(optimization_parameters.reconstruction_parameters,
                                                   regularizer)
        self._optimization_timer = optimization_timer
        self._live_view_handler = live_view_handler

        self._new_iteration = True
        self._calculated_objective_function = False
        self._old_coefficients = None

    def run_optimization(self):
        """ Method which executes the optimization.
        """
        # Copy so that cached functions from previous instances of ``Optimizer`` are not used.
        self._minimize_args = self._optimization_parameters.minimize_args.copy()
        self._minimize_options = self._optimization_parameters.minimize_options.copy()
        if 'fun' not in self._minimize_args.keys():
            self._minimize_args['fun'] = self._objective_function
        if 'jac' not in self._minimize_args.keys():
            self._minimize_args['jac'] = self._jacobian
        if 'callback' not in self._minimize_args.keys():
            self._minimize_args['callback'] = self._callback
        print('Running optimization...')
        self._difference = np.zeros_like(self._recon_out.reconstruction_projection)
        self._gradient_field = np.zeros_like(self._recon_in.optimization_coefficients)
        self._wall_time = None
        self._total_wall_time = None
        self._result = minimize(**self._minimize_args,
                                options=self._minimize_options)
        self._recon_in.optimization_coefficients = self._result.x

    def _project_stack(self, tensor_field: NDArray):
        start_time = time()
        accum = 0.
        input_field = tensor_field.reshape(tuple(self._proj_params.volume_shape) + (-1,))
        for i in range(self._proj_params.number_of_projections):
            start, stop = self._proj_params.cumulative_projection_size[i:i+2]
            shape = self._proj_params.data_shape[i]
            field_matrix = self._sph_params.spherical_harmonic_factors[i]
            temp_frame = np.zeros(tuple(shape[:-1]) + (input_field.shape[-1],), dtype=np.float64)
            last = time()
            self._proj_params.project(input_field, i, temp_frame, get_num_threads())
            np.einsum('ijk, lk->ijl', temp_frame, field_matrix,
                      out=self._recon_out.reconstruction_projection[start:stop].reshape(shape),
                      order='C',
                      optimize='greedy')
            accum += time() - last
        print(f'End time forward: {time() - start_time:.2f}')
        print(f'Total projection time forward: {accum:.2f}')

    def _project_stack_adjoint(self, gradient_field: NDArray):
        start_time = time()
        accum = 0.
        temp_volume = np.zeros((get_num_threads(),) + gradient_field.shape, dtype=np.float64)
        temp_volume = temp_volume.reshape((get_num_threads(),) +
                                          tuple(self._proj_params.volume_shape) + (-1,))
        for i in range(self._proj_params.number_of_projections):
            start, stop = self._proj_params.cumulative_projection_size[i:i+2]
            shape = self._proj_params.data_shape[i]
            field_matrix = self._sph_params.spherical_harmonic_factors[i]
            temp_frame = np.einsum('ijl, lk->ijk',
                                   self._difference[start:stop].reshape(shape),
                                   field_matrix,
                                   order='C',
                                   optimize='greedy')
            last = time()
            self._proj_params.adjoint(temp_frame, i, temp_volume, get_num_threads())
            accum += time() - last
        np.einsum('i...->...', temp_volume.reshape(-1, gradient_field.size),
                  out=gradient_field, order='C', optimize='greedy')
        print(f'End time adjoint: {time() - start_time:.2f}')
        print(f'Total projection time adjoint: {accum:.2f}')

    def _objective_function(self,
                            new_coefficients: ArrayLike):
        if self._wall_time is None:
            self._wall_time = time()
            self._total_wall_time = 0
        else:
            print(f'Iteration wall time: {time() - self._wall_time:.2f}')
            self._total_wall_time += time() - self._wall_time
            print(f'Total wall time: {self._total_wall_time:.2f}')
            self._wall_time = time()
        if self._live_view_handler is not None:
            print('Updating plot...')
            self._recon_in.optimization_coefficients = new_coefficients
            self._live_view_handler.update_plots()
        print('Calculating residual...')
        self._project_stack(new_coefficients)
        np.subtract(self._recon_out.reconstruction_projection,
                    self._reconstruction_parameters.data,
                    out=self._difference)
        self._recon_out.residual = np.reciprocal(np.float64(self._difference.size)) * \
            np.einsum('i, i, i', self._difference,
                      self._difference,
                      self._reconstruction_parameters.projection_weights,
                      order='C',
                      optimize='greedy')
        objective_function = self._recon_out.residual
        print(f'Residual norm: {self._recon_out.residual:.4e}')
        if self._regularizer is not None:
            print('Regularizing...')
            S = self._recon_in.optimization_coefficients.view()
            S = S.reshape(self._proj_params.number_of_voxels, -1)
            reg_norm, elist = self._regularizer.apply_regularization(S=S, get_gradient=False)
            print('Regularization norm:', [f'{e:.4e}' for e in elist])
            objective_function += reg_norm
        return objective_function

    def _jacobian(self,
                  new_coefficients: ArrayLike):
        np.einsum('..., ...', self._difference,
                  self._reconstruction_parameters.projection_weights,
                  out=self._difference, casting='same_kind')
        self._project_stack_adjoint(self._gradient_field)
        self._gradient_field *= np.reciprocal(np.float64(self._difference.size))
        gradient = self._gradient_field.ravel()
        print(f'Gradient norm: {abs(gradient).max():.4e}')
        if self._regularizer is not None:
            S = new_coefficients[...]
            S = S.reshape(self._proj_params.number_of_voxels, -1)
            reg_norm, elist, reg_grad, glist = self._regularizer.apply_regularization(S=S, get_gradient=True)
            gradient += reg_grad.ravel()
            print('Regularization gradients:', [f'{g:.4e}' for g in glist])
        return gradient

    def _callback(self, *args):
        self._new_iteration = True
