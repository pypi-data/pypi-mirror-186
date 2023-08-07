# Gary Koplik
# gary<dot>koplik<at>geomdata<dot>com
# December, 2021
# utils_p2cp.py


"""
Utility functions for building Polar Parallel Coordinate Plots.
"""


import numpy as np
import pandas as pd
from typing import Hashable, List


def indices_for_unique_values(df: pd.DataFrame, column: Hashable):
    """
    Find the indices corresponding to each unique value in a column of a ``pandas`` dataframe.

    :param df: dataframe from which to find index values.
    :param column: column of the dataframe to use to find indices corresponding to each of the column's unique values.
    :return: ``dict`` whose keys are the unique values in the column of data and whose values are 1d arrays of index
        values.
    """
    return df.groupby(column).groups


def split_df_on_variable(df: pd.DataFrame, column: Hashable,
                         cutoffs: List or int, labels: List or None = None):
    """
    Generate value for each record in a dataframe according to a splitting criterion.

    Using either specified cutoff values or a specified number of quantiles for ``cutoffs``, return an ``(n, 1)``
    ``np.ndarray`` where the ith value corresponds to the partition assignment of the ith record of ``df``.

    If ``column`` corresponds to numerical data, and a ``list`` of ``cutoffs`` is provided, then dataframe records will
    be assigned according to the following binning scheme:

    (-inf, ``cutoff[0]``], (``cutoff[0]``, ``cutoff[1]``], ... , (``cutoff[-1]``, inf]

    If ``column`` corresponds to numerical data, and ``cutoffs`` is provided as an ``int``, then dataframe records will
    be assigned into ``cutoffs`` equal-sized quantiles.

    :param df: dataframe whose records will be assigned to a partition.
    :param column: column of the dataframe to use to assign partition of records.
    :param cutoffs: cutoffs to use in partitioning records according to the data under ``column``. When provided as a
        ``list``, the specified cutoffs will partition according to
        (-inf, ``cutoffs[0]``], `(`cutoffs[0]``, ``cutoffs[1]``], ... , (``cutoffs[-1]``, inf).
        When provided as an ``int``, the exact numerical break points will be determined to create ``cutoffs``
        equally-sized quantiles.
    :param labels: labels assigned to each bin. Default ``None`` labels each bin as a string based on its range of
        values. Note, when ``cutoffs`` is a list, ``len(labels)`` must be 1 greater than ``len(cutoffs)``. When
        ``cutoffs`` is an ``int``, ``len(labels)`` must be equal to ``cutoffs``.
    :return: ``(n, 1)`` ``np.ndarray`` whose values are partition assignments corresponding to records in ``df``.
    """
    # int cutoffs dictates quantile cut, otherwise cut
    if type(cutoffs) != int:
        if labels is not None:
            assert len(labels) == len(cutoffs) + 1, \
                "Must have 1 more label than `cutoffs` (n cutoffs => n + 1 bins)"

        bins = [-np.inf, *cutoffs, np.inf]
        # create pandas categorical array with binning information
        bin_cuts = pd.cut(df[column].values, bins=bins, labels=labels)
    else:
        if labels is not None:
            assert len(labels) == cutoffs, \
                "Must have 1 label per `cutoffs` (n quantiles => n labels)"

        bin_cuts = pd.qcut(df[column].values, q=cutoffs, labels=labels)

    # convert to np array with shape `df.shape[0]` whose values are bin assignments (labels)
    bin_assignments = bin_cuts.to_numpy()

    return bin_assignments
