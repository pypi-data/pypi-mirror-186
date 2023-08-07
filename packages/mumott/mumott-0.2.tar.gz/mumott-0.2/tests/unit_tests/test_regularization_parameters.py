import pytest
import numpy as np
from mumott.optimization.regularization_parameters import RegularizationParameters


@pytest.mark.parametrize('test_input,outcome',
                         [
                             (dict(function_name='myfunc',
                                   orders=(0, 2, 3),
                                   regularization_coefficients=(1, 5.2, -1.0, 4),
                                   dampening_factor=(0.1, 0.4, -0.9),
                                   characteristic_ratio=(5.0, -2.0),
                                   ratio_upper_bound=(-9.3, 1.2),
                                   reg_callable=lambda x: 1 / x,
                                   ), None),
                             (dict(function_name='myfunc2',
                                   orders=[0, 2, 3],
                                   regularization_coefficients=(1, 5.2, -1.0, 4),
                                   dampening_factor=np.array([0.1, 0.4, -0.9]),
                                   characteristic_ratio=1.0,
                                   ratio_upper_bound=(-9.3, 1.2),
                                   reg_callable=lambda x: 1 / x ** 2,
                                   ), None),
                         ])
def test_init(test_input, outcome):
    if outcome is None:
        regpars = RegularizationParameters(**test_input)
        assert regpars.function_name == test_input['function_name']
        assert np.all(regpars.orders == test_input['orders'])
        assert np.all(regpars.regularization_coefficients == test_input['regularization_coefficients'])
        assert np.all(regpars.dampening_factor == test_input['dampening_factor'])
        assert np.all(regpars.characteristic_ratio == test_input['characteristic_ratio'])
        assert np.all(regpars.ratio_upper_bound == test_input['ratio_upper_bound'])
        assert regpars.reg_callable == test_input['reg_callable']
    else:
        with pytest.raises(outcome):
            _ = RegularizationParameters(**test_input)


def test_setter():
    funcname = 'blabla'
    regpars = RegularizationParameters(funcname)
    assert regpars.function_name == funcname
    newval = (1.0, 2.0)
    regpars.dampening_factor = newval
    assert np.all(regpars.dampening_factor == newval)
