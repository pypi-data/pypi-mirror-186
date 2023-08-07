""" Container module for the dataclass RegularizationParameters. """

from dataclasses import dataclass
from typing import Tuple, Callable


@dataclass
class RegularizationParameters:
    """
    This dataclass defines the parameters used by the Regularizer class.

    Parameters
    ----------
    function_name : str
        The name of the :class:`mumott.optimization.Regularizer` function that this set of
        parameters should apply to. Possible values are ``hybrid``, ``rms``, ``l2``,
        ``nearest_neighbor_l2``, ``partial_rms``, ``exponential_l2``, ``exponential_rms``,
        ``echelon_rms``, and ``echelon_l2``.
    orders : tuple(int)
        The spherical harmonic orders that the :class:`mumott.optimization.Regularizer`
        function should apply to.
        Its precise application depends on the function, in some cases higher
        or lower orders than specified may also be affected.
    regularization_coefficients : tuple(float)
        The coefficient that is applied to each order. Note that not all
        regularizing functions are resolved by order; in these cases the
        first entry will be used. If fewer entries than the number of orders
        are specified, the last entry will be used for the remaining orders.
        This applies to all following which can be specified for each order.
    dampening_factor : tuple(float)
        The dampening factor ``d`` in the expression ``a / (b + d)`` in certain
        :class:`mumott.optimization.Regularizer` functions, for each order.
    characteristic_ratio : tuple(float)
        The characteristic ratio ``c`` in ``(a / (b * c))`` in certain
        :class:`mumott.optimization.Regularizer` functions, for each order.
    ratio_upper_bound : tuple(float)
        The upper bound ``u`` in the expression ``(a / b).clip(0, u)`` in certain
        :class:`mumott.optimization.Regularizer` functions, for each order.
    """
    function_name: str
    orders: Tuple[int, ...] = (-1,)
    regularization_coefficients: Tuple[float, ...] = (0,)
    dampening_factor: Tuple[float, ...] = (0.1,)
    characteristic_ratio: Tuple[float, ...] = (1.,)
    ratio_upper_bound: Tuple[float, ...] = (1.5,)
    reg_callable: Callable = lambda *args: None
