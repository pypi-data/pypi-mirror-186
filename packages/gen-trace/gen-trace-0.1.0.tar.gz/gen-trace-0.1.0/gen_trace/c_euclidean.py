"""Calculate customized Euclidean distance."""
from math import dist
from sys import maxsize

# import logzero
# from set_loglevel import set_loglevel
# from logzero import logger
from .get_angle import get_angle

# logzero.loglevel(set_loglevel())


# def c_euclidean(x, y, scale=10.):
def c_euclidean(x, y, delta=3.0, thr=19.5):
    """Calculate customized Euclidean distance.

    Args:
        x, y: coordinates
        delta: 0..45, default 3.0 (degrees), math.tan(math.radians(3)) = 0.0524
            c_euclidean([0, 0], [1, 0.052], thr=maxsize) = maxsize
            c_euclidean([0, 0], [1, 0.053], thr=maxsize) = 1.0014035150727203
        thr: threhold, default 19.5

    Returns:
        customized Euclidean distance:
            points in 2-4 quadrants quadrant set to sys.maxsize

    >>> from math import sqrt
    >>> 1.7 > c_euclidean([0, 0], [1, 1]) > 1.4
    True
    >>> c_euclidean([0, 0], [-1, -1]) == maxsize # 1.7 > c_euclidean([0, 0], [-1, -1]) > 1.4
    True
    >>> c_euclidean([0, 0], [-1, 1]) == maxsize
    True
    >>> c_euclidean([0, 0], [1, -1]) == maxsize
    True
    >>> c_euclidean([0, 0], [2, 2]) <= sqrt(4+4)
    True
    >>> c_euclidean([0, 0], [1, 3]) == maxsize
    False
    >>> c_euclidean([0, 0], [1, 2]) <= sqrt(1 + 4)
    True
    >>> c_euclidean([0, 0], [-1, -2]) == maxsize # c_euclidean([0, 0], [-1, -2]) <= sqrt(1 + 4)
    True
    >>> c_euclidean([0, 0], [1, 1.25]) < 10
    True
    >>> c_euclidean([0, 0], [1, 0.05]) == maxsize  # math.tan(math.radians(3)) 0.05240777928304121
    True
    >>> c_euclidean([0, 0], [1, 19]) < 19.5  # math.tan(math.radians(87)) 19.08113668772816
    True
    >>> c_euclidean([0, 0], [1, 19.1]) == maxsize
    True
    """
    _ = """
    if x[0] == y[0] or x[1] == y[1]:
        return maxsize

    if abs(x[0] - y[0]) >= scale * abs(x[1] - y[1]) or abs(x[1] - y[1]) > scale * abs(
        x[0] - y[0]
    ):
        return maxsize
    """
    if delta < 0:
        delta = 3
    if delta > 45:
        delta = 3
    angle = get_angle(y, x)
    # if angle > 90 - delta and angle < 180 + delta:  # second quadrant

    _ = """
    if 90 < angle < 180 + delta:  # second quadrant
        return maxsize
    if angle < delta or angle > 270 - delta:  # fourth quadrant
        return maxsize
    # """

    if angle < delta or angle > 90 - delta:  # fourth quadrant
        return maxsize

    dist_ = dist(x, y)
    if dist_ > thr:
        dist_ = maxsize

    return dist_
