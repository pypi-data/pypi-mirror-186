"""Calculate the angle (0...360) from p1 to p2."""
# pylint: disable=invalid-name
import math
from typing import List, Optional, Tuple, Union


def get_angle(
    p2: Union[List[float], Tuple[float, ...]],
    p1: Optional[Union[List[float], Tuple[float, ...]]] = None,
):
    """Calculate the angle from p1 to p2.

    Notice the order (p2, p1), not (p1, p2)

    Args:
      p2: second points, Union[List[float], Tuple[float...])

    Returns:
      0...360 (anti-clockwise) directional degrees
    >>> get_angle((1, 0), (1, -1)) == 90.0
    True
    >>> get_angle((0, 0), (1, -1)) == 135
    True
    >>> get_angle((1, -1), (0, 0)) == 360 - 45
    True
    """
    if p1 is None:
        p1 = [0, 0]
    try:
        _ = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0])) % 360
    except (IndexError, TypeError) as exc:
        raise Exception("Expect a list or tuple of at least 2 elements.") from exc

    return _
