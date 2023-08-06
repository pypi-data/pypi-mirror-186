"""Gen pset from cmat. Find pairs for a given cmat.

tinybee.find_pairs.py with fixed estimator='dbscan' eps=eps, min_samples=min_samples
"""
# pylint: disable=invalid-name
from typing import Any  # , List, Tuple

import logzero
from logzero import logger
from nptyping import Float, NDArray, Shape
from set_loglevel import set_loglevel

import numpy as np

logzero.loglevel(set_loglevel())  # default to os.environ['loglevel'] or 20 (info)


def tset2pset(
    tset: NDArray[Shape["Any, 3"], Float],
    n_col0: int,
    n_col1: int,
) -> NDArray[Shape["Any, 3"], Float]:
    """Gen pset from tset.

    Find valid pairs (non-decreasing) for a given tset.

    Args:
        tset: triple set
        n_col0: max value of column 0 of tset
        n_col1: max value of column 1 of tset

    Returns:
        pairs + "" or metric (float)

    gen_pset in cmat2aset
    """
    # n_col0, n_col1 = endpoint

    buff = [(-1, -1, ""), (n_col0, n_col1, "")]

    # for idx, tset_elm in enumerate(tset):
    for tset_elm in tset:
        # logger.debug("buff: %s", buff)
        # postion max in ymax and insert in buff
        # if with range given by iset+-delta and
        # it's valid (do not exceed constraint
        # by neighboring points

        # argmax = int(np.argmax(ymax))

        logger.debug("tset_elm: %s", tset_elm)

        # ymax[_] = low_
        # elm = tset[argmax]
        # elm0, *_ = elm

        elm0 = tset_elm[0]

        # position elm in buff
        idx = -1  # for making pyright happy
        for idx, loc in enumerate(buff):
            if loc[0] > elm0:
                break
        else:
            idx += 1  # last

        if tset_elm[1] > buff[idx - 1][1] and tset_elm[1] < buff[idx][1]:
            buff.insert(idx, tset_elm)
            logger.debug("idx: %s, tset_elm: %s", idx, tset_elm)
        else:
            logger.debug("\t***\t idx: %s, tset_elm: %s", idx, tset_elm)

    # remove first and last entry in buff
    buff.pop(0)
    buff.pop()

    # return [(int(elm0), int(elm1), elm2) for elm0, elm1, elm2 in buff]
    return np.array(buff)
