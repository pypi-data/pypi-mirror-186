"""Gen triple-set from a matrix."""
# pylint: disable=unused-import

from typing import List, Tuple, Union  # noqa

import numpy as np
# import pandas as pd


def cmat2tset(
    cmat1: Union[List[List[float]], np.ndarray],
    # thirdcol: bool = True
) -> np.ndarray:
    """Gen triple-set from a matrix.

    Args:
        cmat1: 2d-array or list, correlation or other metric matrix

    Returns:
        Obtain the max and argmax for each column, erase the row afterwards to eliminate
        one single row  that would dominate every column.
    """
    # if isinstance(cmat, list):
    cmat = np.array(cmat1)

    if cmat.ndim != 2:
        raise SystemError("data not 2d...")

    _ = """
    # y00 = range(cmat.shape[1])  # cmat.shape[0] long time wasting bug

    yargmax = cmat.argmax(axis=0)
    if thirdcol:
        ymax = cmat.max(axis=0)

        res = [*zip(y00, yargmax, ymax)]  # type: ignore
        # to unzip
        # a, b, c = zip(*res)

        return res

    _ = [*zip(y00, yargmax)]  # type: ignore
    return _
    """
    # low_ = cmat.min() - 1
    low_ = -0.1
    argmax_max = []
    src_len, tgt_len = cmat.shape  # ylim, xlim
    for _ in range(min(src_len, tgt_len)):
        argmax = int(cmat.argmax())  # numpy.int64 to int
        row, col = divmod(argmax, tgt_len)
        argmax_max.append([col, row, cmat.max()])  # x-axis, y-axis

        # erase row-th row and col-th col of cmat
        cmat[row, :] = low_
        cmat[:, col] = low_

    return np.array(argmax_max)
