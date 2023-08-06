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
Functions for plotting confidence ellipses.
"""
from __future__ import annotations

from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from qctrlcommons.preconditions import check_argument

from .style import (
    FIG_HEIGHT,
    QCTRL_STYLE_COLORS,
    qctrl_style,
)
from .utils import (
    create_axes,
    figure_as_kwarg_only,
    get_units,
)


@qctrl_style()
@figure_as_kwarg_only
def plot_confidence_ellipses(
    ellipse_matrix: np.ndarray,
    estimated_parameters: np.ndarray,
    actual_parameters: Optional[np.ndarray] = None,
    parameter_names: Optional[list[str]] = None,
    parameter_units: str | list[str] = "Hz",
    *,
    figure: plt.Figure,
):
    """
    Create an array of confidence ellipse plots.

    From an (N,N) matrix transformation and N estimated parameters,
    plots the confidence ellipse for each pair of parameters.

    Parameters
    ----------
    ellipse_matrix : np.ndarray
        The square matrix which transforms a unit hypersphere in an
        N-dimensional space into a hyperellipse representing the confidence
        region. Must be of shape (N, N), with N > 1.
    estimated_parameters : np.ndarray
        The values of the estimated parameters. Must be of shape (N,).
    actual_parameters : np.ndarray, optional
        The actual values of the estimated parameters.
        If you provide these, they're plotted alongside the ellipses and
        estimated parameters. Must be of shape (N,).
    parameter_names : list[str], optional
        The name of each parameter, to be used as axes labels.
        If provided, it must be of length N. If not provided,
        the axes are labelled "Parameter 0", "Parameter 1", ...
    parameter_units : str or list[str], optional
        The units of each parameter. You can provide a list of strings with
        the units of each parameter, or a single string if all parameters have
        the same units. Defaults to "Hz".
    figure : matplotlib.figure.Figure, optional
        A matplotlib Figure in which to place the plots.
        If passed, its dimensions and axes will be overridden.
    """

    ellipse_matrix = np.asarray(ellipse_matrix)
    estimated_parameters = np.asarray(estimated_parameters)
    if actual_parameters is not None:
        actual_parameters = np.asarray(actual_parameters)

    check_argument(
        len(estimated_parameters.shape) == 1 and len(estimated_parameters) > 1,
        "The estimated parameters must be a 1D array containing at least two parameters.",
        {"estimated_parameters": estimated_parameters},
        extras={"estimated_parameters.shape": estimated_parameters.shape},
    )

    parameter_count = len(estimated_parameters)

    check_argument(
        ellipse_matrix.shape == (parameter_count, parameter_count),
        "The ellipse_matrix must be a square 2D array, "
        "with the same length as the estimated parameters.",
        {"ellipse_matrix": ellipse_matrix},
        extras={
            "ellipse_matrix.shape": ellipse_matrix.shape,
            "len(estimated_parameters)": parameter_count,
        },
    )

    if actual_parameters is not None:
        check_argument(
            actual_parameters.shape == (parameter_count,),
            "If passed, the actual parameters must be a 1D array "
            "with the same shape as estimated parameters.",
            {"actual_parameters": actual_parameters},
            extras={
                "actual_parameters.shape": actual_parameters.shape,
                "estimated_parameters.shape": estimated_parameters.shape,
            },
        )

    if parameter_names is not None:
        check_argument(
            len(parameter_names) == parameter_count,
            "If passed, the parameter names must be a list "
            "with the same length as the estimated parameters.",
            {"parameter_names": parameter_names},
            extras={
                "len(parameter_names)": len(parameter_names),
                "len(estimated_parameters)": parameter_count,
            },
        )

    else:
        parameter_names = [f"Parameter {k}" for k in range(parameter_count)]

    if isinstance(parameter_units, str):
        parameter_units = [parameter_units] * parameter_count
    else:
        check_argument(
            len(parameter_units) == parameter_count,
            "The parameter units must be either a string or a list "
            "with the same length as the estimated parameters.",
            {"parameter_units": parameter_units},
            extras={
                "len(parameter_units)": len(parameter_units),
                "len(estimated_parameters)": parameter_count,
            },
        )

    # Set the N (N-1) / 2 plots in a 2D grid of axes.
    if parameter_count % 2 == 0:
        plot_count_x = parameter_count - 1
        plot_count_y = parameter_count // 2
    else:
        plot_count_x = parameter_count
        plot_count_y = (parameter_count - 1) // 2

    axes_array = create_axes(
        figure, plot_count_x, plot_count_y, FIG_HEIGHT, FIG_HEIGHT
    ).flatten()

    # Create pairs of indices with all possible parameter pairings.
    index_1_list, index_2_list = np.triu_indices(parameter_count, k=1)

    for axes, index_1, index_2 in zip(axes_array, index_1_list, index_2_list):

        # Obtain points representing the correct parameters and their estimates.
        estimated_dot = estimated_parameters[[index_1, index_2]]

        # Obtain coordinates for a circle.
        theta = np.linspace(0, 2 * np.pi, 101)
        circle_coordinates = np.array([np.cos(theta), np.sin(theta)])

        # Define matrix that transforms circle coordinates into ellipse coordinates.
        coordinate_change = ellipse_matrix[
            np.ix_([index_1, index_2], [index_1, index_2])
        ]
        ellipse = coordinate_change @ circle_coordinates + estimated_dot[:, None]
        scale_x, units_x = get_units(ellipse[0])
        scale_y, units_y = get_units(ellipse[1])
        scale = np.array([scale_x, scale_y])

        # Define labels of the axes.
        axes.set_xlabel(
            f"{parameter_names[index_1]} ({units_x}{parameter_units[index_1]})",
            labelpad=0,
        )
        axes.set_ylabel(
            f"{parameter_names[index_2]} ({units_y}{parameter_units[index_2]})",
            labelpad=0,
        )

        # Plot estimated parameters.
        estimated_dot = estimated_dot / scale
        axes.plot(
            *estimated_dot, "o", label="Estimated parameters", c=QCTRL_STYLE_COLORS[0]
        )

        # Plot confidence ellipse.
        ellipse = ellipse / scale[:, None]
        axes.plot(*ellipse, "--", label="Confidence region", c=QCTRL_STYLE_COLORS[0])

        # Plot actual parameters (if available).
        if actual_parameters is not None:
            actual_dot = actual_parameters[[index_1, index_2]] / scale
            axes.plot(
                *actual_dot, "o", label="Actual parameters", c=QCTRL_STYLE_COLORS[1]
            )

    # Create legends.
    handles, labels = axes_array[0].get_legend_handles_labels()
    figure.legend(
        handles=handles, labels=labels, loc="center", bbox_to_anchor=(0.5, 0.95), ncol=3
    )
