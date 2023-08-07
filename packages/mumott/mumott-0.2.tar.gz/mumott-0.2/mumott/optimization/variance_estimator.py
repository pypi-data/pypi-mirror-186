""" Container for class VarianceEstimator. """
import logging

import numpy as np
import matplotlib.pyplot as plt

from typing import Tuple
from numpy.typing import NDArray

from mumott.data_handling.reconstruction_parameters import ReconstructionParameters
from mumott.output_handling.projection_viewer import ProjectionViewer


class VarianceEstimator:
    """
    Class for estimating data variance to aid in optimization,
    and applying this to the weights used in computing the objective
    function and gradient.

    Parameters
    ----------
    reconstruction_parameters : ReconstructionParameters
        A :class:`ReconstructionParameters
        <mumott.data_handling.reconstruction_parameters.ReconstructionParameters>`
        object. See docstring for details.
    pixel_rectification : numpy.ndarray(dtype=float)
        An array containing the number of pixels in each segment. If ``None``,
        the numbers will be estimated from the data and diode.
    """
    def __init__(self,
                 reconstruction_parameters: ReconstructionParameters,
                 pixel_rectification: NDArray[float] = None):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
        self._reconstruction_parameters = reconstruction_parameters
        self._raw_projection_weights = np.copy(self._reconstruction_parameters.projection_weights)
        self._variance = np.ones_like(self._reconstruction_parameters.projection_weights)
        self._number_of_segments = \
            reconstruction_parameters.projection_parameters.number_of_detector_segments
        self._raw_data = reconstruction_parameters.data.reshape(
                            -1, self._number_of_segments) * reconstruction_parameters.diode.reshape(-1, 1)
        if pixel_rectification is None:
            self._renormalizing_value = np.reciprocal(
                self._raw_data[self._raw_data > 0].min(axis=0)).reshape(1, -1)
        else:
            self._renormalizing_value = pixel_rectification.reshape(1, -1)
        self._data = np.copy(self._reconstruction_parameters.data)
        self._raw_data = self._raw_data * self._renormalizing_value
        self._raw_data[self._raw_data == 0] = 1.
        self._raw_data = self._raw_data.flatten()
        self._diode = np.copy(self._reconstruction_parameters.diode)
        self._diode[self._diode <= 0] = self._diode[self._diode > 0].min()
        self._transmission = np.reciprocal((self._diode.reshape(-1, 1) *
                                            np.ones((1, self._number_of_segments))).flatten()) ** 2
        dimensions = np.copy(
                reconstruction_parameters.projection_parameters.projection_data_shape.reshape(-1, 3))
        self._projection_number = dimensions.shape[0]
        cumulative_size = np.zeros(1, dtype=int)
        cumulative_size = np.append(cumulative_size,
                                    np.cumsum(dimensions[:, :-1].prod(axis=1)))
        self._projections = []
        for i, dims in enumerate(dimensions):
            data_start = cumulative_size[i] * self._number_of_segments
            data_stop = cumulative_size[i+1] * self._number_of_segments
            self._projections.append((data_start, data_stop))

    def reset_variance(self):
        """ Reset the variance to unity. This is the smallest possible value.
        """
        self._variance[...] = 1.

    def apply_photon_counting_variance(self,
                                       clipping_bounds: Tuple[float, float] = (1., None)):
        """Apply the basic photon counting Poisson variance.

        Parameters
        ----------
        clipping_bounds
            Maximum and minimum values permitted in this variance contribution.
        """
        self._variance += self._raw_data.clip(*clipping_bounds)

    def apply_projection_multiplier(self,
                                    projections: NDArray[int],
                                    multipliers: NDArray[int]):
        """Apply a multiplier to some projections. Use after applying all
        other variances.

        Parameters
        ----------
        projections
            Array of projection numbers to apply multiplier to.
        multiplier
            Multiplier to apply to each projection
        """
        for i, s in enumerate(projections):
            start = self._projections[s][0]
            stop = self._projections[s][1]
            self._variance[start:stop] *= multipliers[i]

    def apply_diode_variance(self,
                             clipping_bounds: Tuple[float, float] = (1., None),
                             background_standard_deviation: float = 0.01):
        """Apply variance based on estimate of diode uncertainty.

        Parameters
        ----------
        clipping_bounds
            Maximum and minimum values permitted in this variance contribution.
        background_standard_deviation
            Estimated relative noise level of the background scattering. Used
            to estimate the noise levels in the sample.
        """
        background_standard_deviation = background_standard_deviation / self._diode.max()
        diode_var = (self._raw_data.reshape(-1, self._number_of_segments) ** 2) * \
                    ((background_standard_deviation ** 2) / (self._diode / self._diode.max())).reshape(-1, 1)
        self._variance += diode_var.clip(*clipping_bounds).flatten()

    def inspect_rectified_variance(self,
                                   show_bar_chart: bool = True,
                                   show_projection_viewer: bool = True):
        """
        Convenience method for inspecting the rectified variance used by
        the method :func:`shift_variance_distribution
        <mumott.optimization.VarianceEstimator.shift_variance_distribution>`.
        Use this to find the percentile cutoff and to see the result of the
        shift exponents after using the method.

        Parameters
        ----------
        show_bar_chart
            Show a bar chart of the rectified variance.
        show_projection_viewer
            Show the variance over the projections using the :class:`ProjectionViewer
            <mumott.projection_viewer.ProjectionViewer>` class.
        """
        distribution_var = self.rectified_variance
        binning = np.percentile(
            distribution_var, [i for i in np.arange(1, 100.01, 1).clip(0.0, 100.0-1e-14)])
        f, ax = plt.subplots(1)
        if show_bar_chart:
            ax.bar(np.linspace(1, 100, binning.size), binning, width=1)
            ax.set_yscale('log')
            ax.set_title('Bar chart of rectified variance')
            ax.set_xlabel('Percentile')
            ax.set_ylabel('Rectified variance')
        if show_projection_viewer:
            ProjectionViewer(
                self.rectified_variance,
                self._reconstruction_parameters.projection_parameters.projection_data_shape,
                self._reconstruction_parameters.projection_parameters.detector_segment_phis)
        plt.show(block=True)

    def shift_variance_distribution(self,
                                    lower_percentile: float,
                                    shift_exponent_bounds: Tuple[float, float] = (0., -0.5)):
        """Shift a rectified variance distribution and set a lower bound for the variance.
        This is in order to prevent poor reconstruction behaviour due to the
        background variance being much smaller than the sample variance, which
        can lead to very poor convergence as some of the gradient will "leak"
        into the background region during early iterations.

        Parameters
        ----------
        lower_percentile
            The percentile of the rectified variance distribution to set as the
            lower bound for the variance. This should be the percentile where
            the smallest variance in your sample is.
        shift_exponent_bounds
            The exponents used to shift the lower and upper bounds of the variance,
            which are interpolated linearly for all bins. The shifting formula is
            ``shifted_variance = (original_variance / minimum_variance) ** -shift_exponent``.
            Set, e.g., ``shift_exponent_bounds = (0, 0.25)`` for a more slim-tailed distribution,
            or ``shift_exponent_bounds = (0, -0.25)`` for a more fat-tailed distribution.
            Set them to be equal to modify the spread of the variance without modifying
            the shape of the distribution. Be careful when making the distribution
            more slim-tailed, as a too-large upper exponent can shuffle the variances.
        """
        if shift_exponent_bounds[0] < shift_exponent_bounds[1]:
            logging.info('`shift_exponent_bounds[0]` is smaller than `shift_exponent_bounds[1]`!\n'
                         'This may change the ordering of the variances and not merely shift\n'
                         'the distribution. Please use with caution!')
        distribution_transmission = (
            ((self._renormalizing_value.max() / self._renormalizing_value) ** 2).reshape(1, -1) *
            (self.transmission / self.transmission.max()).reshape(-1, self._renormalizing_value.size))
        distribution_transmission = distribution_transmission.flatten()
        distribution_var = self._variance * distribution_transmission
        cutoff = np.percentile(
            distribution_var, [i for i in np.arange(lower_percentile, 100.01, 0.1).clip(0.0, 100.0-1e-14)])
        cutoff[-1] = distribution_var.max()
        old_inds = np.zeros_like(distribution_var).astype(bool)
        weight = np.linspace(*(shift_exponent_bounds), cutoff.size) * np.log10(cutoff / cutoff[0])
        for i, val in enumerate(cutoff):
            inds = (distribution_var <= val) & (~old_inds)
            factor = 10 ** (-weight[i])
            distribution_var[inds] *= factor
            old_inds = old_inds + inds
        distribution_var = distribution_var.clip(cutoff[0] * (10 ** -weight[0]), None)
        distribution_var *= 1 / distribution_var.min()
        self._variance = distribution_var / distribution_transmission

    def update_projection_weights(self):
        """Updates the projection weights to incorporate the variances
        calculated. Not cumulative; always uses the projection weights
        defined at the creation of the class instance. Defined so that
        the minimum non-zero value in the weights is 1. Zeroes which were already
        in the weights remain at zero, acting as a mask for e.g. poor-quality
        measurements.
        """
        var = (self._variance * self._transmission).reshape(-1, self._number_of_segments) / \
            (self._renormalizing_value ** 2)
        var = var.flatten()
        self._reconstruction_parameters.projection_weights = \
            var.min() * self._raw_projection_weights / (var)

    @property
    def variance(self) -> NDArray[np.float64]:
        """
        Variance calculated using this class. If another method
        is used to calculate the variance of the measurements, this
        value can be overridden by a direct assignment.
        """
        return self._variance.flatten()

    @variance.setter
    def variance(self, new_var: NDArray[np.float64]):
        self._variance = new_var.astype(np.float64)

    @property
    def transmission(self) -> NDArray[np.float64]:
        """ Transmission calculated using this class. """
        return self._transmission[...]

    @property
    def relative_std(self) -> NDArray[np.float64]:
        """ Relative standard deviation calculated using this class. """
        return np.sqrt(self._variance * self._transmission) / self._data

    @property
    def raw_data(self) -> NDArray[np.float64]:
        """
        The raw data, with the transmission correction and
        (possibly estimated) pixel averaging undone.
        """
        return self._raw_data[...]

    @property
    def rectified_variance(self) -> NDArray[np.float64]:
        """
        The rectified variance used by the method :func:`shift_variance_distribution
        <mumott.optimization.VarianceEstimator.shift_variance_distribution>`.
        Inspect using a bar chart and a :class:`ProjectionViewer
        <mumott.projection_viewer.ProjectionViewer>` instance before and after
        shifting the distribution.
        """
        distribution_transmission = (self.transmission /
                                     self.transmission.max()).reshape(-1, self._renormalizing_value.size)
        distribution_transmission = distribution_transmission.flatten()
        return self._variance * distribution_transmission
