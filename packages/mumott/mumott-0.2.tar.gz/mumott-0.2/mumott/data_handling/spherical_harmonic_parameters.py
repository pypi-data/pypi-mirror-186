"""Container for the class SphericalHarmonicParameters."""
import numpy as np
from scipy.special import sph_harm
from numpy.typing import NDArray
from numpy import pi


class SphericalHarmonicParameters:
    """
    Class containing parameters pertaining to the orders and degrees of spherical harmonics used.
    Should be attached to a
    :class:`ReconstructionParameters <mumott.reconstruction_parameters.ReconstructionParameters>` instance.

    Parameters
    ----------
    l_max : int
        The maximum order of spherical harmonics that should be reconstructed.
    number_of_coefficients : int
        The number of coefficients used in each voxel. Typically equal
        to ``(max_order + 1) * (max_order // 2 + 1)`` when all orders and degrees of
        spherical harmonics up to and including ``max_order`` are used.
    spherical_harmonic_factors : np.ndarray, optional
        The factors of the spherical harmonic basis functions at each point on the
        unit sphere which are probed by a measurement. If not set, will be set to a
        dummy value and needs to be later calculated using the class method
        ``compute_spherical_harmonic_factors``.
    """

    def __init__(self,
                 l_max: int,
                 number_of_coefficients: int,
                 spherical_harmonic_factors: NDArray[float] = np.zeros(1)):
        self._generated_struct = False
        self._l_max = np.int32(l_max)
        self._m_max = np.int32(l_max)
        self._spherical_harmonic_factors = spherical_harmonic_factors.astype(np.float64)
        self._spherical_harmonic_gradient_factors = spherical_harmonic_factors.astype(np.float64)
        self._update_coefficient_indices()
        self._number_of_coefficients = np.int32(number_of_coefficients)

    def update_spherical_harmonic_orders(self,
                                         new_l_max: int):
        """
        Updates the class instance so that it supports higher orders.
        Can be called directly, but is typically called by the method
        :func:`ReconstructionParameters.increase_maximum_order()
        <mumott.reconstruction_parameters.ReconstructionParameters.increase_maximum_order>`.

        Parameters
        ----------
        new_l_max
            The new maximum order.
        """
        self._l_max = np.int32(new_l_max)
        self._m_max = np.int32(new_l_max)
        self._update_coefficient_indices()

    def _update_coefficient_indices(self):
        """
        Updates the attributes `l_indices` and `m_indices`. Called by `update_spherical_harmonic_orders()`.
        """
        mm = np.zeros((self._l_max + 1) * (self._l_max // 2 + 1))
        ll = np.zeros((self._l_max + 1) * (self._l_max // 2 + 1))
        count = 0
        for h in range(0, self._l_max + 1, 2):
            for i in range(-h, h + 1):
                ll[count] = h
                mm[count] = i
                count += 1
        self._l_indices = ll.astype(np.int32)
        self._m_indices = mm.astype(np.int32)

    def compute_spherical_harmonic_gradient(self,
                                            use_kernel: bool = False,
                                            kernel_exponent: float = -1.) -> None:
        """ Method for computing gradient factors for spherical harmonics. Must be called
        after ``compute_spherical_harmonic_factors``.

        Parameters
        ----------
        probed_theta
            Probed polar angle, equal to ``numpy.arccos(z)`` with ``z`` in ``[-1, 1]``.
            Should have shape ``(number_of_projections, number_of_detector_segments, N)``.
            The dimension ``N`` is used to integrate over a section of the unit sphere.
            If ``N`` is 1, ``(number_of_projections, number_of_detector_segments)`` is
            also an accepted shape.
        probed_phi
            Probed azimuthal angle, equal to ``numpy.arctan2(y, x)``. Should have the same
            shape as :attr:`probed_theta`.
        use_kernel
            Whether to use a kernel to prioritize certain orders. Default is ``False``.
        kernel_exponent
            The power law exponent of the kernel used if :attr:`use_kernel` is set to ``True``.
            Order zero will have weight ``1``, other orders  will have weight
            ``ell ** kernel_exponent`` where ``ell`` is the order. Default is ``-1``,
            which prioritizes lower orders. Positive values prioritize higher orders.
        """
        if use_kernel:
            kernel_weights = np.zeros(self._l_indices.size)
            kernel_weights[self._l_indices != 0] = \
                self._l_indices[self._l_indices != 0] ** float(kernel_exponent)
            kernel_weights[self._l_indices == 0] = 1
            kernel = kernel_weights
            kernel *= np.sqrt(1 / np.sum(kernel ** 2))
            kernel = kernel.reshape(1, -1).astype(complex)
            self._spherical_harmonic_gradient_factors = self._spherical_harmonic_factors * kernel
        else:
            self._spherical_harmonic_gradient_factors = self._spherical_harmonic_factors

    def compute_spherical_harmonic_factors(self,
                                           probed_theta: NDArray[np.float64],
                                           probed_phi: NDArray[np.float64],
                                           integration_weights: NDArray[np.float64] = None) -> None:
        """ Method for computing real spherical harmonic factors. Computes the
        contribution of the basis function of each order and degree at a set of
        probed points on the unit sphere. Generally the input used is from a
        :class:`ProjectionParameters <mumott.data_handling.ProjectionParameters>` object.
        By default, the :attr:`probed_theta_integ` of a projection_parameters will contain 12
        points on the circular segments between neighboring probed points, using the assumption
        that the data is averaged over all pixels in that segment.

        Parameters
        ----------
        probed_theta
            Probed polar angle, equal to ``numpy.arccos(z)`` with ``z`` in ``[-1, 1]``.
            Should have shape ``(number_of_projections, number_of_detector_segments, N)``.
            The dimension ``N`` is used to integrate over a section of the unit sphere.
            If ``N`` is 1, ``(number_of_projections, number_of_detector_segments)`` is
            also an accepted shape.
        probed_phi
            Probed azimuthal angle, equal to ``numpy.arctan2(y, x)``. Should have same
            shape as :attr:`probed_theta`.
        integration_weights
            If the data is computed using a fitted distribution or similar, the weights of the distribution
            can be provided. Should have the same shape as probed_theta, and normalized so that
            ``integration_weights.sum(axis=3) = 1``

        Notes
        -----
            This function uses
            :func:`scipy.special.sph_harm <https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.sph_harm.html>`, # noqa
            the documentation and source code of which use the opposite naming convention
            for the polar and azimuthal angles.
        """
        if len(probed_theta.shape) == 2:
            probed_theta = probed_theta.reshape(probed_theta.shape + (1,))
            probed_phi = probed_phi.reshape(probed_phi.shape + (1,))
        self._data_theta = probed_theta
        self._data_phi = probed_phi
        spherical_harmonic_factors = np.zeros((
            probed_theta.shape[0],
            probed_theta.shape[1],
            self._l_indices.size))
        if integration_weights is None:
            integration_weights = np.ones_like(probed_theta) * 1. / probed_theta.shape[2]
        for i, arc in enumerate(zip(probed_theta, probed_phi)):
            for j, angles in enumerate(zip(arc[0], arc[1])):
                theta, phi = angles
                complex_function = (integration_weights[i, j, np.newaxis, :] *
                                    sph_harm(abs(self._m_indices.reshape(-1, 1)),
                                             self._l_indices.reshape(-1, 1),
                                             phi.reshape(1, -1),
                                             theta.reshape(1, -1))).sum(axis=1)
                spherical_harmonic_factors[i, j, self._m_indices == 0] = \
                    np.sqrt((4 * pi)) * complex_function[self._m_indices == 0].real
                spherical_harmonic_factors[i, j, self._m_indices > 0] = \
                    ((-1.) ** (self._m_indices[self._m_indices > 0])) * np.sqrt((4 * pi)) * \
                    np.sqrt(2) * complex_function[self._m_indices > 0].real
                spherical_harmonic_factors[i, j, self._m_indices < 0] = \
                    ((-1.) ** (self._m_indices[self._m_indices < 0])) * np.sqrt((4 * pi)) * \
                    np.sqrt(2) * complex_function[self._m_indices < 0].imag
        self._spherical_harmonic_factors = spherical_harmonic_factors

    @property
    def l_max(self) -> np.int32:
        """ Maximum spherical harmonic order. """
        return self._l_max

    @property
    def m_max(self) -> np.int32:
        """ Maximum spherical harmonic degree. """
        return self._m_max

    @property
    def l_indices(self) -> NDArray[np.int32]:
        """
        Array of spherical harmonic orders, indicating the order
        of the coefficient at the corresponding index.
        """
        return self._l_indices

    @property
    def m_indices(self) -> NDArray[np.int32]:
        """
        Array of spherical harmonic degrees, indicating the
        degree of the coefficient at the corresponding index.
        """
        return self._m_indices

    @property
    def number_of_coefficients(self) -> np.int32:
        """ Number of spherical harmonic coefficients.

        The number of coefficients used in each voxel. Typically equal
        to ``(max_order + 1) * (max_order // 2 + 1)`` when all orders and degrees of
        spherical harmonics up to and including ``max_order`` are used.
        """
        return self._number_of_coefficients

    @number_of_coefficients.setter
    def number_of_coefficients(self, new_number: int):
        self._number_of_coefficients = np.int32(new_number)

    @property
    def spherical_harmonic_factors(self) -> NDArray[np.float64]:
        return self._spherical_harmonic_factors

    @property
    def spherical_harmonic_gradient_factors(self) -> NDArray[np.float64]:
        return self._spherical_harmonic_gradient_factors
