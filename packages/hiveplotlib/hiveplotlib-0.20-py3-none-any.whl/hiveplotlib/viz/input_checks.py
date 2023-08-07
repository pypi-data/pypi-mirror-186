# input_checks.py

"""
Functions to check inputs for input-agnostic viz functions in the ``hiveplotlib.viz`` module.
"""

from hiveplotlib import HivePlot, P2CP
from typing import Union, Tuple


def input_check(instance: Union[HivePlot, P2CP]) -> Tuple[HivePlot, str]:
    """
    Check whether a provided instance is supported by the instance-agnostic plotting tools.

    Current supported data structures are :py:class:`~hiveplotlib.HivePlot()` and
    :py:class:`~hiveplotlib.P2CP()` instances.

    :param instance: instance to plot.
    :return: the underlying ``HivePlot`` instance (all the plotting is based on a ``HivePlot`` object, even the ``P2CP``
        instance), plus a string of the name of the instance (for more clear warning for downstream viz calls).
    """
    if type(instance) == HivePlot:
        hive_plot = instance.copy()
        name = "Hive Plot"
    elif type(instance) == P2CP:
        hive_plot = instance._hiveplot.copy()
        name = "P2CP"
    else:
        raise NotImplementedError("Can only handle `HivePlot` and `P2CP` instances")
    return hive_plot, name
