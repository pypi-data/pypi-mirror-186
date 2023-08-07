""" Container module for the Regularizer class. """

from typing import List

import numpy as np
from numpy.typing import ArrayLike

from mumott.data_handling.reconstruction_parameters import ReconstructionParameters
from .regularization_parameters import RegularizationParameters


class Regularizer:
    """ This class implements regularization of a SAXSTT reconstruction, when
    provided with a :class:`mumott.data_handling.ReconstructionParameters` and a
    list of :class:`mumott.optimization.RegularizationParameters` objects, and handed
    to :class:`mumott.optimization.Optimizer`.

    Parameters
    ----------
    reconstruction_parameters : ReconstructionParameters
        A :class:`mumott.data_handling.ReconstructionParameters` object created
        from your dataset.
    regularization_parameter_list : list(RegularizationParameters)
        A list consisting of :class:`mumott.optimization.RegularizationParameters` objects
        for each regularizing function that should be applied.
    """
    # todo: Consider refactoring of the _regularize_* methods. There is a lot of repetition.
    def __init__(self,
                 reconstruction_parameters: ReconstructionParameters,
                 regularization_parameter_list: List[RegularizationParameters]):
        self._check_input_typing(regularization_parameter_list)
        self._tiny = np.finfo(np.float64).tiny
        self._regularization_parameter_list = regularization_parameter_list
        self._reconstruction_parameters = reconstruction_parameters
        self._regularizer_calls = 0
        self._last_iter_reg_all = 0.0
        self._last_iter_reg_specific = []
        self._refresh_order_indices()
        for params in self._regularization_parameter_list:
            if params.orders == (-1,):
                params.orders = self._orders
            for key, entry in params.__dict__.items():
                if isinstance(entry, tuple):
                    if len(entry) < len(params.orders):
                        temp = list(entry)
                        temp.extend(entry[-1]
                                    for i in range(len(params.orders)-len(entry)))
                        params.__dict__[key] = tuple(temp)
            if params.function_name == 'hybrid':
                params.reg_callable = self._regularize_hybrid
            if params.function_name == 'rms':
                params.reg_callable = self._regularize_rms
            if params.function_name == 'l2':
                params.reg_callable = self._regularize_l2
            if params.function_name == 'nearest_neighbor_l2':
                params.reg_callable = self._regularize_nearest_neighbor_l2
            if params.function_name == 'partial_rms':
                params.reg_callable = self._regularize_partial_rms
            if params.function_name == 'exponential_l2':
                params.reg_callable = self._regularize_exponential_l2
            if params.function_name == 'exponential_rms':
                params.reg_callable = self._regularize_exponential_rms
            if params.function_name == 'echelon_rms':
                params.reg_callable = self._regularize_echelon_rms
            if params.function_name == 'echelon_l2':
                params.reg_callable = self._regularize_echelon_l2

    def _check_input_typing(self,
                            regularization_parameter_list: List[RegularizationParameters]):
        for i, item in enumerate(regularization_parameter_list):
            if not isinstance(item, RegularizationParameters):
                raise TypeError('regularization_parameters must consist only of'
                                f' RegularizationParameters entries but entry {i} is not valid')

    def _regularize_partial_rms(self,
                                S: ArrayLike,
                                params: RegularizationParameters):
        if self._get_gradient:
            S_grad = np.zeros_like(S)
        inds = self._l_indices < 0
        for ll in params.orders:
            inds = (inds) | (self._l_indices == ll)
        rms = np.sqrt(np.sum((S[:, inds] ** 2), axis=1))
        errors = params.regularization_coefficients[0] * np.sum(rms)
        if self._get_gradient:
            S_grad[:, inds] = params.regularization_coefficients[0] * \
                S[:, inds] / (self._tiny + rms.reshape(-1, 1))
            return errors, S_grad.reshape(-1, 1)
        else:
            return errors

    def _regularize_hybrid(self,
                           S: ArrayLike,
                           params: RegularizationParameters):
        if self._get_gradient:
            S_grad = np.zeros_like(S)
        errors = 0.0
        for i, ll in enumerate(params.orders):
            inds = (self._l_indices == ll)
            errors += params.regularization_coefficients[i] * \
                np.sum((np.sqrt(np.sum((S[:, inds] ** 2), axis=1))))
            if self._get_gradient:
                S_grad[:, inds] = (params.regularization_coefficients[i] * S[:, inds]) / \
                    (self._tiny + np.sqrt(np.sum((S[:, inds] ** 2), axis=1)).reshape(-1, 1))

        if self._get_gradient:
            return errors, S_grad.reshape(-1, 1)
        else:
            return errors

    def _regularize_rms(self,
                        S: ArrayLike,
                        params: RegularizationParameters):
        if self._get_gradient:
            S_grad = (params.regularization_coefficients[0] *
                      S / (self._tiny + np.sqrt(np.sum((S ** 2), axis=1)).reshape(-1, 1)))
            return params.regularization_coefficients[0] * \
                np.sum((np.sqrt(np.sum((S ** 2), axis=1)))), S_grad.reshape(-1, 1)
        else:
            return params.regularization_coefficients[0]*np.sum((np.sqrt(np.sum((S ** 2), axis=1))))

    def _regularize_l2(self,
                       S: ArrayLike,
                       params: RegularizationParameters):
        if self._get_gradient:
            S_grad = np.zeros_like(S)
        errors = 0.0
        for i, ll in enumerate(params.orders):
            inds = (self._l_indices == ll)
            errors += params.regularization_coefficients[i] * np.sum(S[:, inds] ** 2)
            if self._get_gradient:
                S_grad[:, inds] = 2 * params.regularization_coefficients[i] * S[:, inds]

        if self._get_gradient:
            return errors, S_grad.reshape(-1, 1)
        else:
            return errors

    def _regularize_echelon_l2(self,
                               S: ArrayLike,
                               params: RegularizationParameters):
        if self._get_gradient:
            S_grad = np.zeros_like(S)
        errors = 0.0
        old_order_indices = None
        for i, ll in enumerate(params.orders):
            order_indices = (self._l_indices == ll)
            if i > 0:
                s1 = 1. / (
                    self._tiny + params.dampening_factor[i] +
                    np.sum(S[:, old_order_indices] ** 2, axis=1)).reshape(-1, 1)
                s2 = np.sum(S[:, order_indices] ** 2, axis=1).reshape(-1, 1)
                ratio = (s2 * s1 / params.characteristic_ratio[i]).clip(
                    0.0, params.ratio_upper_bound[i])
                exp_val = np.exp(ratio)
                errors += params.regularization_coefficients[i] * np.sum(exp_val - 1.0)
                if self._get_gradient:
                    S_grad[:, order_indices] += 2 * params.regularization_coefficients[i] * exp_val * \
                        S[:, order_indices] * (s1 / params.characteristic_ratio[i])
                    S_grad[:, old_order_indices] -= 2 * params.regularization_coefficients[i] * exp_val * \
                        S[:, old_order_indices] * ratio * (s1)
            old_order_indices = (self._l_indices == ll)
        if self._get_gradient:
            return errors, S_grad.reshape(-1, 1)
        else:
            return errors

    def _regularize_echelon_rms(self,
                                S: ArrayLike,
                                params: RegularizationParameters):
        if self._get_gradient:
            S_grad = np.zeros_like(S)
        errors = 0.0
        old_order_indices = None
        for i, ll in enumerate(params.orders):
            order_indices = (self._l_indices == ll)
            if i > 0:
                denom_rms = \
                    (self._tiny + np.sqrt(np.sum(S[:, old_order_indices] ** 2, axis=1))).reshape(-1, 1)
                s1 = 1. / (params.dampening_factor[i] + denom_rms)
                s2 = np.sqrt(np.sum(S[:, order_indices] ** 2, axis=1)).reshape(-1, 1)
                ratio = (s2 * s1 / params.characteristic_ratio[i]).clip(
                    0.0, params.ratio_upper_bound[i])
                exp_val = np.exp(ratio)
                errors += params.regularization_coefficients[i] * np.sum(exp_val - 1.0)
                if self._get_gradient:
                    S_grad[:, order_indices] += params.regularization_coefficients[i] * exp_val * \
                        S[:, order_indices] * (s1 / (self._tiny + s2 * params.characteristic_ratio[i]))
                    S_grad[:, old_order_indices] -= params.regularization_coefficients[i] * exp_val * \
                        S[:, old_order_indices] * ratio * (s1) / denom_rms
            old_order_indices = (self._l_indices == ll)
        if self._get_gradient:
            return errors, S_grad.reshape(-1, 1)
        else:
            return errors

    def _regularize_exponential_l2(self,
                                   S: ArrayLike,
                                   params: RegularizationParameters):
        if self._get_gradient:
            S_grad = np.zeros_like(S)
        errors = 0.0
        old_order_indices = None
        for i, ll in enumerate(params.orders):
            print(params.orders)
            order_indices = (self._l_indices >= ll)
            if i > 0:
                s1 = 1.0 / (params.dampening_factor[i] +
                            np.sum(S[:, old_order_indices] ** 2, axis=1)).reshape(-1, 1)
                s2 = np.sum(S[:, order_indices] ** 2, axis=1).reshape(-1, 1)
                ratio = (s2 * s1 / params.characteristic_ratio[i]
                         ).clip(0.0, params.ratio_upper_bound[i])
                exp_val = np.exp(ratio)
                errors += params.regularization_coefficients[i] * np.sum(exp_val - 1.0)
                if self._get_gradient:
                    S_grad[:, order_indices] += S[:, order_indices] * 2 * \
                        params.regularization_coefficients[i] * exp_val * \
                        s1 / params.characteristic_ratio[i]
                    S_grad[:, old_order_indices] -= S[:, old_order_indices] * 2 * \
                        params.regularization_coefficients[i] * exp_val * ratio * (s1)
            old_order_indices = (self._l_indices == ll)
        if self._get_gradient:
            return errors, S_grad.reshape(-1, 1)
        else:
            return errors

    def _regularize_exponential_rms(self,
                                    S: ArrayLike,
                                    params: RegularizationParameters):
        if self._get_gradient:
            S_grad = np.zeros_like(S)
        errors = 0.0
        old_order_indices = None
        for i, ll in enumerate(params.orders):
            order_indices = (self._l_indices >= ll)
            if i > 0:
                denom_rms = (self._tiny +
                             np.sqrt(np.sum(S[:, old_order_indices] ** 2, axis=1))).reshape(-1, 1)
                s1 = 1. / (params.dampening_factor[i] +
                           denom_rms)
                s2 = np.sqrt(np.sum(S[:, order_indices] ** 2, axis=1)).reshape(-1, 1)
                ratio = (s2 * s1 / params.characteristic_ratio[i]).clip(
                         0.0, params.ratio_upper_bound[i])
                exp_val = np.exp(ratio)
                errors += params.regularization_coefficients[i] * np.sum(exp_val - 1.0)
                if self._get_gradient:
                    S_grad[:, order_indices] += params.regularization_coefficients[i] * exp_val * \
                        S[:, order_indices] * s1 / (self._tiny + s2 * params.characteristic_ratio[i])
                    S_grad[:, old_order_indices] -= params.regularization_coefficients[i] * exp_val * \
                        S[:, old_order_indices] * ratio * s1 / denom_rms
            old_order_indices = (self._l_indices == ll)
        if self._get_gradient:
            return errors, S_grad.reshape(-1, 1)
        else:
            return errors

    def _regularize_nearest_neighbor_l2(self,
                                        S: ArrayLike,
                                        params: RegularizationParameters):
        S = S.reshape(self._dimensions)
        if self._get_gradient:
            S_grad = np.zeros_like(S)
        errors = 0.0
        for i, ll in enumerate(params.orders):
            inds = (self._l_indices == ll)
            a0 = S[1:-1, 1:-1, 1:-1, inds]
            a0 = a0.reshape(a0.shape[:3] + (-1,))

            a1 = S[:-2, 1:-1, 1:-1, inds].reshape(a0.shape[:3] + (-1,))
            a2 = S[1:-1, :-2, 1:-1, inds].reshape(a0.shape[:3] + (-1,))
            a3 = S[1:-1, 1:-1, :-2, inds].reshape(a0.shape[:3] + (-1,))

            a4 = S[2:, 1:-1, 1:-1, inds].reshape(a0.shape[:3] + (-1,))
            a5 = S[1:-1, 2:, 1:-1, inds].reshape(a0.shape[:3] + (-1,))
            a6 = S[1:-1, 1:-1, 2:, inds].reshape(a0.shape[:3] + (-1,))
            an_sum = 2 * (a1 + a2 + a3 + a4 + a5 + a6)
            corr = params.regularization_coefficients[i] * np.sum((
                6 * a0 * a0 + a1 * a1 + a2 * a2 +
                a3 * a3 + a4 * a4 + a5 * a5 + a6 * a6 - a0 * an_sum), axis=3)
            errors += np.sum(corr)
            if self._get_gradient:
                S_grad[1:-1, 1:-1, 1:-1, inds] = params.regularization_coefficients[i] * (12 * a0 - an_sum)
        if self._get_gradient:
            return errors, S_grad.reshape(-1, 1)
        else:
            return errors

    def rescale_coefficients(self,
                             multiplier: float,
                             index: int):
        self._regularization_parameters[index].regularization_coefficients = \
            np.multiply(self._regularization_parameters[index].regularization_coefficients, multiplier)

    def apply_regularization(self,
                             S: ArrayLike,
                             get_gradient: bool = True):
        self._get_gradient = get_gradient
        self._refresh_order_indices()
        error = 0.0
        error_normed = 0.0
        if self._get_gradient:
            grad = np.zeros((S.size, 1))
            glist = []
        elist = []
        elist_normed = []
        coefficients = []
        self._regularizer_calls += 1
        for params in self._regularization_parameter_list:
            if self._get_gradient:
                e, g = params.reg_callable(S, params)
                error += e
                error_normed += e / params.regularization_coefficients[0]
                coefficients.append(params.regularization_coefficients[0])
                grad += g
                elist.append(e)
                elist_normed.append(e / params.regularization_coefficients[0])
                glist.append(np.max(g))
            else:
                e = params.reg_callable(S, params)
                error += e
                elist.append(e)
                elist_normed.append(e / params.regularization_coefficients[0])
                error_normed += e / params.regularization_coefficients[0]
                coefficients.append(params.regularization_coefficients[0])
        self._last_iter_reg_all = error_normed
        self._last_iter_reg_specific = elist_normed
        self._last_iter_reg_coefficients = coefficients
        if self._get_gradient:
            print('Regularizer call: {}'.format(self._regularizer_calls))
            return error, elist, grad, glist
        else:
            return error, elist

    def _refresh_order_indices(self):
        self._l_indices = self._reconstruction_parameters.spherical_harmonic_parameters.l_indices
        self._l_max = self._reconstruction_parameters.spherical_harmonic_parameters.l_max
        l_max = self._reconstruction_parameters.spherical_harmonic_parameters.l_max
        self._orders = [ll for ll in range(0, l_max + 1, 2)]
        self._dimensions = (tuple(self._reconstruction_parameters.projection_parameters.volume_shape) +  # noqa
                            (self._reconstruction_parameters.spherical_harmonic_parameters.number_of_coefficients,))  # noqa

    @property
    def last_iter_reg_all(self) -> float:
        return self._last_iter_reg_all

    @property
    def last_iter_reg_specific(self) -> List[float]:
        return self._last_iter_reg_specific

    @property
    def last_iter_reg_coefficients(self) -> List[float]:
        return self._last_iter_reg_coefficients

    @property
    def regularization_parameter_list(self) -> List[RegularizationParameters]:
        return self._regularization_parameter_list
