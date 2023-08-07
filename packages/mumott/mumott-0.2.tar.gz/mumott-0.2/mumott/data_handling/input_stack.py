""" Container for class InputStack. """
import numpy as np
from dataclasses import dataclass
from .input_frame import InputFrame
from numpy.typing import NDArray


@dataclass
class InputStack:
    """
    A stack of data and metadata. Contains flattened data which may have a "rugged"
    structure, i.e., not necessarily be representible as a structured array. This class
    behaves like a list of :class:`InputFrame <mumott.data_handling.input_frame.InputFrame>`
    objects allowing for iteration over frames as well as access by index for retrieval,
    modification or deletion. Instances of this class do not store the
    :class:`InputFrame <mumott.data_handling.input_frame.InputFrame>` objects appended to it,
    indexing it will return "virtual"
    :class:`InputFrame <mumott.data_handling.input_frame.InputFrame>` objects with views to
    the data stored in the :class:`InputStack <mumott.data_handling.input_stack.InputStack>`.

    Parameters
    ----------
    data
        Flat, contiguous storage of the data referred to by each
        :class:`InputStack <mumott.data_handling.input_stack.InputStack>`.
    diode
        Flat, contiguous storage of the diode referred to by each
        :class:`InputStack <mumott.data_handling.input_stack.InputStack>`.
    weights
        Flat, contiguous storage of the projection weights referred to by each
        :class:`InputStack <mumott.data_handling.input_stack.InputStack>`.
    dimensions
        Contains the dimensions of :attr:`data` as structured in each
        :class:`InputStack <mumott.data_handling.input_stack.InputStack>`,
        with shape ``(N, 3)``.
    diode_dimensions
        Contains the dimensions of the :attr:`diode` and :attr:`weights` as structured
        in each :class:`InputStack <mumott.data_handling.input_stack.InputStack>`,
        with shape ``(N, 2)``.
    principal_rotation
        Contains the :attr:`principal_rotation` of each frame.
    secondary_rotation
        Contains the :attr:`secondary_rotation` of each frame.
    j_offset
        Contains the :attr:`j_offset` of each frame.
    k_offset
        Contains the :attr:`k_offset` of each frame.
    detector_angles
        Contains the detector angles associated with the whole data set.
    volume_shape
        Contains shape of the volume that will be reconstructed from the
        whole data set.
    """
    _data_start: NDArray[np.int32] = np.array([]).astype(np.int32)
    _data_stop: NDArray[np.int32] = np.array([]).astype(np.int32)
    _diode_start: NDArray[np.int32] = np.array([]).astype(np.int32)
    _diode_stop: NDArray[np.int32] = np.array([]).astype(np.int32)
    data: NDArray[np.float64] = np.array([]).astype(np.float64)
    diode: NDArray[np.float64] = np.array([]).astype(np.float64)
    weights: NDArray[np.float64] = np.array([]).astype(np.float64)
    dimensions: NDArray[np.int32] = np.array([[]]).astype(np.int32)
    diode_dimensions: NDArray[np.int32] = np.array([[]]).astype(np.int32)
    principal_rotation: NDArray[np.float64] = np.array([]).astype(np.float64)
    secondary_rotation: NDArray[np.float64] = np.array([]).astype(np.float64)
    j_offset: NDArray[np.float64] = np.array([]).astype(np.float64)
    k_offset: NDArray[np.float64] = np.array([]).astype(np.float64)
    detector_angles: NDArray[np.float64] = np.array([]).astype(np.float64)
    volume_shape: NDArray[np.int32] = np.array([]).astype(np.int32)

    def __delitem__(self, i: int) -> None:
        """ Deletes the data contained in one frame. """
        if abs(i) > len(self) - round(float(i >= 0)):
            raise IndexError(f"Index {i} is out of bounds for InputStack of length {len(self)}!")
        self.data = np.delete(self.data, slice(self._data_start[i], self._data_stop[i]))
        self.diode = np.delete(self.diode, slice(self._diode_start[i], self._diode_stop[i]))
        self.weights = np.delete(self.weights, slice(self._diode_start[i], self._diode_stop[i]))
        self.principal_rotation = np.delete(self.principal_rotation, i, axis=0)
        self.secondary_rotation = np.delete(self.secondary_rotation, i, axis=0)
        self.j_offset = np.delete(self.j_offset, i, axis=0)
        self.k_offset = np.delete(self.k_offset, i, axis=0)
        self._data_start[i:] -= self.dimensions[i].prod()
        self._data_stop[i:] -= self.dimensions[i].prod()
        self._diode_start[i:] -= self.diode_dimensions[i].prod()
        self._diode_stop[i:] -= self.diode_dimensions[i].prod()
        self._data_start = np.delete(self._data_start, i, axis=0)
        self._data_stop = np.delete(self._data_stop, i, axis=0)
        self._diode_start = np.delete(self._diode_start, i, axis=0)
        self._diode_stop = np.delete(self._diode_stop, i, axis=0)
        self.dimensions = np.delete(self.dimensions, i, axis=0)
        self.diode_dimensions = np.delete(self.diode_dimensions, i, axis=0)

    def append(self, frame: InputFrame) -> None:
        """
        Appends an :class:`InputStack <mumott.data_handling.input_stack.InputStack>` to the
        :class:`InputStack <mumott.data_handling.input_stack.InputStack>`. All data in the frame
        is copied over to the stack, and can be accessed by indexing the stack as a "virtual frame".

        Parameters
        ----------
        frame
            The :class:`InputStack
            <mumott.data_handling.input_stack.InputStack>` object to
            be appended to the :class:`InputStack
            <mumott.data_handling.input_stack.InputStack>`.
        """
        data = self.data
        diode = self.diode
        weights = self.weights
        _data_start = self._data_start
        _data_stop = self._data_stop
        _diode_start = self._diode_start
        _diode_stop = self._diode_stop
        dimensions = self.dimensions
        diode_dimensions = self.diode_dimensions
        principal_rotation = self.principal_rotation
        secondary_rotation = self.secondary_rotation
        j_offset = self.j_offset
        k_offset = self.k_offset
        self.data = np.append(data, frame.data.flatten())
        self.diode = np.append(diode, frame.diode.flatten())
        self.weights = np.append(weights, frame.weights.flatten())
        if len(self) == 0:
            self._data_start = np.append(_data_start, 0)
            self._data_stop = np.append(_data_stop, frame.data.size)
            self._diode_start = np.append(_diode_start, 0)
            self._diode_stop = np.append(_diode_stop, frame.diode.size)
            self.dimensions = np.copy(np.array(frame.data.shape).reshape(1, -1))
            self.diode_dimensions = np.copy(np.array(frame.diode.shape).reshape(1, -1))
        else:
            self._data_start = np.append(_data_start, _data_stop[-1])
            self._data_stop = np.append(_data_stop, _data_stop[-1] + frame.data.size)
            self._diode_start = np.append(_diode_start, _diode_stop[-1])
            self._diode_stop = np.append(_diode_stop, _diode_stop[-1] + frame.diode.size)
            self.dimensions = np.append(
                dimensions, np.array(frame.data.shape).reshape(1, -1), axis=0)
            self.diode_dimensions = np.append(
                diode_dimensions, np.array(frame.diode.shape).reshape(1, -1), axis=0)
        self.principal_rotation = np.append(principal_rotation, frame.principal_rotation)
        self.secondary_rotation = np.append(secondary_rotation, frame.secondary_rotation)
        self.j_offset = np.append(j_offset, frame.j_offset)
        self.k_offset = np.append(k_offset, frame.k_offset)

    def __setitem__(self, i: int, frame: InputFrame) -> None:
        """
        This allows each frame of the InputStack to be safely modified,
        by replacing the contents with those of an
        :class:`InputStack <mumott.data_handling.input_stack.InputStack>` object.
        """
        if abs(i) > len(self) - round(float(i >= 0)):
            raise IndexError(f"Index {i} is out of bounds for InputStack of length {len(self)}!")
        self.dimensions[i, :] = frame.data.shape
        self.diode_dimensions[i, :] = frame.diode.shape
        self.data[self._data_start[i]:self._data_stop[i]] = frame.data.ravel()
        self.diode[self._diode_start[i]:self._diode_stop[i]] = frame.diode.ravel()
        self.weights[self._diode_start[i]:self._diode_stop[i]] = frame.weights.ravel()
        self.principal_rotation[i:i+1] = frame.principal_rotation
        self.secondary_rotation[i:i+1] = frame.secondary_rotation
        self.j_offset[i:i+1] = frame.j_offset
        self.k_offset[i:i+1] = frame.k_offset

    def __getitem__(self, i: int) -> InputFrame:
        """
        This allows the InputStack to be indexed and iterated over, creating a
        "virtual" :class:`InputStack <mumott.data_handling.input_stack.InputStack>` for every member.
        """
        if (abs(i) > len(self) - round(float(i >= 0))):
            raise IndexError(f"Index {i} is out of bounds for InputStack of length {len(self)}!")
        f = InputFrame(data=self.data[self._data_start[i]:self._data_stop[i]].reshape(self.dimensions[i]),
                       diode=self.diode[
                           self._diode_start[i]:self._diode_stop[i]].reshape(self.diode_dimensions[i]),
                       weights=self.weights[
                           self._diode_start[i]:self._diode_stop[i]].reshape(self.diode_dimensions[i]),
                       principal_rotation=self.principal_rotation[i:i+1],
                       secondary_rotation=self.secondary_rotation[i:i+1],
                       j_offset=self.j_offset[i:i+1],
                       k_offset=self.k_offset[i:i+1])
        return f

    def __len__(self) -> int:
        return len(self._data_start)

    def __str__(self) -> str:
        s = []
        wdt = 74
        s = []
        s += ['-' * wdt]
        s += ['InputStack'.center(wdt)]
        s += ['-' * wdt]
        with np.printoptions(threshold=4, precision=5, linewidth=60):
            s += ['{:18} : {}'.format('Data', self.data)]
            s += ['{:18} : {}'.format('Number of pixels j', self.diode_dimensions[:, 0])]
            s += ['{:18} : {}'.format('Number of pixels k', self.diode_dimensions[:, 1])]
            s += ['{:18} : {}'.format('Detector angles', self.detector_angles)]
            s += ['{:18} : {}'.format('Principal rotation', self.principal_rotation)]
            s += ['{:18} : {}'.format('Secondary rotation', self.secondary_rotation)]
        s += ['-' * wdt]
        return '\n'.join(s)

    def _repr_html_(self) -> str:
        s = []
        s += ['<h3>InputStack</h3>']
        s += ['<table border="1" class="dataframe">']
        s += ['<thead><tr><th style="text-align: left;">Field</th><th>Size</th><th>Data</th></tr></thead>']
        s += ['<tbody>']
        with np.printoptions(threshold=4, precision=5, linewidth=40):
            s += ['<tr><td style="text-align: left;">Data</td>']
            s += [f'<td>{len(self.data)}</td><td>{self.data}</td></tr>']
            s += ['<tr><td style="text-align: left;">Number of pixels i</td>']
            s += [f'<td>{len(self.diode_dimensions[:, 0])}</td>']
            s += [f'<td>{self.diode_dimensions[:, 0]}</td></tr>']
            s += ['<tr><td style="text-align: left;">Number of pixels j</td>']
            s += [f'<td>{len(self.diode_dimensions[:, 1])}</td>']
            s += [f'<td>{self.diode_dimensions[:, 1]}</td></tr>']
            s += ['<tr><td style="text-align: left;">Detector angles (rad)</td>']
            s += [f'<td>{len(self.detector_angles)}</td>']
            s += [f'<td>{self.detector_angles}</td></tr>']
            s += ['<tr><td style="text-align: left;">Principal rotation</td>']
            s += [f'<td>{len(self.principal_rotation)}</td>']
            s += [f'<td>{self.principal_rotation}</td></tr>']
            s += ['<tr><td style="text-align: left;">Secondary rotation</td>']
            s += [f'<td>{len(self.secondary_rotation)}</td>']
            s += [f'<td>{self.secondary_rotation}</td></tr>']
        s += ['</tbody>']
        s += ['</table>']
        return '\n'.join(s)
