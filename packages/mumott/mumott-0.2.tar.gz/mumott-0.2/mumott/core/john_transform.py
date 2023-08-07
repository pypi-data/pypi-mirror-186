""" Numba version of John transform. """

from numba import njit, int32, float64, void, prange, optional
from numpy.typing import NDArray
from typing import Optional
import numba
import numpy as np

numba.config.THREADING_LAYER = 'omp'


@njit(int32(float64[:, ::1], float64[::1]), fastmath=True, cache=True, nogil=True)
def _check_bounds(position: NDArray[float64],
                  bounds: NDArray[float64]) -> int32:
    """ Checks whether the given positions are inside a rectangular volume
    defined by the two corners at ``(0, 0, 0)`` and ``bounds``.

    Parameters
    ----------
    position
        ``position[i, :]`` gives the ``(x, y, z)`` coordinates
        of each point in space to be checked.
    bounds
        Contains the ``(x, y, z)`` coordinates for the three planes
        that define the rectangular volume.

    Returns
    -------
    out
        ``True`` if the positions are all inside the volume,
        ``False`` if at least one position is outside the volume.
    """
    out = int32(1)
    for h in range(position.shape[0]):
        out &= (int32(position[h, 0]) >= 0) & \
            (int32(position[h, 0]) < bounds[0]) & \
            (int32(position[h, 1]) >= 0) & \
            (int32(position[h, 1]) < bounds[1]) & \
            (int32(position[h, 2]) >= 0) & \
            (int32(position[h, 2]) < bounds[2])
    return out


@njit(void(float64[:, ::1], int32, float64[::1]), fastmath=True, cache=True, nogil=True)
def _update_position(position: NDArray[float64],
                     steps: int32,
                     projection_vector: NDArray[float64]) -> None:
    """ Updates the position for a set of rays with
    the specified number of additions of the given projection vector.

    Parameters
    ----------
    position
        ``position[i, :]`` contains the starting ``(x, y, z)`` coordinates of
        ray ``i``. This is modified in-place to update the position.
    steps
        Number of additions of ``projection_vector`` that are performed.
    projection_vector
        Determines the size and direction of each step.
    """
    for i in range(position.shape[0]):
        position[i, 0] += projection_vector[0] * steps
        position[i, 1] += projection_vector[1] * steps
        position[i, 2] += projection_vector[2] * steps


@njit(int32[:, ::1](float64[:, ::1], float64[::1], float64[::1], int32),
      fastmath=True, cache=True, nogil=True)
def _get_indices(position: NDArray[float64],
                 projection_vector: NDArray[float64],
                 volume_indexer: NDArray[float64],
                 steps: int32) -> NDArray[int32]:
    """ Computes all the (flattened) indices sampled by each ray of
    integration. Does not do bounds checks, so use with caution.

    Parameters
    ----------
    position
        ``position[i, :]`` contains the starting ``(x, y, z)`` coordinates of
        ray ``i``. No checks are performed to ensure that the position
        remains inside the volume, so use with caution. The provided
        ``position`` array is not modified by this function.
    projection_vector
        Determines the size and direction of each integration step.
    volume_indexer
        Contains the three-dimensional ``(x, y, z)`` shape of the volume.
    steps
        Number of steps needed for each ray of integration to reach its
        end point. No checks are performed to ensure that the number of
        steps do not result in stepping outside the volume, so use with caution.

    Returns
    -------
    out_vector
        Contains the flattened indices, such that out_vector[i, j]
        is the index sampled by ray ``j`` after ``i```steps.
    """
    out_vector = np.empty((steps, position.shape[0]), dtype=np.int32)
    for i in range(steps):
        for j in range(position.shape[0]):
            out_vector[i, j] = int32(int32((position[j, 0] + i * projection_vector[0])) * volume_indexer[0] +
                                     int32((position[j, 1] + i * projection_vector[1])) * volume_indexer[1] +
                                     int32((position[j, 2] + i * projection_vector[2])) * volume_indexer[2])
    return out_vector


@njit(int32(int32[:, ::1], float64[::1], int32[::1], float64[::1]),
      fastmath=True, cache=True, nogil=True)
def _reduce_indices(indices: NDArray[int32],
                    sampling_kernel: NDArray[float64],
                    reduced_indices: NDArray[int32],
                    weights: NDArray[float64]) -> NDArray[int32]:
    """ Reduces repeated indices by accumulating their weights,
    in order to reduce the number of reads or writes to the volume.

    Parameters
    ----------
    indices
        Array of flat indices of the volume, with
        ``indices[i, j]`` referring to the index of the volume samped by the ray of
        integration with weight ``sampling_kernel[j]`` after ``i`` steps.
    sampling_kernel
        Array of weights for each ray of integration.
    reduced_indices
        Output variable with the reduced indices. Must be large enough to
        store all indices after reduction.
    weights
        Output variable with ``weight[i]`` containing the accumulated
        weight of ``reduced_indices[i]``. Must be large enough to store
        all weights after reduction.

    Returns
    -------
    counter
        The number of valid entries of ``reduced_indices`` and
        ``weights``, such that ``reduced_indices[counter - 1]`` contains
        the last sampled index.
    """
    current_index = np.int32(-1)
    counter = 0
    ii = 0
    for i in range(indices.shape[0]):
        for j in range(indices.shape[1]):
            if current_index == indices[i, j]:
                weights[counter - 1] += sampling_kernel[j]
            else:
                if reduced_indices[ii] == indices[i, j]:
                    weights[ii] += sampling_kernel[j]
                else:
                    for ii in range(counter - 2, counter - sampling_kernel.size - 1, -1):
                        if reduced_indices[ii] == indices[i, j]:
                            weights[ii] += sampling_kernel[j]
                            break
                    else:
                        current_index = indices[i, j]
                        reduced_indices[counter] = indices[i, j]
                        weights[counter] = sampling_kernel[j]
                        counter += 1
    return counter


@njit(void(int32, int32, float64[:, ::1], float64[::1],
           float64[::1], float64[::1], float64[::1],
           float64, float64[::1], float64[:, ::1]), fastmath=True, cache=True, nogil=True)
def _initialize_position(j: int32, k: int32, offsets: NDArray[float64],
                         projection_bounds: NDArray[float64],
                         unit_vector_p: NDArray[float64],
                         unit_vector_j: NDArray[float64],
                         unit_vector_k: NDArray[float64],
                         scalar_bound: NDArray[float64],
                         volume_shift: NDArray[float64],
                         position: NDArray[float64]) -> None:
    """ Initializes the position of a ray of integration
    by accounting for the volume geometry, projection geometry,
    projection alignment offsets, and sampling kernel offsets.

    Parameters
    ----------
    j
        The first index of the pixel in the projection.
    k
        The second index of the pixel in the projection.
    offsets
        Offsets for each ray of the sampling kernel.
    projection_bounds
        The spatial position of index ``(0, 0)`` of the
        projection after aligning the point on the projection
        that includes the center of the volume with the origin,
        in the directions of ``unit_vector_j`` and ``unit_vector_k``.
    scalar_bound
        The offset in the direction of ``unit_vector_p``, from
        the plane that intersects the center of the volume.
    volume_shift
        The position of the center of the volume.
    position
        Output variable containing positions for each ray.
        Modified in-place.

    Notes
    -----
    It is possible to use an alignment which aligns some other
    point of the volume and the projection. In that case,
    ``projection_bounds``, ``scalar_bound`` and ``volume_shift``
    would all need to be modified to refer to this point of alignment
    rather than the center.
    """
    shift_j = j + 0.5 + projection_bounds[0]
    shift_k = k + 0.5 + projection_bounds[1]
    for i in range(position.shape[0]):
        position[i, 0] = (shift_j + offsets[0, i]) * unit_vector_j[0] + \
            (shift_k + offsets[1, i]) * unit_vector_k[0] + \
            scalar_bound * unit_vector_p[0] + volume_shift[0]
        position[i, 1] = (shift_j + offsets[0, i]) * unit_vector_j[1] + \
            (shift_k + offsets[1, i]) * unit_vector_k[1] + \
            scalar_bound * unit_vector_p[1] + volume_shift[1]
        position[i, 2] = (shift_j + offsets[0, i]) * unit_vector_j[2] + \
            (shift_k + offsets[1, i]) * unit_vector_k[2] + \
            scalar_bound * unit_vector_p[2] + volume_shift[2]


@njit(int32(float64[:, ::1], float64[::1], float64[::1]), fastmath=True, cache=True, nogil=True)
def _get_start_and_end_points(position: NDArray[float64],
                              projection_vector: NDArray[float64],
                              volume_bounds: NDArray[float64]) -> NDArray[int32]:
    """ Places the positions of each ray inside the volume bounds,
    and returns the number of steps needed to reach the edge
    of the volume.

    Parameters
    ----------
    position
        A set of ``(x, y, z)`` positions at which each parallel ray begins.
        If inside the volume, the region opposite to ``projection_vector``
        will not be integrated over. If outside the volume, all positions
        will be shifted to the inside of the volume.
    projection_vector
        The direction in which each ray is to travel, with the magnitude
        of the vector giving the step size.
    volume_bounds
        The ``(x, y, z)`` shape of thre three-dimensional volume
        that the rays are to travel through.

    Returns
    -------
    end_steps
        The number of steps needed before the first ray reaches
        the end of the volume, such that
        ``position[i, :] + end_steps * projection_vector``
        will be inside the volume for all ``i``, and
        ``position[i, :] + (end_steps + 1) * projection_vector``
        will be outside the volume for at least one ``i``.
    """
    adj_vector = np.empty(3)
    for i in range(3):
        if projection_vector[i] == 0:
            adj_vector[i] = np.finfo(float64).max
        else:
            adj_vector[i] = float64(1) / projection_vector[i]
    upper_length_bound = volume_bounds[0] * volume_bounds[1] * volume_bounds[2]
    bounds = np.empty(6, dtype=np.float64)
    for i in range(3):
        bounds[i] = volume_bounds[i] * (projection_vector[i] < 0)
        bounds[i + 3] = volume_bounds[i] * (projection_vector[i] >= 0)
    step_diff = float64(0.)
    temp_diff = float64(0.)
    for i in range(position.shape[0]):
        for j in range(3):
            temp_diff = (bounds[j] - position[i, j]) * adj_vector[j]
            step_diff = max(step_diff, temp_diff)
    start_steps = int32(step_diff + 1)
    if start_steps > upper_length_bound:
        return int32(0)
    _update_position(position, start_steps, projection_vector)
    bounds_okay = _check_bounds(position, volume_bounds)
    if not bounds_okay:
        return int32(0)
    step_diff = float64(volume_bounds[0] * volume_bounds[1] * volume_bounds[2])
    temp_diff = float64(0.)
    for i in range(position.shape[0]):
        for j in range(3):
            temp_diff = (bounds[j + 3] - position[i, j]) * adj_vector[j]
            step_diff = min(temp_diff, step_diff)
    end_steps = int32(step_diff)
    if end_steps <= 0:
        return int32(0)
    _update_position(position, end_steps, projection_vector)
    bounds_okay &= _check_bounds(position, volume_bounds)
    if bounds_okay:
        _update_position(position, -end_steps, projection_vector)
        return end_steps
    else:
        return int32(0)


@njit(void(float64[:, ::1], float64[::1], float64[:, ::1],
           float64[::1], float64[::1], int32, float64[::1]), fastmath=True, cache=True, nogil=True)
def _integrate(position: NDArray[float64], sampling_kernel: NDArray[float64],
               volume: NDArray[float64], volume_indexer: NDArray[float64],
               projection_vector: NDArray[float64], total_steps: int32,
               pixel: NDArray[float64]) -> None:
    """ Performs the integration necessary to compute the
    the John transform.

    Parameters
    ----------
    position
        ``position[i, :]`` is the position of the ray with weight ``sampling_kernel[i]``
        in ``(x, y, z)`` coordinates. No checks are performed to verify
        that the position is inside the volume, so proceed with caution.
    sampling_kernel
        Contains the weights for each ray of integration.
    volume
        Two-dimensional volume. The first index
        corresponds to the internal coordinates of the volume
        determined by ``volume_indexer``, and the final index
        stores multichannel data identically to ``pixel``.
    volume_indexer
        ``volume_indexer[i]`` gives the ``[x, y, z]`` coordinates
        of ``volume[i, :]``.
    projection_vector
        The direction of projection in Cartesian coordinates,
        scaled according to integration step size.
    total_steps
        Total number of additions of ``projection_vector``
        needed to reach the end of the
        volume from the starting position, for the ray which
        would need the least number of steps to reach it.
        No checks are performed to see if the rays remain
        inside the volume, so proceed with caution.
    pixel
        Output variable where the projection of each
        channel of ``volume`` is stored.
    """
    indices = _get_indices(position, projection_vector, volume_indexer, total_steps)
    reduced_indices = np.empty(indices.size, dtype=np.int32)
    weights = np.empty(indices.size, dtype=np.float64)
    counter = _reduce_indices(indices, sampling_kernel, reduced_indices, weights)
    for i in range(counter):
        for j in range(pixel.size):
            pixel[j] += volume[reduced_indices[i], j] * weights[i]


@njit(void(float64[:, ::1], float64[::1], float64[::1], float64[:, ::1],
           float64[::1], float64[::1], int32), fastmath=True, cache=True, nogil=True)
def _back_integrate(position: NDArray[float64], distributor: NDArray[float64],
                    sampling_kernel: NDArray[float64], volume: NDArray[float64],
                    volume_indexer: NDArray[float64], projection_vector: NDArray[float64],
                    total_steps: int32) -> None:
    r""" Performs the integration necessary to compute the
    adjoint of the John transform.

    Parameters
    ----------
    position
        ``position[i, :]`` is the position of the ray with weight ``sampling_kernel[i]``
        in ``(x, y, z)`` coordinates. No checks are performed to verify
        that the position is inside the volume, so proceed with caution.
    distributor
        Contains the values to be distributed to each channel of the volume
        along the ray of integration.
    sampling_kernel
        Contains the weights for each ray of integration.
    volume
        Two-dimensional volume. The first index
        corresponds to the internal coordinates of the volume
        determined by ``volume_indexer``, and the final index
        stores multichannel data identically to ``distributor``.
    volume_indexer
        ``volume_indexer[i]`` gives the ``[x, y, z]`` coordinates
        of ``volume[i, :]``.
    projection_vector
        The direction of projection in Cartesian coordinates,
        scaled according to integration step size.
    total_steps
        Total number of additions of ``projection_vector``
        needed to reach the end of the
        volume from the starting position, for the ray which
        would need the least number of steps to reach it.
        No checks are performed to see if the rays remain
        inside the volume, so proceed with caution.
    """
    indices = _get_indices(position, projection_vector, volume_indexer, total_steps)
    reduced_indices = np.empty(indices.size, dtype=np.int32)
    weights = np.empty(indices.size, dtype=np.float64)
    counter = _reduce_indices(indices, sampling_kernel, reduced_indices, weights)
    for i in range(counter):
        for j in range(distributor.size):
            volume[reduced_indices[i], j] += weights[i] * distributor[j]


@njit(void(float64[:, ::1],
           float64[::1],
           float64[::1], float64[::1],
           float64[::1], float64[::1], float64[::1],
           float64[:, ::1], float64[::1]), fastmath=True, cache=True, nogil=True)
def _project_for_one_pixel(shifted_positions: NDArray[float64],
                           projection_vector: NDArray[float64],
                           unit_vector_j: NDArray[float64], unit_vector_k: NDArray[float64],
                           sampling_kernel: NDArray[float64], volume_bounds: NDArray[float64],
                           pixel: NDArray[float64], volume: NDArray[float64],
                           volume_indexer: NDArray[float64]) -> None:
    """ Computes the projection into one pixel in the projection.

    Parameters
    ----------
    shifted_positions
        ``shifted_positions[i, :]`` initial ``(x, y, z)`` positions
        for the projection ray with weight ``sampling_kernel[i]``.
    projection_vector
        The direction of projection in Cartesian coordinates.
    unit_vector_j
        One of the directions for the pixels of ``projection``.
    unit_vector_k
        The other direction for the pixels of ``projection``.
    volume_bounds
        Contains the non-flattened shape of dimension 0 of ``volume``.
    sampling_kernel
        A kernel for upsampling or convolution of the projection,
        scaled by the size of each integration step. For a single ray,
        this array has only one element containing the step size.
    pixel
        The pixel into which the projection is calculated, with
        multichannel indices.
    volume
        Two-dimensional volume variable. The first index
        corresponds to the internal coordinates of the volume
        determined by ``volume_indexer``, and the final index
        stores multichannel data identically to ``pixel``.
    volume_indexer
        ``volume_indexer[i]`` gives the ``[x, y, z]`` coordinates
        of ``volume[i, :]``.
    """
    steps = _get_start_and_end_points(shifted_positions, projection_vector, volume_bounds)
    if steps == 0:
        return
    _integrate(shifted_positions, sampling_kernel,
               volume, volume_indexer,
               projection_vector, steps, pixel)


@njit(void(float64[:, ::1], float64[::1], float64[::1],
           float64[::1], float64[::1],
           float64[::1], float64[::1],
           float64[:, ::1], float64[::1]), fastmath=True, cache=True, nogil=True)
def _back_project_for_one_pixel(shifted_positions: NDArray[float64], distributor: NDArray[float64],
                                sampling_kernel: NDArray[float64],
                                projection_vector: NDArray[float64],
                                unit_vector_j: NDArray[float64], unit_vector_k: NDArray[float64],
                                volume_bounds: NDArray[float64],
                                volume: NDArray[float64], volume_indexer: NDArray[float64]) -> None:
    """ Computes the adjoint from one pixel in the projection.

    Parameters
    ----------
    shifted_positions
        ``shifted_positions[i, :]`` initial ``(x, y, z)`` positions
        for the projection ray with weight ``sampling_kernel[i]``.
    distributor
        Contains the contribution to the adjoint for the pixel
        in question, for each multichannel index.
    sampling_kernel
        A kernel for upsampling or convolution of the projection,
        scaled by the size of each integration step. For a single ray,
        this array has only one element equal to the step size.
    projection_vector
        The direction of projection in Cartesian coordinates,
        scaled by the size of each integration step.
    unit_vector_j
        One of the directions for the pixels of ``projection``.
    unit_vector_k
        The other direction for the pixels of ``projection``.
    volume_bounds
        Contains the non-flattened shape of dimension 0 of ``volume``.
    volume
        Two-dimensional volume variable. The first index
        corresponds to the internal coordinates of the volume
        determined by ``volume_indexer``, and the final index
        stores multichannel data identically to ``distributor``.
    volume_indexer
        ``volume_indexer[i]`` gives the ``[x, y, z]`` coordinates
        of ``volume[i, :]``.
    """
    steps = _get_start_and_end_points(shifted_positions, projection_vector, volume_bounds)
    if steps == 0:
        return
    _back_integrate(shifted_positions, distributor, sampling_kernel,
                    volume, volume_indexer,
                    projection_vector, steps)


@njit(void(float64[:, :, ::1], float64[::1], float64[:, ::1],
           float64[::1], float64[::1], float64[::1], float64[::1], float64[::1],
           float64[::1], float64[:, ::1], float64, float64),
      parallel=True, fastmath=True, cache=True, nogil=True)
def _john_transform(projection: NDArray[float64], projection_offsets: NDArray[float64],
                    volume: NDArray[float64], volume_bounds: NDArray[float64],
                    volume_indexer: NDArray[float64], unit_vector_p: NDArray[float64],
                    unit_vector_j: NDArray[float64], unit_vector_k: NDArray[float64],
                    sampling_kernel: NDArray[float64], kernel_offsets: NDArray[float64],
                    step_size: NDArray[float64], scalar_bound: NDArray[float64]) -> None:
    """ Internal method for computing the John transform
    with CPU multithreading.

    Parameters
    ----------
    projection
        A 3-dimensional numpy array for which the adjoint is calculated.
        The last index contains the
        data channels for multi-channel data. For scalar data, use
        ``1`` as the size of the last dimension.
    projection_offsets
        The j, k offsets that align the projections.
    volume
        Two-dimensional volume variable. The first index
        corresponds to the internal coordinates of the volume
        determined by ``volume_indexer``, and the final index
        stores multichannel data identically to the last
        index of ``projection``.
    volume_bounds
        Contains the non-flattened shape of dimension 0 of ``volume``.
    volume_indexer
        ``volume_indexer[i]`` gives the ``[x, y, z]`` coordinates
        of ``volume[i, :]``.
    unit_vector_p
        The direction of projection in Cartesian coordinates.
    unit_vector_j
        One of the directions for the pixels of ``projection``.
    unit_vector_k
        The other direction for the pixels of ``projection``.
    sampling_kernel
        A kernel for upsampling or convolution of the projection.
        Should be normalized so that it sums to unity.
    kernel_offsets
        Offsets for each entry of the kernel.
    step_size
        The size of each step for the quadrature of the integral.
    scalar_bound
        The offset from the center of the volume at which the
        projection begins, in the direction of ``unit_vector_p``.
    """
    projection_vector = unit_vector_p * step_size
    kernel = sampling_kernel * step_size
    volume_shift = float64(0.5) * volume_bounds
    projection_shift = (projection_offsets - np.array(projection.shape[:-1]) * 0.5).astype(np.float64)
    for j in prange(projection.shape[0]):
        shifted_positions = np.empty((sampling_kernel.size, 3), dtype=np.float64)
        for k in range(projection.shape[1]):
            _initialize_position(j, k, kernel_offsets, projection_shift,
                                 unit_vector_p, unit_vector_j, unit_vector_k,
                                 scalar_bound, volume_shift,
                                 shifted_positions)
            _project_for_one_pixel(shifted_positions,
                                   projection_vector,
                                   unit_vector_j, unit_vector_k,
                                   kernel, volume_bounds,
                                   projection[j, k, ...], volume, volume_indexer)


@njit(void(float64[:, :, ::1], float64[::1], float64[:, :, ::1],
           float64[::1], float64[::1], float64[::1], float64[::1], float64[::1],
           float64[::1], float64[:, ::1], float64, float64),
      parallel=True, fastmath=True, cache=True, nogil=True)
def _john_transform_adjoint(projection: NDArray[float64], projection_offsets: NDArray[float64],
                            volume: NDArray[float64], volume_bounds: NDArray[float64],
                            volume_indexer: NDArray[float64], unit_vector_p: NDArray[float64],
                            unit_vector_j: NDArray[float64], unit_vector_k: NDArray[float64],
                            sampling_kernel: NDArray[float64], kernel_offsets: NDArray[float64],
                            step_size: float64, scalar_bound: float64) -> None:
    """ Internal method for computing the adjoint of the John transform
    with CPU multithreading. All arrays must be row major and contiguous,
    also called C-contiguous.

    Parameters
    ----------
    projection
        A 3-dimensional numpy array for which the adjoint is calculated.
        The last index contains the
        data channels for multi-channel data. For scalar data, use
        ``1`` as the size of the last dimension.
    projection_offsets
        The j, k offsets that align the projections.
    volume
        Three-dimensional volume variable. The first index
        must equal ``numba.get_num_threads``, the second index
        correspond to the internal coordinates of the volume
        determined by ``volume_indexer``, and the final index
        stores multichannel data identically to the last
        index of ``projection``.
    volume_bounds
        Contains the non-flattened shape of dimension 1 of ``volume``.
    volume_indexer
        ``volume_indexer[i]`` gives the ``[x, y, z]`` coordinates
        of ``volume[:, i, :]``.
    unit_vector_p
        The direction of projection in Cartesian coordinates.
    unit_vector_j
        One of the directions for the pixels of ``projection``.
    unit_vector_k
        The other direction for the pixels of ``projection``.
    sampling_kernel
        A kernel for upsampling or convolution of the projection.
        Should be normalized so that it sums to unity.
    kernel_offsets
        Offsets for each entry of the kernel.
    step_size
        The size of each step for the quadrature of the integral.
    scalar_bound
        The offset from the center of the volume at which the
        projection begins, in the direction of ``unit_vector_p``.
    """
    projection_vector = unit_vector_p * step_size
    kernel = sampling_kernel * step_size
    volume_shift = float64(0.5) * volume_bounds
    projection_shift = (projection_offsets - np.array(projection.shape[:-1]) * 0.5).astype(np.float64)
    for j in prange(projection.shape[0]):
        thread_volume = volume[numba.get_thread_id()]
        shifted_positions = np.empty((sampling_kernel.size, 3), dtype=np.float64)
        for k in range(projection.shape[1]):
            _initialize_position(j, k, kernel_offsets, projection_shift,
                                 unit_vector_p, unit_vector_j, unit_vector_k,
                                 scalar_bound, volume_shift,
                                 shifted_positions)
            distributor = projection[j, k, ...]
            _back_project_for_one_pixel(shifted_positions, distributor, kernel,
                                        projection_vector,
                                        unit_vector_j, unit_vector_k,
                                        volume_bounds, thread_volume, volume_indexer)


@njit(void(float64[:, :, ::1], float64[:, :, :, ::1],
           float64[::1], float64[::1], float64[::1],
           float64, float64[::1],
           optional(float64[::1]), optional(float64[:, ::1])),
      fastmath=True, cache=True, nogil=True)
def john_transform(projection: NDArray[float64],
                   volume: NDArray[float64],
                   unit_vector_p: NDArray[float64],
                   unit_vector_j: NDArray[float64],
                   unit_vector_k: NDArray[float64],
                   step_size: float64,
                   projection_offsets: NDArray[float64],
                   sampling_kernel: Optional[NDArray[float64]],
                   kernel_offsets: Optional[NDArray[float64]]) -> None:
    r""" Frontend for performing the John transform with parallel
    CPU computing. The number of threads is regulated with
    ``numba.set_num_threads()``. All arrays must be row-major and contiguous,
    also called C-contiguous.

    Parameters
    ----------
    projection
        A 3-dimensional numpy array where the projection is stored.
        The last index contains the
        data channels for multi-channel data. For scalar data, use
        ``1`` as the size of the last dimension.
    volume
        The volume to be projected, with 4 dimensions. The last index
        is the same as for ``projection``.
    unit_vector_p
        The direction of projection in Cartesian coordinates.
    unit_vector_j
        One of the directions for the pixels of ``projection``.
    unit_vector_k
        The other direction for the pixels of ``projection``.
    step_size
        The size of each step for the quadrature of the integral.
    projection_offsets
        The j, k offsets that align the projections.
    sampling_kernel
        A kernel for uppsampling or convolution of the projection.
        Should be normalized so that it sums to unity.
    kernel_offsets
        Offsets for each entry of the kernel.

    Notes
    -----
    The computation performed by this function may be written as

    .. math::

        p(J, K)_i = \sum_{s=0}^{N} \sum_{j=0}^{M} d \cdot w_j \cdot V_i(\lfloor \mathbf{r}_j + d s \cdot \mathbf{v} \rfloor)

    where :math:`p(J, K)_i` is ``projection[J, K, i]``, :math:`d` is `step_size`,
    :math:`N` is the total number of steps, :math:`M` is ``sampling_kernel.size``,
    :math:`w_j` is ``sampling_kernel[j]``,  :math:`V_i` is ``volume[..., i]``,
    and :math:`\mathbf{v}` is ``unit_vector_p``.
    \mathbf{r}_j is the starting position for the ray weighted by ``sampling_kernel[j]``,
    and is given by

    .. math::

        \mathbf{r}_j(J, K) = (J + 0.5 + o_J - 0.5 \cdot J_\text{max}) \cdot \mathbf{u} + \\
                (K + 0.5 + o_K - 0.5 \cdot K_\text{max}) \cdot \mathbf{w} + \\
                (\Delta_p) \cdot \mathbf{v} + 0.5 \cdot \mathbf{r}_\text{max} \\

    where :math:`o_J` is the sum of ``projection_offsets[0]`` and ``kernel_offsets[0, j]``,
    :math:`o_K` is the sum of ``projection_offsets[1]`` and ``kernel_offsets[1, j]``,
    :math:`\mathbf{u}` is ``unit_vector_j``, :math:`mathbf{w}` is ``unit_vector_k``,
    :math:`J_\text{max}` and :math`K_\text{max}` are ``projection.shape[0]`` and
    ``projection.shape[1]`` respectively, and :math:`\mathbf{r}_\text{max}` is
    ``volume.shape[:3]``. :math:`\Delta_p` is an additional offset that places the
    starting position at the edge of the volume.
    """ # noqa
    scalar_bound = -((1. + np.sqrt(np.sum(np.power(float64(volume.shape[:-1]), 2.)))))
    volume_bounds = np.array(volume.shape[:-1]).astype(np.float64)
    volume_indexer = np.flip(np.cumprod(np.array((1,) + volume.shape[-2:0:-1]))).astype(np.float64)
    volume = volume.reshape(-1, volume.shape[-1])
    if sampling_kernel is None or kernel_offsets is None:
        kernel = np.array((1,), dtype=float64)
        offsets = np.array(((0, 0),), dtype=float64)
    else:
        kernel = sampling_kernel
        offsets = kernel_offsets
    _john_transform(projection, projection_offsets,
                    volume, volume_bounds, volume_indexer,
                    unit_vector_p,
                    unit_vector_j, unit_vector_k,
                    kernel, offsets,
                    step_size, scalar_bound)


@njit(void(float64[:, :, ::1], float64[:, :, :, :, ::1],
           float64[::1], float64[::1], float64[::1],
           float64, float64[::1],
           optional(float64[::1]), optional(float64[:, ::1])),
      fastmath=True, cache=True, nogil=True)
def john_transform_adjoint(projection: NDArray[float64],
                           volume: NDArray[float64],
                           unit_vector_p: NDArray[float64],
                           unit_vector_j: NDArray[float64],
                           unit_vector_k: NDArray[float64],
                           step_size: NDArray[float64],
                           projection_offsets: NDArray[float64],
                           sampling_kernel: Optional[NDArray[float64]],
                           kernel_offsets: Optional[NDArray[float64]]) -> None:
    r""" Frontend for performing the John transform adjoint (back-projection)
    with parallel CPU computation. The number of threads is regulated by
    ``numba.set_num_threads``.

    Parameters
    ----------
    projection
        A 3-dimensional numpy array for which the adjoint is calculated.
        The last index contains the
        data channels for multi-channel data. For scalar data, use
        ``1`` as the size of the last dimension.
    volume
        Output variable modified in-place. The volume where the adjoint is stored,
        with 5 dimensions. The last index is the same as the last index in
        ``projection``. The first index is for each thread of
        multi-threaded computation, so ``volume.shape[0]`` must equal
        ``numba.get_num_threads``.
        After computing, it is necessary to reduce over the first
        index to obtain the total result.
    unit_vector_p
        The direction of projection in Cartesian coordinates.
    unit_vector_j
        One of the directions for the pixels of ``projection``.
    unit_vector_k
        The other direction for the pixels of ``projection``.
    step_size
        The size of each step for the quadrature of the integral.
    projection_offsets
        The j, k offsets that align the projections.
    sampling_kernel
        A kernel for upsampling or convolution of the projection.
        Should be normalized so that it sums to unity.
    kernel_offsets
        Offsets for each entry of the kernel.

    Notes
    -----
    The computation performed by this function may be written as

    .. math::

        V_i(\mathbf{x}) = \sum_{s=0}^{N} \sum_{j=0}^{M} d \cdot w_j \cdot p(J, K)_i \delta_{\lfloor\mathbf{r}_j + d s \cdot \mathbf{v} \rfloor}^{\mathbf{x}}

    where :math:`d_i` is ``distributor[i]``, :math:`N` is the total number of steps,
    :math:`d` is ``step_size``. :math:`M` is ``sampling_kernel.size``, :math:`w_j` is ``sampling_kernel[j]``,
    :math:`V_i` is ``volume[:, i]``,
    and :math:`\mathbf{v}` is ``projection_vector``. :math:`\mathbf{x}` is
    understood to run over every triplet of non-negative integers in the domain
    of :math:`V_i`. \mathbf{r}_j is the starting position for the ray weighted by ``sampling_kernel[j]``,
    and is given by

    .. math::

        \mathbf{r}_j(J, K) = (J + 0.5 + o_J - 0.5 \cdot J_\text{max}) \cdot \mathbf{u} + \\
                (K + 0.5 + o_K - 0.5 \cdot K_\text{max}) \cdot \mathbf{w} + \\
                (\Delta_p) \cdot \mathbf{v} + 0.5 \cdot \mathbf{r}_\text{max} \\

    where :math:`o_J` is the sum of ``projection_offsets[0]`` and ``kernel_offsets[0, j]``,
    :math:`o_K` is the sum of ``projection_offsets[1]`` and ``kernel_offsets[1, j]``,
    :math:`\mathbf{u}` is ``unit_vector_j``, :math:`mathbf{w}` is ``unit_vector_k``,
    :math:`J_\text{max}` and :math`K_\text{max}` are ``projection.shape[0]`` and
    ``projection.shape[1]`` respectively, and :math:`\mathbf{r}_\text{max}` is
    ``volume.shape[:3]``. :math:`\Delta_p` is an additional offset that places the
    starting position at the edge of the volume.
    """ # noqa
    scalar_bound = -(1. + np.sqrt(np.sum(np.power(float64(volume.shape[:-1]), 2.))))
    volume_bounds = np.array(volume.shape[1:-1]).astype(np.float64)
    volume_indexer = np.flip(np.cumprod(np.array((1,) + volume.shape[-2:1:-1]))).astype(np.float64)
    volume = volume.reshape(-1, int32(np.prod(volume_bounds)), volume.shape[-1])
    if sampling_kernel is None or kernel_offsets is None:
        kernel = np.array((1,), dtype=float64)
        offsets = np.array(((0, 0),), dtype=float64)
    else:
        kernel = sampling_kernel
        offsets = kernel_offsets
    _john_transform_adjoint(projection, projection_offsets,
                            volume, volume_bounds, volume_indexer,
                            unit_vector_p,
                            unit_vector_j, unit_vector_k,
                            kernel, offsets,
                            step_size, scalar_bound)
