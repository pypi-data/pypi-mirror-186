"""Manipulate the legend of a matplotlib figure."""

from typing import Any

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def topside_legends(
    ax: plt.Axes,
    *args,
    c_max: int = 4,
    alpha: float = 0.8,
    side: str = "top",
    **kwargs: Any,
) -> plt.Axes:
    """Move the legend to the top of the plot.

    Parameters
    ----------
    ax: plt.Axes
        The axes object of the figure
    c_max: int
        Total number of columns allowed. If less than `c_max` labels are used, `c_max` is
        set to the number of labels. Defaults to 4.
    alpha: float
        Alpha value for the background of the legend. Defaults to 0.8.
    side: str
        Places the legend at the given side. Valid sides are 'top', 'bottom', 'right',
        'left', 'top right', 'top left', 'bottom right' and 'bottom left'. Defaults to
        'top'.

    Returns
    -------
    plt.Axes
        Axes object with updated (topside) legend.

    Other Parameters
    ----------------
    args: List
        Parameters given to ax.legend(), i.e. handles and labels. This is useful if you
        have many axes objects with one or more lines on them, but you want all lines in
        one legend at a given axes object.
    kwargs: Any
        All keyword arguments are sent to ax.legend().
        See https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend
        for details.
    """
    _sides = {
        "top": "upper center",
        "bottom": "lower center",
        "right": "center right",
        "left": "center left",
        "top right": "upper right",
        "top left": "upper left",
        "bottom right": "lower right",
        "bottom left": "lower left",
    }
    _anchors = {
        "top": (0.5, 1.05),
        "bottom": (0.5, -0.05),
        "right": (1.04, 0.5),
        "left": (-0.04, 0.5),
        "top right": (1.04, 1.05),
        "top left": (-0.04, 1.05),
        "bottom right": (1.04, -0.05),
        "bottom left": (-0.04, -0.05),
    }
    loc = _sides[side]
    anchor = _anchors[side]
    if len(args) != 0 and isinstance(args[0][0], str):
        raise ValueError(
            "The first args parameter must be a sequence of Artist, not str."
        )
    if len(args) < 2:
        try:
            # If the labels are defined directly in the legend as a list, calling ax.legend()
            # will re-set it to an empty legend. Therefore, we grab the list and re-set it
            # when we update the legend object.
            legend1: matplotlib.legend.Legend = ax.get_legend()
            lst = [l_.get_text() for l_ in legend1.get_texts()]
            l_d = len(legend1.get_texts())
        except AttributeError:
            # If, however, the labels are set when creating the lines objects (e.g. ax.plot(x,
            # y, label="Label for (x, y) data")), we first make sure the legend object is
            # created by calling ax.legend(), then we check how many labels exist in it.
            # Calling ax.legend() will in this case preserve all labels.
            ax.legend()
            legend2: matplotlib.legend.Legend = ax.get_legend()
            lst = []  # The empty list returns False.
            l_d = len(legend2.get_texts())
    else:
        lst = args[1]
        l_d = len(args[1])
    n_row = int(np.ceil(l_d / c_max))
    n_col = 1
    while l_d > n_col * n_row:
        n_col += 1
    if len(args) != 0:
        leg = ax.legend(
            args[0],
            lst,
            loc=loc,
            bbox_to_anchor=anchor,
            bbox_transform=ax.transAxes,
            ncol=n_col,
            **kwargs,
        )
    elif lst:
        leg = ax.legend(
            lst,
            loc=loc,
            bbox_to_anchor=anchor,
            bbox_transform=ax.transAxes,
            ncol=n_col,
            **kwargs,
        )
    else:
        leg = ax.legend(
            loc=loc,
            bbox_to_anchor=anchor,
            bbox_transform=ax.transAxes,
            ncol=n_col,
            **kwargs,
        )
    leg.get_frame().set_alpha(None)
    leg.get_frame().set_facecolor((1, 1, 1, alpha))
    leg.get_frame().set_edgecolor((0.5, 0.5, 0.5))
    return ax
