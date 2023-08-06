"""Get two points' slope."""
# pylint: disable=invalid-name
import math
from sys import maxsize


def get_slope(point1, point2=None):
    """Get the slope of two points (x0, y0), (x1, y1).

    if point2 is None, treat point1 as point2, set point1 to origin

    Hence, get_slope((x0, y0), (x1, y1)) is the same as get_slope((x1-x0, y1-y0).

    >>> get_slope((1, 1)) == 1.0
    True
    >>> get_slope((1, 1), (0, 0)) == 1.0
    True
    """
    if point2 is None:
        x1, y1, *_ = point1
        x0, y0 = 0, 0
    else:
        x0, y0, *_ = point1
        x1, y1, *_ = point2
    return (y1 - y0) / (x1 - x0) if x0 != x1 else math.copysign(maxsize, y1 - y0)
