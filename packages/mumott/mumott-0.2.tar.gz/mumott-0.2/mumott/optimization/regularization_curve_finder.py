from typing import Tuple

import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np

from mumott.data_handling.reconstruction_parameters import ReconstructionParameters
from .regularizer import Regularizer
from .optimization_timer import OptimizationTimer


class RegularizationCurveFinder:

    # todo: Add docstrings
    def __init__(self,
                 regularizer: Regularizer,
                 reconstruction_parameters: ReconstructionParameters,
                 multiplier_range: Tuple[float, float] = (-2., 2.),
                 number_of_iterations: int = 10,
                 regularization_index: int = 0):
        self._optimization_timer = OptimizationTimer(reconstruction_parameters,
                                                     regularizer)
        self._time_per_iteration = []
        self._regularizer = regularizer
        self._reconstruction_parameters = reconstruction_parameters
        self._multipliers = np.logspace(*multiplier_range, number_of_iterations)
        self._iteration = 0
        self._number_of_iterations = number_of_iterations
        self._continue_loop = True
        self._regularization_index = regularization_index
        self._reg_all = []
        self._reg_specific = []
        self._residual = []
        self._actual_coefficient = []
        plt.ion()
        self._fig, self._axes = plt.subplots(2, 2)
        colors = get_cmap('cet_glasbey')
        self._l1, = self._axes[0, 0].loglog(self._residual, self._reg_all,
                                            '--o', color=colors(25), markerfacecolor=colors(25))
        self._l2, = self._axes[0, 1].loglog(self._residual, self._reg_specific, '-.v',
                                            color=colors(66), markerfacecolor=colors(66))
        self._l3, = self._axes[1, 0].loglog(self._actual_coefficient, self._reg_specific,
                                            ':s', color=colors(94), markerfacecolor=colors(94))
        self._l4, = self._axes[1, 1].loglog(self._actual_coefficient,
                                            self._time_per_iteration, '-+', color=colors(5),
                                            markerfacecolor=colors(5))
        self._axes[0, 0].set_xlabel('Residual')
        self._axes[0, 1].set_xlabel('Residual')
        self._axes[1, 0].set_xlabel('Coefficient')
        self._axes[1, 1].set_xlabel('Coefficient')
        self._axes[0, 0].set_ylabel('Regularization value (all)')
        self._axes[0, 1].set_ylabel('Regularization value ({0})'.format(
                self._regularizer.regularizer_dict_list[self._regularization_index]['function_name']))
        self._axes[1, 0].set_ylabel('Regularization value ({0})'.format(
                self._regularizer.regularizer_dict_list[self._regularization_index]['function_name']))
        self._axes[1, 1].set_ylabel('Time to convergence (Minutes)')
        self._fig.canvas.draw()
        self._fig.canvas.flush_events()
        self._regularizer.rescale_coefficients(self._multipliers[0], self._regularization_index)

    def next_iteration(self):
        self._time_per_iteration.append(self._optimization_timer.time_since_start)
        self._actual_coefficient.append(
            self._regularizer.last_iter_reg_coefficients[self._regularization_index])
        self._reg_all.append(self._regularizer.last_iter_reg_all)
        self._reg_specific.append(self._regularizer.last_iter_reg_specific[self._regularization_index])
        self._residual.append(self._reconstruction_parameters.reconstruction_output.residual)
        self._l1.set_xdata(self._residual)
        self._l1.set_ydata(self._reg_all)
        self._l2.set_xdata(self._residual)
        self._l2.set_ydata(self._reg_specific)
        self._l3.set_xdata(self._actual_coefficient)
        self._l3.set_ydata(self._reg_specific)
        self._l4.set_xdata(self._actual_coefficient)
        self._l4.set_ydata(self._time_per_iteration)
        self._optimization_timer.reset()
        self._axes[0, 0].relim()
        self._axes[0, 1].relim()
        self._axes[1, 0].relim()
        self._axes[1, 1].relim()
        self._axes[0, 0].autoscale_view()
        self._axes[1, 0].autoscale_view()
        self._axes[0, 1].autoscale_view()
        self._axes[1, 1].autoscale_view()
        self._fig.canvas.draw()
        self._fig.canvas.flush_events()

        self._iteration += 1
        if self._iteration == self._number_of_iterations:
            self._continue_loop = False
        else:
            self._regularizer.rescale_coefficients(
                self._multipliers[self._iteration] / self._multipliers[self._iteration - 1],
                self._regularization_index)

    @property
    def continue_loop(self) -> bool:
        return self._continue_loop
