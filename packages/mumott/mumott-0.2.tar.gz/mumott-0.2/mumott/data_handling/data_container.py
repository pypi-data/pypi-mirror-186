"""
This file contains the class DataContainer, used to load data files
and initialize reconstruction parameters.
"""
import logging
from os.path import join
import numpy as np
from scipy.io import loadmat
import h5py as h5
from mumott.core.projection_parameters import ProjectionParameters
from .input_stack import InputStack
from .input_frame import InputFrame
from .reconstruction_input import ReconstructionInput
from .reconstruction_output import ReconstructionOutput
from .reconstruction_parameters import ReconstructionParameters
from .spherical_harmonic_parameters import SphericalHarmonicParameters
from .transform_parameters import TransformParameters


class DataContainer:

    """
    Loads SAXSTT data from files, is used to apply transforms and corrections if needed,
    and creates a :class:`ReconstructionParameters
    <mumott.data_handling.ReconstructionParameters>` object.

    Parameters
    ----------
    data_path : str
        Path of the data file relative to the directory of execution.
    data_filename : str
        File name of the data, including the extension.
    data_type : str, optional
        The type of data file. Supported values are ``h5`` (default, for hdf5 format)
        and ``mat`` (for cSAXS Matlab format).
    """
    def __init__(self,
                 data_path: str,
                 data_filename: str,
                 data_type: str = 'h5'):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
        self._correct_for_transmission_called = False
        self._transform_applied = False
        self._generated_parameters = False
        self._angles_in_radians = True
        file_path = join(data_path, data_filename)
        if data_type == 'mat':
            self._matlab_to_stack(file_path)
        elif data_type == 'h5':
            self._h5_to_stack(file_path)
        else:
            raise ValueError(f'Unknown data_type: {data_type}')
        self._check_degrees_or_radians()

    def _h5_to_stack(self, file_path: str):
        """
        Internal method for loading data from hdf5 file.
        """
        h5_data = h5.File(file_path, 'r')
        projections = h5_data['projections']
        number_of_projections = len(projections)
        self._stack = InputStack()
        for i in range(number_of_projections):
            f = InputFrame()
            p = projections[f'{i}']
            f.data = np.copy(p['data'])
            f.diode = np.copy(p['diode'])
            f.weights = np.copy(p['weights'])
            f.principal_rotation = p['rotations'][0]
            f.secondary_rotation = p['tilts'][0]
            f.j_offset = p['offset_j'][0]
            f.k_offset = p['offset_k'][0]
            if f.data.flags['F_CONTIGUOUS']:
                projection_shape = f.data.shape[-1::-1]
                f.data = (f.data.ravel(order='K')).reshape(projection_shape)
                f.diode = (f.diode.ravel(order='K')).reshape(projection_shape[:-1])
                f.weights = (f.weights.ravel(order='K')).reshape(projection_shape[:-1])
            self._stack.append(f)
        self._stack.detector_angles = np.copy(h5_data['detector_angles'])
        if 'volume_shape' in h5_data.keys():
            self._stack.volume_shape = np.copy(h5_data['volume_shape'])
        else:
            max_dimensions = self._stack.dimensions[:, :-1].max(0)
            self._stack.volume_shape = max_dimensions[[0, 0, 1]]

    def _matlab_to_stack(self, file_path: str):
        """
        Internal method for loading data from Matlab file.
        """
        try:
            matlab_data = loadmat(file_path)
            is_v73 = False
        except Exception as e:
            if 'v7.3' in str(e):
                logging.info('Matlab file version is v7.3, using h5py to load!')
                matlab_data = h5.File(file_path)
                is_v73 = True
            else:
                logging.warning(
                    'scipy.io.loadmat failed for unidentified reasons!\nTrying h5py...')
                matlab_data = h5.File(file_path)
                is_v73 = True
                logging.warning(
                    'The following exception was raised during execution of scipy.io.loadmat:\n' + str(e) +
                    '\nPlease proceed with caution!')
        number_of_projections = np.int32(matlab_data['projection']['data'].size)
        self._stack = InputStack()
        for i in range(number_of_projections):
            if is_v73:
                data = np.array(matlab_data[matlab_data['projection']['data'][i, 0]],
                                copy=True).astype(np.float64)
                diode = np.array(matlab_data[matlab_data['projection']['diode'][i, 0]],
                                 copy=True).astype(np.float64)
                temp_rot_x = np.array(matlab_data[matlab_data['projection']['rot_x'][i, 0]],
                                      copy=True).astype(np.float64)
                temp_rot_y = np.array(matlab_data[matlab_data['projection']['rot_y'][i, 0]],
                                      copy=True).astype(np.float64)
                temp_dx = np.array(matlab_data[matlab_data['projection']['dx'][i, 0]],
                                   copy=True).astype(np.float64)
                temp_dy = np.array(matlab_data[matlab_data['projection']['dy'][i, 0]],
                                   copy=True).astype(np.float64)
                window_mask = np.array(matlab_data[matlab_data['projection']['window_mask'][i, 0]],
                                       copy=True).astype(np.float64)
                tomo_axis_x = round(matlab_data[matlab_data['projection']['par'][0, 0]]['tomo_axis_x'][0, 0])
            else:
                data = np.copy(matlab_data['projection']['data'][0, i]).astype(np.float64)
                diode = np.copy(matlab_data['projection']['diode'][0, i]).astype(np.float64)
                temp_rot_x = np.copy(matlab_data['projection']['rot_x'][0, i].squeeze()).astype(np.float64)
                temp_rot_y = np.copy(matlab_data['projection']['rot_y'][0, i].squeeze()).astype(np.float64)
                temp_dx = np.copy(matlab_data['projection']['dx'][0, i].squeeze()).astype(np.float64)
                temp_dy = np.copy(matlab_data['projection']['dy'][0, i].squeeze()).astype(np.float64)
                window_mask = np.copy(matlab_data['projection']['window_mask'][0, i]).astype(np.float64)
                tomo_axis_x = round(matlab_data['projection']['par'][0, 0]['tomo_axis_x'][0, 0][0, 0])
            frame = InputFrame()
            projection_shape = data.shape
            if data.flags['F_CONTIGUOUS']:
                projection_shape = projection_shape[-1::-1]
            frame.data = (data.ravel(order='K')).reshape(projection_shape)
            frame.diode = (diode.ravel(order='K')).reshape(projection_shape[1:])
            frame.j_offset = temp_dx
            frame.k_offset = temp_dy
            if tomo_axis_x:
                frame.principal_rotation = temp_rot_x
                frame.secondary_rotation = temp_rot_y
            else:
                frame.principal_rotation = temp_rot_y
                frame.secondary_rotation = temp_rot_x
            frame.weights = (window_mask.ravel(order='K')).reshape(projection_shape[1:])
            self._stack.append(frame)
        number_of_segments = self._stack.dimensions[0, 0]
        if is_v73:
            self._stack.detector_angles = np.array(matlab_data[matlab_data['projection']['integ'][0, 0]]
                                                   ['phi_det'][:number_of_segments, 0], copy=True)
            matlab_data.close()
        else:
            self._stack.detector_angles = np.copy(matlab_data['projection']['integ'][0, 0]
                                                  ['phi_det'][0, 0][0, :number_of_segments])
        max_dimensions = self._stack.diode_dimensions[:, :].max(0)
        self._stack.volume_shape = max_dimensions[[0, 0, 1]]

    def _check_degrees_or_radians(self) -> None:
        """
        Internal method that tries to check if rotations are in degrees or radians,
        and informs the user to run the necessary conversion.
        """
        var_string = []
        arg_string = []
        if np.any(self._stack.principal_rotation > 2.1 * np.pi):
            var_string.append('Principal rotation')
            arg_string.append('convert_principal=True')
        if np.any(self._stack.secondary_rotation > 0.6 * np.pi):
            var_string.append('Secondary rotation')
            arg_string.append('convert_secondary=True')
        if np.any(self._stack.detector_angles > 2.1 * np.pi):
            var_string.append('Detector')
            arg_string.append('convert_detector=True')

        if len(var_string) > 0:
            logging.info(', '.join(var_string) + ' angles above thresholds found! If these\n'
                         'angles are in degrees, please run:\n'
                         'DataContainer.degrees_to_radians(' + ', '.join(arg_string) + ')\n'
                         'immediately after loading data!\n'
                         'If this check is mistaken and the angles are already in radians, please\n'
                         'set DataContainer.angles_in_radians = True before proceeding.')
            self._angles_in_radians = False
        else:
            self._angles_in_radians = True

    def degrees_to_radians(self,
                           convert_principal: bool = False,
                           convert_secondary: bool = False,
                           convert_detector: bool = False) -> None:
        """
        Converts angles in data from degrees to radians. Radians are
        necessary to run the reconstruction correctly.

        Parameters
        ----------
        convert_principal
            If ``True``, converts the principal rotation angles
            from degrees to radians. Default is ``False``.
        convert_secondary
            If ``True``, converts the secondary rotation angles
            from degrees to radians. Default is ``False``.
        convert_detector
            If ``True``, converts the detector angles
            from degrees to radians. Default is ``False``.
        """
        if convert_principal or convert_secondary or convert_detector:
            if self._transform_applied:
                raise RuntimeError('Transforms have already been applied! This method must\n'
                                   'be called before DataContainer.transform() is called!')
            if self._generated_parameters:
                raise RuntimeError(
                    'Parameters have already been generated! This method must\n'
                    'be called before DataContainer.ReconstructionParameters instance is retrieved!')
            if self._angles_in_radians:
                logging.info('Angles appear to already be in radians, conversion was not re-run.')
                return
        if convert_principal:
            self._stack.principal_rotation *= np.pi / 180
            self._stack.principal_rotation = np.mod(self._stack.principal_rotation, 2 * np.pi)
        if convert_secondary:
            self._stack.secondary_rotation *= np.pi / 180
            self._stack.secondary_rotation = np.mod(self._stack.secondary_rotation, 2 * np.pi)
        if convert_detector:
            self._stack.detector_angles *= np.pi / 180
            self._stack.detector_angles = np.mod(self._stack.detector_angles, 2 * np.pi)
        self._check_degrees_or_radians()

    def _generate_parameter_representation(self) -> None:
        spherical_harmonic_parameters = SphericalHarmonicParameters(
            l_max=0,
            number_of_coefficients=1,
            spherical_harmonic_factors=np.ones(self._stack.detector_angles.size))
        reconstruction_output = ReconstructionOutput(
            residual_gradient=np.ones(np.prod(self._stack.volume_shape)),
            reconstruction_projection=np.zeros_like(self._stack.data),
            residual=0.0,
            residual_per_projection=np.zeros(len(self._stack), dtype=np.float64))
        reconstruction_input = ReconstructionInput(np.ones(np.prod(self._stack.volume_shape)))
        projection_parameters = ProjectionParameters(
            self._stack.principal_rotation,
            self._stack.secondary_rotation,
            self._stack.detector_angles,
            self._stack.j_offset,
            self._stack.k_offset,
            self._stack.volume_shape,
            data_shape=self._stack.dimensions,
            integration_step_size=1. / 3.)
        self._reconstruction_parameters = ReconstructionParameters(
            settings=np.ones(3),
            data=self._stack.data,
            diode=self._stack.diode,
            projection_weights=(self._stack.weights.reshape(-1, 1) *
                                np.ones((1, self._stack.dimensions[0, -1]))).flatten(),
            spherical_harmonic_parameters=spherical_harmonic_parameters,
            projection_parameters=projection_parameters,
            reconstruction_output=reconstruction_output,
            reconstruction_input=reconstruction_input)
        self._generated_parameters = True

    @property
    def angles_in_radians(self) -> bool:
        """
        This indicates whether all the angles of the data are in radians (``True``) or not (``False``).
        Unless this is ``True``, several class methods cannot be run. To remedy a ``False`` value,
        use :func:`degrees_to_radians <mumott.data_handling.DataContainer.degrees_to_radians>`
        to convert the needed values, or if your angles are already in radians and the data loading
        method incorrectly detected them as degrees, simply set ``DataContainer.angles_in_radians = True``.
        """
        return self._angles_in_radians

    @angles_in_radians.setter
    def angles_in_radians(self, val: bool) -> None:
        """
        Setter method for the property `angles_in_radians`, for it to be set to ``True`` or ``False``
        when the loading method either incorrectly identifies angles in radians as being in degrees
        in the data, or when it fails to detect angles in degrees as being in radians.
        """
        self._angles_in_radians = val

    @property
    def stack(self) -> InputStack:
        """
        An :class:`InputStack <mumott.data_handling.input_stack.InputStack>` object that
        contains the data loaded by :class:`DataContainer <mumott.data_handling.DataContainer>`
        during initialization.
        """
        return self._stack

    @property
    def reconstruction_parameters(self) -> ReconstructionParameters:
        """
        Parameters for the SAXSTT reconstruction.
        """
        if not self._generated_parameters:
            self._generate_parameter_representation()
        return self._reconstruction_parameters

    def correct_for_transmission(self) -> None:
        """
        Applies correction from the input provided in the :attr:`diode
        <mumott.data_handling.input_frame.InputFrame>` field.  Should
        only be used if this correction has not already been applied.
        """
        if self._correct_for_transmission_called:
            logging.info(
                'DataContainer.correct_for_transmission() has been called already!'
                '\nThe correction has been applied previously, and the repeat call is ignored!')
            return
        data = self._stack.data.reshape(-1, self._stack.dimensions[0, -1]) / \
            self._stack.diode.reshape(-1, 1)
        self._stack.data = data.flatten()
        if self._generated_parameters:
            self._reconstruction_parameters.data = (
                self._reconstruction_parameters.data.reshape(-1, self._stack.dimensions[0, -1]) /
                self._reconstruction_parameters.diode.reshape(-1, 1)).flatten()
        self._correct_for_transmission_called = True

    def transform(self,
                  transform_parameters: TransformParameters) -> None:
        """
        Modifies the coordinate system of the loaded data to match the coordinate
        system expected by the reconstruction. The transforms must be specified using
        a :class:`TransformParameters <mumott.data_handling.TransformParameters>` object.

        Parameters
        ----------
        transform_parameters
            This object specifies information about the input coordinate system needed
            to transform the data into the expected coordinate system.
        """
        if not self._angles_in_radians:
            raise RuntimeError(
                'Angles do not appear to be in radians! Please\n'
                'run DataContainer.degrees_to_radians(...) to do the necessary\n'
                'conversions, or, if you are sure that they are already in radians,\n'
                'set DataContainer.angles_in_radians = True.')
        # Find the index transpositions and inversion necessary to place data into
        # the coordinate assumed by the reconstruction.
        transpose_inds = np.argsort(transform_parameters.data_sorting)
        sort_array = np.array(transform_parameters.data_sorting)
        wt_transpose_inds = transpose_inds[sort_array[transpose_inds] != 2]
        if wt_transpose_inds[0] < wt_transpose_inds[1]:
            wt_transposer = (0, 1)
        else:
            wt_transposer = (1, 0)
            # Swap offsets if axes are flipped.
            temp = self._stack.j_offset
            self._stack.j_offset = self._stack.k_offset
            self._stack.k_offset = temp
        if not np.all(self._stack.dimensions[:, wt_transpose_inds].prod(axis=1) ==
                      self._stack.diode_dimensions.prod(axis=1)):
            raise ValueError('The data_sorting in TransformParameters appears to be '
                             'incorrect. Please ensure that you have correctly labeled '
                             'the dimension containing the detector segments in your data as `2`.')
        flip_axes = np.array((0, 1))
        flip_axes = flip_axes[np.array(
            transform_parameters.data_index_origin).astype(bool)]
        for i, f in enumerate(self._stack):
            # Reshape the indices of every slice of data, and reinsert them.
            # Every slice corresponds to one projection.
            frame_data = np.copy(f.data)
            frame_data = frame_data.transpose(transpose_inds)
            frame_data = frame_data.flatten()
            frame_data = frame_data.reshape(self._stack.dimensions[i, transpose_inds])
            frame_data = np.flip(frame_data, axis=flip_axes)
            f.data = frame_data

            # Similarly reshape the weight array.
            frame_weights = np.copy(f.weights)
            frame_weights = frame_weights.transpose(wt_transposer)
            frame_weights = frame_weights.flatten()
            frame_weights = frame_weights.reshape(self._stack.dimensions[i, wt_transpose_inds])
            frame_weights = np.flip(frame_weights, axis=flip_axes)
            f.weights = frame_weights

            # And the diode array.
            frame_diode = np.copy(f.diode)
            frame_diode = frame_diode.transpose(wt_transposer)
            frame_diode = frame_diode.flatten()
            frame_diode = frame_diode.reshape(self._stack.dimensions[i, wt_transpose_inds])
            frame_diode = np.flip(frame_diode, axis=flip_axes)
            f.diode = frame_diode

            self._stack[i] = f

        # Adjust the sign of the rotations.
        a = 1 + np.round(transform_parameters.principal_rotation_right_handed)
        self._stack.principal_rotation *= (-1) ** a
        b = 1 + np.round(transform_parameters.secondary_rotation_right_handed)
        self._stack.secondary_rotation *= (-1) ** b

        # Adjust the angles of the detector.
        a = 1 + np.round(transform_parameters.detector_angle_right_handed)
        b = complex(transform_parameters.detector_angle_0[0],
                    transform_parameters.detector_angle_0[1])
        self._stack.detector_angles = np.angle(np.exp((-1) ** a * 1j * self._stack.detector_angles) * b)

        # Adjust the signs of the alignment offsets.
        a = 1 + np.round(transform_parameters.offset_positive[0])
        self._stack.j_offset *= (-1) ** a
        b = 1 + np.round(transform_parameters.offset_positive[1])
        self._stack.k_offset *= (-1) ** b

        # If width/height are swapped in projection, swap also in volume_shape
        if wt_transposer == (1, 0):
            volume_width = self._stack.volume_shape[2]
            volume_height = self._stack.volume_shape[0]
            self._stack.volume_shape[0:2] = volume_width
            self._stack.volume_shape[2] = volume_height
        self._transform_applied = True

    def __str__(self) -> str:
        wdt = 74
        s = []
        s += ['=' * wdt]
        s += ['DataContainer'.center(wdt)]
        s += ['-' * wdt]
        s += ['{:26} : {}'.format('Number of projections', len(self.stack))]
        s += ['{:26} : {}'.format('Volume shape', self.stack.volume_shape)]
        s += ['{:26} : {}'.format('Corrected for transmission', self._correct_for_transmission_called)]
        s += ['{:26} : {}'.format('Angles in radians', self.angles_in_radians)]
        s += ['{:26} : {}'.format('Transformation applied', self._transform_applied)]
        s += ['{:26} : {}'.format('Reconstruction parameters generated', self._generated_parameters)]
        s += ['=' * wdt]
        return '\n'.join(s)

    def _repr_html_(self) -> str:
        s = []
        s += ['<h3>DataContainer</h3>']
        s += ['<table border="1" class="dataframe">']
        s += ['<thead><tr><th style="text-align: left;">Field</th><th>Size</th></tr></thead>']
        s += ['<tbody>']
        s += ['<tr><td style="text-align: left;">Number of projections</td>']
        s += [f'<td>{len(self.stack)}</td></tr>']
        s += ['<tr><td style="text-align: left;">Volume shape</td>']
        s += [f'<td>{self.stack.volume_shape}</td></tr>']
        s += ['<tr><td style="text-align: left;">Corrected for transmission</td>']
        s += [f'<td>{self._correct_for_transmission_called}</td></tr>']
        s += ['<tr><td style="text-align: left;">Angles in radians</td>']
        s += [f'<td>{self.angles_in_radians}</td></tr>']
        s += ['<tr><td style="text-align: left;">Transformation applied</td>']
        s += [f'<td>{self._transform_applied}</td></tr>']
        s += ['<tr><td style="text-align: left;">Reconstruction parameters generated</td>']
        s += [f'<td>{self._generated_parameters}</td></tr>']
        s += ['</tbody>']
        s += ['</table>']
        return '\n'.join(s)
