"""Container for class OutputHandler."""
import os
import logging
from typing import Any, Dict, List

import numpy as np
import h5py
from numpy.typing import NDArray
from scipy.io import savemat

from mumott.data_handling.reconstruction_parameters import ReconstructionParameters


class OutputHandler:

    """This class handles the saving of output after a completed reconstruction.

    Parameters
    ----------
    reconstruction_parameters : ReconstructionParameters
        The :class:`ReconstructionParameters <mumott.reconstruction_parameters.ReconstructionParameters>`
        instance with which the reconstruction was or is to be performed.
    regularization_parameter_list : List[RegularizationParameters], optional
        If regularization is used, the list of :class:`RegularizationParameters
        <mumott.regularization_parameters.RegularizationParameters>`
        instances given to the :class:`Regularizer
        <mumott.regularizer.Regularizer>` should be given here.
    base_output_path : str, optional
        The path to which output should go. Default is ``'.'``.
    create_enclosing_folder : bool, optional
        Whether to create an enclosing folder where output is saved.
        Default is ``True``.
    enclosing_folder_name : str, optional
        If :attr:`create_enclosing_folder` is ``True``, this is the name
        of the folder that is created at :attr:`base_output_path`. Default
        is ``'output_folder'``.
    output_file_name : str, optional
        The base name of the output file without the file extension. Default is
        ``'output_file'``.
    overwrite_existing_files : bool, optional
        Whether to overwrite an existing file with the same path and name.
        Default is ``False``. If ``False`` and a file already exists, no
        output will be created.
    output_format : List[str], optional
        List of formats to output to, given as a list of strings. Valid entries
        for the list are ``'h5'`` (HDF5) and ``'mat'`` (Matlab). Default is ``['h5']``,
        saving to the HDF5 format.
    processed_outputs : List[str], optional
        List of outputs to derive from the reconstruction and write to file. Each output needs to be
        specified with a string. Possible entries are ``'coefficients'``, ``'rms_of_amplitude'``,
        ``'mean_of_amplitude'``, ``'std_of_amplitude'``, ``'relative_std_of_amplitude'``,
        ``'eigenvectors'``, ``'eigenvalues'``, ``'synthetic_data'``, and ``'rank_2_tensor'``.
        By default, all of these are included in the output.
    include_input_data : bool, optional
        Whether to include the raw input data in the output file. Default is ``False``.
    output_metadata : Dict[str, Any], optional
        A dictionary to include miscellaneous information freely specified by the user,
        e.g., names, dates, measurement facility, person responsible for the reconstruction...
        By default, two entries are specified noting the type of reconstruction as
        ``'SAXS tensor tomography'`` and the algorithm as ``'SIGTT'``.
    """
    def __init__(self,
                 reconstruction_parameters: ReconstructionParameters,
                 regularization_parameter_list: List[ReconstructionParameters] = [],
                 base_output_path: str = '.',
                 create_enclosing_folder: bool = True,
                 enclosing_folder_name: str = 'output_folder',
                 output_file_name: str = 'output_file',
                 overwrite_existing_files: bool = False,
                 output_format: List[str] = ['h5'],
                 processed_outputs: List[str] = ['coefficients',
                                                 'rms_of_amplitude',
                                                 'mean_of_amplitude',
                                                 'std_of_amplitude',
                                                 'relative_std_of_amplitude',
                                                 'eigenvectors',
                                                 'eigenvalues',
                                                 'order_amplitude',
                                                 'rank_2_tensor',
                                                 'synthetic_data'],
                 include_input_data: bool = False,
                 output_metadata: Dict[str, Any] = dict(reconstruction_type='SAXS tensor tomography',
                                                        algorithm='SIGTT')):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
        if create_enclosing_folder:
            try:
                os.mkdir(os.path.join(base_output_path, enclosing_folder_name))
            except FileExistsError:
                print('Output directory already exists!')
            self._output_base_dir = os.path.join(base_output_path, enclosing_folder_name)
        else:
            self._output_base_dir = os.path.join(base_output_path)
        self._regularization_parameter_list = regularization_parameter_list
        self._include_input_data = include_input_data
        self._overwrite_existing_files = overwrite_existing_files
        self._output_file_name = output_file_name
        self._reconstruction_parameters = reconstruction_parameters
        self._output_metadata = output_metadata
        self._projection_parameters = self._reconstruction_parameters.projection_parameters
        self._dimensions = (tuple(self._reconstruction_parameters.projection_parameters.volume_shape) + # noqa
                            (self._reconstruction_parameters.spherical_harmonic_parameters.number_of_coefficients,)) # noqa
        self._l_indices = self._reconstruction_parameters.spherical_harmonic_parameters.l_indices
        self._coefficients = self._reconstruction_parameters.reconstruction_input.optimization_coefficients.reshape(self._dimensions)  # noqa
        self._base_output_path = base_output_path
        self._create_enclosing_folder = create_enclosing_folder

        self._output_format_dict = dict(h5=self._save_to_h5,
                                        mat=self._save_to_matlab)
        for i, s in enumerate(output_format):
            if s not in self._output_format_dict.keys():
                logging.warning(f'Format \'{s}\' unknown! '
                                'This entry will be removed from the specified output formats!')
                del output_format[i]
        if len(output_format) < 1:
            raise ValueError('No valid output format specified!')
        self._output_format = output_format

        self._function_dict = dict(coefficients=self._return_coefficients,
                                   rms_of_amplitude=self._rms_of_amplitude,
                                   mean_of_amplitude=self._mean_of_amplitude,
                                   std_of_amplitude=self._std_of_amplitude,
                                   eigenvectors=self._eigenvectors,
                                   eigenvalues=self._eigenvalues,
                                   relative_std_of_amplitude=self._relative_std_of_amplitude,
                                   order_amplitude=self._order_amplitude,
                                   synthetic_data=self._return_synthetic_data,
                                   rank_2_tensor=self._return_rank_2_tensor)
        for i, s in enumerate(processed_outputs):
            if s not in self._function_dict.keys():
                logging.warning(f'Processed output type \'{s}\' unknown! '
                                'This entry will be removed from the specified output types!')
                del processed_outputs[i]
        if len(processed_outputs) < 1:
            raise ValueError('No valid processed output specified!')
        self._processed_outputs = processed_outputs
        self._computed_eigenvalues = False

    def save_output(self) -> None:
        """ Saves output. Run after completing reconstruction. """
        self._output_dict = dict((name, self._function_dict[name]()) for name in self._processed_outputs)
        self._computed_eigenvalues = False
        for key in self._output_format:
            self._output_format_dict[key]()

    def _return_synthetic_data(self) -> NDArray[float]:
        """ Returns synthetic data. """
        return self._reconstruction_parameters.reconstruction_output.reconstruction_projection.astype(float)

    def _return_coefficients(self) -> NDArray[float]:
        """ Returns coefficents. """
        return self._coefficients.astype(float)

    def _return_rank_2_tensor(self) -> NDArray[float]:
        """ Returns rank-2 tensor. """
        if not self._computed_eigenvalues:
            self._solve_eigenvalue_problem()
        return self._rank_2_tensor

    def _rms_of_amplitude(self) -> NDArray[float]:
        """ Returns root-mean-square of the reciprocal space map amplitude. """
        return np.sum(self._coefficients ** 2, axis=3).reshape(self._dimensions[:-1]).astype(float)

    def _mean_of_amplitude(self) -> NDArray[float]:
        """ Returns arithmetic mean of the reciprocal space map amplitude. """
        return self._coefficients[:, :, :, self._l_indices == 0].reshape(self._dimensions[:-1]).astype(float)

    def _std_of_amplitude(self) -> NDArray[float]:
        """ Returns arithmetic mean of the reciprocal space map amplitude. """
        return np.sqrt(np.sum(self._coefficients[:, :, :, self._l_indices > 0] ** 2,
                       axis=3)).reshape(self._dimensions[:-1]).astype(float)

    def _solve_eigenvalue_problem(self):
        """ Solves eigenvalue problem, saving values, vectors and rank-2 tensor. """
        if np.max(self._l_indices) < 2:
            print('Note: Max order < 2, so eigenvalues will be 0 and'
                  ' eigenvectors will be Cartesian basis vectors')
            self._eigenvalues = np.zeros_like(self._coefficients[0:3] + (3,))
            self._eigenvectors = np.zeros_like(self._coefficients[0:3] + (3, 3))
            self._eigenvectors[:, :, :, 0, 0] = 1.
            self._eigenvectors[:, :, :, 1, 1] = 1.
            self._eigenvectors[:, :, :, 2, 2] = 1.
            self._computed_eigenvalues = True
        A = self._coefficients[:, :, :, self._l_indices == 2].reshape(-1, 5)
        c1 = np.sqrt(15 / (4 * np.pi))
        c2 = 2 * np.sqrt(5 / (16 * np.pi))
        c3 = 2 * np.sqrt(15 / (16 * np.pi))
        AM = np.zeros((np.prod(self._dimensions[:-1]), 3, 3))
        AM[:, 0, 0] = c3 * A[:, 4] - c2 * A[:, 2]
        AM[:, 1, 1] = -c3 * A[:, 4] - c2 * A[:, 2]
        AM[:, 2, 2] = c2 * 2 * A[:, 2]
        AM[:, 0, 1] = c1 * A[:, 0]
        AM[:, 1, 0] = c1 * A[:, 0]
        AM[:, 2, 1] = c1 * A[:, 1]
        AM[:, 1, 2] = c1 * A[:, 1]
        AM[:, 2, 0] = c1 * A[:, 3]
        AM[:, 0, 2] = c1 * A[:, 3]
        self._rank_2_tensor = AM
        w, v = np.linalg.eigh(AM)
        sorting = np.argsort(w, axis=1).reshape(-1, 3, 1)
        v = v.transpose(0, 2, 1)
        v = np.take_along_axis(v, sorting, axis=1)
        v = v.transpose(0, 2, 1)
        v = v / np.sqrt(np.sum(v ** 2, axis=1).reshape(-1, 1, 3))
        self._eigenvalues = w.reshape(self._dimensions[:-1] + (3,)).astype(float)
        self._eigenvectors = v.reshape(self._dimensions[:-1] + (3, 3,)).astype(float)
        self._computed_eigenvalues = True

    def _eigenvalues(self):
        """ Returns eigenvalues, solving eigenvalue problem if necessary. """
        if not self._computed_eigenvalues:
            self._solve_eigenvalue_problem()
        return self._eigenvalues

    def _eigenvectors(self):
        """ Returns eigenvectors, solving eigenvalue problem if necessary. """
        if not self._computed_eigenvalues:
            self._solve_eigenvalue_problem()
        return self._eigenvectors

    def _relative_std_of_amplitude(self) -> NDArray[float]:
        """ Returns relative standard deviation of the amplitude. """
        return np.nan_to_num(self._std_of_amplitude() / self._mean_of_amplitude(),
                             nan=0.0, posinf=0.0, neginf=0.0)

    def _order_amplitude(self) -> NDArray[float]:
        """ Returns the standard deviation contribution of each order. """
        return_array = np.zeros(self._dimensions[:-1] + (self._l_indices.max() // 2,), dtype=float)
        for i, ll in enumerate(range(2, self._l_indices.max() + 1, 2)):
            return_array[..., i] = np.sqrt(np.sum(self._coefficients[..., self._l_indices == ll] ** 2,
                                           axis=3)).reshape(self._dimensions[:-1]).astype(float)
        return return_array

    def _save_to_matlab(self) -> None:
        """ Saves to ``'mat'`` format. """
        regularizer_dict = {}
        if self._regularization_parameter_list is not None:
            for item in self._regularization_parameter_list:
                for key, value in item.__dict__.items():
                    if key == 'reg_callable':
                        continue
                    regularizer_dict[key] = value

        mat_full_path = os.path.join(self._output_base_dir, self._output_file_name + '.mat')
        if os.path.exists(mat_full_path):
            if self._overwrite_existing_files:
                print('mat file already exists, but overwrite_existing_files is set to True.'
                      ' File will be overwritten.')
            else:
                print('mat file already exists, and overwrite_existing_files is set to False.'
                      ' mat output cancelled.')
                return
        dimensions = {}
        dimensions['volume_shape'] = \
            np.array(self._projection_parameters.volume_shape).astype(float)
        dimensions['number_of_projections'] = \
            np.array(self._projection_parameters.number_of_projections).astype(float)
        dimensions['number_of_voxels'] = \
            np.array(self._projection_parameters.number_of_voxels).astype(float)
        dimensions['number_of_detector_segments'] = \
            np.array(self._projection_parameters.number_of_detector_segments).astype(float)
        dimensions['integration_step_size'] = \
            np.array(self._projection_parameters.integration_step_size).astype(float)
        dimensions['sampling_kernel'] = \
            np.array(self._projection_parameters.sampling_kernel).astype(float)
        dimensions['kernel_offsets'] = \
            np.array(self._projection_parameters.kernel_offsets).astype(float)
        dimensions['data_shape'] = \
            np.array(self._projection_parameters.data_shape).astype(float)
        mdict = dict(
                    dimensions=dimensions,
                    output=self._output_dict,
                    metadata=self._output_metadata,
                    regularizer_dict=regularizer_dict)
        print('Saving ' + ', '.join(self._output_dict.keys()) + 'to Matlab')
        savemat(file_name=mat_full_path,
                mdict=mdict,
                appendmat=True,
                long_field_names=True,
                do_compression=True)

    def _save_to_h5(self) -> None:
        """ Saves to ``'h5'`` format. """
        h5_full_path = os.path.join(self._output_base_dir, self._output_file_name + '.h5')
        if os.path.exists(h5_full_path):
            if self._overwrite_existing_files:
                print('h5 file already exists, but overwrite_existing_files is set to True.'
                      ' File will be overwritten.')
            else:
                print('h5 file already exists, and overwrite_existing_files is set to False.'
                      ' h5 output cancelled.')
                return

        self._h5_output_file = h5py.File(h5_full_path, 'w')
        data_group = self._h5_output_file.create_group('output_data')
        for key, value in self._output_dict.items():
            print(f'Saving {key} to h5 ...')
            data_group.create_dataset(name=key,
                                      shape=value.shape,
                                      dtype=float,
                                      data=value,
                                      compression='gzip',
                                      compression_opts=9)
        if self._include_input_data:
            _ = self._h5_output_file.create_group('input_data')
            data_group.create_dataset(name='data',
                                      shape=self._reconstruction_parameters.data.shape,
                                      dtype=float,
                                      data=self._reconstruction_parameters.data,
                                      compression='gzip',
                                      compression_opts=9)

        dimension_group = self._h5_output_file.create_group('dimension_data')
        dimensions = {}
        dimensions['volume_shape'] = \
            np.array(self._projection_parameters.volume_shape).astype(float)
        dimensions['number_of_projections'] = \
            np.array(self._projection_parameters.number_of_projections).astype(float)
        dimensions['number_of_voxels'] = \
            np.array(self._projection_parameters.number_of_voxels).astype(float)
        dimensions['number_of_detector_segments'] = \
            np.array(self._projection_parameters.number_of_detector_segments).astype(float)
        dimensions['integration_step_size'] = \
            np.array(self._projection_parameters.integration_step_size).astype(float)
        dimensions['sampling_kernel'] = \
            np.array(self._projection_parameters.sampling_kernel).astype(float)
        dimensions['kernel_offsets'] = \
            np.array(self._projection_parameters.kernel_offsets).astype(float)
        dimensions['data_shape'] = \
            np.array(self._projection_parameters.data_shape).astype(float)
        for key, value in dimensions.items():
            dimension_group.create_dataset(name=key,
                                           shape=np.array(value).shape,
                                           dtype=np.array(value).dtype,
                                           data=np.array(value))

        regularization_group = self._h5_output_file.create_group('regularization_data')
        if self._regularization_parameter_list is not None:
            for item in self._regularization_parameter_list:
                function_group = regularization_group.create_group(item.__dict__['function_name'])
                for key, value in item.__dict__.items():
                    if key == 'reg_callable':
                        continue
                    else:
                        function_group.create_dataset(name=key,
                                                      data=value)

        metadata_group = self._h5_output_file.create_group('metadata')
        for key, value in self._output_metadata.items():
            print(key)
            metadata_group.create_dataset(name=key, data=value)
        self._h5_output_file.close()
