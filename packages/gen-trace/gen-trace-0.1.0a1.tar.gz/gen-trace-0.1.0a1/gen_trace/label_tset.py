"""Label tset -1 or 0 as clustering."""
# pylint: disable=invalid-name
import math
from typing import Any, List

import numpy as np
from nptyping import Float, NDArray, Shape

from gen_trace.get_angle import get_angle


def label_tset(
    tset: NDArray[Shape["Any, 3"], Float], cone=45, delta=5
) -> NDArray[Shape["Any, 1"], Float]:
    """Label tset -1 or 0 as clustering.

    Args:
        delta (in degrees), default 5
        cone: in degrees

    Returns:
        sequence of -1, 0
    """
    polyfit2 = np.polyfit(tset.T[0], tset.T[1], 2)
    slope2 = np.poly1d([2 * polyfit2[0], polyfit2[1]])

    # m_angle = [get_angle(tset[0])]
    labels = []
    last_p: List[float] = [0.0, 0.0]

    for idx, elm in enumerate(tset[1:]):
        deg = math.degrees(math.atan(slope2(elm[0])))
        angle = get_angle(elm.tolist(), last_p)
        if max(delta, deg - cone / 2) < angle < min(90 - delta, deg + cone / 2):
            labels.append(0)
            last_p = elm.tolist()
        else:
            labels.append(-1)

    return np.array([-1] + labels)
