"""Gen slopes."""
# pylint: disable=invalid-name
from typing import Any

import numpy as np
from nptyping import Float, NDArray, Shape


def gen_slopes(
    cset_top10: NDArray[Shape["Any, 2"], Float]
) -> NDArray[Shape["Any, 2"], Float]:
    """Gen slopes for 2-d array[[x0, y0], [x1, y1],... ]."""
    x = cset_top10.T[0]
    y = cset_top10.T[1]
    slopes = [np.polyfit(x[i : (i + 2)], y[i : (i + 2)], 1) for i in range(len(x) - 1)]

    return np.array(slopes)
