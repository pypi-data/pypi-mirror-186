""" Container for class TransformParameters. """
from dataclasses import dataclass
from typing import Tuple


@dataclass
class TransformParameters:
    """
    Class indicating the coordinate system the data was stored and measured in.
    Used to transform it into the coordinate system of the reconstruction.

    Parameters
    ----------
    data_sorting : tuple(int, int, int), optional
        Should contain the numbers ``(0, 1, 2)`` (default order). Indicates the order of
        your data indices. ``0`` indicates the position of the index changing orthogonally
        to the principal axis of rotation (``j``). ``1`` indicates the position of the
        index parallel to the principal axis of rotation. ``2`` indicates the position
        of the index where detector information is stored.
    data_index_origin : tuple(int, int), optional
        Indicates the origin of the system your data is stored in. If incrementing the
        parallel index moves you along the direction of the principal axis, and
        incrementing the orthogonal index moves you opposite to the direction of the
        secondary axis, then the origin would be ``(1, 0)``. If both indices
        move against the axes, the origin would be ``(1, 1)``, and so on.
        Defaults to ``(0, 0)``.
    principal_rotation_right_handed : bool, optional
        If ``True`` (default), the rotation about the principal axis is taken to be
        right-handed. This means that after a rotation of 90 degrees, something originally
        aligned with the positive direction of the secondary axis would now be aligned
        with the positive direction of projection.
    secondary_rotation_right_handed : bool, optional
        If ``True`` (default), the rotation about the secondary axis is taken to be right-handed.
        This means that after a 90 degree rotation, something originally aligned with the
        positive direction of projection would now be aligned with the positive direction of
        the principal axis.
    detector_angle_0 : tuple(int, int), optional
        Indicates how the angle of the detector relates to the two axes. If
        ``(1, 0)`` (default), the zero lies on the secondary axis. If ``(0, 1)``,
        the zero lies on the principal axis.
    detector_angle_right_handed : bool, optional
        Indicates the direction of the angle. If for example zero degrees is at ``(1, 0)``
        and ninety degrees at ``(0, 1)``, then the system is right-handed. If
        zero degrees is at ``(0, 1)`` and ninety degrees is at ``(-1, 0)``,
        it is left handed. Defaults to ``True``.
    offset_positive : bool, optional
        Determines whether the offset of each projection that aligns it with the origin
        is positive or negative with respect to principal and secondary axis.
        If your offset was defined as positive but as aligning the projection coordinate system,
        then it should be negative here. Defaults to ``(True, True)``.
    """
    data_sorting: Tuple[int, int, int] = (0, 1, 2)
    data_index_origin: Tuple[int, int] = (0, 0)
    principal_rotation_right_handed: bool = True
    secondary_rotation_right_handed: bool = True
    detector_angle_0: Tuple[int, int] = (1, 0)
    detector_angle_right_handed: bool = True
    offset_positive: Tuple[bool, bool] = (True, True)
