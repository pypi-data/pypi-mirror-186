""" Container for the class ProjectionViewer. """

import logging

import numpy as np
import matplotlib.pyplot as plt
import colorcet  # noqa

from colorspacious import cspace_converter
from matplotlib import cm
from matplotlib.colors import Colormap
from matplotlib.gridspec import GridSpec
from matplotlib.backend_bases import MouseEvent, KeyEvent
from matplotlib.widgets import Slider
from numpy.typing import NDArray
from typing import Union, Tuple
from time import time

from .projection_frame import ProjectionFrame
from .orientation_image_mapper import OrientationImageMapper


class ProjectionViewer:
    """
    Class for viewing data and synthetic projections in a scrollable plot.
    The viewed projection can be changed with either the arrow keys or
    with the mouse scrolling wheel.

    Parameters
    ----------
    data : numpy.ndarray(dtype=float)
        A flat array of data from e.g. a :class:`ReconstructionParameters
        <mumott.data_handling.reconstruction_parameters.ReconstructionParameters>` object.
    dimensions : numpy.ndarray(dtype=int)
        An ``(N, 3)`` array containing the dimensions of each of the `N`
        frames in :attr:`data`.
    detector_angles : numpy.ndarray(dtype=float)
        An array containing the angles of the detector segments that the data
        was binned into.
    orientation_symmetry : ``'longitudinal'``, ``'transversal'``, optional
        Specifies the assumed three-dimensional symmetry of the reciprocal
        space map, which determines whether the minimum or the maximum of the
        ``cos(phi) ** 2`` component of the of the intensity is interpreted as
        the orientation angle. The default is ``'longitudinal'``, which interprets the
        angle of maximum scattering as the orientation, corresponding to
        an assumed three-dimensional symmetry of polar caps of intensity.
        The other option is ``transversal``, which corresponds to a symmetry
        of a great circle of intensity (also known as fiber symmetry), corresponding
        to a phase shift of ``90`` degrees.
    mean_colormap : str or matplotlib.colors.Colormap
        Specifies the colormap of the mean intensity across all angles. The default
        is ``'cet_linear_bmy_10_95_c71'``, a linear high-contrast with blue, magenta
        and yellow.
    std_colormap : str or matplotlib.colors.Colormap
        Specifies the colormap of the standar deviation of the data across all angles.
        The default is ``'cet_gouldian'``, a linear high-contrast map with blue,
        green and yellow.
    phase_colormap : str or matplotlib.colors.Colormap
        Specifies the colormap of the phase of the ``cos(detector_angles) ** 2`` fit
        of the data. The default is ``'cet_CET_C10'``, an isoluminant cyclic map.
    """

    def __init__(self,
                 data: NDArray[float],
                 dimensions: NDArray[int],
                 detector_angles: NDArray[float],
                 orientation_symmetry: str = 'longitudinal',
                 mean_colormap: Union[str, Colormap] = 'cet_linear_bmy_10_95_c71',
                 std_colormap: Union[str, Colormap] = 'cet_gouldian',
                 phase_colormap: Union[str, Colormap] = 'cet_CET_C10',
                 mean_range: Tuple[float, float] = None,
                 std_range: Tuple[float, float] = None):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
#         todo: Review and resolve the following code.
#         if detector_angles.max() - detector_angles.min() > np.pi + 0.1:
#             logging.warning('The provided `detector_angles` appear to span a range '
#                             'in excess of 180 degrees. Only half of the data points '
#                             'will be used.'
#                             '\nPlease proceed with caution, ensure your angles are '
#                             'provided in radians and consider reducing your data '
#                             'to account for point symmetry.')
#             detector_angles = detector_angles[:detector_angles.size // 2]

        if not np.allclose(np.diff(detector_angles).reshape(1, -1),
                           np.diff(detector_angles).reshape(-1, 1),
                           rtol=2e-01, atol=8e-02):
            logging.warning('The provided `detector_angles` do not appear to be '
                            'sorted and equally spaced to within an absolute tolerance '
                            'of 5 degrees and a relative tolerance of twenty percent of the '
                            'segment width.'
                            '\nThe orientation angle may not behave as expected. Please be cautious'
                            'in interpreting the figure.')
        if orientation_symmetry == 'transversal':
            self._detector_angles = np.arctan2(np.sin(detector_angles), np.cos(detector_angles))
        elif orientation_symmetry == 'longitudinal':
            self._detector_angles = np.arctan2(-np.cos(detector_angles), np.sin(detector_angles))
        else:
            logging.warning(
                    'Unknown `orientation_symmetry` option: "' + orientation_symmetry +
                    '"\nUsing default value: "longitudinal".\n'
                    'Valid options are "transversal" and "longitudinal".')
            self._detector_angles = np.arctan2(-np.cos(detector_angles), np.sin(detector_angles))
        direction = np.arctan2(np.sin(detector_angles[1] - detector_angles[0]),
                               np.cos(detector_angles[1] - detector_angles[0]))
        a = float(np.round(direction >= 0))
        b = np.exp((-2j) * self._detector_angles[0])
        self._mean_colormap = mean_colormap
        self._std_colormap = std_colormap
        self._phase_colormap = phase_colormap
        self._cielab_converter = cspace_converter('sRGB255', 'JCh')
        self._srgb_converter = cspace_converter('JCh', 'sRGB255')
        self._orientation_image_mapper = OrientationImageMapper(phase_colormap)
        self._wheel_properties = self._orientation_image_mapper.wheel_properties
        self._phase_colormap_lut = cm.get_cmap(self._phase_colormap, 256)
        self._data = data[:]
        self._dimensions = dimensions.reshape(-1, 3)
        self._projection_number = dimensions.shape[0]
        self._cumulative_size = np.zeros(1, dtype=int)
        self._cumulative_size = np.append(self._cumulative_size, np.cumsum(self._dimensions.prod(axis=1)))
        self._clims_mean = np.percentile(
            a=self._data.reshape(-1, self._dimensions[0, 2]).mean(axis=1),
            q=(1., 99.9))
        if mean_range is not None:
            if mean_range[0] is not None:
                self._clims_mean[0] = mean_range[0]
            if mean_range[1] is not None:
                self._clims_mean[1] = mean_range[1]
        self._clims_std = np.percentile(
            a=self._data.reshape(-1, self._dimensions[0, 2]).std(axis=1),
            q=(1., 99.9))
        if std_range is not None:
            if std_range[0] is not None:
                self._clims_std[0] = std_range[0]
            if std_range[1] is not None:
                self._clims_std[1] = std_range[1]
        self._projections = []
        for i, dims in enumerate(self._dimensions):
            start = self._cumulative_size[i]
            stop = self._cumulative_size[i+1]
            temp_data = self._data[start:stop].reshape(dims)
            temp_mean = temp_data[:, :, :detector_angles.size].mean(axis=2).T
            temp_std = temp_data[:, :, :detector_angles.size].std(axis=2).T
            temp_fft = np.fft.rfft(temp_data[:, :, :detector_angles.size] ** 2, axis=2, norm='ortho')
            if a:
                temp_angle = (np.sqrt(temp_fft[:, :, 1] * b)).T
            else:
                temp_angle = (np.sqrt(np.conj(temp_fft[:, :, 1]) * b)).T
            temp_angle = np.angle(np.sign(temp_angle.imag) * temp_angle)
            temp_mask = np.round(
                np.sqrt(
                    abs(temp_fft[:, :, 0])) > 0.5 * np.sqrt(abs(temp_fft[:, :, 0])).mean()).astype(float).T
            temp_aniso_factor = np.sqrt(
                abs(temp_fft[:, :, 1]) / (np.finfo(float).tiny + abs(temp_fft[:, :, 0]))).T
            temp_shader = temp_aniso_factor.clip(0., 1)
            phase_rgba = self._phase_colormap_lut(temp_angle / np.pi)
            phase_cielab = self._cielab_converter(phase_rgba[:, :, :-1])
            phase_cielab[:, :, :2] *= 1.1 * ((1 - np.exp(-temp_shader)) /
                                             (1 - np.exp(-1))).reshape(temp_shader.shape + (1,))
            phase_rgba[:, :, :-1] = self._srgb_converter(phase_cielab).clip(0., 1.)
            phase_rgba[:, :, -1] = temp_mask
            temp_frame = ProjectionFrame(
                mean=temp_mean,
                std=temp_std,
                angle_color_quad=phase_rgba)
            self._projections.append(temp_frame)
        plt.ion()
        self._fig = plt.figure()
        self._grid_spec = GridSpec(7, 9, figure=self._fig)
        self._axes = []
        self._axes.append(self._fig.add_subplot(self._grid_spec[0:4, 0:3]))
        self._axes.append(self._fig.add_subplot(self._grid_spec[0:4, 3:6]))
        self._axes.append(self._fig.add_subplot(self._grid_spec[0:4, 6:9]))
        self._axes.append(self._fig.add_subplot(self._grid_spec[4:6, 6:9], projection='polar'))
        self._colorbar_axes = []
        self._colorbar_axes.append(self._fig.add_subplot(self._grid_spec[5, 0:3]))
        self._colorbar_axes.append(self._fig.add_subplot(self._grid_spec[5, 3:6]))
        self._slider_axis = self._fig.add_subplot(self._grid_spec[-1, :])
        for a in self._axes:
            a.grid(False)
            a.set_yticks([])
            a.set_xticks([])
            a.set_yticklabels([])
            a.set_xticklabels([])
        self._im1 = self._axes[0].imshow(
            self._projections[0].mean, origin='lower', cmap=self._mean_colormap)
        self._axes[0].set_title('Mean')
        self._fig.colorbar(
            self._im1, cax=self._colorbar_axes[0], orientation='horizontal')
        self._im2 = self._axes[1].imshow(
            self._projections[0].std, origin='lower', cmap=self._std_colormap)
        self._axes[1].set_title('Standard deviation')
        self._fig.colorbar(self._im2, cax=self._colorbar_axes[1], orientation='horizontal')

        self._im3 = self._axes[2].imshow(self._projections[0].angle_color_quad,
                                         origin='lower',)
        self._axes[2].set_title('Orientation phase')
        self._axes[2].set_facecolor((254 / 255, 254 / 255, 254 / 255))
        self._wheel_rgba = self._wheel_properties[2]
        self._axes[3].set_facecolor((254 / 255, 254 / 255, 254 / 255))
        wheel_shader = self._wheel_properties[1][:-1, :-1] ** 2
        wheel_cielab = self._cielab_converter(self._wheel_rgba[:, :, :-1])
        wheel_cielab[:, :, :2] *= 1.1 * ((1 - np.exp(-wheel_shader)) /
                                         (1 - np.exp(-1))).reshape(wheel_shader.shape + (1,))
        wheel_rgb = self._srgb_converter(wheel_cielab).clip(0., 1.)
        self._wheel_rgba[:, :, :-1] = wheel_rgb
        self._axes[3].grid(False)
        self._color_wheel = self._axes[3].pcolormesh(self._wheel_properties[0],
                                                     1 - np.arccos(self._wheel_properties[1]) * 2 / np.pi,
                                                     wheel_shader[:, :],
                                                     facecolors=self._wheel_rgba.reshape(-1, 4),
                                                     edgecolors=self._wheel_rgba.reshape(-1, 4))
        self._axes[3].set_rmax(1.)
        self._axes[3].set_rmin(0.)
        self._update_timer = time()
        self._fig.canvas.mpl_connect('scroll_event', self._on_scroll)
        self._fig.canvas.mpl_connect('key_press_event', self._on_press)
        self._projection_slider = Slider(
            ax=self._slider_axis,
            label='Projection number',
            valmin=0,
            valmax=self._projection_number-1,
            valstep=1,
            valinit=0)
        self._projection_slider.on_changed(self._update_projections)
        self._projection_ind = -1
        self._scroll_accumulator = 0
        self._update_projections(0)
        self._scroll_timer = time()
        self._key_timer = time()
        self._new_val = 0
        self._callback_timer = self._fig.canvas.new_timer(
            interval=100, callbacks=[(self._update_callback, (), {})])
        self._callback_timer.start()

    def _update_callback(self):
        """
        Internal method for updating the slider approximately every 100 milliseconds
        with accumulated scrolls from the mouse wheel and arrow keys.
        """
        self._new_val = self._projection_slider.val + self._scroll_accumulator
        self._scroll_accumulator = 0
        self._projection_slider.set_val(
            max(min(self._new_val, self._projection_slider.valmax), self._projection_slider.valmin))

    def _on_scroll(self, event: MouseEvent):
        """
        Internal method for accumulating mouse wheel scrolls,
        and updating the slider if it has been long enough since
        the last scroll.

        Parameters
        ----------
        event
            A Matplotlib ``MouseEvent`` object provided by the callback.
        """
        self._scroll_accumulator += event.step
        self._scroll_accumulator = max(min(
            self._scroll_accumulator, self._projection_slider.valmax - self._projection_slider.val),
                self._projection_slider.valmin - self._projection_slider.val)
        self._new_val = self._projection_slider.val
        if time() - self._scroll_timer > 0.2:
            self._new_val = self._projection_slider.val + self._scroll_accumulator
            self._scroll_accumulator = 0
        self._scroll_timer = time()
        self._projection_slider.set_val(
            max(min(self._new_val, self._projection_slider.valmax), self._projection_slider.valmin))

    def _on_press(self, event: KeyEvent):
        """
        Internal method for accumulating arrow key presses,
        and updating the slider if it has been long enough since
        the last key press.

        Parameters
        ----------
        event
            A Matplotlib ``KeyEvent`` object provided by the caller.
        """
        self._new_val = self._projection_slider.val
        if (event.key in {'left', 'right'}) and (time() - self._key_timer > 0.2):
            self._key_timer = time()
            if event.key == 'right':
                self._scroll_accumulator += 1
            elif event.key == 'left':
                self._scroll_accumulator -= 1
            self._scroll_accumulator = max(min(
                self._scroll_accumulator, self._projection_slider.valmax - self._projection_slider.val),
                    self._projection_slider.valmin - self._projection_slider.val)
            self._new_val = self._projection_slider.val + self._scroll_accumulator
            self._scroll_accumulator = 0
        self._projection_slider.set_val(max(min(
            self._new_val, self._projection_slider.valmax), self._projection_slider.valmin))

    def _update_projections(self, ind: int):
        """
        Internal methods for updating the projection shown
        when the projection slider changes.

        Parameters
        ----------
        ind
            The index of the projection to be shown.
        """
        if ind != self._projection_ind:
            self._projection_ind = ind
            ind = int(ind)
            self._im1.set_data(self._projections[ind].mean)
            self._im1.set_clim(*self._clims_mean)
            self._im2.set_data(self._projections[ind].std)
            self._im2.set_clim(*self._clims_std)
            self._im3.set_data(self._projections[ind].angle_color_quad)
            self._im3.autoscale()
            self._axes[0].relim()
            self._axes[1].relim()
            self._axes[2].relim()
            self._axes[0].autoscale_view()
            self._axes[1].autoscale_view()
            self._axes[2].autoscale_view()
            self._axes[0].set_aspect('equal')
            self._axes[1].set_aspect('equal')
            self._axes[2].set_aspect('equal')
            self._fig.canvas.draw_idle()
            self._fig.canvas.flush_events()
