"""Plot pset/tset."""
# pylint: disable=too-many-arguments
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

if "get_ipython" in globals():
    plt.ion()


def plot_pset(pset, scale=25, marker=None, cmap=None, alpha=1, new_figure=True):
    """Plot pset/tset.

    Args:
        pset: /test, nx3 np.array
        scale:  default 25, s=scale * pset.T[2]
        cmap: default LinearSegmentedColormap.from_list('rg', ["red","darkgreen","green", "black"], N=10)
        marker: default None, marker shape
        alpha: default 1,
        new_figure: default True, if True plt.figure()
    """
    # fig, ax = plt.subplots()
    # ax.scatter...
    if cmap is None:
        cmap = LinearSegmentedColormap.from_list(
            "rg", ["red", "darkgreen", "green"], N=10
        )

    pset = np.array(pset)
    if new_figure:
        plt.figure()

    plt.scatter(
        pset.T[0],
        pset.T[1],
        s=scale * pset.T[2],
        marker=marker,
        vmin=0,
        # cmap='viridis',
        cmap=cmap,
        # cmap='gray',
        # c=df.z,
        c=pset.T[2],
        alpha=alpha,
    )

    if new_figure:
        plt.grid()
        plt.colorbar()

    plt.show()  # will block when not in ipython
