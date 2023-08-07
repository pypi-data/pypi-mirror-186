import time
from mumott.data_handling.reconstruction_parameters import ReconstructionParameters
from .regularizer import Regularizer


class OptimizationTimer():

    # todo: Add docstrings and type hinting.
    def __init__(self,
                 reconstruction_parameters: ReconstructionParameters,
                 regularizer: Regularizer = None):
        self._start_time = time.time()
        self._reconstruction_parameters = reconstruction_parameters
        self._regularizer = regularizer
        self._residual_list = []
        self._regerror_list = []
        self._time_list = []

    def _update_residual(self) -> None:
        self._residual_list.append(self._reconstruction_parameters.reconstruction_output.residual)

    def update(self) -> None:
        self._update_residual()
        if self._regularizer is not None:
            self._update_regularization_value()
        self._time_list.append(self.time_since_start)

    def reset(self) -> None:
        self._start_time = time.time()
        self._residual_list = []
        self._regerror_list = []
        self._time_list = []

    def _update_regularization_value(self) -> None:
        self._regerror_list.append(self._regularizer.last_iter_reg_all)

    @property
    def time_list(self) -> list:
        return self._time_list

    @property
    def residual_list(self) -> list:
        return self._residual_list

    @property
    def regerror_list(self) -> list:
        return self._regerror_list

    @property
    def time_since_start(self) -> float:
        return (time.time()-self._start_time)/60.
