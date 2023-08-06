"""Remove entries with undisired  indices."""
import numpy as np

from .gen_slopes import gen_slopes


def remove_indices(out0, slope=1):
    """Remove entries with undisired  indices."""
    slopes = gen_slopes(out0)

    # if no negative slopes, do nothing
    if np.all(slopes.T[0] > 0):
        return out0

    # out0 = [0] + out0

    out1 = out0[
        [0]
        + [1 + idx for idx, el in enumerate(slopes) if 2 * slope > el[0] > slope / 2]
    ]
    return out1
