""" Container for class InputFrame. """
import numpy as np
from dataclasses import dataclass
from numpy.typing import NDArray


@dataclass
class InputFrame:
    """ Frame containing data and metadata from a single SAXSTT measurement. Typically
    appended to an :class:`InputStack <mumott.data_handling.input_stack.InputStack>`.

    Parameters
    ----------
    data
        Data from measurement, structured into 3 dimensions representing
        the two scanning directions and the detector angle.
    diode
        Diode or transmission data from measurement, structured into
        2 dimensions representing the two scanning directions.
    weights
        Weights or masking information, represented as a number
        between ``0.`` and ``1.``. ``0.`` means mask, ``1.`` means
        do not mask. Structured the same way as :attr:`diode`.
    principal_rotation
        The principal rotation angle of this measurement, in radians.
    secondary_rotation
        The secondary rotation angle of this measurement, in radians.
    j_offset
        The offset needed to align the first spatial dimension of
        this measurement, in pixels.
    k_offset
        The offset needed to align the second spatial dimension of
        this measurement, in pixels.
    frame_number
        The index of this frame in a parent
        :class:`InputFrame <mumott.data_handling.input_frame.InputFrame>`.
    """
    data: NDArray[np.float64] = np.array([]).astype(np.float64)
    diode: NDArray[np.float64] = np.array([]).astype(np.float64)
    weights: NDArray[np.float64] = np.array([]).astype(np.float64)
    principal_rotation: np.float64 = np.float64(0)
    secondary_rotation: np.float64 = np.float64(0)
    j_offset: np.float64 = np.float64(0)
    k_offset: np.float64 = np.float64(0)

    def __str__(self) -> str:
        s = []
        wdt = 74
        s = []
        s += ['=' * wdt]
        s += ['InputFrame'.center(wdt)]
        s += ['-' * wdt]
        with np.printoptions(threshold=4, precision=5, linewidth=60, edgeitems=1):
            s += ['{:18} :\n {}'.format('Data', self.data)]
            s += ['{:18} :\n {}'.format('Diode', self.diode)]
            s += ['{:18} :\n {}'.format('Weights', self.weights)]
            s += ['{:18} : {}'.format('Principal rotation', self.principal_rotation)]
            s += ['{:18} : {}'.format('Secondary rotation', self.secondary_rotation)]
            s += ['{:18} : {}'.format('Offset j', self.j_offset)]
            s += ['{:18} : {}'.format('Offset k', self.k_offset)]
        s += ['=' * wdt]
        return '\n'.join(s)

    def _repr_html_(self) -> str:
        s = []
        s += ['<h3>InputFrame</h3>']
        s += ['<table border="1" class="dataframe">']
        s += ['<thead><tr><th style="text-align: left;">Field</th><th>Size</th><th>Data</th></tr></thead>']
        s += ['<tbody>']
        with np.printoptions(threshold=4, precision=5, linewidth=40, edgeitems=1):
            s += ['<tr><td style="text-align: left;">Data</td>']
            s += [f'<td>{self.data.shape}</td><td>{self.data}</td></tr>']
            s += [f'<tr><td style="text-align: left;">Diode</td><td>{self.diode.shape}</td>']
            s += [f'<td>{self.diode}</td></tr>']
            s += [f'<tr><td style="text-align: left;">Weights</td><td>{len(self.weights)}</td>']
            s += [f'<td>{self.weights}</td></tr>']
            s += ['<tr><td style="text-align: left;">Principal rotation</td>']
            s += [f'<td>{len(self.principal_rotation)}</td>']
            s += [f'<td>{self.principal_rotation}</td></tr>']
            s += ['<tr><td style="text-align: left;">Secondary rotation</td>']
            s += [f'<td>{len(self.secondary_rotation)}</td>']
            s += [f'<td>{self.secondary_rotation}</td></tr>']
            s += [f'<tr><td style="text-align: left;">Offset j</td><td>{len(self.j_offset)}</td>']
            s += [f'<td>{self.j_offset}</td></tr>']
            s += [f'<tr><td style="text-align: left;">Offset k</td><td>{len(self.k_offset)}</td>']
            s += [f'<td>{self.k_offset}</td></tr>']
        s += ['</tbody>']
        s += ['</table>']
        return '\n'.join(s)
