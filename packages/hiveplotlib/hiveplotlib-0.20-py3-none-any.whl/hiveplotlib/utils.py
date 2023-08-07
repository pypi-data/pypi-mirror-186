# Gary Koplik
# gary<dot>koplik<at>geomdata<dot>com
# August, 2020
# utils.py

"""
Utility functions for building hive plots.
"""

import numpy as np
import pandas as pd
from typing import Hashable, List


def cartesian2polar(x: np.ndarray or float, y: np.ndarray or float):
    """
    Convert cartesian coordinates e.g. (x, y) to polar coordinates.

    (Polar coordinates e.g. (rho, phi), where `rho` is distance from origin, and `phi` is counterclockwise angle off of
    x-axis in degrees.)

    :param x: Cartesian x coordinates.
    :param y: Cartesian y coordinates.
    :return: (rho, phi) polar coordinates.
    """
    rho = np.sqrt(x**2 + y**2)
    phi = np.degrees(np.arctan2(y, x))
    return rho, phi


def polar2cartesian(rho: np.ndarray or float, phi: np.ndarray or float):
    """
    Convert polar coordinates to cartesian coordinates e.g. (x, y).

    (Polar coordinates e.g. (rho, phi), where `rho` is distance from origin, and `phi` is counterclockwise angle off of
    x-axis in degrees.)

    :param rho: distance from origin.
    :param phi: counterclockwise angle off of x-axis in degrees (not radians).
    :return: (x, y) cartesian coordinates.
    """
    x = rho * np.cos(np.radians(phi))
    y = rho * np.sin(np.radians(phi))
    return x, y


def bezier(start: float, end: float, control: float, num_steps: int = 100):
    """
    Calculate 1-dimensional Bézier curve values between ``start`` and ``end`` with curve based on ``control``.

    Note, this function is hardcoded for exactly 1 control point.

    :param start: starting point.
    :param end: ending point.
    :param control: "pull" point.
    :param num_steps: number of points on Bézier curve.
    :return: ``(num_steps, )`` sized ``np.ndarray`` of 1-dimensional discretized Bézier curve output.
    """
    steps = np.linspace(0, 1, num_steps)
    return (1 - steps) ** 2 * start + 2 * (1 - steps) * steps * control + steps ** 2 * end


def bezier_all(start_arr: List, end_arr: List, control_arr: List, num_steps: int = 100):
    """
    Calculate Bézier curve between multiple start and end values.

    Note, this function is hardcoded for exactly 1 control point per curve.

    :param start_arr: starting point of each curve.
    :param end_arr: corresponding ending point of each curve.
    :param control_arr: corresponding "pull" points for each curve.
    :param num_steps: number of points on each Bézier curve.
    :return: ``(start_arr * num_steps, )`` sized ``np.ndarray`` of 1-dimensional discretized Bézier curve output.
        Note, every ``num_steps`` chunk of the output corresponds to a different Bézier curve.
    """
    assert np.array(start_arr).size == np.array(end_arr).size == np.array(control_arr).size, \
        "params `start_arr`, `end_arr`, and `control_arr` must be the same size"

    # each curve will be represented by the partitioning of the result by every `num_steps` index vals
    steps = np.tile(np.linspace(0, 1, num_steps), np.array(start_arr).size)

    # repeat each start, stop, and control value to multiply point-wise in one line
    start = np.repeat(start_arr, num_steps)
    end = np.repeat(end_arr, num_steps)
    control = np.repeat(control_arr, num_steps)

    return (1 - steps) ** 2 * start + 2 * (1 - steps) * steps * control + steps ** 2 * end


def split_nodes_on_variable(node_list: List, variable_name: Hashable,
                            cutoffs: List or int or None = None, labels: List or None = None):
    r"""
    Split a ``list`` of ``Node`` instances into a partition of node IDs.

    By default, splits will group node IDs on *unique values* of ``variable_name``.

    If ``variable_name`` corresponds to numerical data, and a ``list`` of ``cutoffs``
    is provided, node IDs will be separated into bins according to the following binning scheme:

    (-inf, ``cutoff[0]``], (``cutoff[0]``, ``cutoff[1]``], ... , (``cutoff[-1]``, inf]

    If ``variable_name`` corresponds to numerical data, and ``cutoffs`` is provided as an ``int``, node IDs will be
    separated into ``cutoffs`` equal-sized quantiles.

    :param node_list: list of ``Node`` instances to partition.
    :param variable_name: which variable in each ``Node`` instances to group by.
    :param cutoffs: cutoffs to use in binning nodes according to data under ``variable_name``. Default ``None`` will bin
        nodes by unique values of ``variable_name``. When provided as a ``list``, the specified cutoffs will bin
        according to (-inf, ``cutoffs[0]``], `(`cutoffs[0]``, ``cutoffs[1]``], ... , (``cutoffs[-1]``, inf).
        When provided as an ``int``, the exact numerical break points will be determined to create ``cutoffs``
        equally-sized quantiles.
    :param labels: labels assigned to each bin. Only referenced when ``cutoffs`` is not ``None``. Default ``None``
        labels each bin as a string based on its range of values. Note, when ``cutoffs`` is a list, ``len(labels)`` must
        be 1 greater than ``len(cutoffs)``. When ``cutoffs`` is an ``int``, ``len(labels)`` must be equal to
        ``cutoffs``.
    :return: ``dict`` whose values are lists of ``Node`` unique IDs. If ``cutoffs`` is ``None``, keys will be the unique
        values for the variable. Otherwise, each key will be the string representation of a bin range.
    """
    if cutoffs is None:
        output = dict()
        for node in node_list:
            val = node.data[variable_name]
            if val not in output.keys():
                output[val] = []

            output[val].append(node.unique_id)

        return output

    else:
        data_dict = {}
        for node in node_list:
            data_dict[node.unique_id] = node.data[variable_name]

        # int cutoffs dictates quantile cut, otherwise cut
        if type(cutoffs) != int:
            if labels is not None:
                assert len(labels) == len(cutoffs) + 1, \
                    "Must have 1 more label than `cutoffs` (n cutoffs => n + 1 bins)"

            bins = [-np.inf, *cutoffs, np.inf]
            # create pandas categorical array with binning information
            node_bin_cuts = pd.cut(list(data_dict.values()), bins=bins, labels=labels)
        else:
            if labels is not None:
                assert len(labels) == cutoffs, \
                    "Must have 1 label per `cutoffs` (n quantiles => n labels)"

            node_bin_cuts = pd.qcut(list(data_dict.values()), q=cutoffs, labels=labels)

        # convert to np array with shape `len(node_list)` whose values are bin assignments (labels)
        node_bin_assignments = node_bin_cuts.to_numpy().astype(str)

        output = dict()
        for i, node in enumerate(node_list):
            val = node_bin_assignments[i]
            if val not in output.keys():
                output[val] = []

            output[val].append(node.unique_id)

        return output
