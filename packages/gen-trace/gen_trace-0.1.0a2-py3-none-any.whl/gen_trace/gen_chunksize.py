"""Gen chunksize (np.array_split) for n (number of elements) given a seg_size so that the resultant segment size closest to seg_size."""
# pylint: disable=invalid-name
from math import ceil


def gen_chunksize(n: int, seg_size: int = 600) -> int:
    """Gen chunksize (np.array_split) for n (number of elements) given a seg_size so that the resultant segment size closest to seg_size.

    Args:
        n: no of elements
        seg_size: no of elements in each segment

    Returns:
        chunksize, no of segments

    >>> gen_chunksize(999, 500)
    2
    >>> gen_chunksize(499, 500)
    1
    >>> gen_chunksize(799, 500)
    1
    >>> gen_chunksize(800, 500)
    2
    >>> gen_chunksize(1716, 500)  # 571 71
    3
    >>> gen_chunksize(1712, 500)  # 429 71
    3
    """
    chunksize0 = max(1, n // seg_size)
    chunksize1 = chunksize0 + 1

    seg_size0 = n // chunksize0
    seg_size1 = n // chunksize1
    seg_size0_ = seg_size0 + ceil((n - seg_size0 * chunksize0) / chunksize0)
    seg_size1_ = seg_size1 + ceil((n - seg_size1 * chunksize1) / chunksize1)

    # if abs(seg_size0 - seg_size) < abs(seg_size1 - seg_size):
    # if abs(seg_size0_ - seg_size) < abs(seg_size1_ - seg_size):
    if abs(seg_size0_ - seg_size) < abs(seg_size1_ - seg_size) + 200:
        return chunksize0

    return chunksize1
