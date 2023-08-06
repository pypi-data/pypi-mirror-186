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
Functions for plotting filter functions.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from qctrlcommons.preconditions import check_argument

from .style import (
    FIG_HEIGHT,
    FIG_WIDTH,
    qctrl_style,
)
from .utils import figure_as_kwarg_only


@qctrl_style()
@figure_as_kwarg_only
def plot_filter_functions(filter_functions: dict, *, figure: plt.Figure):
    """
    Create a plot of the specified filter functions.

    Parameters
    ----------
    filter_functions : dict
        The dictionary of filter functions to plot. The keys should be the names of the filter
        functions, and the values represent the filter functions by either a dictionary with the
        keys 'frequencies', 'inverse_powers', and optional 'uncertainties';
        or a list of samples as dictionaries with keys 'frequency', 'inverse_power',
        and optional 'inverse_power_uncertainty'.
        The frequencies must be in Hertz an the inverse powers and their uncertainties in seconds.
        If the uncertainty of an inverse power is provided, it must be non-negative.
    figure : matplotlib.figure.Figure, optional
        A matplotlib Figure in which to place the plot.
        If passed, its dimensions and axes will be overridden.

    Notes
    -----
    For dictionary input, the key 'inverse_power_uncertainties' can be used
    instead of 'uncertainties'. If both are provided then the value corresponding to
    'uncertainties' is used.
    For list of samples input, the key 'inverse_power_precision' can be used instead of
    'inverse_power_uncertainty'. If both are provided then the value corresponding to
    'inverse_power_uncertainty' is used.

    As an example, the following is valid ``filter_functions`` input ::

        filter_functions={
            "Primitive": {
                "frequencies": [0.0, 1.0, 2.0],
                "inverse_powers": [15., 12., 3.],
                "uncertainties": [0., 0., 0.2],
            },
            "CORPSE": [
                {"frequency": 0.0, "inverse_power": 10.},
                {"frequency": 0.5, "inverse_power": 8.5},
                {"frequency": 1.0, "inverse_power": 5., "inverse_power_uncertainty": 0.1},
                {"frequency": 1.5, "inverse_power": 2.5},
            ],
        }


    """

    check_argument(
        filter_functions,
        "At least one filter function must be provided.",
        {"filter_functions": filter_functions},
    )

    figure.set_figwidth(FIG_WIDTH)
    figure.set_figheight(FIG_HEIGHT)

    axes = figure.subplots(nrows=1, ncols=1)

    for name, filter_function in filter_functions.items():
        if isinstance(filter_function, list):
            frequencies, inverse_powers, inverse_power_uncertainties = np.array(
                list(
                    zip(
                        *[
                            (
                                sample["frequency"],
                                sample["inverse_power"],
                                sample["inverse_power_uncertainty"]
                                if "inverse_power_uncertainty" in sample
                                else sample.get("inverse_power_precision", 0.0),
                            )
                            for sample in filter_function
                        ]
                    )
                )
            )
        else:
            check_argument(
                isinstance(filter_function, dict),
                "Each filter function must either be a list or a dictionary.",
                {"filter_functions": filter_functions},
                extras={"filter_function": filter_function},
            )
            check_argument(
                ("frequencies" in filter_function)
                and ("inverse_powers" in filter_function),
                "Each filter function dictionary must contain `frequencies` and"
                " `inverse_powers` keys.",
                {"filter_functions": filter_functions},
                extras={"filter_function": filter_function},
            )
            frequencies = np.asarray(filter_function["frequencies"])
            inverse_powers = np.asarray(filter_function["inverse_powers"])
            inverse_power_uncertainties = filter_function.get(
                "uncertainties", filter_function.get("inverse_power_uncertainties")
            )
            if inverse_power_uncertainties is not None:
                inverse_power_uncertainties = np.asarray(inverse_power_uncertainties)
            else:
                inverse_power_uncertainties = np.zeros_like(frequencies)

        check_argument(
            np.all(inverse_power_uncertainties >= 0.0),
            "Uncertainties must all be non-negative in filter functions.",
            {"filter_functions": filter_functions},
            extras={"filter_function": filter_function},
        )

        inverse_powers_upper = inverse_powers + inverse_power_uncertainties
        inverse_powers_lower = inverse_powers - inverse_power_uncertainties

        lines = axes.plot(frequencies, inverse_powers, label=name)
        axes.fill_between(
            frequencies,
            inverse_powers_lower,
            inverse_powers_upper,
            alpha=0.35,
            hatch="||",
            facecolor="none",
            edgecolor=lines[0].get_color(),
            linewidth=0,
        )

    axes.legend()

    axes.set_xscale("log")
    axes.set_yscale("log")

    axes.autoscale(axis="x", tight=True)

    axes.set_xlabel("Frequency (Hz)")
    axes.set_ylabel("Inverse power (s)")
