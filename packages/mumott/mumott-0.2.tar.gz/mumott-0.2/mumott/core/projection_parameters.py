"""This file contains the class ProjectionParameters.

It is used for determining parameters for the John transform.
"""

import logging
from typing import Tuple
import numpy as np
from numpy import sin, cos
from numpy.typing import NDArray

from mumott.core.john_transform import john_transform, john_transform_adjoint
from numba import get_num_threads, set_num_threads


class ProjectionParameters:
    """ Class for calculating the parameters for the John transform, including
    the probed azimuthal and polar angles of each measurement.

    Parameters
    ----------
    rotation_angles_for_principal_axis : numpy.ndarray
        Rotation angles in radians of the principal tomographic axis, i.e.,
        the axis which is rotated second, for each projection. The length
        of the array must equal the number of projections.
    rotation_angles_for_secondary_axis : numpy.ndarray
        Rotation angles in radians of the secondary tomographic axis, i.e.,
        the tilt axis, which is rotated first. The length
        of the array must equal the number of projections.
    detector_segment_phis : numpy.ndarray
        Angles in radians of the segments or projected points on the detector.
    offsets_j : numpy.ndarray
        Offset of the origin of each projection in the direction of the slow index relative to the volume.
        The length must equal the number of projections.
    offsets_k : numpy.ndarray
        Offset of the origin of each projection in the direction of the fast index relative to the volume.
        The length must equal the number of projections.
    data_shape : numpy.ndarray
        Array of triplets containing the shape of each data frame as
        ``(x_pixels, y_pixels, number_of_detector_segments)``. The length
        of the array must equal the number of projections, and ` number_of_detector_segements``
        must equal ``len(detector_segment_phis)``.
    integration_step_size : float
        Ratio for one-dimensional line upsampling parallel to the projected direction.
        Must be greater than ``0`` and smaller than ``1``.
    """
    def __init__(self,
                 rotation_angles_for_principal_axis: NDArray[float],
                 rotation_angles_for_secondary_axis: NDArray[float],
                 detector_segment_phis: NDArray[float],
                 offsets_j: NDArray[float],
                 offsets_k: NDArray[float],
                 volume_shape: NDArray[int],
                 data_shape: NDArray[int],
                 integration_step_size: float = 1.0):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
        data_shape = np.array(data_shape)
        self._number_of_projections = np.int32(data_shape.shape[0])
        self._projection_size = data_shape.prod(1).astype(np.int32)
        self._cumulative_projection_size = np.concatenate(
            ((0,), np.cumsum(data_shape.prod(1)))).astype(np.int32)
        if len(rotation_angles_for_principal_axis) != data_shape.shape[0]:
            raise ValueError('Length of rotation_angles_for_principal_axis'
                             f' ({len(rotation_angles_for_principal_axis)}) must equal'
                             f' data_shape.shape[0] ({data_shape.shape[0]}).')
        if len(rotation_angles_for_secondary_axis) != data_shape.shape[0]:
            raise ValueError('Length of rotation_angles_for_secondary_axis'
                             f' ({len(rotation_angles_for_secondary_axis)}) must equal'
                             f' data_shape.shape[0] ({data_shape.shape[0]}).')
        self._rotation_angles_for_principal_axis = np.array(rotation_angles_for_principal_axis)
        self._rotation_angles_for_secondary_axis = np.array(rotation_angles_for_secondary_axis)
        self._calculate_basis_vectors(self._rotation_angles_for_principal_axis,
                                      self._rotation_angles_for_secondary_axis)
        if len(volume_shape) != 3:
            raise ValueError('volume_shape must have exactly three dimensions.')
        self._volume_shape = np.array(volume_shape).astype(np.int32)

        if len(data_shape[0]) != 3:
            raise ValueError('The elements of data_shape must each be three-dimensional.')
        self._data_shape = data_shape.astype(np.int32)

        if len(offsets_j) != data_shape.shape[0]:
            raise ValueError(f'Length of offsets_j ({len(offsets_j)})'
                             f' must equal data_shape.shape[0] ({data_shape.shape[0]}).')
        if len(offsets_k) != data_shape.shape[0]:
            raise ValueError(f'Length of offsets_k ({len(offsets_k)})'
                             f' must equal data_shape.shape[0] ({data_shape.shape[0]}).')

        self._number_of_detector_segments = np.int32(len(detector_segment_phis))
        if not np.allclose(len(detector_segment_phis), self._data_shape[:, 2]):
            raise ValueError('All entries in data_shape[:, 2]'
                             f' must equal len(detector_segment_phis) ({len(detector_segment_phis)}).')
        self._detector_segment_phis = detector_segment_phis.astype(np.float64)
        self.calculate_probed_coordinates()

        if not 0.0 < integration_step_size <= 1.0:
            raise ValueError('Integration step size must be less than or'
                             ' equal to 1.0, and greater than 0.0, but the'
                             f' provided value is {integration_step_size}!')
        self._offsets_j = np.array(offsets_j).astype(np.float64)
        self._offsets_k = np.array(offsets_k).astype(np.float64)
        self._integration_step_size = np.float64(integration_step_size)
        self._sampling_kernel = np.array((1.,), dtype=np.float64)
        self._kernel_offsets = np.array((0., 0.), dtype=np.float64)
        self._created_sampling_kernel = False

    def _calculate_basis_vectors(self,
                                 rotation_angles_for_principal_axis: NDArray[float],
                                 rotation_angles_for_secondary_axis: NDArray[float]) -> None:
        """ Calculates the basis vectors for the John transform, one projection vector
        and two coordinate vectors. """
        self._basis_vector_projection = np.zeros((self._number_of_projections, 3))
        self._basis_vector_j = np.zeros((self._number_of_projections, 3))
        self._basis_vector_k = np.zeros((self._number_of_projections, 3))
        for i, (alpha, beta) in enumerate(zip(rotation_angles_for_principal_axis,
                                              rotation_angles_for_secondary_axis)):
            self._basis_vector_projection[i, :] = (sin(-alpha) * cos(beta),
                                                   cos(alpha) * cos(beta),
                                                   sin(-beta))
            self._basis_vector_j[i, :] = (cos(alpha),
                                          sin(alpha),
                                          0.)
            self._basis_vector_k[i, :] = (sin(beta) * sin(-alpha),
                                          sin(beta) * cos(alpha),
                                          cos(beta))

    def calculate_probed_coordinates(self, integration_samples: int = 11) -> None:
        """
        Calculates the probed polar and azimuthal coordinates on the unit sphere at
        a given angle of projection.

        Parameters
        ----------
        integration_samples
            Number of samples to use for the integral around the probed point,
            in order to approximate the effect of summing up pixels in an area
            on the detector. If the probed points were found through a least-
            fit of the detector data, then set this to ``1``. Default is ``11``.
        """
        probed_coordinates = np.zeros((self._number_of_projections,
                                       self._number_of_detector_segments,
                                       3))
        for i, (vj, vk) in enumerate(zip(self._basis_vector_j, self._basis_vector_k)):
            probed_coordinates[i, :] = cos(self._detector_segment_phis)[:, np.newaxis] * \
                vj[np.newaxis, :] + sin(self._detector_segment_phis)[:, np.newaxis] * vk[np.newaxis, :]

        self._probed_theta = np.arccos(probed_coordinates[:, :, 2])
        self._probed_phi = np.arctan2(probed_coordinates[:, :, 1],
                                      probed_coordinates[:, :, 0])
        probed_coordinates_interval = np.zeros((self._number_of_projections,
                                                self._number_of_detector_segments,
                                                integration_samples,
                                                3))
        if len(self._detector_segment_phis) > 1:
            diff = abs(np.diff(self._detector_segment_phis))
            diff = np.insert(diff, 0, diff[-1])
            diff = np.insert(diff, -1, diff[1])
            diff *= 0.5 * integration_samples / (integration_samples + 1)
        else:
            diff = np.array((np.pi / 2, np.pi / 2)) * integration_samples / (integration_samples + 1)
        for i, (vj, vk) in enumerate(zip(self._basis_vector_j, self._basis_vector_k)):
            for j, ph in enumerate(self._detector_segment_phis):
                phi_range = np.linspace(ph - diff[j], ph + diff[j + 1], integration_samples)
                probed_coordinates_interval[i, j, :] = cos(phi_range)[:, np.newaxis] * \
                    vj[np.newaxis, :] + sin(phi_range)[:, np.newaxis] * \
                    vk[np.newaxis, :]
        self._probed_theta_interval = np.arccos(probed_coordinates_interval[:, :, :, 2])
        self._probed_phi_interval = np.arctan2(probed_coordinates_interval[:, :, :, 1],
                                               probed_coordinates_interval[:, :, :, 0])

    def create_sampling_kernel(self,
                               kernel_dimensions: Tuple[int, int] = (3, 3),
                               kernel_width: Tuple[float, float] = (1., 1.),
                               kernel_type: str = 'bessel') -> None:
        """ Creates a kernel to emulate the point spread function (PSF) of the
        beam. This improves the accuracy of the projection function.

        Parameters
        ----------
        kernel_dimensions
            A tuple of how many points should be sampled in each direciton of the kernel.
            The total number of line integrals per pixel in the data is
            ``kernel_dimensions[0] * kernel_dimensions[1]``.
        kernel_width
            Width parameter for the kernel in units of pixels. Typically the full-width-half-maximum of the
            beam used to measure the data.
        kernel_type
            The type of kernel to use. Accepted values are ``'bessel'``, ``'rectangular'``,
            and ``'gaussian'``.
            ``'bessel'`` uses a ``sinc`` function multiplied by a
            Lanczos window with the width parameter being the first Bessel zero. This
            gives a sharply peaked distribution that goes to zero at twice the full
            width half maximum, and samples are taken up to this zero.
            ``'rectangular'`` samples uniformly in a rectangle of size
            ``kernel_width``.
            ``'gaussian'`` uses a normal distribution with the FWHM given by `kernel_width`,
            sampled up to twice the FWHM.
        """
        if self._created_sampling_kernel:
            logging.warning('It appears that you have already created a sampling kernel.\n'
                            'The old sampling kernel will be overwritten.')
        if kernel_type == 'bessel':
            L = 0.7478
            ji = np.linspace(-kernel_width[0], kernel_width[0], kernel_dimensions[0] * 100)
            fj = np.sinc(ji * L / kernel_width[0]) * np.sinc(ji / kernel_width[0])
            ki = np.linspace(-kernel_width[1], kernel_width[1], kernel_dimensions[1] * 100)
            fk = np.sinc(ki * L / kernel_width[1]) * np.sinc(ki / kernel_width[1])
        elif kernel_type == 'rectangular':
            ji = np.linspace(-kernel_width[0] / 2, kernel_width[0] / 2, kernel_dimensions[0] * 100)
            fj = np.ones_like(ji)
            ki = np.linspace(-kernel_width[1] / 2, kernel_width[1] / 2, kernel_dimensions[1] * 100)
            fk = np.ones_like(ki)
        elif kernel_type == 'gaussian':
            std = np.array(kernel_width) / (2 * np.sqrt(2 * np.log(2)))
            ji = np.linspace(-kernel_width[0], kernel_width[0], kernel_dimensions[0] * 100)
            fj = np.exp(-0.5 * (ji ** 2) / ((std[0]) ** 2))
            ki = np.linspace(-kernel_width[1], kernel_width[1], kernel_dimensions[1] * 100)
            fk = np.exp(-0.5 * (ki ** 2) / ((std[1]) ** 2))
        else:
            raise ValueError(f'Unknown kernel type: {kernel_type}!')
        fr = fj.reshape(-1, 1) * fk.reshape(1, -1)
        fr = fr.reshape(kernel_dimensions[0], 100, kernel_dimensions[1], 100)
        fi = fr.sum(axis=(1, 3))
        fi = (fi / fi.sum()).astype(np.float64)
        J = ji.reshape(-1, 1) * np.ones((1, ki.size))
        K = ki.reshape(1, -1) * np.ones((ji.size, 1))
        J = J.reshape(kernel_dimensions[0], 100, kernel_dimensions[1], 100)
        K = K.reshape(kernel_dimensions[0], 100, kernel_dimensions[1], 100)
        Ji = J.mean(axis=(1, 3)).flatten()
        Ki = K.mean(axis=(1, 3)).flatten()
        offset = np.concatenate((Ji, Ki)).astype(np.float64)
        self._sampling_kernel = fi
        self._kernel_offsets = offset
        self._sampling_kernel_size = np.int32(kernel_dimensions[0] * kernel_dimensions[1])
        self._created_sampling_kernel = True

    def project(self,
                input_field: NDArray[np.float64],
                index: int,
                projection: NDArray[np.float64] = None,
                number_of_threads: int = 4) -> NDArray[np.float64]:
        """ Perform a forward projection (John transform) using the geometry defined
        by this class instance. This method can be used directly without providing the
        outut ``projection``, in which case the array will be allocated automatically.
        However, for optimal use when iterating over many projection, you should
        pre-allocate space for each projection.

        Parameters
        ----------
        input_field
            The volume which is to be projected. Must have 4 dimensions,
            the last dimension can be of any size. For scalar projection,
            set the last dimension to size ``1``. Must be row-major and
            contiguous (also-called C-contiguous) and have
            ``dtype = np.float64``.
        index
            The index of the projection. Determines which direction the projection
            should occur in.
        projection
            Output variable. Optional, but if provided,
            the last index must have the same size as the last index of :attr:`input_field`.
            Projection is cumulative and in-place, so initialize with zeros if you do not
            want projection to occur additively when calling several times.
            Must be row-major and contiguous (also-called C-contiguous) and have ``dtype = np.float64``.
        number_of_threads
            The number of threads to use when running on CPUs. Often equals
            the number of physical CPU cores. Default is ``4``.

        Returns
        -------
        projection
            The projection of ``input_field``. If ``projection`` is provided at input,
            this will be the same object.
        """
        shape = self._data_shape[index]
        if not np.allclose(input_field.shape[:-1], self._volume_shape):
            logging.warning('Input field shape differs from the recorded'
                            ' volume_shape of this ProjectionParameters instance.'
                            ' Please exercise caution!')
        if len(input_field.shape) != 4:
            raise ValueError('The input field must be 4-dimensional.'
                             ' If the last dimension is 1, please indicate'
                             ' this explicitly be reshaping it accordingly.')
        if input_field.dtype != np.float64:
            raise TypeError('Input field dtype must be np.float64,'
                            f' but it is currently {input_field.dtype}!')
        if projection is None:
            projection = np.zeros(tuple(shape[:-1]) + (input_field.shape[-1],), dtype=np.float64)
        else:
            if not np.allclose(projection.shape[:-1], shape[:-1]):
                logging.warning('Your input projection shape appears different from the'
                                ' data shape in this ProjectionParameters instance.'
                                ' Alignment may not work corrrectly.'
                                ' Please exercise caution!')
            if projection.dtype != np.float64:
                raise TypeError('Projection dtype must be np.float64,'
                                f' but it is currently {projection.dtype}!')
            if projection.shape[-1] != input_field.shape[-1]:
                raise ValueError(f'The last element of {projection.shape}'
                                 ' must be the same as the last element of'
                                 f' {input_field.shape}!')
            if projection.flags['C_CONTIGUOUS'] is False:
                raise ValueError('Input projection must be row-major and'
                                 ' contiguous (also-called C-contiguous)!'
                                 ' It is currently defined with strides'
                                 f' {projection.strides}. For a C-contiguous'
                                 ' array, the strides are strictly decreasing.')
        if input_field.flags['C_CONTIGUOUS'] is False:
            raise ValueError('Input input_field must be row-major and'
                             ' contiguous (also-called C-contiguous)!'
                             ' It is currently defined with strides'
                             f' {input_field.strides}. For a C-contiguous'
                             ' array, the strides are strictly decreasing.')
        vector_p = self._basis_vector_projection[index].astype(np.float64)
        vector_j = self._basis_vector_j[index].astype(np.float64)
        vector_k = self._basis_vector_k[index].astype(np.float64)
        projection_offsets = np.array((self._offsets_j[index],
                                       self._offsets_k[index]),
                                      dtype=np.float64).ravel()
        old_num_threads = get_num_threads()
        try:
            set_num_threads(number_of_threads)
        except ValueError as v:
            if 'number of threads' in str(v):
                logging.warning('number_of_threads {number_of_threads} exceeds '
                                'maximum number of thread(s) {config.NUMBA_DEFAULT_NUM_THREADS}. '
                                'Computation will proceed with {old_num_threads} thread(s).')
            else:
                raise v
        john_transform(projection, input_field, vector_p,
                       vector_j, vector_k, self._integration_step_size, projection_offsets,
                       self._sampling_kernel.ravel(), self._kernel_offsets.reshape(2, -1))
        set_num_threads(old_num_threads)
        return projection

    def adjoint(self,
                projection: NDArray[np.float64],
                index: int,
                output_field: NDArray[np.float64] = None,
                number_of_threads: int = 4) -> NDArray[np.float64]:
        """ Calculates the projection adjoint (or back-projection) using the geometry defined
        by this class instance. Uses multithreading with reduction summation; if you do not wish
        to perform the reduction immediately, provide ``output_field`` as an input parameter,
        with ``output_field.shape[0] == number_of_threads``, the three middle indices
        indicating ``(x, y, z)``, and the final index indicating the channel.

        Parameters
        ----------
        projection
            The projection to be back-projected. Must have 3 dimensions,
            the last dimension can be of any size. For scalar projection,
            set the last dimension to size 1. Must be row-major and contiguous
            (also-called C-contiguous) and have ``dtype = np.float64``.
        index
            The index of the projection. Determines the direction in which the
            back-projection is applied.
        number_of_threads
            In CPU implementation, the number of threads to use. Often equals
            the number of physical CPU cores. Default is ``4``. Parallelization
            occurs through reduction, so please note that a high number of threads
            can heavily impact memory usage.
        output_field
            Output variable. Optional, but if provided,
            must have a total of five dimensions, where
            the last index has the same size as the last index of ``projection``, and
            ``output_field.shape[0]`` must equal ``number_of_threads``. Must be
            row-major and contiguous (also-called C-contiguous) and have
            ``dtype = np.float64``. If provided, reduction over each thread will not occur.

        Returns
        -------
        output_field
            The adjoint of ``projection``. If ``output_field`` is provided at input,
            this will contain the adjoint calculated by each thread, so that reduction
            must be done to obtain the total adjoint. This allows the same array
            to be re-used over several projections.
        """
        shape = self._data_shape[index]
        if not np.allclose(projection.shape[:-1], shape[:-1]):
            logging.warning('Your input projection shape appears different from the'
                            ' data shape in this ProjectionParameters instance.'
                            ' Please exercise caution!')
        if len(projection.shape) != 3:
            raise ValueError('The input projection must be 3-dimensional.'
                             ' If the last dimension is 1, please indicate'
                             ' this explicitly by reshaping it.')
        if projection.dtype != np.float64:
            raise TypeError('Projection dtype must be np.float64,'
                            f' but it is currently {projection.dtype}!')
        if output_field is None:
            output_field = np.zeros(tuple(self._volume_shape) + (projection.shape[-1],), dtype=np.float64)
        else:
            if not np.allclose(output_field.shape[1:-1], self._volume_shape):
                logging.warning('Input field shape differs from the recorded'
                                ' volume_shape of this ProjectionParameters instance.'
                                ' Please exercise caution!')
            if projection.shape[-1] != output_field.shape[-1]:
                raise ValueError(f'The last element of {projection.shape}'
                                 ' must be the same as the last element of'
                                 f' {output_field.shape}!')
            if output_field.flags['C_CONTIGUOUS'] is False:
                raise ValueError('Input output_field must be row-major and'
                                 ' contiguous (also-called C-contiguous)!'
                                 ' It is currently defined with strides'
                                 f' {output_field.strides}. For a C-contiguous'
                                 ' array, the strides are strictly decreasing.')
        if projection.flags['C_CONTIGUOUS'] is False:
            raise ValueError('Input projection must be row-major and contiguous'
                             ' (also-called C-contiguous)!'
                             ' It is currently defined with strides'
                             f' {projection.strides}. For a C-contiguous'
                             ' array, the strides are strictly decreasing.')
        vector_p = self._basis_vector_projection[index].astype(np.float64)
        vector_j = self._basis_vector_j[index].astype(np.float64)
        vector_k = self._basis_vector_k[index].astype(np.float64)
        projection_offsets = np.array((self._offsets_j[index],
                                       self._offsets_k[index]),
                                      dtype=np.float64).ravel()
        old_num_threads = get_num_threads()
        try:
            set_num_threads(number_of_threads)
        except ValueError as v:
            if 'number of threads' in str(v):
                logging.warning('number_of_threads {number_of_threads} exceeds '
                                'maximum number of thread(s) {config.NUMBA_DEFAULT_NUM_THREADS}. '
                                'Computation will proceed with {old_num_threads} thread(s).')
            else:
                raise v
        if output_field.ndim == 4:
            temp_output_field = np.zeros((number_of_threads,) + output_field.shape, dtype=np.float64)
            john_transform_adjoint(projection, temp_output_field, vector_p,
                                   vector_j, vector_k, self._integration_step_size, projection_offsets,
                                   self._sampling_kernel.ravel(), self._kernel_offsets.reshape(2, -1))
            np.einsum('i...->...', temp_output_field, out=output_field)
        else:
            john_transform_adjoint(projection, output_field, vector_p,
                                   vector_j, vector_k, self._integration_step_size, projection_offsets,
                                   self._sampling_kernel.ravel(), self._kernel_offsets.reshape(2, -1))
        set_num_threads(old_num_threads)
        return output_field

    @property
    def probed_theta(self) -> NDArray[np.float64]:
        """
        Polar coordinates on the unit sphere probed during projection.
        """
        return self._probed_theta

    @property
    def probed_phi(self) -> NDArray[np.float64]:
        """
        Azimuthal coordinates on the unit sphere probed during projection.
        """
        return self._probed_phi

    @property
    def offsets_j(self) -> NDArray[np.float64]:
        """
        Projection offsets for alignment in the ``j``-direction.
        """
        return self._offsets_j

    @property
    def offsets_k(self) -> NDArray[np.float64]:
        """
        Projection offsets for alignment in the ``k``-direction.
        """
        return self._offsets_k

    @property
    def rotation_angles_for_principal_axis(self) -> NDArray[np.float64]:
        """
        Angle at which the principal tomographic axis, or "rotation" axis, is rotated.
        """
        return self._rotation_angles_for_principal_axis

    @property
    def rotation_angles_for_secondary_axis(self) -> NDArray[np.float64]:
        """
        Angles at which the secondary tomographic axis, or "tilt" axis, is rotated.
        """
        return self._rotation_angles_for_secondary_axis

    @property
    def probed_theta_interval(self) -> NDArray[np.float64]:
        """
        Full range of polar coordinates probed during projection.
        """
        return self._probed_theta_interval

    @property
    def probed_phi_interval(self) -> NDArray[np.float64]:
        """
        Full range of azimuthal coordinates probed during projection.
        """
        return self._probed_phi_interval

    @property
    def integration_step_size(self) -> np.float64:
        """
        One-dimensional upsampling ratio for the integration of each projection line.
        """
        return self._integration_step_size

    @integration_step_size.setter
    def integration_step_size(self, new_step_size: np.float64):
        self._integration_step_size = np.float64(new_step_size)

    @property
    def volume_shape(self) -> NDArray[np.int32]:
        """
        Shape of the three-dimensional volume.
        """
        return self._volume_shape

    @property
    def number_of_detector_segments(self) -> np.int32:
        """ Number of detector segments.

        The number of segments that the detector has been binned
        into (or alternatively, the number of points extracted from
        a curve fitted to the detector data).
        """
        return self._number_of_detector_segments

    @property
    def number_of_voxels(self) -> np.int32:
        """ Number of voxels. Integer-typed shorthand for ``nx * ny * nz``. """
        return np.int32(np.prod(self.volume_shape))

    @property
    def number_of_projections(self) -> np.int32:
        """ Number of data frames (data frames), or equivalently,
        the total number of tilts and rotations at which measurements were made.
        """
        return self._number_of_projections

    @property
    def data_shape(self) -> NDArray[np.int32]:
        """ Data shape in a series of triplets ``(x_pixels, y_pixels, number_of_detector_segments)``. """
        return self._data_shape

    @property
    def cumulative_projection_size(self) -> NDArray[np.int32]:
        """ ``cumulative_projetion_size[i:i+2]`` gives the flat start and stop indices
        of ``reconstruction_parameters.data`` for projection ``i``. """
        return self._cumulative_projection_size

    @property
    def basis_vector_projection(self) -> NDArray[np.float64]:
        """ Basis vector for each projection direction. """
        return self._basis_vector_projection

    @property
    def basis_vector_j(self) -> NDArray[np.float64]:
        """ Basis vector for each projection's slow index. """
        return self._basis_vector_j

    @property
    def basis_vector_k(self) -> NDArray[np.float64]:
        """ Basis vector for each projection's fast index. """
        return self._basis_vector_k

    @property
    def detector_segment_phis(self) -> NDArray[np.float64]:
        """ The angle of each detector segment in radians. """
        return self._detector_segment_phis

    @property
    def sampling_kernel(self) -> NDArray[np.float64]:
        """ Convolution kernel for the sampling profile. """
        return self._sampling_kernel

    @property
    def kernel_offsets(self) -> NDArray[np.float64]:
        """ Offsets for the sampling profile kernel. """
        return self._kernel_offsets
