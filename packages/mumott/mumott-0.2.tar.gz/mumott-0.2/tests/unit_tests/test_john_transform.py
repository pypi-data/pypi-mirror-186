import pytest
import numpy as np
from numba import set_num_threads # noqa
from mumott.core.john_transform import (_check_bounds, _update_position, _get_indices, # noqa
                                        _reduce_indices, _initialize_position,
                                        _get_start_and_end_points, _integrate, _back_integrate,
                                        _project_for_one_pixel, _back_project_for_one_pixel,
                                        _john_transform, _john_transform_adjoint, john_transform,
                                        john_transform_adjoint)
from numpy import float64, float32, int32 # noqa


def test_check_bounds():
    position = np.array((10.5, 15.5, 4.1), dtype=float64).reshape(1, 3)
    bounds = np.array((20, 18, 9), dtype=float64)
    out = _check_bounds(position, bounds)
    assert out == 1
    position = np.array((10.5, 15.5, -4.1), dtype=float64).reshape(1, 3)
    bounds = np.array((20, 18, 9), dtype=float64)
    out = _check_bounds(position, bounds)
    assert out == 0
    position = np.array((10.5, 15.5, 7), dtype=float64).reshape(1, 3)
    bounds = np.array((20, 18, 4), dtype=float64)
    out = _check_bounds(position, bounds)
    assert out == 0
    position = np.array(((10.5, 15.5, 4.1), (4, 7, 2)), dtype=float64).reshape(2, 3)
    bounds = np.array((20, 18, 9), dtype=float64)
    out = _check_bounds(position, bounds)
    assert out == 1
    with pytest.raises(TypeError) as e:
        _ = _check_bounds(position.astype(float32), bounds)
        assert 'array(float32, 2d, C)' in str(e)
    with pytest.raises(TypeError) as e:
        _ = _check_bounds(position.T, bounds)
        assert 'array(float64, 2d, F)' in str(e)


def test_update_position():
    position = np.array((10.5, 15.5, 4.1), dtype=float64).reshape(1, 3)
    steps = int32(10)
    projection_vector = np.array((0.8, -10.2, 2), dtype=float64)
    _update_position(position, steps, projection_vector)
    assert np.allclose(position, np.array([[18.5, -86.5,  24.1]]))
    position = np.array(((10.5, 15.5, 4.1), (4, 7, 2)), dtype=float64).reshape(2, 3)
    steps = int32(3)
    projection_vector = np.array((0.8, -10.2, 2), dtype=float64)
    _update_position(position, steps, projection_vector)
    assert np.allclose(position, np.array([[12.9, -15.1, 10.1],
                                           [6.4, -23.6, 8.]]))
    with pytest.raises(TypeError) as e:
        _update_position(position.astype(float32), steps, projection_vector)
        assert 'array(float32, 2d, C)' in str(e)
    with pytest.raises(TypeError) as e:
        _update_position(position.T, steps, projection_vector)
        assert 'array(float64, 2d, F)' in str(e)


def test_get_indices():
    position = np.array((10.5, 15.5, 4.1), dtype=float64).reshape(1, 3)
    steps = int32(4)
    projection_vector = np.array((0.8, -1., 2), dtype=float64)
    volume_indexer = np.array((32, 32, 32), dtype=float64)
    indices = _get_indices(position, projection_vector, volume_indexer, steps)
    assert np.allclose(indices, np.array([[928],
                                          [992],
                                          [1056],
                                          [1088]]))
    position = np.array(((10.5, 15.5, 4.1), (4, 7, 2)), dtype=float64).reshape(2, 3)
    steps = int32(8)
    projection_vector = np.array((1.75, 1.42, 0.01), dtype=float64)
    volume_indexer = np.array((64, 32, 17), dtype=float64)
    indices = _get_indices(position, projection_vector, volume_indexer, steps)
    assert np.allclose(indices, np.array([[1188,  514],
                                          [1348,  610],
                                          [1540,  770],
                                          [1636,  962],
                                          [1828, 1122],
                                          [1988, 1250],
                                          [2180, 1410],
                                          [2276, 1570]], dtype=int32))
    with pytest.raises(TypeError) as e:
        _ = _get_indices(position.astype(float32), projection_vector, volume_indexer, steps)
        assert 'array(float32, 2d, C)' in str(e)
    with pytest.raises(TypeError) as e:
        _ = _get_indices(position.T, projection_vector, volume_indexer, steps)
        assert 'array(float64, 2d, F)' in str(e)


def test_reduce_indices():
    indices = np.array([[928, 928, 928, 960, 960, 992, 992,
                         992, 1024, 1024, 1024, 1024]], dtype=int32).reshape(-1, 1)
    sampling_kernel = np.array((0.5,), dtype=float64)
    reduced_indices = np.empty_like(indices[:, 0])
    weights = np.empty_like(indices[:, 0], dtype=float64)
    counter = _reduce_indices(indices, sampling_kernel, reduced_indices, weights)
    assert counter == 4
    assert np.allclose(reduced_indices[:counter], np.array([928, 960, 992, 1024]))
    assert np.allclose(weights[:counter], np.array([1.5, 1., 1.5, 2.]))


def test_initialize_position():
    j = int32(23)
    k = int32(16)
    offsets = np.array(((0.3, -0.8), (-0.4, 0.1)), dtype=float64)
    projection_bounds = np.array((18, 20), dtype=float64)
    unit_vector_p = np.array((0.5, 1.2, 0.9), dtype=np.float64)
    unit_vector_p = unit_vector_p / np.linalg.norm(unit_vector_p)
    unit_vector_j = np.array((-1.2, 0.5, 0), dtype=np.float64)
    unit_vector_j = unit_vector_j - unit_vector_p * np.dot(unit_vector_j, unit_vector_p)
    unit_vector_j = unit_vector_j / np.linalg.norm(unit_vector_j)
    unit_vector_k = np.cross(unit_vector_j, unit_vector_p)
    scalar_bound = -60.
    volume_shift = np.array((18, 18, 18), dtype=np.float64)
    position = np.zeros((2, 3), dtype=np.float64)
    _initialize_position(j, k, offsets, projection_bounds, unit_vector_p, unit_vector_j,
                         unit_vector_k, scalar_bound, volume_shift, position)
    assert np.allclose(position, np.array([[-31.65501972,   7.50795268, -45.83373685],
                                           [-30.53017164,   7.34758806, -46.24483294]]))


def test_get_start_and_end_points():
    position = np.array((-0.5, -2, -1), dtype=np.float64).reshape(1, 3)
    projection_vector = np.array((0.3, 1.2, 0.6), dtype=np.float64)
    volume_bounds = np.array((10, 15, 18), dtype=np.float64)
    steps = _get_start_and_end_points(position, projection_vector, volume_bounds)
    assert steps == 12
    assert np.allclose(position, np.array([[0.1, 0.4, 0.2]]))
    position = np.array((-0.5, -2, -1), dtype=np.float64).reshape(1, 3)
    projection_vector = np.array((-0.3, -1.2, -0.6), dtype=np.float64)
    steps = _get_start_and_end_points(position, projection_vector, volume_bounds)
    assert steps == 0
    position = np.array((-0.5, -2, -1), dtype=np.float64).reshape(1, 3)
    projection_vector = np.array((1e-16, 1e-16, 1e-16), dtype=np.float64)
    steps = _get_start_and_end_points(position, projection_vector, volume_bounds)
    assert steps == 0
    position = np.array((0.5, 2, 1), dtype=np.float64).reshape(1, 3)
    projection_vector = np.array((0.3, 1.2, 0.6), dtype=np.float64)
    volume_bounds = np.array((-10, -15, -18), dtype=np.float64)
    steps = _get_start_and_end_points(position, projection_vector, volume_bounds)
    assert steps == 0


def test_integrate():
    position = np.array(((0.1, 0.2, 1.1), (0.1, 0.2, 1.1)), dtype=float64).reshape(-1, 3)
    projection_vector = np.array((0.8, 0.61, 1.), dtype=float64)
    volume_indexer = np.array((4, 4, 4), dtype=float64)
    volume = np.ones((4, 4, 4, 2), dtype=float64)
    volume[..., 1] *= 2.6
    volume[:, 0, 1, :] *= 1.2
    volume = volume.reshape(-1, 2)
    sampling_kernel = np.array(((0.26, 0.12)), dtype=float64)
    total_steps = int32(3)
    pixel = np.zeros(2, dtype=float64)
    _integrate(position, sampling_kernel, volume, volume_indexer, projection_vector,
               total_steps, pixel)
    assert np.allclose(pixel, np.array([1.14, 2.964], dtype=float64))


def test_back_integrate():
    position = np.array(((0.1, 0.2, 0.1), (0.1, 0.2, 0.15)), dtype=float64).reshape(-1, 3)
    projection_vector = np.array((0.3, 0.21, 0.3), dtype=float64)
    volume_indexer = np.array((2, 2, 2), dtype=float64)
    volume = np.zeros((2, 2, 2, 2), dtype=float64)
    volume = volume.reshape(-1, 2)
    sampling_kernel = np.array(((0.26, 0.12)), dtype=float64)
    total_steps = int32(3)
    distributor = np.array((0.9, 1.7), dtype=float64)
    _back_integrate(position, distributor, sampling_kernel, volume,
                    volume_indexer, projection_vector,
                    total_steps)
    assert np.allclose(volume, np.array([[1.026, 1.938],
                                         [0., 0.],
                                         [0., 0.],
                                         [0., 0.],
                                         [0., 0.],
                                         [0., 0.],
                                         [0., 0.],
                                         [0., 0.]]))


def test_project_for_one_pixel():
    position = np.array(((-0.1, -0.2, -0.1), (-0.1, -0.2, -0.15)), dtype=float64).reshape(-1, 3)
    projection_vector = np.array((0.3, 0.3, 0.3), dtype=float64)
    volume_indexer = np.array((4, 4, 4), dtype=float64)
    volume_bounds = np.array((4, 4, 4), dtype=float64)
    volume = np.ones((4, 4, 4, 2), dtype=float64)
    volume[..., 1] *= 6.3
    volume[:, 0, 2, :] *= 2.2
    volume = volume.reshape(-1, 2)
    sampling_kernel = np.array(((0.26, 0.12)), dtype=float64)
    unit_vector_j = np.array((-1.2, 0.5, 0), dtype=np.float64)
    unit_vector_k = np.array((1.2, -0.5, 0), dtype=np.float64)
    pixel = np.zeros(2, dtype=float64)
    _project_for_one_pixel(position, projection_vector, unit_vector_j, unit_vector_k,
                           sampling_kernel, volume_bounds, pixel, volume, volume_indexer)
    assert np.allclose(pixel, np.array([4.56, 28.728]))


def test_back_project_for_one_pixel():
    position = np.array(((-0.1, -0.2, -0.1), (-0.1, -0.2, -0.15)), dtype=float64).reshape(-1, 3)
    projection_vector = np.array((0.1, 0.2, 0.1), dtype=float64)
    volume_indexer = np.array((2, 2, 2), dtype=float64)
    volume_bounds = np.array((2, 2, 2), dtype=float64)
    volume = np.zeros((2, 2, 2, 2), dtype=float64)
    volume = volume.reshape(-1, 2)
    distributor = np.array((0.9, 1.7), dtype=float64)
    sampling_kernel = np.array(((0.26, 0.12)), dtype=float64)
    unit_vector_j = np.array((-1.2, 0.5, 0), dtype=np.float64)
    unit_vector_k = np.array((1.2, -0.5, 0), dtype=np.float64)
    _back_project_for_one_pixel(position,  distributor, sampling_kernel,
                                projection_vector, unit_vector_j, unit_vector_k,
                                volume_bounds, volume, volume_indexer)
    assert np.allclose(volume, np.array([[1.368, 2.584],
                                         [0., 0.],
                                         [1.368, 2.584],
                                         [0., 0.],
                                         [0., 0.],
                                         [0., 0.],
                                         [0., 0.],
                                         [0., 0.]]))


def test_john_transform():
    projection = np.zeros((2, 2, 2), dtype=float64)
    projection_offsets = np.array((-0.1, 0.1), dtype=float64)
    volume = np.ones((8, 2), dtype=float64) * 2.4
    volume[3, 0] = 1.6
    volume[5, 1] = 9.12
    volume_bounds = np.array((2, 2, 2), dtype=float64)
    volume_indexer = np.array((4, 2, 1), dtype=float64)
    unit_vector_p = np.array((0.5, 1.2, 0.9), dtype=np.float64)
    unit_vector_p = unit_vector_p / np.linalg.norm(unit_vector_p)
    unit_vector_j = np.array((-1.2, 0.5, 0), dtype=np.float64)
    unit_vector_j = unit_vector_j - unit_vector_p * np.dot(unit_vector_j, unit_vector_p)
    unit_vector_j = unit_vector_j / np.linalg.norm(unit_vector_j)
    unit_vector_k = np.cross(unit_vector_j, unit_vector_p)
    sampling_kernel = np.array((0.15, 0.7, 0.15,), dtype=float64)
    kernel_offsets = np.array(((-0.15, 0.), (0., -0.1), (0.15, 0.1)), dtype=float64).T
    kernel_offsets = np.ascontiguousarray(kernel_offsets)
    step_size = float64(0.5)
    set_num_threads(1)
    scalar_bound = float64(-3.5)
    _john_transform(projection, projection_offsets,
                    volume, volume_bounds,
                    volume_indexer, unit_vector_p,
                    unit_vector_j, unit_vector_k,
                    sampling_kernel, kernel_offsets,
                    step_size, scalar_bound)
    assert np.allclose(projection, np.array([[[3.6, 12.672],
                                              [2.4, 2.4]],
                                             [[4.34, 4.8],
                                              [2.4, 2.4]]]))


def test_john_transform_adjoint():
    projection = np.ones((2, 2, 2), dtype=float64)
    projection[:, 1, :] *= 1.5
    projection[1, :, 0] *= 2.7
    projection[0, :, :] *= 9.9
    projection_offsets = np.array((0.1, -0.1), dtype=float64)
    volume = np.zeros((1, 8, 2), dtype=float64)
    volume_bounds = np.array((2, 2, 2), dtype=float64)
    volume_indexer = np.array((4, 2, 1), dtype=float64)
    unit_vector_p = np.array((0.5, 1.2, 0.9), dtype=np.float64)
    unit_vector_p = unit_vector_p / np.linalg.norm(unit_vector_p)
    unit_vector_j = np.array((-1.2, 0.5, 0), dtype=np.float64)
    unit_vector_j = unit_vector_j - unit_vector_p * np.dot(unit_vector_j, unit_vector_p)
    unit_vector_j = unit_vector_j / np.linalg.norm(unit_vector_j)
    unit_vector_k = np.cross(unit_vector_j, unit_vector_p)
    sampling_kernel = np.array((0.15, 0.7, 0.15,), dtype=float64)
    kernel_offsets = np.array(((-0.01, 0.), (0., -0.01), (0.01, 0.01)), dtype=float64).T
    kernel_offsets = np.ascontiguousarray(kernel_offsets)
    step_size = float64(0.5)
    set_num_threads(1)
    scalar_bound = float64(-3.5)
    _john_transform_adjoint(projection, projection_offsets,
                            volume, volume_bounds,
                            volume_indexer, unit_vector_p,
                            unit_vector_j, unit_vector_k,
                            sampling_kernel, kernel_offsets,
                            step_size, scalar_bound)
    assert np.allclose(volume, np.array([[[2.025, 0.75],
                                          [2.7, 1.],
                                          [4.05, 1.5],
                                          [0., 0.],
                                          [14.85, 14.85],
                                          [9.9, 9.9],
                                          [14.85, 14.85],
                                          [0., 0.]]]))


def test_john_transform_2():
    projection = np.zeros((2, 2, 2), dtype=float64)
    projection_offsets = np.array((0.02, 0.05), dtype=float64)
    volume = np.ones((3, 3, 3, 2), dtype=float64) * 2.4
    volume[0, 2, 1, 0] = 1.6
    volume[2, 1, 1, 1] = 9.12
    unit_vector_p = np.array((0.5, 1.2, 0.9), dtype=np.float64)
    unit_vector_p = unit_vector_p / np.linalg.norm(unit_vector_p)
    unit_vector_j = np.array((-1.2, 0.5, 0), dtype=np.float64)
    unit_vector_j = unit_vector_j - unit_vector_p * np.dot(unit_vector_j, unit_vector_p)
    unit_vector_j = unit_vector_j / np.linalg.norm(unit_vector_j)
    unit_vector_k = np.cross(unit_vector_j, unit_vector_p)
    sampling_kernel = np.array((0.15, 0.7, 0.15,), dtype=float64)
    kernel_offsets = np.array(((0.001, 0.), (0., 0.04), (0.002, 0.03)), dtype=float64).T
    kernel_offsets = np.ascontiguousarray(kernel_offsets)
    step_size = float64(0.5)
    set_num_threads(1)
    john_transform(projection,
                   volume, unit_vector_p,
                   unit_vector_j, unit_vector_k,
                   step_size,
                   projection_offsets,
                   sampling_kernel, kernel_offsets)
    assert np.allclose(projection, np.array([[[7.2, 7.2],
                                              [8.4, 11.76]],
                                             [[8.4, 8.4],
                                              [7.2, 7.2]]]))


def test_john_transform_adjoint_2():
    projection = np.ones((2, 2, 2), dtype=float64)
    projection[1, :, 0] *= 0.2
    projection[:, 1, :] *= 3.5
    projection[:, :, 1] *= 2.1
    projection_offsets = np.array((0.02, 0.05), dtype=float64)
    volume = np.zeros((1, 2, 2, 2, 2), dtype=float64)
    unit_vector_p = np.array((0.5, 1.2, 0.9), dtype=np.float64)
    unit_vector_p = unit_vector_p / np.linalg.norm(unit_vector_p)
    unit_vector_j = np.array((-1.2, 0.5, 0), dtype=np.float64)
    unit_vector_j = unit_vector_j - unit_vector_p * np.dot(unit_vector_j, unit_vector_p)
    unit_vector_j = unit_vector_j / np.linalg.norm(unit_vector_j)
    unit_vector_k = np.cross(unit_vector_j, unit_vector_p)
    sampling_kernel = np.array((0.15, 0.7, 0.15,), dtype=float64)
    kernel_offsets = np.array(((0.001, 0.), (0., 0.04), (0.002, 0.03)), dtype=float64).T
    kernel_offsets = np.ascontiguousarray(kernel_offsets)
    step_size = float64(0.5)
    set_num_threads(1)
    john_transform_adjoint(projection,
                           volume, unit_vector_p,
                           unit_vector_j, unit_vector_k,
                           step_size,
                           projection_offsets,
                           sampling_kernel, kernel_offsets)
    assert np.allclose(volume, np.array([[[[[0.17, 1.785],
                                            [0.13, 1.365]],
                                           [[0.7, 7.35],
                                            [0.1, 1.05]]],
                                          [[[2.1, 4.41],
                                            [1.15, 2.415]],
                                           [[3.5, 7.35],
                                            [0., 0.]]]]]))
