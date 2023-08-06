"""Generate trace funtion for cmat."""
# pylint: disable=too-many-arguments, too-many-locals
from __future__ import annotations

from typing import Any, Callable, Optional, Union

import numpy as np

# import numpy.typing as npt
from logzero import logger
from nptyping import Float, NDArray, Shape
from sklearn import cluster

# from c_euclidean import c_euclidean
from gen_trace.c_euclidean import c_euclidean
from gen_trace.gen_chunksize import gen_chunksize


def with_func_attrs(**attrs: Any) -> Callable:
    """Define with_func_attrs closure."""

    def with_attrs(fct: Callable) -> Callable:
        for key, val in attrs.items():
            setattr(fct, key, val)
        return fct

    return with_attrs


# @with_func_attrs(tset: Optional[NDArray[Shape["Any, 3"], Float]] = None)
@with_func_attrs(tset=None)
def gen_cset(
    # cmat_: npt.NDArray[(Any, Any), float],
    cmat: NDArray[Shape["Any, Any"], Float],
    delta0: Optional[float] = None,
    delta1: Optional[float] = None,
    eps: Optional[float] = None,
    min_samples: Optional[int] = None,
    seg_size: Optional[int] = None,
    metric: Optional[Union[str, Callable]] = None,
) -> NDArray[Shape["Any, 3"], Float]:
    """Generate trace funtion for cmat.

    Args:
        cmat_: cmat = cmat_.T (transpose before processing)
            2-d array, n_row, n_col = cmat.shape, limit_x, limit_y = cmat.T.shape
        delta0: slope > slot_cmat (1 - delta0), default slope_cmat (1 - 1/2)
        delta1: maxsize > slope, default slope_cmat (1 + 1/2)
        eps: default 20, dist between two points smaller than eps to be clustered as one group,
            the bigger the eps, the more points will be clustered
        min_samples: default 3, min no of points in a group to be clustered as a group,
            the smaller the min_samples, the more points will be clustered
        seg_size: chunked into approximately seg_size elements for efficient clustering, default 600

    Returns:
        cset (clustered set) wit most outliers eliminated, hopefully
    """
    logger.debug(" entry ")

    # _ = """
    # cmat = cmat_.T
    n_row, n_col = cmat.shape

    slope_cmat = n_row / n_col
    if delta0 is None:
        delta0 = slope_cmat * (1 - 1 / 2)
    if delta1 is None:
        delta1 = slope_cmat * (1 + 1 / 2)
    if eps is None:
        eps = 20
    if min_samples is None:
        min_samples = 3
    if seg_size is None:
        seg_size = 600

    if metric is None:
        metric = c_euclidean

    tset = [*zip(range(n_col), cmat.argmax(axis=0), cmat.max(axis=0))]
    tset = np.array(tset)

    gen_cset.tset = tset

    chunksize = gen_chunksize(len(tset), seg_size)

    tset_s = np.array_split(tset, chunksize)

    logger.info("len(tset): %s, seg to: %s", len(tset), [*map(len, tset_s)])

    cset = []
    for elm in tset_s:
        try:
            _ = (
                cluster.DBSCAN(eps=eps, min_samples=min_samples, metric=metric)
                .fit(elm)
                .labels_
            )
            cset.append(elm[_ > -1])
        except Exception as exc:
            logger.error(exc)
            raise SystemExit(1) from exc
    _ = np.concatenate(cset, axis=0)

    return np.array(_)

    # plot_pset(tset[cluster.DBSCAN(eps=20, min_samples=3, metric=c_euclidean).fit(tset).labels_ > -1])  # 1833 - 1322

    # labels_2 = cluster.DBSCAN(eps=20, min_samples=2, metric=c_euclidean).fit(tset).labels_  # 0.4342
    # labels_3 = cluster.DBSCAN(eps=20, min_samples=3, metric=c_euclidean).fit(tset).labels_  # 0.2787779
    # labels_4 = cluster.DBSCAN(eps=20, min_samples=4, metric=c_euclidean).fit(tset).labels_  # 20s sum(labels_4 > -1)/1833 = 0.21
    # labels_16_3 = cluster.DBSCAN(eps=16, min_samples=3, metric=c_euclidean).fit(tset).labels_  # 0.198
    # plot_pset(tset[labels_16_3 > -1])
