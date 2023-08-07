from typing import Any, Dict, List, Tuple

import numpy as np

from mumott.data_handling.reconstruction_parameters import ReconstructionParameters


class OptimizationParameters:
    """This class defines how the optimization is carried out.

    Parameters
    ----------
    reconstruction_parameters
        The :class:`ReconstructionParameters
        <mumott.reconstruction_parameters.ReconstructionParameters>` instance for
        the optimization.
    integration_step_size
        The size of each step for the projection-backprojection integrals, in units
        of pixel size.
    maximum_order
        The maximum spherical harmonic order. Should be an even integer.
    initial_value
        The base initial value for each coefficient. Scaled down for higher-order coefficients.
    optimization_bounds_isotropic
        The bounds for the isotropic components of the spherical polynomials. Lower bound
        should generally be ``0``.
    optimization_bounds_anisotropic
        The bounds for the anisotropic components of the spherical polynomials. Generally,
        lower bounds should be the negative of the upper bounds.
    minimize_args
        Arguments to give to the optimizer. See :func:`scipy.optimize.minimize` for details.
    minimize_options
        Options to give to the optimizer. See :func:`scipy.optimize.minimize` for details.
    """
    def __init__(self,
                 reconstruction_parameters: ReconstructionParameters,
                 integration_step_size: float = 1. / 3.,
                 maximum_order: int = 0,
                 initial_value: float = 0.0,
                 optimization_bounds_isotropic: Tuple[float, float] = (0, np.inf),
                 optimization_bounds_anisotropic: Tuple[float, float] = (-np.inf, np.inf),
                 minimize_args: Dict[str, Any] = dict(method='L-BFGS-B'),
                 minimize_options: Dict[str, Any] = dict(maxiter=100,
                                                         maxfun=500,
                                                         ftol=1e-3,
                                                         gtol=1e-5,
                                                         disp=1,
                                                         maxls=10,
                                                         maxcor=30)):
        self._integration_step_size = integration_step_size
        self._maximum_order = maximum_order
        self._initial_value = initial_value
        self._rng = np.random.default_rng()
        self._optimization_bounds_isotropic = optimization_bounds_isotropic
        self._optimization_bounds_anisotropic = optimization_bounds_anisotropic
        self._reconstruction_parameters = reconstruction_parameters
        self._minimize_args = minimize_args
        self._minimize_options = minimize_options
        self._initialize_structures()
        self._initialize_minimize_args()

    def _initialize_minimize_args(self):
        default_args = dict(method='L-BFGS-B',
                            x0=self._reconstruction_parameters.reconstruction_input.optimization_coefficients,
                            bounds=self._bounds)
        for key, value in default_args.items():
            if key not in self._minimize_args:
                self._minimize_args[key] = value
        default_options = dict(maxiter=100,
                               maxfun=500,
                               ftol=1e-3,
                               gtol=1e-5,
                               disp=1,
                               maxls=10,
                               maxcor=30)
        for key, value in default_options.items():
            if key not in self._minimize_options:
                self._minimize_options[key] = value

    def _initialize_structures(self,
                               reset_coefficients: bool = True):
        self._reconstruction_parameters.projection_parameters.integration_step_size = \
            self._integration_step_size
        coeffs = (self._maximum_order + 1) * (self._maximum_order // 2 + 1)
        a = np.zeros((self._reconstruction_parameters.projection_parameters.number_of_voxels, coeffs)).astype(np.float64)  # noqa
        self._reconstruction_parameters.increase_maximum_order(self._maximum_order)
        if reset_coefficients:
            a[:, :] = (self._rng.uniform(self._initial_value / 2, self._initial_value, a.shape) /
                       (2 * self._reconstruction_parameters.spherical_harmonic_parameters.l_indices.reshape(1, -1) + 1) ** 2)  # noqa
        else:
            a[:, :self._reconstruction_parameters.spherical_harmonic_parameters.number_of_coefficients] = \
                self._reconstruction_parameters.reconstruction_input.optimization_coefficients
        self._reconstruction_parameters.reconstruction_input.optimization_coefficients = a.flatten()
        bounds = [self._optimization_bounds_anisotropic for i in range(coeffs)]
        bounds[0] = self._optimization_bounds_isotropic
        self._bounds = [b for n in range(
                        self._reconstruction_parameters.projection_parameters.number_of_voxels)
                        for b in bounds]

    def reinitialize_parameters(self,
                                reset_coefficients: bool = True):
        """ Reinitializes parameters. If :attr:`reset_coefficients` is ``True``,
        the coefficients will be reset to the initial value.
        """
        self._initialize_structures(reset_coefficients=reset_coefficients)
        self._minimize_args['x0'] = \
            self._reconstruction_parameters.reconstruction_input.optimization_coefficients

    @property
    def reconstruction_parameters(self) -> ReconstructionParameters:
        return self._reconstruction_parameters

    @property
    def iterations(self) -> int:
        return self.minimize_options['maxiter']

    @iterations.setter
    def iterations(self, new_iterations: int):
        self._minimize_options['maxiter'] = new_iterations

    @property
    def bounds(self) -> List[Tuple[float, float]]:
        return self._bounds

    @property
    def minimize_args(self) -> Dict[str, Any]:
        return self._minimize_args

    @property
    def minimize_options(self) -> Dict[str, Any]:
        return self._minimize_options
