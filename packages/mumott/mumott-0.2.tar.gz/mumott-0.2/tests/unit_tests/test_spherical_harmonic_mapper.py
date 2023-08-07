import pytest
import numpy as np
from mumott.core.spherical_harmonic_mapper import SphericalHarmonicMapper


@pytest.mark.parametrize('test_input,outcome',
                         [
                             (dict(max_order=4,
                                   polar_resolution=7,
                                   azimuthal_resolution=4,
                                   polar_zero=0,
                                   azimuthal_zero=0,
                                   ), None),
                             (dict(max_order=8,
                                   polar_resolution=13,
                                   azimuthal_resolution=21,
                                   polar_zero=np.pi / 3,
                                   azimuthal_zero=np.pi / 8,
                                   ), None),
                             (dict(max_order=6,
                                   polar_resolution=128,
                                   azimuthal_resolution=256,
                                   polar_zero=0,
                                   azimuthal_zero=0,
                                   ), None),
                         ])
def test_init(test_input, outcome):
    if outcome is None:
        S = SphericalHarmonicMapper(**test_input)
        assert S.max_order == test_input['max_order']
        assert np.all(S.orders == [i for i in range(0, test_input['max_order'] + 1, 2)
                                   for j in range(2 * i + 1)])
        assert np.all(S.degrees == [j for i in range(0, test_input['max_order'] + 1, 2)
                                    for j in range(-i, i + 1)])
        assert np.all(S.phi.shape == (test_input['polar_resolution'], test_input['azimuthal_resolution']))
        assert np.all(S.theta.shape == (test_input['polar_resolution'], test_input['azimuthal_resolution']))
        assert S.polar_zero == test_input['polar_zero']
        assert S.azimuthal_zero == test_input['azimuthal_zero']
        assert np.all(S.theta_interpolator.shape ==
                      (test_input['polar_resolution'], test_input['azimuthal_resolution'] - 1))
        assert np.all(S.phi_interpolator.shape ==
                      (test_input['polar_resolution'], test_input['azimuthal_resolution'] - 1))
        assert np.all(S.map.shape == (test_input['polar_resolution'],
                                      test_input['azimuthal_resolution'],
                                      (test_input['max_order'] // 2 + 1) * (test_input['max_order'] + 1)))
        if (test_input['azimuthal_resolution'] == 128) & \
           (test_input['polar_resolution'] == 256) & (test_input['max_order'] == 6):
            coefficients = np.array([-0.6853447, 1.79851744, -1.23394354, -0.20025308, -2.01433032,
                                     -0.63057234, -0.68189296, 0.09721236, 1.25074053, 0.02795743,
                                     0.9053322, 0.75103781, -3.11883902, 1.96487535, -1.16443111,
                                     -0.06631476, -0.67329735, -0.48743056, 0.09240111, 1.36270693,
                                     0.84001768, -2.31092023, -0.21464363, 1.04476394, -0.77695792,
                                     -1.58423597, 0.87403145, 0.70022989])
            amplitudes = S.get_amplitudes(coefficients)
            fit = S.get_harmonic_coefficients(amplitudes[:, :-1])
            expected = np.array([-0.67149577, 1.80497953, -1.23877695, -0.18810264, -2.02513128,
                                 -0.61917466, -0.68518089, 0.09803488, 1.253694, 0.02785181,
                                 0.8857664, 0.76285412, -3.09020449, 1.9667663, -1.16317915,
                                 -0.06656277, -0.67505851, -0.49411828, 0.09223364, 1.36925961,
                                 0.84341165, -2.30343654, -0.21779937, 1.02573042, -0.77279774,
                                 -1.54228925, 0.87009572, 0.70290764])
            assert np.allclose(fit, expected)
    else:
        with pytest.raises(outcome):
            _ = SphericalHarmonicMapper(**test_input)


def test_setter():
    S = SphericalHarmonicMapper(max_order=2)
    S.max_order = 6
    assert S.max_order == 6
    assert S.orders.size == 28
    assert np.all(S.orders == [i for i in range(0, 7, 2) for j in range(2 * i + 1)])
    assert np.all(S.degrees == [j for i in range(0, 7, 2)
                                for j in range(-i, i + 1)])
