# bokeh.py

"""
``bokeh``-backend visualizations in ``hiveplotlib``.
"""

try:
    from bokeh.models import ColumnDataSource, Label, Range1d
    from bokeh.plotting import figure
except ImportError:  # pragma: no cover
    raise ImportError("bokeh not installed, but can be installed by running `pip install hiveplotlib[bokeh]`")

import numpy as np
from hiveplotlib import HivePlot, P2CP
from hiveplotlib.utils import polar2cartesian
from hiveplotlib.viz.input_checks import input_check
import warnings
from typing import Hashable, List, Optional, Union


def axes_viz(instance: Union[HivePlot, P2CP],
             fig: Optional[figure] = None,
             buffer: float = 0.2, show_axes_labels: bool = True, axes_labels_buffer: float = 1.1,
             axes_labels_fontsize: str = "13px", width: int = 600, height: int = 600, center_plot: bool = True,
             axes_off: bool = True, fig_kwargs: Optional[dict] = None, label_kwargs: Optional[dict] = None,
             **line_kwargs) -> figure:
    """
    ``bokeh`` visualization of axes in a ``HivePlot`` or ``P2CP`` instance.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw axes.
    :param fig: default ``None`` builds new figure. If a figure is specified, axes will be drawn on that figure.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param show_axes_labels: whether to label the hive plot axes in the figure (uses ``Axis.long_name`` for each
        ``Axis``.)
    :param axes_labels_buffer: fraction which to radially buffer axes labels (e.g. setting ``axes_label_buffer`` to 1.1
        will be 10% further past the end of the axis moving from the origin of the plot).
    :param axes_labels_fontsize: font size for axes labels.
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``bokeh`` figure (default ``True``
        hides the x and y axes).
    :param fig_kwargs: additional values to be called in
        `bokeh.plotting.figure() <https://docs.bokeh.org/en/2.4.1/docs/reference/plotting/figure.html>`__ call. Note if
        ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and ``height``
        parameters.
    :param label_kwargs: additional kwargs passed to
        `bokeh.models.Label() <https://docs.bokeh.org/en/test/docs/reference/models/annotations.html#bokeh.models.Label>`__
        call.
    :param line_kwargs: additional params that will be applied to all hive plot axes. Note, these are kwargs that
        affect a `bokeh.models.Line() <https://docs.bokeh.org/en/test/docs/reference/models/glyphs/line.html>`__ call.
    :return: ``bokeh`` figure.
    """
    hive_plot, name = input_check(instance)

    # custom warnings based on which input given
    if len(hive_plot.axes.values()) == 0:
        if name == "Hive Plot":
            warnings.warn(
                "No axes have been added yet. "
                "Axes can be added by running `HivePlot.add_axes()`",
                stacklevel=2)
        elif name == "P2CP":
            warnings.warn(
                "No axes have been set yet. "
                "Nodes can be placed on axes by running `P2CP.set_axes()`",
                stacklevel=2)
        return None

    if fig_kwargs is None:
        fig_kwargs = dict()
    if label_kwargs is None:
        label_kwargs = dict()

    # allow for plotting onto specified figure
    if fig is None:
        fig_kwargs.setdefault("height", height)
        fig_kwargs.setdefault("width", width)
        fig = figure(**fig_kwargs)

    # some default kwargs for the axes
    line_kwargs.setdefault("color", "black")
    line_kwargs.setdefault("line_alpha", 0.5)
    line_kwargs.setdefault("line_width", 1.5)

    for axis in hive_plot.axes.values():
        to_plot = np.row_stack((axis.start, axis.end))
        fig.line(to_plot[:, 0], to_plot[:, 1], **line_kwargs)

    if center_plot:
        # center plot at (0, 0)
        max_radius = max([axis.polar_end for axis in hive_plot.axes.values()])
        # throw in a minor buffer
        buffer_radius = buffer * max_radius
        max_radius += buffer_radius

        fig.x_range = Range1d(-max_radius, max_radius)
        fig.y_range = Range1d(-max_radius, max_radius)

    if show_axes_labels:
        label_axes(instance=hive_plot, fig=fig, center_plot=False,
                   axes_labels_buffer=axes_labels_buffer, axes_labels_fontsize=axes_labels_fontsize,
                   axes_off=axes_off, **label_kwargs)
    if axes_off:
        fig.axis.visible = False
        fig.grid.visible = False
        fig.outline_line_color = None
    else:
        fig.axis.visible = True
        fig.grid.visible = True
        fig.outline_line_color = "#e5e5e5"

    return fig


def label_axes(instance: Union[HivePlot, P2CP],
               fig: Optional[figure] = None,
               axes_labels_buffer: float = 1.1, axes_labels_fontsize: str = "13px", buffer: float = 0.2,
               width: int = 600, height: int = 600, center_plot: bool = True,
               axes_off: bool = True, fig_kwargs: Optional[dict] = None, **label_kwargs) -> figure:
    """
    ``bokeh`` visualization of axis labels in a ``HivePlot`` or ``P2CP`` instance.

    For ``HivePlot`` instances, each axis' ``long_name`` attribute will be used. For ``P2CP`` instances, column names in
    the ``data`` attribute will be used.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw nodes.
    :param fig: default ``None`` builds new figure. If a figure is specified, axis labels will be drawn on that figure.
    :param axes_labels_buffer: fraction which to radially buffer axes labels (e.g. setting ``axes_label_buffer`` to 1.1
        will be 10% further past the end of the axis moving from the origin of the plot).
    :param axes_labels_fontsize: font size for axes labels.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``bokeh`` figure (default ``True``
        hides the x and y axes).
    :param fig_kwargs: additional values to be called in
        `bokeh.plotting.figure() <https://docs.bokeh.org/en/2.4.1/docs/reference/plotting/figure.html>`__ call. Note if
        ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and ``height``
        parameters.
    :param label_kwargs: additional kwargs passed to
        `bokeh.models.Label() <https://docs.bokeh.org/en/test/docs/reference/models/annotations.html#bokeh.models.Label>`__
        call.
    :return: ``bokeh`` figure.
    """
    hive_plot, name = input_check(instance)

    # custom warnings based on which input given
    if len(hive_plot.axes.values()) == 0:
        if name == "Hive Plot":
            warnings.warn(
                "No axes have been added yet. "
                "Axes can be added by running `HivePlot.add_axes()`",
                stacklevel=2)
        elif name == "P2CP":
            warnings.warn(
                "No axes have been set yet. "
                "Nodes can be placed on axes by running `P2CP.set_axes()`",
                stacklevel=2)
        return None

    if fig_kwargs is None:
        fig_kwargs = dict()

    # allow for plotting onto specified figure
    if fig is None:
        fig_kwargs.setdefault("height", height)
        fig_kwargs.setdefault("width", width)
        fig = figure(**fig_kwargs)

    for axis in hive_plot.axes.values():
        # choose horizontal and vertical alignment based on axis angle in [0, 360)
        # range in each direction from 0, 180 to specify horizontal alignment
        horizontal_angle_span = 60
        if axis.angle >= 360 - horizontal_angle_span or axis.angle <= 0 + horizontal_angle_span:
            horizontalalignment = "left"
        elif 180 + horizontal_angle_span >= axis.angle >= 180 - horizontal_angle_span:
            horizontalalignment = "right"
        else:
            horizontalalignment = "center"

        # range in each direction from 90, 270 to specify vertical alignment
        vertical_angle_span = 60
        if 90 + vertical_angle_span >= axis.angle >= 90 - vertical_angle_span:
            verticalalignment = "bottom"
        elif 270 - vertical_angle_span <= axis.angle <= 270 + vertical_angle_span:
            verticalalignment = "top"
        else:
            verticalalignment = "middle"

        x, y = polar2cartesian(axes_labels_buffer * axis.polar_end, axis.angle)
        label = Label(x=x, y=y, text=axis.long_name, text_font_size=axes_labels_fontsize,
                      text_align=horizontalalignment, text_baseline=verticalalignment, **label_kwargs)
        fig.add_layout(label)

    if center_plot:
        # center plot at (0, 0)
        max_radius = max([axis.polar_end for axis in hive_plot.axes.values()])
        # throw in a minor buffer
        buffer_radius = buffer * max_radius
        max_radius += buffer_radius

        fig.x_range = Range1d(-max_radius, max_radius)
        fig.y_range = Range1d(-max_radius, max_radius)

    if axes_off:
        fig.axis.visible = False
        fig.grid.visible = False
        fig.outline_line_color = None
    else:
        fig.axis.visible = True
        fig.grid.visible = True
        fig.outline_line_color = "#e5e5e5"

    return fig


def node_viz(instance: Union[HivePlot, P2CP],
             fig: Optional[figure] = None,
             width: int = 600, height: int = 600, center_plot: bool = True, buffer: float = 0.2,
             axes_off: bool = True, fig_kwargs: Optional[dict] = None,
             **scatter_kwargs) -> figure:
    """
    ``bokeh`` visualization of nodes in a ``HivePlot`` or ``P2CP`` instance that have been placed on its axes.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw nodes.
    :param fig: default ``None`` builds new figure. If a figure is specified, nodes will be drawn on that figure.
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``bokeh`` figure (default ``True``
        hides the x and y axes).
    :param fig_kwargs: additional values to be called in
        `bokeh.plotting.figure() <https://docs.bokeh.org/en/2.4.1/docs/reference/plotting/figure.html>`__ call. Note if
        ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and ``height``
        parameters.
    :param scatter_kwargs: additional params that will be applied to all hive plot nodes. Note, these are kwargs that
        affect a `fig.scatter() <https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.scatter>`__
        call.
    :return: ``bokeh`` figure.
    """
    hive_plot, name = input_check(instance)

    if fig_kwargs is None:
        fig_kwargs = dict()

    # allow for plotting onto specified figure
    if fig is None:
        fig_kwargs.setdefault("height", height)
        fig_kwargs.setdefault("width", width)
        fig = figure(**fig_kwargs)

    # some default kwargs for the axes
    scatter_kwargs.setdefault("color", "black")
    scatter_kwargs.setdefault("alpha", 0.8)
    scatter_kwargs.setdefault("size", 5)

    # p2cp warning only happens when axes don't exist
    if len(hive_plot.axes.values()) == 0:
        if name == "P2CP":
            warnings.warn(
                "No axes have been set yet, thus no nodes have been placed on axes. "
                "Nodes can be placed on axes by running `P2CP.set_axes()`",
                stacklevel=2)
    else:
        for axis in hive_plot.axes.values():
            to_plot = axis.node_placements.values[:, :2]
            if to_plot.shape[0] > 0:
                fig.scatter(to_plot[:, 0], to_plot[:, 1], **scatter_kwargs)
            else:
                if name == "Hive Plot":
                    warnings.warn(
                        "At least one of your axes has no nodes placed on it yet. "
                        "Nodes can be placed on axes by running `HivePlot.place_nodes_on_axis()`",
                        stacklevel=2)

        if center_plot:
            # center plot at (0, 0)
            max_radius = max([axis.polar_end for axis in hive_plot.axes.values()])
            # throw in a minor buffer
            buffer_radius = buffer * max_radius
            max_radius += buffer_radius

            fig.x_range = Range1d(-max_radius, max_radius)
            fig.y_range = Range1d(-max_radius, max_radius)

    if axes_off:
        fig.axis.visible = False
        fig.grid.visible = False
        fig.outline_line_color = None
    else:
        fig.axis.visible = True
        fig.grid.visible = True
        fig.outline_line_color = "#e5e5e5"

    return fig


def edge_viz(instance: Union[HivePlot, P2CP],
             fig: Optional[figure] = None,
             tags: Optional[Union[Hashable, List[Hashable]]] = None,
             width: int = 600, height: int = 600, center_plot: bool = True, buffer: float = 0.2,
             axes_off: bool = True, fig_kwargs: Optional[dict] = None, **edge_kwargs) -> figure:
    """
    ``bokeh`` visualization of constructed edges in a ``HivePlot`` or ``P2CP`` instance.

    :param instance: ``HivePlot`` or ``P2CP`` instance for which we want to draw edges.
    :param fig: default ``None`` builds new figure. If a figure is specified, edges will be drawn on that figure.
    :param tags: which tag(s) of data to plot. Default ``None`` plots all tags of data. Can supply either a single tag
        or list of tags.
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``bokeh`` figure (default ``True``
        hides the x and y axes).
    :param fig_kwargs: additional values to be called in
        `bokeh.plotting.figure() <https://docs.bokeh.org/en/2.4.1/docs/reference/plotting/figure.html>`__ call. Note if
        ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and ``height``
        parameters.
    :param edge_kwargs: additional params that will be applied to all edges on all axes (but kwargs specified beforehand
        in ``HivePlot.connect_axes()`` / ``P2CP.build_edges`` or ``HivePlot.add_edge_kwargs()`` /
        ``P2CP.add_edge_kwargs()`` will take priority).
        To overwrite previously set kwargs, see ``HivePlot.add_edge_kwargs()`` / ``P2CP.add_edge_kwargs()`` for more.
        Note, these are kwargs that affect a
        `bokeh.models.MultiLine() <https://docs.bokeh.org/en/test/docs/reference/models/glyphs/multi_line.html>`__ call.
    :return: ``bokeh`` figure.
    """
    hive_plot, name = input_check(instance)

    # custom warnings based on which input given
    if len(list(hive_plot.edges.keys())) == 0:
        if name == "Hive Plot":
            warnings.warn(
                "Your `HivePlot` instance does not have any specified edges yet. "
                "Edges can be created for plotting by running `HivePlot.connect_axes()`",
                stacklevel=2)
        elif name == "P2CP":
            warnings.warn(
                "Your `P2CP` instance does not have any specified edges yet. "
                "Edges can be created for plotting by running `P2CP.build_edges()`",
                stacklevel=2)
        return None

    if fig_kwargs is None:
        fig_kwargs = dict()

    # allow for plotting onto specified figure
    if fig is None:
        fig_kwargs.setdefault("height", height)
        fig_kwargs.setdefault("width", width)
        fig = figure(**fig_kwargs)

    # p2cp warnings only need to happen once per tag
    #  because all axes behave in unison
    already_warned_p2cp_tags = []

    for a0 in hive_plot.edges.keys():
        for a1 in hive_plot.edges[a0].keys():
            # use all tags if no specific tags requested
            if tags is None:
                tags_to_plot = hive_plot.edges[a0][a1].keys()
            # otherwise, make sure we have a flat list of tags
            else:
                tags_to_plot = list(np.array(tags).flatten())

            for tag in tags_to_plot:
                temp_edge_kwargs = edge_kwargs.copy()

                # only run plotting of edges that exist
                if "curves" in hive_plot.edges[a0][a1][tag]:

                    # create edge_kwargs key if needed
                    if "edge_kwargs" not in hive_plot.edges[a0][a1][tag]:
                        hive_plot.edges[a0][a1][tag]["edge_kwargs"] = dict()

                    # don't use kwargs specified in this function call if already specified
                    for k in list(temp_edge_kwargs.keys()):
                        if k in hive_plot.edges[a0][a1][tag]["edge_kwargs"]:
                            if name == "Hive Plot":
                                warnings.warn(f"Specified kwarg {k} but already set as kwarg for edge tag {tag} "
                                              f"going from edges {a0} to {a1}. Preserving kwargs already set.\n"
                                              "(These kwargs can be changed using the `add_edge_kwargs()` method "
                                              "for your `HivePlot` instance)", stacklevel=2)
                            elif name == "P2CP":
                                # only warn once per tag over all axes
                                if tag not in already_warned_p2cp_tags:
                                    warnings.warn(f"Specified kwarg {k} but already set as kwarg for edge tag {tag}. "
                                                  f"Preserving kwargs already set.\n"
                                                  "(These kwargs can be changed using the `add_edge_kwargs()` method "
                                                  "for your `P2CP` instance)", stacklevel=2)
                                    already_warned_p2cp_tags.append(tag)
                            del temp_edge_kwargs[k]

                    # some default kwargs for the axes if not specified anywhere
                    if 'color' not in hive_plot.edges[a0][a1][tag]["edge_kwargs"] and 'color' not in temp_edge_kwargs:
                        temp_edge_kwargs['color'] = 'black'
                    if 'alpha' not in hive_plot.edges[a0][a1][tag]["edge_kwargs"] and 'alpha' not in temp_edge_kwargs:
                        temp_edge_kwargs['alpha'] = 0.5
                    if 'line_width' not in hive_plot.edges[a0][a1][tag]["edge_kwargs"] and \
                            'line_width' not in temp_edge_kwargs:
                        temp_edge_kwargs['line_width'] = 1.5

                    # grab the requested array of discretized curves
                    edge_arr = hive_plot.edges[a0][a1][tag]["curves"]
                    # if there's no actual edges there, don't plot
                    if edge_arr.size > 0:
                        split_arrays = np.split(edge_arr, np.where(np.isnan(edge_arr[:, 0]))[0])
                        xs = [arr[:, 0] for arr in split_arrays]
                        ys = [arr[:, 1] for arr in split_arrays]
                        source = ColumnDataSource(dict(xs=xs, ys=ys))
                        # add legend labels but then remove them to not plot unless legend formally called later
                        fig.multi_line(xs="xs", ys="ys", source=source, legend_label=str(tag),
                                       **hive_plot.edges[a0][a1][tag]["edge_kwargs"],
                                       **temp_edge_kwargs)
    # kill all legend labeling for initial rendering (if there is anything that plotted with labels)
    if fig.legend != []:
        for i in fig.legend.items:
            i.visible = False

    if center_plot:
        # center plot at (0, 0)
        max_radius = max([axis.polar_end for axis in hive_plot.axes.values()])
        # throw in a minor buffer
        buffer_radius = buffer * max_radius
        max_radius += buffer_radius

        fig.x_range = Range1d(-max_radius, max_radius)
        fig.y_range = Range1d(-max_radius, max_radius)

    if axes_off:
        fig.axis.visible = False
        fig.grid.visible = False
        fig.outline_line_color = None
    else:
        fig.axis.visible = True
        fig.grid.visible = True
        fig.outline_line_color = "#e5e5e5"

    return fig


def hive_plot_viz(hive_plot: HivePlot,
                  fig: Optional[figure] = None,
                  tags: Optional[Union[Hashable, List[Hashable]]] = None,
                  width: int = 600, height: int = 600, center_plot: bool = True, buffer: float = 0.2,
                  show_axes_labels: bool = True, axes_labels_buffer: float = 1.1,
                  axes_labels_fontsize: str = "13px", axes_off: bool = True,
                  node_kwargs: dict or None = None, axes_kwargs: dict or None = None,
                  label_kwargs: Optional[dict] = None,
                  fig_kwargs: Optional[dict] = None, **edge_kwargs) -> figure:
    """
    Create default ``bokeh`` visualization of a ``HivePlot`` instance.

    :param hive_plot: ``HivePlot`` instance for which we want to draw edges.
    :param fig: default ``None`` builds new figure. If a figure is specified, hive plot will be drawn on that figure.
    :param tags: which tag(s) of data to plot. Default ``None`` plots all tags of data. Can supply either a single tag
        or list of tags.
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param show_axes_labels: whether to label the hive plot axes in the figure (uses ``Axis.long_name`` for each
        ``Axis``.)
    :param axes_labels_buffer: fraction which to radially buffer axes labels (e.g. setting ``axes_label_buffer`` to 1.1
        will be 10% further past the end of the axis moving from the origin of the plot).
    :param axes_labels_fontsize: font size for hive plot axes labels.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``bokeh`` figure (default ``True``
        hides the x and y axes).
    :param node_kwargs: additional params that will be applied to all hive plot nodes. Note, these are kwargs that
        affect a `fig.scatter() <https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.scatter>`_
        call.
    :param axes_kwargs: additional params that will be applied to all hive plot axes. Note, these are kwargs that
        affect a `bokeh.models.Line() <https://docs.bokeh.org/en/test/docs/reference/models/glyphs/line.html>`__ call.
    :param label_kwargs: additional kwargs passed to
        `bokeh.models.Label() <https://docs.bokeh.org/en/test/docs/reference/models/annotations.html#bokeh.models.Label>`__
        call.
    :param fig_kwargs: additional values to be called in
        `bokeh.plotting.figure() <https://docs.bokeh.org/en/2.4.1/docs/reference/plotting/figure.html>`__ call. Note if
        ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and ``height``
        parameters.
    :param edge_kwargs: additional params that will be applied to all edges on all axes (but kwargs specified beforehand
        in ``HivePlot.connect_axes()``  or ``HivePlot.add_edge_kwargs()`` will take priority).
        To overwrite previously set kwargs, see ``HivePlot.add_edge_kwargs()`` for more.
        Note, these are kwargs that affect a
        `bokeh.models.MultiLine() <https://docs.bokeh.org/en/test/docs/reference/models/glyphs/multi_line.html>`__ call.
    :return: ``bokeh`` figure.
    """
    if node_kwargs is None:
        node_kwargs = dict()

    if axes_kwargs is None:
        axes_kwargs = dict()

    fig = edge_viz(instance=hive_plot, fig=fig, width=width, height=height,
                   tags=tags, center_plot=False,
                   fig_kwargs=fig_kwargs, **edge_kwargs)

    axes_viz(instance=hive_plot, fig=fig, center_plot=False,
             show_axes_labels=show_axes_labels, axes_labels_buffer=axes_labels_buffer,
             axes_labels_fontsize=axes_labels_fontsize,
             label_kwargs=label_kwargs,
             **axes_kwargs)

    # do the centering / redim-ing if requested only before the last call, otherwise it will be overridden
    node_viz(instance=hive_plot, fig=fig, buffer=buffer, center_plot=center_plot, axes_off=axes_off, **node_kwargs)

    return fig


def p2cp_viz(p2cp: P2CP,
             fig: Optional[figure] = None,
             tags: Optional[Union[Hashable, List[Hashable]]] = None,
             width: int = 600, height: int = 600, center_plot: bool = True, buffer: float = 0.2,
             show_axes_labels: bool = True, axes_labels_buffer: float = 1.1,
             axes_labels_fontsize: str = "13px", axes_off: bool = True,
             node_kwargs: dict or None = None, axes_kwargs: dict or None = None,
             label_kwargs: Optional[dict] = None,
             fig_kwargs: Optional[dict] = None, **edge_kwargs) -> figure:
    """
    Create default ``bokeh`` visualization of a ``P2CP`` instance.

    :param p2cp: ``P2CP`` instance we want to visualize.
    :param fig: default ``None`` builds new figure. If a figure is specified, P2CP will be drawn on that figure.
    :param tags: which tag(s) of data to plot. Default ``None`` plots all tags of data. Can supply either a single tag
        or list of tags.
    :param width: width of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param height: height of figure in pixels. Note: only works if instantiating new figure (e.g. ``fig`` is ``None``).
    :param center_plot: whether to center the figure on ``(0, 0)``, the currently fixed center that the axes are drawn
        around by default.
    :param buffer: fraction of the axes past which to buffer x and y dimensions (e.g. setting ``buffer`` will
        find the maximum radius spanned by any ``Axis`` instance and set the x and y bounds as
        ``(-max_radius - buffer * max_radius, max_radius + buffer * max_radius)``).
    :param show_axes_labels: whether to label the hive plot axes in the figure (uses ``Axis.long_name`` for each
        ``Axis``.)
    :param axes_labels_buffer: fraction which to radially buffer axes labels (e.g. setting ``axes_label_buffer`` to 1.1
        will be 10% further past the end of the axis moving from the origin of the plot).
    :param axes_labels_fontsize: font size for P2CP axes labels.
    :param axes_off: whether to turn off Cartesian x, y axes in resulting ``bokeh`` figure (default ``True``
        hides the x and y axes).
    :param node_kwargs: additional params that will be applied to all hive plot nodes. Note, these are kwargs that
        affect a `fig.scatter() <https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html#bokeh.plotting.figure.scatter>`__
        call.
    :param axes_kwargs: additional params that will be applied to all hive plot axes. Note, these are kwargs that
        affect a `bokeh.models.Line() <https://docs.bokeh.org/en/test/docs/reference/models/glyphs/line.html>`__ call.
    :param label_kwargs: additional kwargs passed to
        `bokeh.models.Label() <https://docs.bokeh.org/en/test/docs/reference/models/annotations.html#bokeh.models.Label>`__
        call.
    :param fig_kwargs: additional values to be called in
        `bokeh.plotting.figure() <https://docs.bokeh.org/en/2.4.1/docs/reference/plotting/figure.html>`__ call. Note if
        ``width`` and ``height`` are added here, then they will be prioritized over the ``width`` and ``height``
        parameters.
    :param edge_kwargs: additional params that will be applied to all edges on all axes (but kwargs specified beforehand
        in ``P2CP.build_edges()`` or ``P2CP.add_edge_kwargs()`` will take priority).
        To overwrite previously set kwargs, see ``P2CP.add_edge_kwargs()`` for more.
        Note, these are kwargs that affect a
        `bokeh.models.MultiLine() <https://docs.bokeh.org/en/test/docs/reference/models/glyphs/multi_line.html>`__ call.
    :return: ``bokeh`` figure.
    """
    if node_kwargs is None:
        node_kwargs = dict()

    if axes_kwargs is None:
        axes_kwargs = dict()

    fig = edge_viz(instance=p2cp, fig=fig, width=width, height=height,
                   tags=tags, center_plot=False,
                   fig_kwargs=fig_kwargs, **edge_kwargs)

    axes_viz(instance=p2cp, fig=fig, center_plot=False,
             show_axes_labels=show_axes_labels, axes_labels_buffer=axes_labels_buffer,
             axes_labels_fontsize=axes_labels_fontsize,
             label_kwargs=label_kwargs,
             **axes_kwargs)

    # do the centering / redim-ing if requested only before the last call, otherwise it will be overridden
    node_viz(instance=p2cp, fig=fig, buffer=buffer, center_plot=center_plot, axes_off=axes_off, **node_kwargs)

    return fig


def p2cp_legend(p2cp: P2CP, fig: figure,
                tags: Optional[Union[List[Hashable] or Hashable]] = None,
                title: str = "Tags") -> figure:
    """
    Generate a legend for a ``P2CP`` instance, where entries in the legend will be tags of data added to the instance.

    .. note::
        The legend can be further modified by changing its attributes under ``fig.legend``. For more on the flexibility
        in changing the legend, see the
        `bokeh.models.Legend() <https://docs.bokeh.org/en/test/docs/reference/models/annotations.html#bokeh.models.Legend>`__
        docs.

    :param p2cp: ``P2CP`` instance we want to visualize.
    :param fig: ``bokeh`` figure on which we will draw the legend.
    :param tags: which tags of data to include in the legend. Default ``None`` uses all tags under
        ``p2cp.tags``. This can be ignored unless explicitly wanting to _exclude_ certain tags from the legend.
    :param title: title of the legend. Default "Tags".
    :return: ``bokeh`` figure.
    """
    # kill all legend labeling before rebuilding legend
    for i in fig.legend.items:
        i.visible = False

    # need to convert tags to strings, as we needed to coax to strings to make them legend values with bokeh
    if tags is None:
        tags = [str(i) for i in p2cp.tags[:]]
    else:
        tags = list(np.array(tags).flatten().astype(str))

    for i in fig.legend.items:
        if str(i.label["value"]) in tags:
            i.visible = True

    fig.legend.title = title

    return fig
