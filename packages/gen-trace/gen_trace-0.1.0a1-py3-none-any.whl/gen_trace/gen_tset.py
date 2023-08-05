"""Gne tset from cmat based on argmax max axis=0."""
# pylint: disable=invalid-name

from typing import List, Tuple, Union  # noqa

import numpy as np
# import pandas as pd


def gen_tset(
    cmat_: Union[List[List[float]], np.ndarray],
    # thirdcol: bool = True
) -> np.ndarray:
    """Gen triple-set from a matrix.

    Args
        cmat: 2d-array or list, correlation or other metric matrix
        # thirdcol: bool, whether to output a third column (max value)

    Returns
        Obtain the max and argmax along axis=0 line.
    """
    cmat = np.array(cmat_)

    # if not cmat.ndim == 2:
    if cmat.ndim != 2:
        raise SystemError("data not 2d...")

    _, ncol = cmat.shape
    argmax = cmat.argmax(axis=0)
    max_ = cmat.max(axis=0)

    return np.array(zip(range(ncol), argmax, max_))
