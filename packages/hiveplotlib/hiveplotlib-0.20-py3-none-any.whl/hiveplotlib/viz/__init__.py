# Gary Koplik
# gary<dot>koplik<at>geomdata<dot>com
# August, 2020
# viz.py

"""
Viz functions to be called on ``hiveplotlib.HivePlot`` or ``hiveplotlib.P2CP`` instances.

Default visualization functions exposed in ``hiveplotlib.viz`` use ``matplotlib``, but additional viz backends are
supported in additional submodules of ``hiveplotlib.viz``.
"""

from hiveplotlib.viz.matplotlib import axes_viz, edge_viz, hive_plot_viz, label_axes, node_viz, p2cp_legend, p2cp_viz
import warnings


def deprecated(func):  # pragma: no cover # noqa
    def with_deprecation_warning(*args, **kwargs):
        """Show a ``DeprecationWarning`` for functions to be removed in release ``0.21``."""
        # Extend some capabilities of func
        deprecated.__name__ = func.__name__

        warnings.warn(f"`{deprecated.__name__}()` has been renamed `{deprecated.__name__.replace('_mpl', '')}()`. "
                      "This DeprecationWarning will raise an error starting in hiveplotlib v0.21",
                      category=DeprecationWarning, stacklevel=2)
        return func(*args, **kwargs)

    return with_deprecation_warning


@deprecated
def axes_viz_mpl(*args, **kwargs):  # pragma: no cover # noqa
    return axes_viz(*args, **kwargs)


@deprecated
def edge_viz_mpl(*args, **kwargs):  # pragma: no cover # noqa
    return edge_viz(*args, **kwargs)


@deprecated
def hive_plot_viz_mpl(*args, **kwargs):  # pragma: no cover # noqa
    return hive_plot_viz(*args, **kwargs)


@deprecated
def label_axes_mpl(*args, **kwargs):  # pragma: no cover # noqa
    return label_axes(*args, **kwargs)


@deprecated
def node_viz_mpl(*args, **kwargs):  # pragma: no cover # noqa
    return node_viz(*args, **kwargs)


@deprecated
def p2cp_legend_mpl(*args, **kwargs):  # pragma: no cover # noqa
    return p2cp_legend(*args, **kwargs)


@deprecated
def p2cp_viz_mpl(*args, **kwargs):  # pragma: no cover # noqa
    return p2cp_viz(*args, **kwargs)
