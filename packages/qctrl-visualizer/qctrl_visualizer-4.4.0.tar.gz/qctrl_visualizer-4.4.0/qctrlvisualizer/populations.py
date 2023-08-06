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
Function for plotting the populations.
"""
from __future__ import annotations

from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np
from qctrlcommons.preconditions import check_argument

from .style import (
    FIG_HEIGHT,
    FIG_WIDTH,
    qctrl_style,
)
from .utils import (
    figure_as_kwarg_only,
    get_units,
)


@qctrl_style()
@figure_as_kwarg_only
def plot_populations(
    sample_times: np.ndarray, populations: dict, *, figure: plt.Figure
):
    """
    Create a plot of the specified populations.

    Parameters
    ----------
    sample_times : np.ndarray
        The 1D array of times in seconds at which the populations have been sampled.
    populations : dict
        The dictionary of populations to plot, of the form
        ``{"label_1": population_values_1, "label_2": population_values_2, ...}``.
        Each `population_values_n` is a 1D array of population values with the same
        length as `sample_times` and `label_n` is its label.
        Population values must lie between 0 and 1.
    figure : matplotlib.figure.Figure, optional
        A matplotlib Figure in which to place the plots.
        If passed, its dimensions and axes will be overridden.
    """

    population_data = _create_population_data(sample_times, populations)

    figure.set_figwidth(FIG_WIDTH)
    figure.set_figheight(FIG_HEIGHT)

    axes = figure.subplots(nrows=1, ncols=1)

    scale, prefix = get_units(sample_times)
    for data in population_data:
        axes.plot(sample_times / scale, data.values, label=data.label)

    axes.set_xlabel(f"Time ({prefix}s)")
    axes.set_ylabel("Probability")

    axes.legend()


_PopulationData = namedtuple("_PopulationData", ["values", "label"])


def _create_population_data(
    sample_times: np.ndarray, populations: dict
) -> list[_PopulationData]:
    """
    Validate inputs and create a list of _PopulationData objects.

    Parameters
    ----------
    sample_count : np.ndarray
        The times at which the populations have been sampled.
    populations : dict
        The populations to plot.

    Returns
    -------
    list[_PopulationData]
        A list of _PopulationData.
    """

    def safe_less_than(arr, bound):
        """
        Returns False if any of the elements of arr are less than bound (within rounding error).
        Returns True otherwise.
        """
        return np.any((1 - np.isclose(arr, bound)) * (arr < bound))

    def safe_greater_than(arr, bound):
        """
        Returns False if any of the elements of arr are greater than bound (within rounding error).
        Returns True otherwise.
        """
        return np.any((1 - np.isclose(arr, bound)) * (arr > bound))

    check_argument(
        isinstance(sample_times, np.ndarray) and len(sample_times.shape) == 1,
        "The sample times must be a 1D array.",
        {"sample_times": sample_times},
    )
    check_argument(
        isinstance(populations, dict),
        "The populations must be a dictionary.",
        {"populations": populations},
    )

    sample_count = len(sample_times)

    plot_data = []
    for label, pop in populations.items():
        check_argument(
            isinstance(pop, (list, np.ndarray)),
            "Each element in the dictionary of populations must be an array or a list.",
            {"populations": populations},
            extras={f"populations[{label}]": pop},
        )
        check_argument(
            not safe_less_than(np.asarray(pop), 0)
            and (not safe_greater_than(np.asarray(pop), 1)),
            "Population values must lie between 0 and 1.",
            {"populations": populations},
            extras={f"populations[{label}]": pop},
        )
        check_argument(
            len(pop) == sample_count,
            "The number of population values must match the number of sample times.",
            {"sample_times": sample_times, "populations": populations},
            extras={
                f"len(populations[{label}])": len(pop),
                "len(sample_times)": sample_count,
            },
        )
        plot_data.append(_PopulationData(np.asarray(pop), label))

    return plot_data
