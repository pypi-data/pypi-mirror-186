"""Obtain topn sorted."""
from typing import Any

import numpy as np

# import numpy.typing as npt
from nptyping import Float, NDArray, Shape


def topn_sorted(
    # cset: npt.NDArray[(Any, 3), float], topn: int = 10
    cset: NDArray[Shape["Any, 3"], Float],
    topn: int = 10,
) -> NDArray[Shape["Any, 3"], Float]:
    """Obtain topn sorted.

    Args:
        cset: nx3 np.array
        topn: default 10, topn of cset.T[2]

    Retrns:
        sorted cset.T[0], topn of
    """
    _ = cset[np.argpartition(-cset.T[2], topn)[:topn]]
    _ = np.array(sorted(_, key=lambda x: x[0]))

    return _
