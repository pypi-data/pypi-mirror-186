"""Container for the class ReconstructionParameters."""
import numpy as np
from numpy.typing import NDArray
from mumott.core.projection_parameters import ProjectionParameters
from .reconstruction_input import ReconstructionInput
from .spherical_harmonic_parameters import SphericalHarmonicParameters
from .reconstruction_output import ReconstructionOutput


class ReconstructionParameters:
    """
    Container object with the data, its weights, and sub-containers.
    Initialization requires a range of data parameters which must be loaded
    from data files in order to create all the necessary reconstruction parameters.
    In addition, it takes other class instances containing other data parameters,
    which are attached as children to this instance.
    Finally, the class has methods for input pre-processing.

    Parameters
    ----------
    settings : numpy.ndarray
        Array with bool or int type specifying residual and gradient calculation options.
    data : numpy.ndarray
        Array of transmission corrected measurement data, sorted ``(frame, x, y, phi_n)``.
        Does not need to be structured, as different frames can have different sizes.
    projection_weights : numpy.ndarray
        Array of weights (valued from 0.0 to 1.0) indicating the weight
        assigned to each data point in ``data``, structured ``(x, y)``.
        A value of 0.0 indicates that the point is masked out.
    spherical_harmonic_parameters : SphericalHarmonicParameters
        Object containing parameters pertaining to the orders and degrees
        of spherical harmonics used.
    reconstruction_output : ReconstructionOutput
        Object containing the gradient and residual from each iteration of
        the reconstruction.
    reconstruction_input : ReconstructionInput
        Object containing the coefficients which are optimized for during
        reconstruction.
    projection_parameters : ProjectionParameters
        Object containing information needed for the John transform.
    diode : numpy.ndarray, None
        Array containing transmission data. For future implementations, not currently in use.
    """

    def __init__(self,
                 settings: NDArray,
                 data: NDArray,
                 projection_weights: NDArray,
                 spherical_harmonic_parameters: SphericalHarmonicParameters,
                 reconstruction_output: ReconstructionOutput,
                 reconstruction_input: ReconstructionInput,
                 projection_parameters: ProjectionParameters,
                 diode: NDArray = [0]):
        self._data = data.astype(np.float64)
        self._projection_weights = projection_weights.astype(np.float64)
        self._diode = diode.astype(np.float64)
        self._spherical_harmonic_parameters = spherical_harmonic_parameters
        self._reconstruction_output = reconstruction_output
        self._reconstruction_input = reconstruction_input
        self._projection_parameters = projection_parameters
        self._spherical_harmonic_parameters.compute_spherical_harmonic_factors(
            self._projection_parameters.probed_theta_interval,
            self._projection_parameters.probed_phi_interval)
        self._spherical_harmonic_parameters.compute_spherical_harmonic_gradient()

    def increase_maximum_order(self,
                               new_maximum_order: int):
        """
        Increase the maximum spherical harmonic order of spherical harmonics to be reconstructed.
        Also updates contained classes ``spherical_harmonic_parameters``,
        ``reconstruction_output``, and ``reconstruction_input``.

        Parameters
        ----------
        new_maximum_order
            New maximum order for spherical harmonics.
            Must be an even, positive integer greater than the current maximum order.

        Raises
        ------
        ValueError
            If ``new_maximum_order`` is smaller than ``spherical_harmonic_parameters.l_max``.
        """
        if new_maximum_order < self._spherical_harmonic_parameters.l_max:
            raise ValueError('new_maximum_order must be greater than the old maximum order,'
                             f' but the new maximum is {new_maximum_order}'
                             f' and the old one is {self.spherical_harmonic_parameters.l_max}')
        elif new_maximum_order == self._spherical_harmonic_parameters.l_max:
            print('Maximum order not increased.')
        else:
            print('Increasing maximum order ...')
            self._spherical_harmonic_parameters.update_spherical_harmonic_orders(new_maximum_order)
            self._spherical_harmonic_parameters.compute_spherical_harmonic_factors(
                self._projection_parameters.probed_theta_interval,
                self._projection_parameters.probed_phi_interval)
            self._spherical_harmonic_parameters.compute_spherical_harmonic_gradient()
            self._spherical_harmonic_parameters.number_of_coefficients = \
                np.int32(self._spherical_harmonic_parameters.m_indices.size)
            self._reconstruction_input.increase_input_size(
                self._spherical_harmonic_parameters.number_of_coefficients,
                self._projection_parameters.number_of_voxels)
            self._reconstruction_output.increase_output_size(
                self._spherical_harmonic_parameters.number_of_coefficients,
                self._projection_parameters.number_of_voxels)

    @property
    def projection_weights(self) -> NDArray[np.float64]:
        """
        Array containing weights for each data point, sorted
        ``(frame, x, y, phi)`` but not structured. Frames may be of different length.
        """
        return self._projection_weights

    @property
    def data(self) -> NDArray[np.float64]:
        """
        Array containing data for reconstruction, sorted in the order
        ``(frame, x, y, phi)`` but not structured. Frames may be of different length.
        """
        return self._data

    @data.setter
    def data(self, new_data: NDArray[np.float64]):
        """
        Parameters
        ---------
        new_data : numpy.ndarray(dtype = numpy.float64)
            New data to be inserted into class data attribute. Must have same size and shape as ``data``.
        """
        self._data[...] = new_data

    @property
    def spherical_harmonic_parameters(self) -> SphericalHarmonicParameters:
        """ Spherical harmonic parameter object. """
        return self._spherical_harmonic_parameters

    @property
    def projection_parameters(self) -> ProjectionParameters:
        """ Input dimension object. """
        return self._projection_parameters

    @property
    def reconstruction_output(self) -> ReconstructionOutput:
        """ Reconstruction output object. """
        return self._reconstruction_output

    @property
    def reconstruction_input(self) -> ReconstructionInput:
        """ Optimization input object. """
        return self._reconstruction_input
