""" Container for class ProjectionFrame. """
from dataclasses import dataclass
from numpy.typing import NDArray


@dataclass
class ProjectionFrame:
    """
    A dataclass for storing "frames" for instances of
    class:`ProjectionViewer <mumott.output_handling.ProjectionViewer>`.

    Attributes
    ----------
    mean
        The mean value of the data.
    std
        The standard deviation of the data.
    angle_color_quad
        A quadruplet of RGBA colors mapping phase angles
        that indicate the orientation of the image.
    """
    mean: NDArray[float]
    std: NDArray[float]
    angle_color_quad: NDArray[float]
