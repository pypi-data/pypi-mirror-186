"""This contains the class SimulatedDataGenerator.

It is used to generate simple simulated data sets for testing."""

from os.path import join

import matplotlib.pyplot as plt
import numpy as np
from numpy import array, zeros, zeros_like, ones, cos, pi, \
                  arange, append, finfo, float64
from scipy.io import savemat
import h5py as h5
from mumott.core.projection_parameters import ProjectionParameters
from mumott.data_handling.spherical_harmonic_parameters import SphericalHarmonicParameters


class SimulatedDataGenerator:
    """Generates a simple cubic dataset with rank-2 tensor anisotropy in each voxel.

    Parameters
    ----------
    volume_size : int, optional
        The size of the full volume to generate the simulation in.
        Default is ``5``.
    sample_size : int, optional
        Size of the cubic sample inside the volume.
        Default is ``3``.
    projection_size : int, optional
        Size of the projection, ideally at least ``volume_size * sqrt(3)`` to allow
        the corners to be captured at all tilts.
    rotations_at_0_tilt : int, optional
        Number of rotations at zero tilt. Should be odd to prevent mirrored projections.
        Default is ``5``.
    number_of_tilts : int, optional
        Number of tilts above zero. The highest tilt will be ``pi / 2``. The number of rotations
        will fall off as ``cos(pi / 2)``. Default is ``4``.
    number_of_detector_segments : int, optional
        Number of samplings of the tensor to make at each projected pixel.
        Default is ``3``, which is usually the ideal value for a rank-2 tensor.
    view_projections : bool, optional
        Whether to view the projections in a plot as they are made. Defaults to ``False``.
    """
    def __init__(self,
                 volume_size: int = 5,
                 sample_size: int = 3,
                 projection_size: int = 7,
                 projections_at_0_tilt: int = 5,
                 number_of_tilts: int = 4,
                 number_of_detector_segments: int = 3,
                 view_projections: bool = False):
        # todo: replace with RandomState
        self._rng = np.random.default_rng()
        self._volume = zeros((volume_size,) * 3 + (6,), dtype=float64)
        sample_bounds = slice(int(np.floor((volume_size - sample_size) / 2)),
                              int(volume_size - np.ceil((volume_size - sample_size) / 2)))
        self._volume[sample_bounds, sample_bounds, sample_bounds, 0] = \
            np.ones((sample_size,) * 3) * 10
        self._volume[sample_bounds, sample_bounds, sample_bounds, 1:] = \
            np.ones((sample_size,) * 3 + (1,)) * self._rng.uniform(-3, 3, (sample_size,)*3 + (5,))
        tilts = arange(0, pi / 2 + pi / (4 * number_of_tilts), pi / (2 * number_of_tilts))
        self._tiltarr = array(())
        self._rotarr = array(())
        for t in tilts:
            t_rotations = \
                arange(0, 2 * pi,
                       pi / ((projections_at_0_tilt * 0.5) * cos(t) + finfo(float64).tiny))
            self._tiltarr = append(self._tiltarr, t * ones(t_rotations.size))
            self._rotarr = append(self._rotarr, t_rotations)
        self._projection_size = ones((self._rotarr.size,)) * (projection_size ** 2)
        self._number_of_detector_segments = number_of_detector_segments
        self._projection_shape = ones((self._rotarr.size, 3)) * \
            array((projection_size, projection_size, number_of_detector_segments)).reshape(1, 3)
        self._projection_shape = self._projection_shape.astype(np.int32)
        number_of_projections = self._rotarr.size
        self._detector_segment_phis = arange(0, pi, pi / number_of_detector_segments)
        self._cumulative_projection_size = array((0,))
        self._cumulative_projection_size = \
            append(self._cumulative_projection_size, np.cumsum(self._projection_size))
        self._projection_parameters = ProjectionParameters(
            rotation_angles_for_principal_axis=self._rotarr,
            rotation_angles_for_secondary_axis=self._tiltarr,
            detector_segment_phis=self._detector_segment_phis,
            offsets_j=zeros_like(self._rotarr),
            offsets_k=zeros_like(self._rotarr),
            volume_shape=array(self._volume.shape[:-1]),
            data_shape=self._projection_shape)
        self._spherical_harmonic_parameters = SphericalHarmonicParameters(
            l_max=2,
            number_of_coefficients=6,
            spherical_harmonic_factors=zeros(1))
        self._spherical_harmonic_parameters.compute_spherical_harmonic_factors(
            self._projection_parameters.probed_theta,
            self._projection_parameters.probed_phi)
        self._canvas = zeros((number_of_projections,) +
                             tuple(self._projection_shape[0])).astype(float64)
        if view_projections:
            plt.ion()
            f, ax = plt.subplots(1)
            im = ax.imshow(np.sqrt(np.sum(self._canvas[0]**2, 2)).T, origin='upper')
            f.canvas.draw()
            f.canvas.flush_events()
        for i in range(number_of_projections):
            volume_view = np.sum(
                self._volume.reshape(-1, 1, 6) *
                self._spherical_harmonic_parameters.spherical_harmonic_factors[i].reshape(1, -1, 6), 2)
            volume_view = volume_view.reshape(self._volume.shape[:-1] + (self._number_of_detector_segments,))
            self._projection_parameters.project(
                input_field=volume_view,
                projection=self._canvas[i, :, :],
                index=i)
            if view_projections:
                im.set_data(np.sqrt(np.sum(self._canvas[i] ** 2, 2)).T)
                im.autoscale()
                ax.relim()
                ax.autoscale_view()
                f.canvas.draw()
                f.canvas.flush_events()
                plt.pause(0.5)

    def save_to_mat(self, file_path: str = './', file_name: str = 'simulated_data'):
        """Saves the simulation to a ``.mat`` file that can be loaded using
        a :class:`DataContainer <mumott.data_handling.DataContainer>` object.

        Parameters
        ----------
        file_path
            Path to save the file in. Default is ``./``
        file_name
            What name to give the saved file. Default is ``simulated_data``.
            The ``.mat`` file ending will be appended automatically.
        """
        mdict = dict(
            data_shape=self._projection_shape.astype(np.int32).flatten(),
            cumsize=self._cumulative_projection_size.flatten().astype(np.int32),
            num_segments=np.int32(self._number_of_detector_segments),
            num_projections=np.int32(self._rotarr.size),
            projection_size=self._projection_size.flatten().astype(np.int32),
            nx=np.int32(self._volume.shape[0]),
            ny=np.int32(self._volume.shape[1]),
            dx=zeros_like(self._rotarr).astype(float64),
            dy=zeros_like(self._tiltarr).astype(float64),
            phi_det=self._detector_segment_phis.flatten().astype(float64),
            data=self._canvas.flatten(),
            rot_y=((180 / pi) * self._rotarr.flatten()).astype(float64),
            rot_x=((180 / pi) * self._tiltarr.flatten()).astype(float64),
            window_mask=np.ones(self._canvas.shape[:3]).flatten().astype(float64),
            tomo_axis_y=np.int32(1))
        savemat(join(file_path, file_name) + '.mat', mdict)

    def save_to_h5(self, output_path: str = 'output.h5'):
        output_file = h5.File(output_path, 'w')
        projections = output_file.create_group('projections')
        model_file = output_file.create_group('model')
        groups = []
        out_data = []
        out_diode = []
        out_weights = []
        out_rotations = []
        out_tilts = []
        out_offsets_j = []
        out_offsets_k = []
        for i in range(len(self._canvas)):
            groups.append(projections.create_group(f'{i}'))
            dshape = tuple(self._canvas[i].shape)
            out_data.append(groups[i].create_dataset('data', dshape, dtype=float64))
            out_diode.append(groups[i].create_dataset('diode', dshape[:-1], dtype=float64))
            out_weights.append(groups[i].create_dataset('weights', dshape[:-1], dtype=float64))
            out_rotations.append(groups[i].create_dataset('rotations', (1,), dtype=float64))
            out_tilts.append(groups[i].create_dataset('tilts', (1,), dtype=float64))
            out_offsets_j.append(groups[i].create_dataset('offset_j', (1,), dtype=float64))
            out_offsets_j[i][:] = 0.
            out_offsets_k.append(groups[i].create_dataset('offset_k', (1,), dtype=float64))
            out_offsets_k[i][:] = 0.
        out_angles = \
            output_file.create_dataset('detector_angles', (self._canvas[0].shape[-1],), dtype=float64)
        volume_shape = output_file.create_dataset('volume_shape', (3,), dtype=np.int32)
        volume_shape[:] = self._volume.shape[:-1]
        out_angles[:] = np.copy(self._projection_parameters.detector_segment_phis)
        for i, c in enumerate(self._canvas):
            out_data[i][...] = np.copy(self._canvas[i])
            out_diode[i][...] = np.ones(self._canvas[i].shape[:-1])
            out_weights[i][...] = np.ones(self._canvas[i].shape[:-1])
            out_rotations[i][...] = self._projection_parameters.rotation_angles_for_principal_axis[i]
            out_tilts[i][...] = self._projection_parameters.rotation_angles_for_secondary_axis[i]
        model_file.create_dataset('coefficients', self._volume.shape, dtype=float64)
        model_file['coefficients'][...] = np.copy(self._volume)
        output_file.close()

    def __str__(self) -> str:
        wdt = 72
        s = []
        s += ['=' * wdt]
        s += ['SimulatedDataGenerator'.center(wdt)]
        s += ['-' * wdt]
        s += ['{:22} : {}'.format('Number of detector segments', self._number_of_detector_segments)]
        s += ['{:22} : {}'.format('Number of projections', self._rotarr.size)]
        s += ['{:22} : {}'.format('Detection segment phis', self._detector_segment_phis)]
        s += ['-' * wdt]
        s += [str(self._spherical_harmonic_parameters)]
        s += [str(self._projection_parameters)]
        s += ['=' * wdt]
        return '\n'.join(s)

    def _repr_html_(self) -> str:
        s = []
        s += ['<table border="1" class="dataframe">']
        s += ['<thead><tr><th style="text-align: left;">SimulatedDataGenerator</th></tr></thead>']
        s += ['<tbody>']
        s += ['<tr><td style="text-align: left;">Number of detector segments</td>']
        s += [f'<td>{self._number_of_detector_segments}</td></tr>']
        s += ['<tr><td style="text-align: left;">Number of projections</td>']
        s += [f'<td>{self._rotarr.size}</td></tr>']
        s += ['<tr><td style="text-align: left;">Detection segment phis</td>']
        s += [f'<td>{self._detector_segment_phis}</td></tr>']
        s += ['</tbody>']
        return '\n'.join(s)

    def number_of_projectsion(self) -> int:
        """Number of projections."""
        return self._rotarr.size

    def number_of_detector_segments(self) -> int:
        """Number of detector segments."""
        return self._number_of_detector_segments
