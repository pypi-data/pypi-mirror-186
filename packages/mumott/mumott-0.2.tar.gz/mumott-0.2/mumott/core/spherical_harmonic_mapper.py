""" Container for class SphericalHarmonicMapper. """
import numpy as np
from numpy.typing import NDArray
from scipy.spatial.transform import Rotation as rot
from scipy.special import sph_harm, factorial2
from typing import Tuple


class SphericalHarmonicMapper:
    """
    Helper class for visualizing and analyzing spherical harmonics.
    Using this class, one can obtain the amplitudes for a given set
    of even-ordered harmonics and apply the Funk-Radon transform.
    These can then be plotted, analyzed, and so forth. In addition, the class
    allows one to represent functions in terms of spherical harmonics,
    if they are given as functions of the azimuthal and polar angles
    of the class instance.

    Parameters
    ----------
    max_order : int, optional
        Maximum order of the spherical harmonics. Default is ``2``.
    polar_resolution : int, optional
        Number of samples in the polar direction. Default is ``16``.
    azimuthal_resolution : int, optional
        Number of samples in the azimuthal direction. Default is ``32``.
    polar_zero : float, optional
        The polar angle of the spherical harmonic coordinate system's
        pole, relative to the reference coordinate system. Default is ``0``.
    azimuthal_zero : float, optional
        The azimuthal angle of the spherical harmonic coordinate system's
        pole, relative to a reference coordinate system. Default is ``0``.

    Example
    -------
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> S = SphericalHarmonicMapper(max_order=4, polar_resolution=16, azimuthal_resolution=8)
        >>> S.orders
        array([0, 2, 2, 2, 2, 2, 4, 4, ...])
        >>> S.degrees
        array([ 0, -2, -1,  0,  1,  2, -4, -3, ...])
        >>> a = S.get_amplitudes(np.random.rand(S.orders.size) - 0.5)
        >>> plt.pcolormesh(S.phi * np.sqrt(1 / 2), # basic cylindrical equal-area projection
                           np.cos(S.theta) / np.sqrt(1 / 2),
                           a[:-1, :-1])
        ...
    """

    def __init__(self,
                 max_order: int = 2,
                 polar_resolution: int = 16,
                 azimuthal_resolution: int = 32,
                 polar_zero: float = 0,
                 azimuthal_zero: float = 0):
        self._polar_zero = polar_zero
        self._azimuthal_zero = azimuthal_zero
        self._max_order = max_order
        polar_coordinates = np.linspace(0, np.pi, polar_resolution)
        azimuthal_coordinates = np.linspace(-np.pi, np.pi, azimuthal_resolution + 1)[:-1]
        self._theta, self._phi = np.meshgrid(
            polar_coordinates,
            azimuthal_coordinates,
            indexing='ij')
        self._update_l_and_m()

        self._map = np.zeros(self._theta.shape + self._l.shape)
        self._complex_map = np.zeros(self._theta.shape + self._l.shape).astype(complex)
        self._update_map()

        self._rotated_system = True
        self._get_coordinates()
        self._update_funk_coefficients()

        self._xyz = np.concatenate((self._X[..., None], self._Y[..., None], self._Z[..., None]), axis=2)
        self.update_zeros(self._polar_zero, self._azimuthal_zero)

    def get_amplitudes(self,
                       coefficients: NDArray[float],
                       apply_funk_transform: bool = False) -> NDArray[float]:
        """
        Returns the amplitudes of a set of spherical harmonics. For sorting
        of the coefficients, see the :attr:`orders` and :attr:`degrees` attributes.

        Parameters
        ----------
        coefficients
            The coefficients for which the amplitudes are to be calculated.
            Size must be equal to ``(max_order + 1) * (max_order / 2 + 1)``.
        apply_funk_fransform
            Whether to apply the Funk-Radon transform to the coefficients.
            This is useful for orientation analysis in some cases.
            Default is ``False``.
        """
        if apply_funk_transform:
            coefficients = (self._funk_coefficients * coefficients.ravel()).reshape(1, 1, -1)
        else:
            coefficients = coefficients.reshape(1, 1, -1)
        return np.einsum('...i, ...i', coefficients, self._map)

    def get_harmonic_coefficients(self, amplitude: NDArray[float]) -> NDArray[float]:
        """ Returns the spherical harmonic coefficients for the given amplitudes.
        Can be used with amplitudes from another instance of
        :class:`SphericalHarmonicParameters` with a different orientation
        in order to solve for the rotated coefficients. The accuracy of the
        representation depends on the maximum order and the polar and azimuthal
        resolution.

        Parameters
        ----------
        amplitude
            The amplitude of the spherical function to be
            represented, as a function of ``theta_interpolator``
            and ``phi_interpolator``.
        """
        area_normer = np.sin(self.theta_interpolator)
        area_normer /= np.sum(area_normer)
        scaled_amp = np.einsum('..., ...',
                               amplitude,
                               area_normer).reshape(self.theta_interpolator.shape + (1,))
        coeffs = np.einsum('ij..., ij...', self.map_interpolator, scaled_amp)
        return coeffs

    def _get_coordinates(self) -> Tuple[NDArray[float], NDArray[float], NDArray[float]]:
        """ Gets the X, Y, and Z-coordinates. Updates them only if the system has
        been rotated since the last call. """
        if self._rotated_system:
            self._X, self._Y, self._Z = \
                (np.multiply(0.5, np.einsum('..., ...', np.sin(self._theta), np.cos(self._phi))),
                 np.multiply(0.5, np.einsum('..., ...', np.sin(self._theta), np.sin(self._phi))),
                 np.multiply(0.5, np.cos(self._theta)))
            self._rotated_system = False
        return self._X, self._Y, self._Z

    def _update_funk_coefficients(self) -> None:
        """ Updates the Funk coefficients used for the Funk transform. """
        funk_coefficients = []
        for i in range(self._max_order+1):
            if i % 2 == 0:
                funk_coefficients.append(((-1) ** (i // 2)) * factorial2(i - 1) / factorial2(i))
        funk_coefficients = np.array(funk_coefficients)
        self._funk_coefficients = funk_coefficients[self._l // 2]

    def _update_l_and_m(self) -> None:
        """ Updates the order and degree vectors of the system. """
        self._l = []
        self._m = []
        for ll in range(0, self._max_order+1, 2):
            for mm in range(-ll, ll+1):
                self._l.append(ll)
                self._m.append(mm)
        self._l = np.array(self._l)
        self._m = np.array(self._m)

    def _update_map(self) -> None:
        """ Updates the map of the system. """
        self._update_complex_map()
        self._update_real_map()

    def _update_complex_map(self) -> None:
        """ Retrieves the complex map used for determining
        the real map. """
        self._complex_map[...] = sph_harm(
            abs(self._m.reshape(1, 1, -1)),
            self._l.reshape(1, 1, -1),
            self._phi[:, :, None],
            self._theta[:, :, None])

    def _update_real_map(self) -> None:
        """ Calculates the real spherical harmonic map based on
        the complex map. """
        self._map[:, :, self._m == 0] = \
            np.sqrt(4 * np.pi) * self._complex_map[:, :, self._m == 0].real
        self._map[:, :, self._m > 0] = \
            ((-1.) ** (self._m[self._m > 0])) * np.sqrt(2) * \
            np.sqrt(4 * np.pi) * self._complex_map[:, :, self._m > 0].real
        self._map[:, :, self._m < 0] = \
            ((-1.) ** (self._m[self._m < 0])) * np.sqrt(2) * \
            np.sqrt(4 * np.pi) * self._complex_map[:, :, self._m < 0].imag

    def update_zeros(self, polar_zero: float, azimuthal_zero: float) -> None:
        """Changes the orientation of the coordinate system.

        Parameters
        ----------
        polar_zero
            The new polar angle at which the pole should be,
            relative to a fixed reference system.
        azimuthal_zero
            The new azimuthal angle at which the pole should be,
            relative to a fixed reference system.
        """
        if polar_zero == 0 and azimuthal_zero == 0:
            self._theta = np.arccos(self._xyz[..., 2] / np.sqrt((self._xyz ** 2).sum(-1)))
            self._phi = np.arctan2(self._xyz[..., 1], self._xyz[..., 0])
            return
        xyz = np.copy(self._xyz)
        xyz = xyz.reshape(-1, 3)
        rotvec = rot.from_euler('Z', (-azimuthal_zero))
        rotvec = rot.from_euler('Y', (-polar_zero)) * rotvec
        xyz = rotvec.apply(xyz).reshape(self._theta.shape + (3,))
        self._theta = np.arccos(xyz[..., 2] / np.sqrt((xyz ** 2).sum(-1)))
        self._phi = np.arctan2(xyz[..., 1], xyz[..., 0])
        self._polar_zero = polar_zero
        self._azimuthal_zero = azimuthal_zero
        self._rotated_system = True
        self._update_map()

    @property
    def orders(self) -> NDArray[int]:
        """ The orders of the harmonics calculated
        by the class instance. """
        return self._l

    @property
    def degrees(self) -> NDArray[int]:
        """ The degrees of the harmonics calculated
        by the class instance. """
        return self._m

    @property
    def polar_zero(self) -> NDArray[float]:
        """ The polar angle of the spherical harmonic pole,
        relative to a fixed reference system. """
        return self._polar_zero

    @property
    def azimuthal_zero(self) -> NDArray[float]:
        """ The azimuthal angle of the spherical harmonic pole,
        relative to a fixed reference system. """
        return self._azimuthal_zero

    @property
    def theta(self) -> NDArray[float]:
        """ The polar angle to which the amplitude is mapped. """
        return self._theta

    @property
    def phi(self) -> NDArray[float]:
        """ The azimuthal angle to which the amplitude is mapped. """
        return self._phi

    @property
    def phi_interpolator(self) -> NDArray[float]:
        """ The azimuthal angle with an end-point removed,
        to be used for solving for spherical harmonics. """
        return self._phi[:, :-1]

    @property
    def theta_interpolator(self) -> NDArray[float]:
        """ The polar angle with an end-point removed,
        to be used for solving for spherical harmonics. """
        return self._theta[:, :-1]

    @property
    def max_order(self) -> int:
        """ Maximum order of the spherical harmonics. """
        return self._max_order

    @property
    def map(self) -> NDArray[float]:
        """ Map between amplitude and harmonics. """
        return self._map

    @property
    def map_interpolator(self) -> NDArray[float]:
        """ Maximum order of the spherical harmonics. """
        return self._map[:, :-1]

    @property
    def coordinates(self) -> Tuple[NDArray[float], NDArray[float], NDArray[float]]:
        """ The X, Y, Z coordinates that the amplitudes
        are mapped to. """
        return self._get_coordinates()

    @max_order.setter
    def max_order(self, new_max_order: int):
        self._max_order = new_max_order
        self._update_l_and_m()
        self._map = np.zeros(self._theta.shape + self._l.shape)
        self._complex_map = np.zeros(self._theta.shape + self._l.shape).astype(complex)
        self._update_map()
        self._update_funk_coefficients()
