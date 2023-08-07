""" Container for class LiveViewHandler. """
from typing import Union

import numpy as np
import matplotlib.pyplot as plt
import colorcet # noqa
from colorspacious import cspace_converter
from matplotlib import cm
from matplotlib.colors import Colormap
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec
from numpy.typing import ArrayLike

from mumott.data_handling.reconstruction_parameters import ReconstructionParameters
from mumott.output_handling.orientation_image_mapper import OrientationImageMapper


class LiveViewHandler:
    """
    This class is used to create an automatically updating plot with a cut of the reconstruction for
    live monitoring of the optimization. An instance of this class
    should be passed to the class:`Optimizer
    <mumott.optimization.Optimizer>` instance used if live feedback
    is desired.

    Parameters
    ----------
    reconstruction_paramteters : class:`ProjectionViewer <mumott.output_handling.ProjectionViewer>`.
        The class:`ReconstructionParameters <mumott.output_handling.ReconstructionParameters>`
        instance used for the optimization.
    shown_orders : ArrayLike
        A list, tuple or similar containing the orders the power
        of which are to be shown in a separate plot. Default value is ``[2]``.
    plane : int
        The plane which the shown cut should go through. ``0``, ``1`` and
        ``2`` map to the normal planes of the ``X``, ``Y`` and ``Z`` directions respectively.
        Default is ``2``.
    cut_index : Union[str, int]
        The index of the cut to be shown. Can be either set to ``middle`` for a central cut
        or to an integer to specify a particular cut.
    orientation : str
        Whether the three-dimensional symmetry of the sample reciprocal space map is primarly transversal
        (great circle symmetry) or longitudinal (pole symmetry). This affects whether the
        minimum (``'transversal'``) or maximum (``'longitudinal'``) of the rank-2 tensor
        component of the three-dimensional reciprocal space map is considered to indicate
        the sample orientation.
        Possible values are ``'transversal'`` and ``'longitudinal'``. Default is ``'transversal'``.
    isotropy_colormap : Union[str, Colormap]
        The colormap to use for the isotropic/mean component of the reciprocal space map.
        Maps from ``colorcet`` can be used if prefixed with ``'cet_'``. Default is
        ``'cet_CET_L8'``.
    anisotropy_colormap : Union[str, Colormap]
        The colormap to use for the anisotropic/standard deviation component of the reciprocal space map.
        Maps from ``colorcet`` can be used if prefixed with ``'cet_'``. Default is
        ``'cet_gouldian'``.
    spectral_orders_colormap : Union[str, Colormap]
        The colormap to use for the anisotropic/standard deviation contribution
        of the individual orders specified in ``shown_orders``.
        Maps from ``colorcet`` can be used if prefixed with ``'cet_'``. Default is
        ``'cet_fire'``.
    orientation_colormap : Union[str, Colormap]
        The colormap to use for the orientation of the reciprocal space map. Should be cyclic.
        Maps from ``colorcet`` can be used if prefixed with ``'cet_'``. Default is
        ``'cet_cyclic_isoluminant'``. Map undergoes lightness modulation, so an
        isoluminant map is preferred.
    """
    def __init__(self,
                 reconstruction_parameters: ReconstructionParameters,
                 shown_orders: ArrayLike = [2],
                 plane: int = 2,
                 cut_index: Union[str, int] = 'middle',
                 orientation: Union[str, Colormap] = 'transversal',
                 isotropy_colormap: Union[str, Colormap] = 'cet_CET_L8',
                 anisotropy_colormap: Union[str, Colormap] = 'cet_gouldian',
                 spectral_orders_colormap: Union[str, Colormap] = 'cet_fire',
                 orientation_colormap: Union[str, Colormap] = 'cet_cyclic_isoluminant'):
        self._orientation = orientation
        axis_labels = [('Y', 'Z'), ('X', 'Z'), ('X', 'Y')][plane]
        self._reconstruction_parameters = reconstruction_parameters
        self._isotropy_colormap = isotropy_colormap
        self._anisotropy_colormap = anisotropy_colormap
        self._orientation_colormap = orientation_colormap
        self._orientation_colormap_lut = cm.get_cmap(self._orientation_colormap, 256)
        self._cam_converter = cspace_converter('sRGB255', 'JCh')
        self._srgb_converter = cspace_converter('JCh', 'sRGB255')
        orientation_image_mapper = OrientationImageMapper(orientation_colormap)
        self._wheel_properties = orientation_image_mapper.wheel_properties
        self._spectral_orders_colormap = spectral_orders_colormap
        self._shown_orders = shown_orders
        n_harmonic_coefficients = \
            self._reconstruction_parameters.spherical_harmonic_parameters.l_indices.size
        self._dimensions = tuple(
            self._reconstruction_parameters.projection_parameters.volume_shape) + \
            (n_harmonic_coefficients,) # noqa
        self._coefficients = self._reconstruction_parameters.reconstruction_input.optimization_coefficients.reshape(self._dimensions)  # noqa
        self._plane = plane
        if cut_index == 'middle':
            self._cut_index = self._dimensions[self._plane] // 2
        else:
            self._cut_index = cut_index
        self._update_images()

        plt.ion()
        self._fig = plt.figure()
        self._grid_spec = GridSpec(6, 9, figure=self._fig)
        self._axes = []
        self._axes.append(self._fig.add_subplot(self._grid_spec[0:4, 0:3]))
        self._axes.append(self._fig.add_subplot(self._grid_spec[0:4, 3:6]))
        self._axes.append(self._fig.add_subplot(self._grid_spec[0:4, 6:9]))
        self._axes.append(self._fig.add_subplot(self._grid_spec[4:, 6:9], projection='polar'))
        self._colorbar_axes = []
        self._colorbar_axes.append(self._fig.add_subplot(self._grid_spec[5, 0:3]))
        self._colorbar_axes.append(self._fig.add_subplot(self._grid_spec[5, 3:6]))
        axis_titles = ['Mean of Intensity',
                       'STD of intensity',
                       'Rank-2 tensor orientation']
        for i, a in enumerate(self._axes):
            a.grid(False)
            a.set_yticks([])
            a.set_xticks([])
            a.set_yticklabels([])
            a.set_xticklabels([])
            if i < 3:
                a.set_xlabel(axis_labels[0])
                a.set_ylabel(axis_labels[1])
                a.set_title(axis_titles[i])
        # Set up view of isotropic component.
        self._im1 = self._axes[0].imshow(self._mean_image.T, origin='lower', cmap=self._isotropy_colormap)
        self._fig.colorbar(self._im1, cax=self._colorbar_axes[0], orientation='horizontal')

        # Set up view of anisotropic component.
        self._im2 = self._axes[1].imshow(self._stdev_image.T, origin='lower', cmap=self._anisotropy_colormap)
        self._fig.colorbar(self._im2, cax=self._colorbar_axes[1], orientation='horizontal')

        # Set up view of orientation.
        self._orientation_rgba = self._orientation_colormap_lut(self._orientation_image / np.pi)
        self._orientation_rgba[:, :, -1] = self._orientation_mask
        self._im3 = self._axes[2].imshow(self._orientation_rgba.transpose(1, 0, 2), origin='lower')
        self._axes[2].set_facecolor((255 / 255, 255 / 255, 255 / 255))

        # Set up color wheel.
        self._axes[3].set_facecolor((255 / 255, 255 / 255, 255 / 255))
        wheel_rgba = self._wheel_properties[2]
        wheel_shader = self._wheel_properties[1][:-1, :-1]
        wheel_cam = self._cam_converter(wheel_rgba[:, :, :-1])
        wheel_cam[:, :, :2] *= 1.1 * wheel_shader.reshape(wheel_shader.shape + (1,))
        wheel_rgb = self._srgb_converter(wheel_cam).clip(0., 1.)
        wheel_rgba[:, :, :-1] = wheel_rgb
        self._color_wheel = self._axes[3].pcolormesh(self._wheel_properties[0],
                                                     1 - np.arccos(self._wheel_properties[1]) * 2 / np.pi,
                                                     wheel_shader[:, :],
                                                     facecolors=wheel_rgba.reshape(-1, 4),
                                                     edgecolors=wheel_rgba.reshape(-1, 4))
        self._axes[3].grid(False)
        self._axes[3].set_rmax(1.)
        self._axes[3].set_rmin(0)

        # Set up view of spectral orders in separate plot.
        if self._shown_orders is not None:
            self._orders_fig = plt.figure()
            self._orders_grid_spec = GridSpec(5, 3 * len(self._shown_orders), figure=self._orders_fig)
            self._orders_axes = []
            self._orders_image_plots = []
            for i, o in enumerate(self._shown_orders):
                self._orders_axes.append(self._orders_fig.add_subplot(self._orders_grid_spec[0:4, 3*i:3+3*i]))
                self._orders_image_plots.append(self._orders_axes[i].imshow(self._orders_images[i].T,
                                                                            origin='lower', cmap='cet_fire'))
                self._orders_axes[i].set_title(r'STD from $\ell = {0}$'.format(o))
            for a in self._orders_axes:
                a.grid(False)
                a.set_yticks([])
                a.set_xticks([])
                a.set_yticklabels([])
                a.set_xticklabels([])
                a.set_xlabel(axis_labels[0])
                a.set_ylabel(axis_labels[1])
            self._orders_colorbar_axis = self._orders_fig.add_subplot(self._orders_grid_spec[4, 1:8])
            self._orders_fig.colorbar(self._orders_image_plots[0],
                                      cax=self._orders_colorbar_axis,
                                      orientation='horizontal')

        self.update_plots()

    def _update_images(self):
        """ Updates the attributes used to make plots. """
        if self._plane == 0:
            self._cut = self._coefficients[self._cut_index, :, :].reshape(self._dimensions[1:])
        elif self._plane == 1:
            self._cut = self._coefficients[:, self._cut_index, :].reshape(self._dimensions[0::2] +
                                                                          (self._dimensions[3],))
        else:
            self._cut = self._coefficients[:, :, self._cut_index].reshape(self._dimensions[:2] +
                                                                          (self._dimensions[3],))
        self._mean_image = abs(self._cut[:, :, 0])
        self._stdev_image = np.sqrt(np.sum(self._cut[:, :, 1:] ** 2, axis=2))
        self._orders_images = []
        if self._shown_orders is not None:
            for o in self._shown_orders:
                indices = self._reconstruction_parameters.spherical_harmonic_parameters.l_indices == o
                self._orders_images.append(np.sqrt(np.sum(self._cut[:, :, indices] ** 2, axis=2)))

        if self._dimensions[3] > 1:
            self._update_orientations()
            self._orientation_colormap_lut = cm.get_cmap(self._orientation_colormap, 256)
            self._orientation_mask = (np.log(self._mean_image + 1)
                                      > np.log(np.mean(self._mean_image) + 1)).astype(float)
            self._orientation_image = np.arctan2(self._vector[:, :, 0], self._vector[:, :, 1])
            self._orientation_image[self._orientation_image < 0] += np.pi
            self._orientation_rgba = self._orientation_colormap_lut(self._orientation_image / np.pi)
            orientation_cam = self._cam_converter(self._orientation_rgba[:, :, :-1])
            shader = np.sqrt(1 - self._in_plane ** 2)
            orientation_cam[:, :, :2] *= 1.1 * shader.reshape(shader.shape + (1,))
            orientation_rgb = self._srgb_converter(orientation_cam).clip(0., 1.)
            self._orientation_rgba[:, :, :-1] = orientation_rgb
            self._orientation_rgba[:, :, -1] = self._orientation_mask
        else:
            self._orientation_mask = np.zeros_like(self._mean_image)
            self._orientation_image = np.zeros_like(self._mean_image)
            self._image_in_plane = np.zeros_like(self._mean_image)

    def update_plots(self):
        """ Calling this method updates the live view plots. """
        self._update_images()

        self._im1.set_data(self._mean_image.T)
        self._im1.autoscale()
        self._im1.set_cmap(self._isotropy_colormap)

        self._im2.set_data(self._stdev_image.T)
        self._im2.set_clim(0, self._mean_image.max())
        self._im2.set_cmap(self._anisotropy_colormap)

        self._im3.set_data(self._orientation_rgba.transpose(1, 0, 2))
        self._im3.autoscale()
        for ax in self._axes[:3]:
            ax.relim()
            ax.autoscale_view()
        self._fig.canvas.draw()
        self._fig.canvas.flush_events()
        if self._shown_orders is not None:
            for i, o in enumerate(self._shown_orders):
                self._orders_image_plots[i].set_data(self._orders_images[i].T)
                self._orders_image_plots[i].set_clim(0, self._mean_image.max())
                self._orders_axes[i].relim()
                self._orders_axes[i].autoscale_view()
                self._orders_image_plots[i].set_cmap(self._spectral_orders_colormap)
            self._orders_fig.canvas.draw()
            self._orders_fig.canvas.flush_events()

    @property
    def figure(self) -> Figure:
        """The main figure of the LiveViewHandler instance."""
        return self._fig

    @property
    def figure_with_higher_orders(self) -> Figure:
        """The higher-order spectral power figure of the LiveViewHandler instance."""
        return self._orders_fig

    @property
    def isotropy_colormap(self) -> Union[str, Colormap]:
        """ Colormap used for the isotropic component. """
        return self._isotropy_colormap

    @property
    def anisotropy_colormap(self) -> Union[str, Colormap]:
        """ Colormap used for the anisotropic component. """
        return self._anisotropy_colormap

    @property
    def orientation_colormap(self) -> Union[str, Colormap]:
        """ Colormap used for the orientation. """
        return self._orientation_colormap

    @property
    def spectral_orders_colormap(self) -> Union[str, Colormap]:
        """ Colormap used for the separately plotted spectral orders. """
        return self._spectral_orders_colormap

    @isotropy_colormap.setter
    def isotropy_colormap(self, new_colormap: Union[str, Colormap]):
        self._isotropy_colormap = new_colormap

    @anisotropy_colormap.setter
    def anisotropy_colormap(self, new_colormap: Union[str, Colormap]):
        self._anisotropy_colormap = new_colormap

    @orientation_colormap.setter
    def orientation_colormap(self, new_colormap: Union[str, Colormap]):
        self._orientation_colormap = new_colormap

    @spectral_orders_colormap.setter
    def spectral_orders_colormap(self, new_colormap: Union[str, Colormap]):
        self._spectral_orders_colormap = new_colormap

    def _update_orientations(self):
        """ Retrieves orientations from rank-2 component of reciprocal space map. """
        A = self._cut[:, :, 1:6].reshape(-1, 5)
        c1 = np.sqrt(15 / (4 * np.pi))
        c2 = np.sqrt(5 / (16 * np.pi)) * 2
        c3 = np.sqrt(15 / (16 * np.pi)) * 2
        AM = np.zeros((self._cut[:, :, 0].size, 3, 3))
        AM[:, 0, 0] = c3 * A[:, 4] - c2 * A[:, 2]
        AM[:, 1, 1] = - c3 * A[:, 4] - c2 * A[:, 2]
        AM[:, 2, 2] = c2 * 2 * A[:, 2]
        AM[:, 0, 1] = c1 * A[:, 0]
        AM[:, 1, 0] = c1 * A[:, 0]
        AM[:, 2, 1] = c1 * A[:, 1]
        AM[:, 1, 2] = c1 * A[:, 1]
        AM[:, 2, 0] = c1 * A[:, 3]
        AM[:, 0, 2] = c1 * A[:, 3]
        try:
            w, v = np.linalg.eigh(AM)
            eigenfail = False
        except np.linalg.LinAlgError:
            eigenfail = True
        if not eigenfail:
            sorting = np.argsort(w, axis=1).reshape(-1, 3, 1)
            v = v.transpose(0, 2, 1)
            v = np.take_along_axis(v, sorting, axis=1)
            v = v.transpose(0, 2, 1)
            if self._orientation == 'transversal':
                self._vector = v[:, :, 0] / np.sqrt(np.sum(v[:, :, 0] ** 2, axis=1).reshape(-1, 1))
            else:
                self._vector = v[:, :, 2] / np.sqrt(np.sum(v[:, :, 2] ** 2, axis=1).reshape(-1, 1))
            if self._plane == 0:
                self._in_plane = abs(self._vector[:, 0].reshape(self._dimensions[1:3]))
                self._vector = self._vector[:, 1:].reshape(self._dimensions[1:3] + (-1,))
            elif self._plane == 1:
                self._in_plane = abs(self._vector[:, 1].reshape(
                    self._dimensions[0::2]))
                self._vector = self._vector[:, 0::2].reshape(
                    self._dimensions[0::2] + (-1,))
            else:
                self._in_plane = abs(self._vector[:, 2].reshape(self._dimensions[:2]))
                self._vector = self._vector[:, :2].reshape(self._dimensions[:2] + (-1,))
        else:
            self._in_plane = np.zeros(self._cut.shape[:-1])
            self._vector = np.zeros(self._cut.shape[:-1] + (2,))
