import pytest
import numpy as np
from mumott.core.projection_parameters import ProjectionParameters


default_kwargs = dict(rotation_angles_for_principal_axis=np.array([0, 0.5 * np.pi, 1.0, 0]),
                      rotation_angles_for_secondary_axis=np.array([np.pi / 8,
                                                                   np.pi / 6,
                                                                   np.pi / 5,
                                                                   np.pi / 4]),
                      detector_segment_phis=np.arange(0, np.pi, np.pi / 10),
                      offsets_j=np.array([-2.4, 1.1, -3.5, 6.6]),
                      offsets_k=np.array([3.1, -1.5, 5.2, 3.6]),
                      volume_shape=np.array([10, 10, 20]),
                      data_shape=np.array([(10, 20, 10),
                                           (12, 18, 10),
                                           (14, 16, 10),
                                           (15, 15, 10)]),
                      integration_step_size=1.0)


def test_init():
    test_input = default_kwargs.copy()
    pp = ProjectionParameters(**test_input)
    pp.__repr__  # sanity check
    assert pp.number_of_projections == len(test_input['data_shape'])
    assert pp.number_of_voxels == 2000
    assert np.all(pp.data_shape == test_input['data_shape'])
    assert np.all(pp.volume_shape == test_input['volume_shape'])

    test_input = default_kwargs.copy()
    test_input['rotation_angles_for_principal_axis'] = np.array([0, 0.5 * np.pi])
    with pytest.raises(ValueError) as e:
        _ = ProjectionParameters(**test_input)
        assert 'rotation_angles_for_principal_axis' in str(e)

    test_input = default_kwargs.copy()
    test_input['rotation_angles_for_secondary_axis'] = np.array([0, 0.5 * np.pi])
    with pytest.raises(ValueError) as e:
        _ = ProjectionParameters(**test_input)
        assert 'rotation_angles_for_secondary_axis' in str(e)

    test_input = default_kwargs.copy()
    test_input['offsets_j'] = np.arange(10)
    with pytest.raises(ValueError) as e:
        _ = ProjectionParameters(**test_input)
        assert 'offsets_j' in str(e)

    test_input = default_kwargs.copy()
    test_input['offsets_k'] = np.arange(10)
    with pytest.raises(ValueError) as e:
        _ = ProjectionParameters(**test_input)
        assert 'offsets_k' in str(e)

    test_input = default_kwargs.copy()
    test_input['volume_shape'] = np.arange(10)
    with pytest.raises(ValueError) as e:
        _ = ProjectionParameters(**test_input)
        assert 'volume_shape' in str(e)

    test_input = default_kwargs.copy()
    test_input['data_shape'] = np.reshape(range(12), (6, 2))
    with pytest.raises(ValueError) as e:
        _ = ProjectionParameters(**test_input)
        assert 'data_shape' in str(e)
        assert 'Length' in str(e)

    test_input = default_kwargs.copy()
    test_input['data_shape'] = np.reshape(range(8), (4, 2))
    with pytest.raises(ValueError) as e:
        _ = ProjectionParameters(**test_input)
        assert 'data_shape' in str(e)
        assert 'three-dimensional' in str(e)

    test_input = default_kwargs.copy()
    test_input['detector_segment_phis'] = np.arange(30)
    with pytest.raises(ValueError) as e:
        _ = ProjectionParameters(**test_input)
        assert 'detector_segment_phis' in str(e)


def test_probed_theta_phi():
    test_input = default_kwargs.copy()
    pp = ProjectionParameters(**test_input)
    target = (np.array([[1.57079633, 1.28127399, 0.99673983, 0.72660482, 0.49774455,
                         0.39269908, 0.49774455, 0.72660482, 0.99673983, 1.28127399],
                        [1.57079633, 1.29987781, 1.03673075, 0.7945173, 0.60299801,
                         0.52359878, 0.60299801, 0.7945173, 1.03673075, 1.29987781],
                        [1.57079633, 1.31811607, 1.07523189, 0.85726398, 0.69286232,
                         0.62831853, 0.69286232, 0.85726398, 1.07523189, 1.31811607],
                        [1.57079633, 1.35051105, 1.14216434, 0.96177941, 0.83321678,
                         0.78539816, 0.83321678, 0.96177941, 1.14216434, 1.35051105]]),
              np.array([[0., 0.12370646, 0.27118636, 0.48479328, 0.86685051,
                         1.57079633, 2.27474214, 2.65679938, 2.87040629, 3.01788619],
                        [1.57079633, 1.73184911, 1.91924483, 2.17355271, 2.56533035,
                         3.14159265, -2.56533035, -2.17355271, -1.91924483, -1.73184911],
                        [1., 1.18871053, 1.40360657, 1.68021498, 2.06581636,
                         2.57079633, 3.07577629, -2.82180763, -2.54519922, -2.33030318],
                        [0., 0.22583371, 0.47458158, 0.77184216, 1.14006552,
                         1.57079633, 2.00152713, 2.36975049, 2.66701107, 2.91575894]]))

    results = (pp.probed_theta, pp.probed_phi)
    assert len(results) == 2
    assert np.all([np.allclose(r, t) for r, t in zip(target, results)])


def test_project():
    test_input = default_kwargs.copy()
    test_input['offsets_j'] *= 0.01
    test_input['offsets_k'] *= 0.01
    test_input['volume_shape'] = np.array((2, 2, 2))
    test_input['integration_step_size'] = 0.5
    test_input['data_shape'] = np.array([(2, 2, 2),
                                         (2, 2, 2),
                                         (2, 2, 2),
                                         (2, 2, 2)])
    test_input['detector_segment_phis'] = np.array((0, np.pi))
    pp = ProjectionParameters(**test_input)
    vol = np.ones((2, 2, 2, 2), dtype=np.float64)
    vol[:, 1, :, 0] *= 0.7
    vol[0, :, 1, :] *= 0.7
    proj = pp.project(vol, 1, None, 1)
    assert np.allclose(proj, np.array([[[1.5, 1.5],
                                        [1.35, 1.35]],
                                       [[1.05, 1.5],
                                        [0.945, 1.35]]]))


def test_adjoint():
    test_input = default_kwargs.copy()
    test_input['offsets_j'] *= 0.01
    test_input['offsets_k'] *= 0.01
    test_input['volume_shape'] = np.array((2, 2, 2))
    test_input['integration_step_size'] = 0.5
    test_input['data_shape'] = np.array([(2, 2, 2),
                                         (2, 2, 2),
                                         (2, 2, 2),
                                         (2, 2, 2)])
    test_input['detector_segment_phis'] = np.array((0, np.pi))
    pp = ProjectionParameters(**test_input)
    proj = np.ones((2, 2, 2), dtype=np.float64)
    proj[:, 0, :] += 0.4
    proj[1, :, 1] *= 1.7
    proj[0, :, :] *= 1.3
    vol = pp.adjoint(proj, 1, None, 1)
    assert np.allclose(vol, np.array([[[[0.91, 0.91],
                                        [0.65, 0.65]],
                                       [[0.7, 1.19],
                                        [0.5, 0.85]]],
                                      [[[1.82, 1.82],
                                        [1.3, 1.3]],
                                       [[1.4, 2.38],
                                        [1., 1.7]]]]))


def test_integration_step_size():
    test_input = default_kwargs.copy()
    pp = ProjectionParameters(**test_input)
    assert pp.integration_step_size == test_input['integration_step_size']

    for value in [2, 6, 9.4]:
        pp.integration_step_size = value
        assert pp.integration_step_size == value


def test_calculate_basis_vectors():
    # todo: Implement a more extensive test for _calculate_basis_vectors.
    pass
