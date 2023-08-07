import numpy as np
from numpy.typing import NDArray


class ReconstructionOutput:
    """
    Container object for residual and gradient output.

    Parameters
    ----------
    residual_gradient : numpy.ndarray
        Container for the residual gradient.
        Must be an ndarray of size ``(nx, ny, nz, number_of_coefficients)``.
    reconstruction_projection : numpy.ndarray
        Container for the synthetic projections that come out of the calculations of the residuals.
        Must be of size ``cumulative_projection_size[-1] * number_of_detector_segments``
    residual : float, optional
        Default is ``0``, but if desired, an initial residual value can be specified.
    residual_per_projection : numpy.ndarray
        Container for the residual per projection. Must be ndarray of size ``number_of_projections``.
    """
    def __init__(self,
                 residual_gradient: NDArray,
                 reconstruction_projection: NDArray,
                 residual: float,
                 residual_per_projection: NDArray):
        self._residual_gradient = residual_gradient.astype(np.float64).reshape(-1, 1)
        self._reconstruction_projection = reconstruction_projection.astype(np.float64)
        self._residual = np.array(residual).astype(np.float64)
        self._residual_per_projection = residual_per_projection.astype(np.float64)

    def increase_output_size(self,
                             new_coefficient_number: np.int32,
                             number_of_voxels: np.int32):
        """
        Increases the size of output when the number of coefficients is increased.
        Normally called from :func:`ReconstructionParameters.increase_maximum_order()
        <mumott.reconstruction_parameters.ReconstructionParameters.increase_maximum_order>`.

        Parameters
        ----------
        new_coefficient_number
            The new number of coefficients, calculated from the new maximum order.
        number_of_voxels
            The total number of voxels. Must be the same as it was previously.
        """
        old_gradient = self._residual_gradient.reshape(number_of_voxels, -1)
        new_gradient = np.zeros((number_of_voxels, new_coefficient_number))
        new_gradient[:, :old_gradient.shape[1]] = old_gradient
        self._residual_gradient = new_gradient.reshape(-1, 1)

    @property
    def residual_gradient(self) -> NDArray[np.float64]:
        """
        Residual gradient resulting from the most recent gradient calculation.

        **Note:**
        Exposes a view of the array.
        """
        return self._residual_gradient[...]

    @residual_gradient.setter
    def residual_gradient(self,
                          gradient: NDArray[np.float64]):
        """
        Parameters
        ----------
        gradient : numpy.ndarray(dtype = numpy.float64)
            New gradient. Set using in-place operation.
        """
        self._residual_gradient[...] = gradient

    @property
    def reconstruction_projection(self) -> NDArray[np.float64]:
        """ Reconstruction projection from the most recent residual calculation. """
        return self._reconstruction_projection

    @property
    def residual(self) -> np.float64:
        """
        Residual from the most recent residual calculation.
        """
        return np.float64(self._residual)

    @residual.setter
    def residual(self, val: np.float64) -> None:
        """
        Parameters
        ----------
        val
            New value for the residual.
        """
        self._residual = np.float64(val)

    @property
    def residual_per_projection(self) -> NDArray[np.float64]:
        """ Residual per projection from the most recent residual calculation. """
        return self._residual_per_projection

    @residual_per_projection.setter
    def residual_per_projection(self, val: NDArray) -> None:
        """
        Parameters
        ----------
        val
            The new values for the residual per projection.
            Modified using in-place operation.
        """
        self._residual_per_projection[...] = val.astype(np.float64)
