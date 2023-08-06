# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

"""
Utility functions for plotting.
"""

from __future__ import annotations

from functools import wraps
from inspect import (
    Parameter,
    Signature,
    signature,
)
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter
from qctrlcommons.preconditions import check_argument


def get_units(values) -> tuple[float, str]:
    """
    Calculate the units to be used for plotting the given range of values.

    Specifically, returns a tuple (scaling factor, prefix), for example (1000, 'k') or (0.001, 'm').
    The values should be divided by the first element, and the unit label prepended with the second
    element. If the values are zero the scaling factor is 1.
    """
    prefixes = {
        -24: "y",
        -21: "z",
        -18: "a",
        -15: "f",
        -12: "p",
        -9: "n",
        -6: "\N{MICRO SIGN}",
        -3: "m",
        0: "",
        3: "k",
        6: "M",
        9: "G",
        12: "T",
        15: "P",
        18: "E",
        21: "Z",
        24: "Y",
    }
    # We apply a simple algorithm: get the element with largest magnitude, then map according to
    # [0.001, 1) -> 0.001x/milli,
    # [1, 1000) -> no scaling,
    # [1000, 1e6) -> 1000x/kilo,
    # and so on.
    max_value = max(np.abs(values))
    exponent = float(
        3
        * np.floor_divide(np.log10(max_value, out=np.zeros(1), where=max_value > 0), 3)
    )
    # Clip the scaling to the allowable range.
    exponent_clipped = np.clip(exponent, -24, 24)
    return 10**exponent_clipped, prefixes[exponent_clipped]


def create_axes(
    figure: plt.Figure,
    count_x: int,
    count_y: int,
    width: float,
    height: float,
    share_x: bool = False,
    share_y: bool = False,
) -> np.ndarray:
    """
    Create a set of axes with default axis labels and axis formatting.

    Parameters
    ----------
    figure : matplotlib.figure.Figure
        The matplotlib Figure in which the axes should be placed.
        Its dimensions will be overridden by this method.
    count_x : int
        The number of axes to create horizontally.
    count_y : int
        The number of axes to create vertically.
    width : float
        The width (in inches) for each axes.
    height : float
        The height (in inches) for each axes.
    share_x : bool, optional
        Whether the axes share the x-axis.
        Defaults to False.
    share_y : bool, optional
        Whether the axes share the y-axis.
        Defaults to False.

    Returns
    -------
    np.ndarray
        A 2D array of Axes objects.
    """
    figure.set_figheight(height * count_y)
    figure.set_figwidth(width * count_x)
    figure.subplots_adjust(hspace=0.2, wspace=0.25)

    axes_array = figure.subplots(
        nrows=count_y, ncols=count_x, sharex=share_x, sharey=share_y, squeeze=False
    )

    # Set axis formatting.
    for axes in axes_array.flat:
        axes.yaxis.set_major_formatter(ScalarFormatter())
        axes.xaxis.set_major_formatter(ScalarFormatter())

    return axes_array


def figure_as_kwarg_only(func):
    """
    Decorator to mark functions which take a figure as kwarg-only parameter.
    The decorator:
        - checks that the first positional argument passed
            to the decorated function is not a Figure.
        - if no kwarg figure is passed, create one
            and pass it to the decorated function.
        - if a kwarg figure is passed, remove all of its axes.
    """

    @wraps(func)
    def new_func(*args, **kwargs):
        if len(args) > 0:
            check_argument(  # Remove 2023/01/01
                not isinstance(args[0], plt.Figure),
                "The figure parameter is now optional. "
                "You can omit it or pass it as a keyword parameter.",
                {func.__code__.co_varnames[0]: args[0]},
            )

        figure = kwargs.get("figure")
        if figure is None:
            # If a figure is not passed, create one.
            kwargs["figure"] = plt.figure()
        else:
            # If a figure is passed, remove all of its axes.
            for axes in figure.get_axes():
                axes.remove()

        return func(*args, **kwargs)

    # Update decorated function signature and annotations making the figure parameter optional.
    sig_params = dict(signature(new_func).parameters)
    sig_params["figure"] = Parameter(
        "figure", Parameter.KEYWORD_ONLY, default=None, annotation=Optional[plt.Figure]
    )
    # Ignoring type due to https://github.com/python/mypy/issues/12472
    new_func.__signature__ = Signature(parameters=list(sig_params.values()))  # type: ignore
    new_func.__annotations__["figure"] = Optional[plt.Figure]

    return new_func
