"""Manipulate the axis of matplotlib figures."""

from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker


def dark_theme(
    *ax: plt.Axes, fig: Optional[plt.Figure] = None, keep_yaxis: bool = False
):
    """Change plot style to fit a dark background.

    This is better in e.g. beamers with dark theme.

    Parameters
    ----------
    ax: plt.Axes
        Send in any number of matplotlib axes and the changes will be applied to all
    keep_yaxis: bool
        Keep the colour of the label along the vertical axis as is.
        Useful if a plot has y-labels that are coloured to match the plotted
        lines. Defaults to False.
    """
    for a in ax:
        if not keep_yaxis:
            a.tick_params(axis="both", colors="w")
            a.yaxis.label.set_color("w")
        else:
            a.tick_params(axis="x", colors="w")
        a.xaxis.label.set_color("w")
        plt.setp(a.spines.values(), color="gray")
    if fig is not None:
        fig.patch.set_alpha(0)


def log_tick_format(axes: plt.Axes, which: str, base: float = 10) -> plt.Axes:
    """Change the tick formatter.

    Change the logarithmic axes to use '1' and '10' (or the given base), i.e. without
    power, otherwise use the base to some power. For more robust and less error prone
    results, the plotting type is also re-set with the same base ('loglog', 'semilogx' and
    'semilogy').

    Modified from:
    https://stackoverflow.com/questions/21920233/matplotlib-log-scale-tick-label-number-formatting/33213196

    Parameters
    ----------
    axes: plt.Axes
        An axes object
    which: str
        Whether to update both x and y axis, or just one of them.
    base: float
        The base of the logarithm. Defaults to base 10 (same as loglog, etc.)

    Returns
    -------
    plt.Axes
        The updated axes object.

    Raises
    ------
    ValueError
        If `which` is not 'both', 'x' or 'y'.
    """
    if which == "both":
        axs, pltype = ["xaxis", "yaxis"], "loglog"
    elif which == "x":
        axs, pltype = ["xaxis"], "semilogx"
    elif which == "y":
        axs, pltype = ["yaxis"], "semilogy"
    else:
        raise ValueError(
            "No valid axis found. 'which' must be either of 'both', 'x' or 'y'."
        )
    getattr(axes, pltype)(base=base)
    for ax in axs:
        f = getattr(axes, ax)
        f.set_major_formatter(
            ticker.FuncFormatter(
                lambda x, _: "{:g}".format(x)
                if np.log(x) / np.log(base) in [0, 1]
                else r"$"
                + str(base)
                + "^{"
                + "{:g}".format(np.log(x) / np.log(base))
                + r"}$"
            )
        )
    return axes
