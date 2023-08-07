from typing import Union

import numpy as np
from numpy.typing import NDArray


class ReconstructionInput:
    """
    Container class for the coefficients that are optimized for during SAXSTT reconstruction.

    Parameters
    ----------
    optimization_coefficients : numpy.ndarray
        Coefficients to be optimized for. Size should equal ``number_of_voxels * number_of_coefficients``.
    """
    def __init__(self,
                 optimization_coefficients: NDArray):
        self._optimization_coefficients = optimization_coefficients.astype(np.float64)

    @property
    def optimization_coefficients(self) -> NDArray[np.float64]:
        """ Coefficients from the most recent residual or gradient calculation. """
        return self._optimization_coefficients[...]

    @optimization_coefficients.setter
    def optimization_coefficients(self,
                                  new_coefficients: NDArray[np.float64]):
        """
        Modifies coefficients from the most recent residual or gradient calculation.

        Parameters
        -------
        new_coefficients : numpy.ndarray(dtype = numpy.float64)

        Notes
        -----
        Uses in-place modification.
        """
        self._optimization_coefficients[...] = new_coefficients

    def increase_input_size(self,
                            new_coefficient_number: Union[int, np.int32],
                            number_of_voxels: Union[int, np.int32]):
        """
        Normally called from :func:`ReconstructionParameters.increase_maximum_order
        <mumott.reconstruction_parameters.ReconstructionParameters.increase_maximum_order>`.
        Used to increase the size of the input when the maximum spherical harmonic order is increased.

        Parameters
        ----------
        new_coefficient_number
            The new coefficient number, calculated from the new maximum order.
        number_of_voxels
            The new number of voxels. Must be the same as before the size increase.
        """
        old_coefficients = self._optimization_coefficients.reshape(number_of_voxels, -1)
        new_coefficients = np.zeros((number_of_voxels, new_coefficient_number))
        new_coefficients[:, 0:old_coefficients.shape[1]] = old_coefficients
        self._optimization_coefficients = new_coefficients.flatten()
