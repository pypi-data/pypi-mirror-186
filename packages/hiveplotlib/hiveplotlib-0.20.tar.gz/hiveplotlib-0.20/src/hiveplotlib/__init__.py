# Gary Koplik
# gary<dot>koplik<at>geomdata<dot>com
# August, 2020
# __init__.py

"""
Generates the necessary structure for constructing hive plot visualizations.
"""

from copy import deepcopy
from hiveplotlib.utils import polar2cartesian, bezier_all
from hiveplotlib.utils_p2cp import indices_for_unique_values
import json
import numpy as np
import pandas as pd
from typing import Hashable, List
import warnings


class Node:
    """
    ``Node`` instances hold the data for individual network node.

    Each instance is initialized with a ``unique_id`` for identification. These IDs must be ``Hashable``.
    One can also initialize with a dictionary of ``data``, but data can also be added later with the ``add_data()``
    method.

    :example:

        .. highlight:: python
        .. code-block:: python

            my_node = Node(unique_id="my_unique_node_id", data=my_dataset)

            my_second_node = Node(unique_id="my_second_unique_node_id")
            my_second_node.add_data(data=my_second_dataset)
    """

    def __init__(self, unique_id: Hashable, data: dict or None = None):
        """
        Initialize ``Node`` instance.

        :param unique_id: identifier for the instance (intended to be unique).
        :param data: dictionary of data.
        """
        self.unique_id = unique_id
        self.data = dict()
        if data is None:
            data = dict()
        self.add_data(data, overwrite_old_data=True)
        # Hashable value that points to which `Axis` instance the node is assigned to
        #  (this will point to an `Axis` instance via `HivePlot.axes[label]`)
        self.axis_label = None

    def __repr__(self):
        """
        Make printable representation (repr) for ``Node`` instance.
        """
        return f"hiveplotlib.Node {self.unique_id}"

    def add_data(self, data: dict, overwrite_old_data: bool = False):
        """
        Add dictionary of data to ``Node.data``.

        :param data: dict of data to associate with ``Node`` instance.
        :param overwrite_old_data: whether to delete existing data dict and overwrite with ``data``. Default ``False``.
        :return: ``None``.
        """
        assert type(data) == dict, \
            "`data` must be dictionary."

        if overwrite_old_data:
            self.data = data

        else:
            for k in data.keys():
                self.data[k] = data[k]

        return None


class Axis:
    """
    ``Axis`` instance.

    ``Axis`` instances are initialized based on their intended final position when plotted. Each ``Axis`` is also
    initialized with a unique, hashable ``axis_id`` for clarity when building hive plots with multiple axes.

    The eventual size and positioning of the ``Axis`` instance is dictated in the context of polar coordinates by three
    parameters:

    ``start`` dictates the distance from the origin to the *beginning* of the axis when eventually plotted.

    ``stop`` dictates the distance from the origin to the *end* of the axis when eventually plotted.

    ``angle`` sets the angle the ``Axis`` is rotated counterclockwise. For example, ``angle=0`` points East,
    ``angle=90`` points North, and ``angle=180`` points West.

    ``Node`` instances placed on each ``Axis`` instance will be scaled to fit onto the span of the ``Axis``, but this is
    discussed further in the ``HivePlot`` class, which handles this placement.

    Since ``axis_id`` values may be shorthand for easy referencing when typing code, if one desires a formal name to
    plot against each axis when visualizing, one can provide a separate ``long_name`` that will show up as the axis
    label when running ``hiveplotlib.viz`` code. (For example, one may choose ``axis_id="a1"`` and
    ``long_name="Axis 1"``.

    .. note::
        ``long_name`` defaults to ``axis_id`` if not specified.

    :example:

        .. highlight:: python
        .. code-block:: python

            # 3 axes, spaced out 120 degrees apart, all size 4, starting 1 unit off of origin
            axis0 = Axis(axis_id="a0", start=1, end=5, angle=0, long_name="Axis 0")
            axis1 = Axis(axis_id="a1", start=1, end=5, angle=120, long_name="Axis 1")
            axis2 = Axis(axis_id="a2", start=1, end=5, angle=240, long_name="Axis 2")
    """

    def __init__(self, axis_id: Hashable, start: float = 1, end: float = 5, angle: float = 0,
                 long_name: str or None = None):
        """
        Initialize ``Axis`` object with start and end positions and angle. Default to axis normalized on [0, 1].

        :param axis_id: unique name for ``Axis`` instance.
        :param start: point closest to the center of the plot (using the same positive number for multiple axes in a
            hive plot is a nice way to space out the figure).
        :param end: point farthest from the center of the plot.
        :param angle: angle to set the axis, in degrees (moving counterclockwise, e.g.
            0 degrees points East, 90 degrees points North).
        :param long_name: longer name for use when labeling on graph (but not for referencing the axis).
            Default ``None`` sets it to ``axis_id``.
        """
        self.axis_id = axis_id

        if long_name is None:
            self.long_name = str(axis_id)
        else:
            self.long_name = str(long_name)

        # keep internal angle in [0, 360)
        self.angle = angle % 360

        self.polar_start = start
        self.start = polar2cartesian(self.polar_start, self.angle)

        self.polar_end = end
        self.end = polar2cartesian(self.polar_end, self.angle)

        # key from each node's data dictionary that we will use to position the node along the `Axis`
        self.node_placement_label = None

        # hold all the cartesian coordinates, polar rho, and corresponding labels in a pandas dataframe
        self.node_placements = pd.DataFrame(columns=['x', 'y', 'unique_id', 'rho'])

    def __repr__(self):
        """
        Make printable representation (repr) for ``Axis`` instance.
        """
        return f"hiveplotlib.Axis {self.axis_id}"

    def _set_node_placements(self, x: List, y: List, node_ids: List, rho: List):
        """
        Set ``Axis.node_placements`` to a ``pandas.DataFrame``.

        Dataframe consists of x cartesian coordinates, y cartesian coordinates, unique node IDs, and polar *rho* values
        (e.g. distance from the origin).

        .. note::
            This is an internal setter method to be called downstream by the ``HivePlot.place_nodes_on_axis()``
            method.

        :param x: ``list-like`` of x cartesian coordinates.
        :param y: ``list-like`` of y cartesian coordinates corresponding to x coordinates.
        :param node_ids: ``list-like`` of unique node IDs corresponding to x and y coordinates.
        :param rho: ``list-like`` of polar coordinate distance values corresponding to x, y, and unique ID values.
        :return: ``None``.
        """
        assert np.array(x).shape[0] == np.array(y).shape[0] == np.array(node_ids).shape[0] == np.array(rho).shape[0], \
            "Must provide the same number of x values, y values, and node IDs"

        self.node_placements = pd.DataFrame.from_dict({'x': x, 'y': y, 'unique_id': node_ids, 'rho': rho})

        return None

    def _set_node_placement_label(self, label: Hashable):
        """
        Set which scalar variable in each ``Node`` instance will be used to place each node on the axis when plotting.

        .. note::
            This is an internal setter method to be called downstream by the ``HivePlot.place_nodes_on_axis()``
            method.

        :param label: which scalar variable in the node data to reference.
        :return: ``None``.
        """
        self.node_placement_label = label

        return None


class HivePlot:
    """
    Hive Plots built from combination of ``Axis`` and ``Node`` instances.

    This class is essentially methods for creating and maintaining the nested dictionary attribute ``edges``,
    which holds constructed Bézier curves, edge ids, and matplotlib keyword arguments for various sets of edges to be
    plotted. The nested dictionary structure can be abstracted to the below example.

    .. highlight:: python
    .. code-block:: python

        HivePlot.edges["starting axis"]["ending axis"]["tag"]

    The resulting dictionary value holds the edge information relating to an addition of edges that are tagged as
    "tag," specifically the edges going *FROM* the axis named "starting axis" *TO* the axis named "ending axis." This
    value is in fact another dictionary, meant to hold the discretized Bézier curves (``curves``), the matplotlib
    keyword arguments for plotting (``edge_kwargs``), and the abstracted edge ids (an ``(m, 2) np.ndarray``) between
    which we are drawing Bézier curves (``ids``).
    """

    def __init__(self):
        """
        Initialize ``HivePlot`` object.
        """
        # keep dictionary of axes, so we can find axes by label
        self.axes = dict()

        # keep dictionary of nodes with keys as unique IDs
        self.nodes = dict()

        # maintain dictionary of node assignments to axes
        #  (note, this may not always be a partition, e.g. repeat axis)
        self.node_assignments = dict()

        # maintain dictionary of dictionaries of dictionaries of edge information
        self.edges = dict()

    def add_axes(self, axes: List):
        """
        Add list of ``Axis`` instances to ``HivePlot.axes``.

        .. note::
            All resulting Axis IDs *must* be unique.

        :param axes: ``Axis`` objects to add to `HivePlot` instance.
        :return: ``None``.
        """
        current_ids = list(self.axes.keys())
        new_ids = [axis.axis_id for axis in axes]
        combined_ids = current_ids + new_ids
        assert len(combined_ids) == len(set(combined_ids)), \
            "New specified axis IDs combined with existing IDs led to non-unique IDs. Not adding specified axes."

        for axis in axes:
            self.axes[axis.axis_id] = axis
            self.node_assignments[axis.axis_id] = None
        return None

    def add_nodes(self, nodes: List, check_uniqueness: bool = True):
        """
        Add ``Node`` instances to ``HivePlot.nodes``.

        :param nodes: collection of ``Node`` instances, will be added to ``HivePlot.nodes`` dict with unique IDs as
            keys.
        :param check_uniqueness: whether to formally check for uniqueness.
            WARNING: the only reason to turn this off is if the dataset becomes big enough that this operation becomes
            expensive, and you have already established uniqueness another way (for example, you are pulling data from
            a database and the key in your table is the unique ID). If you add non-unique IDs with
            ``check_uniqueness=False``, we make no promises about output.
        :return: ``None``.
        """
        # make sure ids are unique or things could break later
        if check_uniqueness:
            current_ids = list(self.nodes.keys())
            new_ids = [node.unique_id for node in nodes]
            combined_ids = current_ids + new_ids
            assert len(combined_ids) == len(set(combined_ids)), \
                "New specified IDs combined with existing IDs led to non-unique IDs. Not adding specified nodes."

        for node in nodes:
            self.nodes[node.unique_id] = node

        return None

    def _allocate_nodes_to_axis(self, unique_ids: List, axis_id: Hashable):
        """
        Allocate a set of nodes (pointers by unique node id's) to a single ``Axis`` (specified by a unique ``axis_id``).

        .. note::
            This is NOT sufficient for plotting nodes, only an underlying setter method called in
            ``HivePlot.place_nodes_on_axis()``.

        :param unique_ids: list of node IDs to place on specified axis.
        :param axis_id: unique ID of ``Axis`` assigned to ``HivePlot`` instance on which we want to place nodes.
        :return: ``None``.
        """
        self.node_assignments[axis_id] = unique_ids

        return None

    def place_nodes_on_axis(self, axis_id: Hashable, unique_ids: List or None = None,
                            sorting_feature_to_use: Hashable or None = None,
                            vmin: float or None = None, vmax: float or None = None):
        """
        Set node positions on specific ``Axis``.

        Cartesian coordinates will be normalized to specified ``vmin`` and ``vmax``. Those ``vmin`` and ``vmax``
        values will then be normalized to span the length of the axis when plotted.

        :param axis_id: which axis (as specified by the keys from ``HivePlot.axes``) for which to plot nodes.
        :param unique_ids: list of node IDs to assign to this axis. If previously set with
            ``HivePlot._allocate_nodes_to_axis()``, this will overwrite those node assignments. If ``None``, method
            will check and confirm there are existing node ID assignments.
        :param sorting_feature_to_use: which feature in the node data to use to align nodes on an axis.
            Default ``None`` uses the feature previously assigned via
            ``HivePlot.axes[axis_id]._set_node_placement_label()``.
        :param vmin: all values less than ``vmin`` will be set to ``vmin``. Default ``None`` sets as global minimum of
            feature values for all ``Node`` instances on specified ``Axis``.
        :param vmax: all values greater than ``vmax`` will be set to ``vmin``. Default ``None`` sets as global maximum
            of feature values for all ``Node`` instances on specified ``Axis``.
        :return: ``None``.
        """
        # ToDo: allow rescaling option before thresholding on min and max values (e.g. put in log scale)

        if unique_ids is None:
            assert self.node_assignments[axis_id] is not None, \
                f"No existing node IDs assigned to axis {axis_id}. Please provide `unique_ids` to place on this axis."
        else:
            self._allocate_nodes_to_axis(unique_ids=unique_ids, axis_id=axis_id)

        # assign which data label to use
        if sorting_feature_to_use is not None:
            self.axes[axis_id]._set_node_placement_label(label=sorting_feature_to_use)

        else:
            assert self.axes[axis_id].node_placement_label is not None, \
                "Must either specify which feature to use in " + \
                "`HivePlot.place_nodes_on_axis(feature_to_use=<Hashable>)` " + \
                "or set the feature directly on the `Axis._set_node_placement_label(label=<Hashable>)`."

        axis = self.axes[axis_id]

        assert axis.node_placement_label is not None, \
            "Must choose a node feature on which to order points with `Axis._set_node_placement_label()`"

        all_node_ids = self.node_assignments[axis_id]
        all_vals = np.array([self.nodes[node_id].data[axis.node_placement_label]
                             for node_id in all_node_ids]).astype(float)

        if vmin is None:
            vmin = np.min(all_vals)
        if vmax is None:
            vmax = np.max(all_vals)

        # handle case of one point on an axis but no vmin or vmax specified (put it at the midpoint)
        if all_vals.size == 1 and vmin == vmax:
            vmin -= 1
            vmax += 1

        # handle case of one unique value on an axis but no vmin or vmax specified (put it at the midpoint)
        if np.unique(all_vals).size == 1 and vmin == vmax:
            vmin -= 1
            vmax += 1

        # scale values to [vmin, vmax]
        all_vals[all_vals < vmin] = vmin
        all_vals[all_vals > vmax] = vmax

        # normalize to vmin = 0, vmax = 1
        all_vals -= vmin
        all_vals /= (vmax - vmin)
        # scale to length of axis
        all_vals *= np.abs(axis.polar_end - axis.polar_start)
        # shift to correct starting point which could be off the origin
        all_vals += axis.polar_start

        # translate into cartesian coords
        x_coords, y_coords = polar2cartesian(all_vals, axis.angle)

        # update pandas dataframe of cartesian coordinate information and polar rho coordinates
        axis._set_node_placements(x=x_coords, y=y_coords, node_ids=all_node_ids, rho=all_vals)

        # remove any curves that were previously pointing to this axis
        #  (since they were based on a different alignment of nodes)
        for a0 in list(self.edges.keys()):
            for a1 in list(self.edges[a0].keys()):
                if a0 == axis_id or a1 == axis_id:
                    for k in self.edges[a0][a1].keys():
                        if "curves" in self.edges[a0][a1][k]:
                            del self.edges[a0][a1][k]["curves"]

        return None

    def reset_edges(self, axis_id_1: Hashable or None = None, axis_id_2: Hashable or None = None,
                    tag: Hashable or None = None, a1_to_a2: bool = True, a2_to_a1: bool = True):
        """
        Reset ``HivePlot.edges``.

        Setting all the parameters to ``None`` deletes any stored connections between axes previously computed. If any
        subset of the parameters is not ``None``, the resulting edges will be deleted:

        If ``axis_id_1``, ``axis_id_2``, and ``tag`` are all specified as *not* ``None``, the implied
        single subset of edges will be deleted. (Note, tags are required to be unique within a specified
        (axis_id_1, axis_id_2) pair.) In this case, the default is to delete all the edges bidirectionally (e.g. going
        ``axis_id_1`` -> ``axis_id_2`` *and* ``axis_id_2`` -> ``axis_id_1``) with the specified ``tag``. To
        only delete edges in one of these directions, see the description of the ``bool`` parameters ``a1_to_a2`` and
        ``a2_to_a1`` below.

        If *only* ``axis_id_1`` and ``axis_id_2`` are provided as not ``None``, then the default is to delete all edge
        subsets bidirectionally between ``axis_id_1`` to ``axis_id_2`` (e.g. going
        ``axis_id_1`` -> ``axis_id_2`` *and* ``axis_id_2`` -> ``axis_id_1``) with the specified ``tag``. To
        only delete edges in one of these directions, see the description of the ``bool`` parameters ``a1_to_a2`` and
        ``a2_to_a1`` below.

        If *only* ``axis_id_1`` is provided as not ``None``, then all edges going *TO* and *FROM* ``axis_id_1`` will be
        deleted. To only delete edges in one of these directions, see the description of the ``bool`` parameters
        ``a1_to_a2`` and ``a2_to_a1`` below.

        :param axis_id_1: specifies edges all coming FROM the axis identified by this unique ID.
        :param axis_id_2: specifies edges all coming TO the axis identified by this unique ID.
        :param tag: tag corresponding to explicit subset of added edges.
        :param a1_to_a2: whether to remove the connections going FROM ``axis_id_1`` TO ``axis_id_2``. Note, if
            ``axis_id_1`` is specified by ``axis_id_2`` is ``None``, then this dictates whether to remove all edges
            going *from* ``axis_id_1``.
        :param a2_to_a1: whether to remove the connections going FROM ``axis_id_2`` TO ``axis_id_1``. Note, if
            ``axis_id_1`` is specified by ``axis_id_2`` is ``None``, then this dictates whether to remove all edges
            going *to* ``axis_id_1``.
        :return: ``None``.
        """
        # all None => reset all edges
        if axis_id_1 is None and axis_id_2 is None and tag is None:
            self.edges = dict()
            return None

        # all specified => reset just unique tag subset
        elif tag is not None and axis_id_2 is not None and axis_id_1 is not None:
            if a1_to_a2:
                if tag in self.edges[axis_id_1][axis_id_2].keys():
                    del self.edges[axis_id_1][axis_id_2][tag]
                else:
                    raise ValueError("Key to delete not found. No edge data deleted.")
            if a2_to_a1:
                if tag in self.edges[axis_id_2][axis_id_1].keys():
                    del self.edges[axis_id_2][axis_id_1][tag]
                else:
                    raise ValueError("Key to delete not found. No edge data deleted.")
            return None

        # just to and from axes => kill all the connections between the two axes
        elif axis_id_2 is not None and axis_id_1 is not None:
            if a1_to_a2:
                del self.edges[axis_id_1][axis_id_2]
            if a2_to_a1:
                del self.edges[axis_id_2][axis_id_1]
            return None

        # just one axis => kill all connections coming to / from it
        elif axis_id_1 is not None and axis_id_2 is None:
            # kill "from" connections
            if a1_to_a2:
                del self.edges[axis_id_1]
            # kill "to" connections
            if a2_to_a1:
                for a0 in self.edges.keys():
                    if axis_id_1 in self.edges[a0].keys():
                        del self.edges[a0][axis_id_1]
            return None

        else:
            raise NotImplementedError("See the docstring for ``HivePlot.reset_edges()`` for more on supported uses.")

    def __check_unique_edge_subset_tag(self, tag: Hashable, from_axis_id: Hashable, to_axis_id: Hashable):
        """
        Make sure any ``tag`` specified to represent a subset of added edges is unique in its pair of (from, to) axes.

        Raises ``ValueError`` if ``tag`` is not unique.

        :param tag: unique ID corresponding to an added edge set.
        :param from_axis_id: ID of axis that nodes are coming "from."
        :param to_axis_id: ID of axis that nodes are going "to."
        :return: ``None``.
        """
        if tag in self.edges[from_axis_id][to_axis_id].keys():
            raise ValueError(f"Non-unique tag ({tag}) specified from {from_axis_id} to {to_axis_id}.\n"
                             "Please provide edge subset with a new unique tag.")
        return None

    def _find_unique_tag(self, from_axis_id: Hashable, to_axis_id: Hashable, bidirectional: bool = False) -> Hashable:
        """
        Find the first unique, unused ``tag`` value between ``from_axis_id`` and ``to_axis_id``.

        Check by starting at 0 and incrementing up by 1 until the integer is unique.

        :param from_axis_id: ID of axis that nodes are coming "from."
        :param to_axis_id: ID of axis that nodes are going "to."
        :param bidirectional: whether to generate a tag that is unique for *both*
            ``from_axis_id`` -> ``to_axis_id`` AND ``to_axis_id`` -> ``from_axis_id``. Default ``False`` only guarantees
            the former direction.
        :return: ``Hashable`` of resulting unique tag.
        """
        tag_list = list(self.edges[from_axis_id][to_axis_id].keys())
        if bidirectional:
            # if the other direction of edges doesn't exist, then this tag would have to be unique
            if to_axis_id in self.edges:
                if from_axis_id in self.edges[to_axis_id]:
                    tag_list += list(self.edges[to_axis_id][from_axis_id].keys())

        tag = 0
        while True:
            if tag not in tag_list:
                break
            tag += 1

        return tag

    def __store_edge_ids(self, edge_ids: np.ndarray, from_axis_id: Hashable, to_axis_id: Hashable,
                         tag: Hashable or None = None, bidirectional: bool = False) -> Hashable:
        """
        Store edge ids to ``HivePlot.edges`` (e.g. the unique identifiers of nodes "from" and "to" for each edge).

        :param edge_ids: node IDs of "from" and "to" nodes.
        :param from_axis_id: ID of axis that nodes are coming "from."
        :param to_axis_id: ID of axis that nodes are going "to."
        :param tag: tag corresponding to subset of specified edges. If ``None`` is provided, the tag will be set as
            the lowest unused integer of the tags specified for this (``from_axis_id``, ``to_axis_id``) pair, starting
            at ``0`` amongst the available tags under ``HivePlot.edges[from_axis_id][to_axis_id]``.
        :param bidirectional: if ``tag`` is ``None``, this boolean value if ``True`` guarantees that the resulting tag
            that will be generated is unique  for *both* ``from_axis_id`` -> ``to_axis_id``
            AND ``to_axis_id`` -> ``from_axis_id``. Default ``False`` only guarantees uniqueness for the former
            direction. Note: edges are still only added for ``from_axis_id`` -> ``to_axis_id``. This parameter exists
            solely for validating whether a newly generated tag must be unique bidirectionally.
        :return: the resulting unique tag.
        """
        from_keys = list(self.edges.keys())
        if from_axis_id not in from_keys:
            self.edges[from_axis_id] = dict()
            self.edges[from_axis_id][to_axis_id] = dict()

        to_keys = list(self.edges[from_axis_id].keys())
        if to_axis_id not in to_keys:
            self.edges[from_axis_id][to_axis_id] = dict()

        # make sure we create a unique integer tag if no tag is specified
        if tag is None:
            tag = self._find_unique_tag(from_axis_id=from_axis_id, to_axis_id=to_axis_id,
                                        bidirectional=bidirectional)

        # make sure tag sufficiently unique when specified
        else:
            self.__check_unique_edge_subset_tag(tag=tag, from_axis_id=from_axis_id, to_axis_id=to_axis_id)

        self.edges[from_axis_id][to_axis_id][tag] = dict()

        self.edges[from_axis_id][to_axis_id][tag]["ids"] = edge_ids

        return tag

    def add_edge_ids(self, edges: np.ndarray, axis_id_1: Hashable, axis_id_2: Hashable, tag: Hashable or None = None,
                     a1_to_a2: bool = True, a2_to_a1: bool = True) -> Hashable:
        """
        Find and store the edge IDs relevant to the specified pair of axes.

        Find the subset of network connections that involve nodes on ``axis_id_1`` and ``axis_id_2``.
        looking over the specified ``edges`` compared to the IDs of the ``Node`` instances currently placed on each
        ``Axis``. Edges discovered between the specified two axes (depending on the values specified by ``a1_to_a2`` and
        ``a2_to_a1``, more below) will have the relevant edge IDs stored, with other edges disregarded.

        Generates ``(j, 2)`` and ``(k, 2)`` numpy arrays of ``axis_id_1`` to ``axis_id_2`` connections and ``axis_id_2``
        to ``axis_id_1`` connections (or only 1 of those arrays depending on parameter choices for ``a1_to_a2`` and
        ``a2_to_a1``).

        The resulting arrays of relevant edge IDs (e.g. each row is a [<FROM ID>, <TO ID>] edge) will be stored
        automatically in ``HivePlot.edges``, a dictionary of dictionaries of dictionaries of edge information,
        which can later be converted into discretized edges to be plotted in Cartesian space. They are stored as
        ``HivePlot.edges[<source_axis_id>][<sink_axis_id>][<tag>]["ids"]``.

        .. note::
            If no ``tag`` is provided (e.g. default ``None``), one will be automatically generated and returned by
            this method call.

        :param edges: ``(n, 2)`` array of ``Hashable`` values representing unique IDs of specific ``Node`` instances.
            The first column is the IDs for the "from" nodes and the second column is the IDS for the "to" nodes for
            each connection.
        :param axis_id_1: pointer to first of two ``Axis`` instances in ``HivePlot.axes`` between which we want to
            find connections.
        :param axis_id_2: pointer to second of two ``Axis`` instances in ``HivePlot.axes`` between which we want to
            find connections.
        :param tag: tag corresponding to subset of specified edges. If ``None`` is provided, the tag will be set as
            the lowest unused integer starting at ``0`` amongst the available tags under
            ``HivePlot.edges[axis_id_1][axis_id_2]`` and / or ``HivePlot.edges[axis_id_2][axis_id_1]``.
        :param a1_to_a2: whether to find the connections going FROM ``axis_id_1`` TO ``axis_id_2``.
        :param a2_to_a1: whether to find the connections going FROM ``axis_id_2`` TO ``axis_id_1``.
        :return: the resulting unique tag. Note, if both ``a1_to_a2`` and ``a2_to_a1`` are ``True`` the resulting
            unique tag returned will be the same for both directions of edges.
        """
        # only need to validate a bidirectional tag if generating it from scratch
        if a1_to_a2 and a2_to_a1 and tag is None:
            bidirectional = True
        elif not a1_to_a2 and not a2_to_a1:
            raise ValueError("One of `a1_to_a2` or `a2_to_a1` must be true.")
        else:
            bidirectional = False
        # axis 1 to axis 2
        if a1_to_a2:
            a1_input = np.isin(edges[:, 0], self.axes[axis_id_1].node_placements.values[:, 2])
            a2_output = np.isin(edges[:, 1], self.axes[axis_id_2].node_placements.values[:, 2])
            a1_to_a2 = np.logical_and(a1_input, a2_output)
            new_tag = self.__store_edge_ids(edge_ids=edges[a1_to_a2], from_axis_id=axis_id_1,
                                            to_axis_id=axis_id_2, tag=tag, bidirectional=bidirectional)

        # axis 2 to axis 1
        if a2_to_a1:
            a1_output = np.isin(edges[:, 1], self.axes[axis_id_1].node_placements.values[:, 2])
            a2_input = np.isin(edges[:, 0], self.axes[axis_id_2].node_placements.values[:, 2])
            a2_to_a1 = np.logical_and(a2_input, a1_output)
            # if doing both, be sure to supply the same tag
            if bidirectional:
                tag = new_tag
            new_tag = self.__store_edge_ids(edge_ids=edges[a2_to_a1], from_axis_id=axis_id_2,
                                            to_axis_id=axis_id_1, tag=tag)

        return new_tag

    def add_edge_curves_between_axes(self, axis_id_1: Hashable, axis_id_2: Hashable, tag: Hashable or None = None,
                                     a1_to_a2: bool = True, a2_to_a1: bool = True,
                                     num_steps: int = 100, short_arc: bool = True):
        """
        Construct discretized edge curves between two axes of a ``HivePlot`` instance.

        .. note::
            One must run ``HivePlot.add_edge_ids()`` first for the two axes of interest.

        Resulting discretized Bézier curves will be stored as an ``(n, 2) numpy.ndarray`` of multiple sampled curves
        where the first column is x position and the second column is y position in Cartesian coordinates.

        .. note::
            Although each curve is represented by a ``(num_steps, 2)`` array, all the curves are stored curves in a
            single collective ``numpy.ndarray`` separated by rows of ``[np.nan, np.nan]`` between each discretized
            curve. This allows ``matplotlib`` to accept a single array when plotting lines via ``plt.plot()``, which
            speeds up plotting later.

        This output will be stored in ``HivePlot.edges[axis_id_1][axis_id_2][tag]["curves"]``.

        :param axis_id_1: pointer to first of two ``Axis`` instances in ``HivePlot.axes`` between which we want to
            find connections.
        :param axis_id_2: pointer to second of two ``Axis`` instances in ``HivePlot.axes`` between which we want to
            find connections.
        :param tag: unique ID specifying which subset of edges specified by their IDs to construct
            (e.g. ``HivePlot.edges[axis_id_1][axis_id_2][tag]["ids"]``).
            Note, if no tag is specified (e.g. ``tag=None``), it is presumed there is only one tag for the specified
            set of axes to look over, which can be inferred. If no tag is specified and there are multiple tags to
            choose from, a ``ValueError`` will be raised.
        :param a1_to_a2: whether to build out the edges going FROM ``axis_id_1`` TO ``axis_id_2``.
        :param a2_to_a1: whether to build out the edges going FROM ``axis_id_2`` TO ``axis_id_1``.
        :param num_steps: number of points sampled along a given Bézier curve. Larger numbers will result in
            smoother curves when plotting later, but slower rendering.
        :param short_arc: whether to take the shorter angle arc (``True``) or longer angle arc (``False``).
            There are always two ways to traverse between axes: with one angle being x, the other option being 360 - x.
            For most visualizations, the user should expect to traverse the "short arc," hence the default ``True``.
            For full user flexibility, however, we offer the ability to force the arc the other direction, the
            "long arc" (``short_arc=False``). Note: in the case of 2 axes 180 degrees apart, there is no "wrong" angle,
            so in this case an initial decision will be made, but switching this boolean will switch the arc to the
            other hemisphere.
        :return: ``None``.
        """
        if tag is None:
            a1_to_a2_failure = False
            a2_to_a1_failure = False
            if a1_to_a2:
                assert len(list(self.edges[axis_id_1][axis_id_2].keys())) > 0, \
                    "No edges specified to construct. Be sure to run `HivePlot.add_edge_ids()` first."

                a1_to_a2_tag = list(self.edges[axis_id_1][axis_id_2].keys())[0]

                if len(list(self.edges[axis_id_1][axis_id_2].keys())) > 1:
                    a1_to_a2_failure = True

            if a2_to_a1:
                assert len(list(self.edges[axis_id_2][axis_id_1].keys())) > 0, \
                    "No edges specified to construct. Be sure to run `HivePlot.add_edge_ids()` first."

                a2_to_a1_tag = list(self.edges[axis_id_2][axis_id_1].keys())[0]

                if len(list(self.edges[axis_id_2][axis_id_1].keys())) > 1:
                    a2_to_a1_failure = True

            if a1_to_a2_failure and a2_to_a1_failure:
                raise ValueError("Must specify precise `tag` to handle both `a1_to_a2=True` and `a2_to_a1=True` here. "
                                 "The current tags for the specified axes are:\n"
                                 f"{axis_id_2} -> {axis_id_1: {list(self.edges[axis_id_2][axis_id_1].keys())}}\n"
                                 f"{axis_id_2} -> {axis_id_1: {list(self.edges[axis_id_2][axis_id_1].keys())}}")

            elif a1_to_a2_failure:
                raise ValueError("Must specify precise `tag` to handle `a1_to_a2=True` here. "
                                 "The current tags for the specified axes are:\n"
                                 f"{axis_id_1} -> {axis_id_2: {list(self.edges[axis_id_1][axis_id_2].keys())}}")
            elif a2_to_a1_failure:
                raise ValueError("Must specify precise `tag` to handle `a2_to_a1=True` here. "
                                 "The current tags for the specified axes are:\n"
                                 f"{axis_id_2} -> {axis_id_1: {list(self.edges[axis_id_2][axis_id_1].keys())}}")

        else:
            a1_to_a2_tag = tag
            a2_to_a1_tag = tag

        all_connections = []
        direction = []
        if a1_to_a2:
            try:
                ids = self.edges[axis_id_1][axis_id_2][a1_to_a2_tag]["ids"]
                temp_connections = ids.copy().astype("O")
                all_connections.append(temp_connections)
                direction.append("a1_to_a2")
            except KeyError:
                raise KeyError(
                    f"`self.edges[{axis_id_1}][{axis_id_2}][{a1_to_a2_tag}]['ids']` does not appear to exist. "
                    "It is expected you have run `self.add_edge_ids()` first for the two axes of interest."
                )
        if a2_to_a1:
            try:
                ids = self.edges[axis_id_2][axis_id_1][a2_to_a1_tag]["ids"]
                temp_connections = ids.copy().astype("O")
                all_connections.append(temp_connections)
                direction.append("a2_to_a1")
            except KeyError:
                raise KeyError(
                    f"`self.edges[{axis_id_2}][{axis_id_1}][{a2_to_a1_tag}]['ids']` does not appear to exist. "
                    "It is expected you have run `self.add_edge_ids()` first for the two axes of interest."
                )

        if len(all_connections) == 0:
            raise ValueError("One of `a1_to_a2` or `a2_to_a1` must be true.")

        for connections, edge_direction in zip(all_connections, direction):

            # left join the flattened start and stop values array with the cartesian and polar node locations
            #  Note: sorting behavior is not cooperating, so needed a trivial np.arange to re-sort at end
            #   (dropped before using `out`)
            if edge_direction == "a1_to_a2":
                start_axis = axis_id_1
                stop_axis = axis_id_2
            elif edge_direction == "a2_to_a1":
                start_axis = axis_id_2
                stop_axis = axis_id_1

            start = pd.DataFrame(np.c_[connections[:, 0], np.arange(connections.shape[0])]) \
                .merge(self.axes[start_axis].node_placements,
                       left_on=0, right_on="unique_id", how="left") \
                .sort_values(1) \
                .drop(columns=[0, 1, "unique_id"]) \
                .values

            stop = pd.DataFrame(np.c_[connections[:, 1], np.arange(connections.shape[0])]) \
                .merge(self.axes[stop_axis].node_placements,
                       left_on=0, right_on="unique_id", how="left") \
                .sort_values(1) \
                .drop(columns=[0, 1, "unique_id"]) \
                .values

            start_arr = start[:, :2]
            end_arr = stop[:, :2]

            # we only want one rho for the start, stop pair (using the mean rho)
            control_rho = (start[:, 2] + stop[:, 2]) / 2

            # all interactions between same two axes, so only one angle
            angles = [self.axes[axis_id_1].angle, self.axes[axis_id_2].angle]
            angle_diff = angles[1] - angles[0]

            # make sure we take the short arc if requested
            if short_arc:
                if np.abs(angle_diff) > 180:
                    # flip the direction in this case and angle between is now "360 minus"
                    control_angle = angles[0] + -1 * np.sign(angle_diff) * (360 - np.abs(angle_diff)) / 2
                else:
                    control_angle = angles[0] + angle_diff / 2
            # long arc
            else:
                if np.abs(angle_diff) <= 180:
                    # flip the direction in this case and angle between is now "360 minus"
                    control_angle = angles[0] + -1 * np.sign(angle_diff) * (360 - np.abs(angle_diff)) / 2
                else:
                    control_angle = angles[0] + angle_diff / 2

            control_cartesian = polar2cartesian(control_rho, control_angle)
            bezier_output = np.column_stack(
                [bezier_all(start_arr=start_arr[:, i], end_arr=end_arr[:, i],
                            control_arr=control_cartesian[i], num_steps=num_steps)
                 for i in range(2)]
            )

            # put `np.nan` spacers in
            bezier_output = np.insert(arr=bezier_output,
                                      obj=np.arange(bezier_output.shape[0], step=num_steps) + num_steps,
                                      values=np.nan, axis=0)

            # store the output in the right place(s)
            if edge_direction == "a1_to_a2":
                self.edges[axis_id_1][axis_id_2][a1_to_a2_tag]["curves"] = bezier_output

            elif edge_direction == "a2_to_a1":
                self.edges[axis_id_2][axis_id_1][a2_to_a1_tag]["curves"] = bezier_output

        return None

    def construct_curves(self, num_steps: int = 100, short_arc: bool = True):
        """
        Construct Bézier curves for any connections for which we've specified the edges to draw.

        (e.g. ``HivePlot.edges[axis_0][axis_1][<tag>]["ids"]`` is non-empty but
        ``HivePlot.edges[axis_0][axis_1][<tag>]["curves"]`` does not yet exist).

        .. note::
            Checks all <tag> values between axes.

        :param num_steps: number of points sampled along a given Bézier curve. Larger numbers will result in
            smoother curves when plotting later, but slower rendering.
        :param short_arc: whether to take the shorter angle arc (``True``) or longer angle arc (``False``).
            There are always two ways to traverse between axes: with one angle being x, the other option being 360 - x.
            For most visualizations, the user should expect to traverse the "short arc," hence the default ``True``.
            For full user flexibility, however, we offer the ability to force the arc the other direction, the
            "long arc" (``short_arc=False``). Note: in the case of 2 axes 180 degrees apart, there is no "wrong" angle,
            so in this case an initial decision will be made, but switching this boolean will switch the arc to the
            other hemisphere.
        :return: ``None``.
        """
        for a0 in list(self.edges.keys()):
            for a1 in list(self.edges[a0].keys()):
                for tag in list(self.edges[a0][a1].keys()):
                    if "ids" in self.edges[a0][a1][tag] and "curves" not in self.edges[a0][a1][tag]:
                        self.add_edge_curves_between_axes(axis_id_1=a0, axis_id_2=a1, a2_to_a1=False,
                                                          tag=tag, num_steps=num_steps, short_arc=short_arc)
        return None

    def add_edge_kwargs(self, axis_id_1: Hashable, axis_id_2: Hashable, tag: Hashable or None = None,
                        a1_to_a2: bool = True, a2_to_a1: bool = True, **edge_kwargs):
        """
        Add edge kwargs to the constructed ``HivePlot.edges`` between two axes of a ``HivePlot``.

        For a given set of edges for which edge kwargs were already set, any redundant edge kwargs specified by this
        method call will overwrite the previously set kwargs.

        Expected to have found edge IDs between the two axes before calling this method, which can be done either
        by calling ``HivePlot.connect_axes()`` method or the lower-level ``HivePlot.add_edge_ids()`` method for the two
        axes of interest.

        Resulting kwargs will be stored as a dict. This output will be stored in
        ``HivePlot.edges[axis_id_1][axis_id_2][tag]["edge_kwargs"]``.

        .. note::
            There is special handling in here for when the two provided axes have names ``"<axis_name>"`` and
            ``"<axis_name>_repeat"``. This is for use with ``hiveplotlib.hive_plot_n_axes()``, which when creating
            repeat axes always names the repeated one ``"<axis_name>_repeat"``. By definition, the edges between an axis
            and its repeat are the same, and therefore edges between these two axes should *only* be plotted in one
            direction. If one is running this method on a ``Hiveplot`` instance from ``hiveplotlib.hive_plot_n_axes()``
            though, a warning of a lack of edges in both directions for repeat edges is not productive, so we formally
            catch this case.

        :param axis_id_1: Hashable pointer to the first ``Axis`` instance in ``HivePlot.axes`` we want to add plotting
            kwargs to.
        :param axis_id_2: Hashable pointer to the second ``Axis`` instance in ``HivePlot.axes`` we want to add plotting
            kwargs to.
        :param tag: which subset of curves to modify kwargs for.
            Note, if no tag is specified (e.g. ``tag=None``), it is presumed there is only one tag for the specified
            set of axes to look over and that will be inferred. If no tag is specified and there are multiple tags to
            choose from, a ``ValueError`` will be raised.
        :param a1_to_a2: whether to add kwargs for connections going FROM ``axis_id_1`` TO ``axis_id_2``.
        :param a2_to_a1: whether to add kwargs for connections going FROM ``axis_id_2`` TO ``axis_id_1``.
        :param edge_kwargs: additional ``matplotlib`` keyword arguments that will be applied to the specified edges.
        :return: ``None``.
        """
        if tag is None:
            a1_to_a2_failure = False
            a2_to_a1_failure = False

            # special warning if repeat axes have no edges between each other
            if a1_to_a2 and a2_to_a1 and str(axis_id_2).rstrip("_repeat") == str(axis_id_1).rstrip("_repeat"):
                repeat_edges_defined = False
                if axis_id_1 in self.edges.keys():
                    if axis_id_2 in self.edges[axis_id_1].keys():
                        if len(list(self.edges[axis_id_1][axis_id_2].keys())) > 0:
                            repeat_edges_defined = True
                if axis_id_2 in self.edges.keys():
                    if axis_id_1 in self.edges[axis_id_2].keys():
                        if len(list(self.edges[axis_id_2][axis_id_1].keys())) > 0:
                            repeat_edges_defined = True
                if not repeat_edges_defined:
                    warnings.warn(f"Repeat axes {axis_id_1} and {axis_id_2} have no edges."
                                  "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                                  "first.", stacklevel=2)
            if a1_to_a2:
                if axis_id_1 in self.edges.keys():
                    if axis_id_2 not in self.edges[axis_id_1].keys():
                        # special handling for the "_repeat" axis
                        #  we check and warn with respect to repeat axes above
                        if str(axis_id_2).rstrip("_repeat") != str(axis_id_1).rstrip("_repeat"):
                            warnings.warn(f"No edges exist between axes {axis_id_1} -> {axis_id_2}."
                                          "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                                          "first.", stacklevel=2)
                        a1_to_a2 = False
                    elif len(list(self.edges[axis_id_1][axis_id_2].keys())) == 0:
                        warnings.warn(f"No edges exist between axes {axis_id_1} -> {axis_id_2}."
                                      "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                                      "first.", stacklevel=2)
                        a1_to_a2 = False

                    else:
                        a1_to_a2_tag = list(self.edges[axis_id_1][axis_id_2].keys())[0]

                        if len(list(self.edges[axis_id_1][axis_id_2].keys())) > 1:
                            a1_to_a2_failure = True
                else:
                    if str(axis_id_2).rstrip("_repeat") != str(axis_id_1).rstrip("_repeat"):
                        warnings.warn(f"No edges exist between axes {axis_id_1} -> {axis_id_2}."
                                      "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                                      "first.", stacklevel=2)
                    a1_to_a2 = False

            if a2_to_a1:
                if axis_id_2 in self.edges.keys():
                    if axis_id_1 not in self.edges[axis_id_2].keys():
                        # special handling for the "_repeat" axis
                        #  we check and warn with respect to repeat axes above
                        if str(axis_id_2).rstrip("_repeat") != str(axis_id_1).rstrip("_repeat"):
                            warnings.warn(f"No edges exist between axes {axis_id_2} -> {axis_id_1}."
                                          "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                                          "first.", stacklevel=2)
                        a2_to_a1 = False
                    elif len(list(self.edges[axis_id_2][axis_id_1].keys())) == 0:
                        warnings.warn(f"No edges exist between axes {axis_id_2} -> {axis_id_1}."
                                      "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                                      "first.", stacklevel=2)
                        a2_to_a1 = False

                    else:
                        a2_to_a1_tag = list(self.edges[axis_id_2][axis_id_1].keys())[0]

                        if len(list(self.edges[axis_id_2][axis_id_1].keys())) > 1:
                            a2_to_a1_failure = True
                else:
                    if str(axis_id_2).rstrip("_repeat") != str(axis_id_1).rstrip("_repeat"):
                        warnings.warn(f"No edges exist between axes {axis_id_2} -> {axis_id_1}."
                                      "Be sure to run `HivePlot.connect_axes()` or  `HivePlot.add_edge_ids()` "
                                      "first.", stacklevel=2)
                    a2_to_a1 = False

            if a1_to_a2_failure and a2_to_a1_failure:
                raise ValueError("Must specify precise `tag` to handle both `a1_to_a2=True` and `a2_to_a1=True` here. "
                                 "The current tags for the specified axes are:\n"
                                 f"{axis_id_2} -> {axis_id_1}: {list(self.edges[axis_id_2][axis_id_1].keys())}\n"
                                 f"{axis_id_2} -> {axis_id_1}: {list(self.edges[axis_id_2][axis_id_1].keys())}")
            elif a1_to_a2_failure:
                raise ValueError("Must specify precise `tag` to handle `a1_to_a2=True` here. "
                                 "The current tags for the specified axes are:\n"
                                 f"{axis_id_1} -> {axis_id_2}: {list(self.edges[axis_id_1][axis_id_2].keys())}")
            elif a2_to_a1_failure:
                raise ValueError("Must specify precise `tag` to handle `a2_to_a1=True` here. "
                                 "The current tags for the specified axes are:\n"
                                 f"{axis_id_2} -> {axis_id_1}: {list(self.edges[axis_id_2][axis_id_1].keys())}")

        else:
            a1_to_a2_tag = tag
            a2_to_a1_tag = tag

        axes = []
        tags = []
        if a1_to_a2:
            try:
                if "ids" in self.edges[axis_id_1][axis_id_2][a1_to_a2_tag]:
                    axes.append([axis_id_1, axis_id_2])
                    tags.append(a1_to_a2_tag)
            except KeyError:
                raise KeyError(
                    f"`self.edges[{axis_id_1}][{axis_id_2}][{a1_to_a2_tag}]['ids']` does not appear to exist. "
                    "It is expected you have run `HivePlot.connect_axes()` or `HivePlot.add_edge_ids()` first "
                    "for the two axes of interest with a specified tag."
                )
        if a2_to_a1:
            try:
                if "ids" in self.edges[axis_id_2][axis_id_1][a2_to_a1_tag]:
                    axes.append([axis_id_2, axis_id_1])
                    tags.append(a2_to_a1_tag)
            except KeyError:
                raise KeyError(
                    f"`self.edges[{axis_id_2}][{axis_id_1}][{a2_to_a1_tag}]['ids']` does not appear to exist. "
                    "It is expected you have run `HivePlot.connect_axes()` or `HivePlot.add_edge_ids()` first "
                    "for the two axes of interest with a specified tag."
                )
        # store the kwargs
        for [a1, a2], t in zip(axes, tags):
            # being sure to include existing kwargs
            if "edge_kwargs" in self.edges[a1][a2][t].keys():
                for k in list(self.edges[a1][a2][t]["edge_kwargs"]):
                    if k not in edge_kwargs.keys():
                        edge_kwargs[k] = self.edges[a1][a2][t]["edge_kwargs"][k]

            self.edges[a1][a2][t]["edge_kwargs"] = edge_kwargs

        return None

    def connect_axes(self, edges: np.ndarray, axis_id_1: Hashable, axis_id_2: Hashable, tag: Hashable or None = None,
                     a1_to_a2: bool = True, a2_to_a1: bool = True,
                     num_steps: int = 100, short_arc: bool = True, **edge_kwargs) -> Hashable:
        """
        Construct all the curves and set all the curve kwargs between ``axis_id_1`` and ``axis_id_2``.

        Based on the specified ``edges`` parameter, build out the resulting Bézier curves, and set any kwargs for those
        edges for later visualization.

        The curves will be tracked by a unique ``tag``, and the resulting constructions will be stored in
        ``HivePlot.edges[axis_id_1][axis_id_2][tag]`` if ``a1_to_a2`` is ``True`` and
        ``HivePlot.edges[axis_id_2][axis_id_1][tag]`` if ``a2_to_a1`` is ``True``.

        .. note::
            If trying to draw different subsets of edges with different kwargs, one can run this method multiple times
            with different subsets of the entire edges array, providing unique ``tag`` values with each subset of
            ``edges``, and specifying different ``edge_kwargs`` each time. The resulting ``HivePlot`` instance would be
            plotted showing each set of edges styled with each set of unique kwargs.

        .. note::
            You can choose to construct edges in only one of either directions by specifying `a1_to_a2` or `a2_to_a1`
            as False (both are True by default).

        :param edges: ``(n, 2)`` array of ``Hashable`` values representing pointers to specific ``Node`` instances.
            The first column is the "from" and the second column is the "to" for each connection.
        :param axis_id_1: Hashable pointer to the first ``Axis`` instance in ``HivePlot.axes`` we want to find
            connections between.
        :param axis_id_2: Hashable pointer to the second ``Axis`` instance in ``HivePlot.axes`` we want to find
            connections between.
        :param tag: tag corresponding to specified ``edges``. If ``None`` is provided, the tag will be set as
            the lowest unused integer starting at ``0`` amongst the available tags under
            ``HivePlot.edges[from_axis_id][to_axis_id]`` and / or ``HivePlot.edges[to_axis_id][from_axis_id]``.
        :param a1_to_a2: whether to find and build the connections going FROM ``axis_id_1`` TO ``axis_id_2``.
        :param a2_to_a1: whether to find and build the connections going FROM ``axis_id_2`` TO ``axis_id_1``.
        :param num_steps: number of points sampled along a given Bézier curve. Larger numbers will result in
            smoother curves when plotting later, but slower rendering.
        :param short_arc: whether to take the shorter angle arc (``True``) or longer angle arc (``False``).
            There are always two ways to traverse between axes: with one angle being x, the other option being 360 - x.
            For most visualizations, the user should expect to traverse the "short arc," hence the default ``True``.
            For full user flexibility, however, we offer the ability to force the arc the other direction, the
            "long arc" (``short_arc=False``). Note: in the case of 2 axes 180 degrees apart, there is no "wrong" angle,
            so in this case an initial decision will be made, but switching this boolean will switch the arc to the
            other hemisphere.
        :param edge_kwargs: additional ``matplotlib`` params that will be applied to the related edges.
        :return: ``Hashable`` tag that identifies the generated curves and kwargs.
        """
        # if `tag` is `None`, will be relevant to store the new tag, otherwise `new_tag` will just be the same as `tag`
        new_tag = self.add_edge_ids(edges=edges, tag=tag, axis_id_1=axis_id_1, axis_id_2=axis_id_2,
                                    a1_to_a2=a1_to_a2, a2_to_a1=a2_to_a1)

        self.add_edge_curves_between_axes(axis_id_1=axis_id_1, axis_id_2=axis_id_2, tag=new_tag,
                                          a1_to_a2=a1_to_a2, a2_to_a1=a2_to_a1,
                                          num_steps=num_steps, short_arc=short_arc)

        self.add_edge_kwargs(axis_id_1=axis_id_1, axis_id_2=axis_id_2, tag=new_tag,
                             a1_to_a2=a1_to_a2, a2_to_a1=a2_to_a1, **edge_kwargs)

        return new_tag

    def copy(self) -> "HivePlot":
        """
        Return a copy of the ``HivePlot`` instance.

        :return: ``HivePlot`` instance.
        """
        return deepcopy(self)

    def to_json(self) -> str:
        """
        Return the information from the axes, nodes, and edges in Cartesian space as JSON.

        This allows users to visualize hive plots with arbitrary libraries, even outside of python.

        The dictionary structure of the resulting JSON will consist of two top-level keys:

        "axes" - contains the information for plotting each axis, plus the nodes on each axis in Cartesian space.

        "edges" - contains the information for plotting the discretized edges in Cartesian space, plus the corresponding
        *to* and *from* IDs that go with each edge, as well as any kwargs that were set for plotting each set of edges.

        :return: JSON output of axis, node, and edge information.
        """
        # axis endpoints and node placements (both in Cartesian space).
        axis_node_dict = dict()

        for axis in self.axes:
            # endpoints of axis in Cartesian space
            start, end = self.axes[axis].start, self.axes[axis].end

            temp_dict = dict(start=start, end=end,
                             nodes=self.axes[axis].node_placements.loc[:, ["unique_id", "x", "y"]]
                             .to_dict(orient="list")
                             )
            axis_node_dict[axis] = temp_dict

        edge_info = deepcopy(self.edges)

        # edge ids, discretized curves (in Cartesian space), and kwargs
        for e1 in edge_info:
            for e2 in edge_info[e1]:
                for tag in edge_info[e1][e2]:
                    for i in ["ids", "curves"]:
                        # curves have nan values, must revise to `None` then coax to list
                        if i == "curves":
                            arr = edge_info[e1][e2][tag][i]
                            temp = arr.astype("O")
                            temp[np.where(np.isnan(arr))] = None
                            edge_info[e1][e2][tag][i] = temp.tolist()
                        # ids don't have nan values, can be converted to list right away
                        elif i == "ids":
                            edge_info[e1][e2][tag][i] = edge_info[e1][e2][tag][i].tolist()

        collated_output = dict(axes=axis_node_dict,
                               edges=edge_info)

        return json.dumps(collated_output)


def hive_plot_n_axes(node_list: List, edges: np.ndarray or list, axes_assignments: List,
                     sorting_variables: List, axes_names: List or None = None,
                     repeat_axes: List or None = None,
                     vmins: List or None = None, vmaxes: List or None = None,
                     angle_between_repeat_axes: float = 40, orient_angle: float = 0,
                     all_edge_kwargs: dict or None = None, edge_list_kwargs: list or None = None,
                     cw_edge_kwargs: dict or None = None, ccw_edge_kwargs: dict or None = None,
                     repeat_edge_kwargs: dict or None = None) -> HivePlot:
    """
    Generate a ``HivePlot`` Instance with an arbitrary number of axes, as specified by passing a partition of node IDs.

    Repeat axes can be generated for any desired subset of axes, but repeat axes will be sorted by the same variable
    as the original axis.

    Axes will be added in counterclockwise order.

    Axes will all be the same length and position from the origin.

    Changes to all the edge kwargs can be affected with the ``all_edge_kwargs`` parameter. If providing multiple sets
    of edges (e.g. a ``list`` input for the ``edges`` parameter), one can also provide unique kwargs for each set of
    edges by specifying a corresponding ``list`` of kwargs with the ``edge_list_kwargs`` parameter.

    Edges directed counterclockwise will be drawn as solid lines by default. Clockwise edges will be drawn as solid
    lines by default. All CW / CCW lines kwargs can be changed with the ``cw_edge_kwargs`` and ``ccw_edge_kwargs``
    parameters, respectively. Edges between repeat axes will be drawn as solid lines by default. Repeat edges operate
    under their own set of visual kwargs (``repeat_edge_kwargs``) as clockwise vs counterclockwise edges don't have much
    meaning when looking within a single group.

    Specific edge kwargs can also be changed by running the ``add_edge_kwargs()`` method on the resulting ``HivePlot``
    instance, where the specified ``tag`` of ``edges`` to change will be the index value in the list of
    lists in ``edges`` (note: a tag is only necessary if the ``indices`` input is a list of lists, otherwise there
    would only be a single tag of edges, which can be inferred).

    There is a hierarchy to these various kwarg arguments. That is, if redundant / overlapping kwargs are provided for
    different kwarg parameters, a warning will be raised and priority will be given according to the below hierarchy
    (Note: ``cw_edge_kwargs, ``ccw_edge_kwargs``, and ``repeat_edge_kwargs`` do not interact with each other in
    practice, and are therefore equal in the hierarchy):

    ``edge_list_kwargs`` > ``cw_edge_kwargs`` / ``ccw_edge_kwargs`` / ``repeat_edge_kwargs`` > ``all_edge_kwargs``.

    :param node_list: List of ``Node`` instances to go into output ``HivePlot`` instance.
    :param edges: ``(n, 2)`` array of ``Hashable`` values representing pointers to specific ``Node`` instances.
        The first column is the "from" and the second column is the "to" for each connection.
        Alternatively, one can provide a list of two-column arrays, which will allow for plotting different sets of
        edges with different kwargs.
    :param axes_assignments: list of lists of node unique IDs. Each list of nodes will be assigned to a separate axis in
        the resulting ``HivePlot`` instance, built out in counterclockwise order.
    :param sorting_variables: list of ``Hashable`` variables on which to sort each axis, where the ith index
        ``Hashable`` corresponds to the ith index list of nodes in ``axes_assignments`` (e.g. the ith axis of the
        resulting ``HivePlot``).
    :param axes_names: list of ``Hashable`` names for each axis, where the ith index ``Hashable`` corresponds to the ith
        index list of nodes in ``axes_assignments`` (e.g. the ith axis of the resulting ``HivePlot``). Default ``None``
        names the groups as "Group 1," "Group 2," etc.
    :param repeat_axes: list of ``bool`` values of whether to generate a repeat axis, where the ith index bool
        corresponds to the ith index list of nodes in ``axes_assignments`` (e.g. the ith axis of the resulting
        ``HivePlot``). A ``True`` value generates a repeat axis. Default ``None`` assumes no repeat axes (e.g. all
        ``False``).
    :param vmins: list of ``float`` values (or ``None`` values) specifying the vmin for each axis, where the ith index
        value corresponds to the ith index list of nodes in ``axes_assignments`` (e.g. the ith axis of the resulting
        ``HivePlot``). A ``None`` value infers the global min for that axis. Default ``None`` uses the global min for
        all the axes.
    :param vmaxes: list of ``float`` values (or ``None`` values) specifying the vmax for each axis, where the ith index
        value corresponds to the ith index list of nodes in ``axes_assignments`` (e.g. the ith axis of the resulting
        ``HivePlot``). A ``None`` value infers the global max for that axis. Default ``None`` uses the global max for
        all the axes.
    :param angle_between_repeat_axes: angle between repeat axes. Default 40 degrees.
    :param orient_angle: rotates all axes counterclockwise from their initial angles (default 0 degrees).
    :param all_edge_kwargs: kwargs for all edges. Default ``None`` specifies no additional kwargs.
    :param edge_list_kwargs: list of dictionaries of kwargs for each element of ``edges`` when ``edges`` is a ``list``.
        The ith set of kwargs in ``edge_list_kwargs`` will only be applied to edges constructed from the ith element of
        ``edges``. Default ``None`` provides no additional kwargs. Note, list must be same length as ``edges``.
    :param cw_edge_kwargs: kwargs for edges going clockwise. Default ``None`` specifies a solid line.
    :param ccw_edge_kwargs: kwargs for edges going counterclockwise. Default ``None`` specifies a solid line.
    :param repeat_edge_kwargs: kwargs for edges between repeat axes. Default ``None`` specifies a solid line.
    :return: ``HivePlot`` instance.
    """
    # make sure kwarg arguments are correct
    if all_edge_kwargs is None:
        all_edge_kwargs = dict()

    if type(edges) == list:
        if edge_list_kwargs is not None:
            assert len(edges) == len(edge_list_kwargs), \
                f"Must provide same number of sets of edges (currently len(edges) = {len(edges)}) as edge kwargs" + \
                f"(currently len(edge_list_kwargs) = {len(edge_list_kwargs)}"
            for idx, k in enumerate(edge_list_kwargs):
                if k is None:
                    edge_list_kwargs[idx] = dict()
        else:
            edge_list_kwargs = [dict() for _ in edges]
    else:
        edge_list_kwargs = [dict()]

    if cw_edge_kwargs is None:
        cw_edge_kwargs = dict()
    if ccw_edge_kwargs is None:
        ccw_edge_kwargs = dict()
    if repeat_edge_kwargs is None:
        repeat_edge_kwargs = dict()
    # make sure specified instructions match the number of specified axes
    assert len(axes_assignments) == len(sorting_variables), \
        "Must specify a sorting variable (`sorting_variables`) for every axis (`axes_assignments`). " + \
        f"Currently have {len(sorting_variables)} sorting variables and {len(axes_assignments)} axes assignments."

    if axes_names is not None:
        assert len(axes_assignments) == len(axes_names), \
            "Must specify a axis name (`axes_names`) for every axis (`axes_assignments`). " + \
            f"Currently have {len(axes_names)} axes names and {len(axes_assignments)} axes assignments."

    else:
        axes_names = [f"Group {i + 1}" for i in range(len(axes_assignments))]

    if repeat_axes is not None:
        assert len(axes_assignments) == len(repeat_axes), \
            "Must specify a repeat axis (`repeat_axes`) for every axis (`axes_assignments`). " + \
            f"Currently have {len(repeat_axes)} repeat axes specified and {len(axes_assignments)} axes assignments."
    else:
        repeat_axes = [False] * len(axes_assignments)

    if vmins is not None:
        assert len(axes_assignments) == len(vmins), \
            "Must specify a vmin (`vmins`) for every axis (`axes_assignments`). " + \
            f"Currently have {len(vmins)} vmins specified and {len(axes_assignments)} axes assignments."
    else:
        vmins = [None] * len(axes_assignments)

    if vmaxes is not None:
        assert len(axes_assignments) == len(vmaxes), \
            "Must specify a vmax (`vmaxes`) for every axis (`axes_assignments`). " + \
            f"Currently have {len(vmaxes)} vmaxes specified and {len(axes_assignments)} axes assignments."
    else:
        vmaxes = [None] * len(axes_assignments)

    hp = HivePlot()
    hp.add_nodes(nodes=node_list)

    # space out axes evenly
    spacing = 360 / len(axes_assignments)

    if spacing <= angle_between_repeat_axes:
        warnings.warn(
            f"Your angle between repeat axes ({angle_between_repeat_axes}) is going to cause repeat axes to cross "
            "past other axes, which will lead to overlapping edges in the final Hive Plot visualization. "
            f"To space out axes equally, they are {spacing} degrees apart. "
            "We recommend setting a lower value for `angle_between_repeat_axes`.",
            stacklevel=2
        )

    for i, assignment in enumerate(axes_assignments):
        angle = spacing * i
        sorting_variable = sorting_variables[i]
        axis_name = axes_names[i]
        repeat_axis = repeat_axes[i]
        vmin = vmins[i]
        vmax = vmaxes[i]

        # add axis / axes
        if not repeat_axis:
            temp_axis = Axis(axis_id=axis_name, start=1, end=5, angle=angle + orient_angle)
            hp.add_axes([temp_axis])
        else:
            # space out on either side of the well-spaced angle
            temp_axis = Axis(axis_id=axis_name, start=1, end=5,
                             angle=angle - angle_between_repeat_axes / 2 + orient_angle)
            temp_axis_repeat = Axis(axis_id=f"{axis_name}_repeat", start=1, end=5,
                                    angle=angle + angle_between_repeat_axes / 2 + orient_angle,
                                    long_name=axis_name)
            hp.add_axes([temp_axis, temp_axis_repeat])

        # place nodes on the axis / axes
        hp.place_nodes_on_axis(axis_id=axis_name, unique_ids=assignment,
                               sorting_feature_to_use=sorting_variable, vmin=vmin, vmax=vmax)
        # also place values on the repeat axis if we have one
        if repeat_axis:
            hp.place_nodes_on_axis(axis_id=f"{axis_name}_repeat", unique_ids=assignment,
                                   sorting_feature_to_use=sorting_variable, vmin=vmin, vmax=vmax)

    # add in edges
    if type(edges) != list:
        edges = [edges]
    for i, axis_name in enumerate(axes_names):

        first_axis_name = axis_name

        # figure out next axis to connect to
        if i != len(axes_names) - 1:
            next_axis_name = axes_names[i + 1]
        # circle back to first axis
        else:
            next_axis_name = axes_names[0]

        # repeat axis kwarg handling and connecting
        if repeat_axes[i]:
            for idx, e in enumerate(edges):
                # gather kwargs according to hierarchy
                collated_kwargs = edge_list_kwargs[idx].copy()
                for k in list(repeat_edge_kwargs.keys()):
                    if k in collated_kwargs.keys():
                        warnings.warn(
                            f"Specified kwarg {k} in `repeat_edge_kwargs` but already set as kwarg for "
                            f"edge set index {idx} with `edge_list_kwargs`. Preserving kwargs in `edge_list_kwargs`",
                            stacklevel=2
                        )
                    else:
                        collated_kwargs[k] = repeat_edge_kwargs[k]
                for k in list(all_edge_kwargs.keys()):
                    if k in collated_kwargs.keys():
                        warnings.warn(
                            f"Specified kwarg {k} in `all_edge_kwargs` but already set as kwarg for "
                            f"edge set index {idx} with `edge_list_kwargs` or `repeat_edge_kwargs`. "
                            f"Disregarding `all_edge_kwargs` here.",
                            stacklevel=2
                        )
                    else:
                        collated_kwargs[k] = all_edge_kwargs[k]

                # add repeat axis edges (only in ccw direction) if we have a repeat axis
                hp.connect_axes(edges=e, axis_id_1=first_axis_name, axis_id_2=f"{first_axis_name}_repeat",
                                a2_to_a1=False, **collated_kwargs)
                # the following intergroup edges will instead come off of the repeat edge
            first_axis_name += "_repeat"

        for idx, e in enumerate(edges):
            # gather kwargs according to hierarchy
            collated_kwargs_cw = edge_list_kwargs[idx].copy()
            for k in list(cw_edge_kwargs.keys()):
                if k in collated_kwargs_cw.keys():
                    warnings.warn(
                        f"Specified kwarg {k} in `cw_edge_kwargs` but already set as kwarg for "
                        f"edge set index {idx} with `edge_list_kwargs`. Preserving kwargs in `edge_list_kwargs`",
                        stacklevel=2
                    )
                else:
                    collated_kwargs_cw[k] = cw_edge_kwargs[k]
            for k in list(all_edge_kwargs.keys()):
                if k in collated_kwargs_cw.keys():
                    warnings.warn(
                        f"Specified kwarg {k} in `all_edge_kwargs` but already set as kwarg for "
                        f"edge set index {idx} with `edge_list_kwargs` or `cw_edge_kwargs`. "
                        f"Disregarding `all_edge_kwargs` here.",
                        stacklevel=2
                    )
                else:
                    collated_kwargs_cw[k] = all_edge_kwargs[k]

            hp.connect_axes(edges=e, axis_id_1=first_axis_name, axis_id_2=next_axis_name,
                            a1_to_a2=False, **collated_kwargs_cw)

            # gather kwargs according to hierarchy
            collated_kwargs_ccw = edge_list_kwargs[idx].copy()
            for k in list(ccw_edge_kwargs.keys()):
                if k in collated_kwargs_ccw.keys():
                    warnings.warn(
                        f"Specified kwarg {k} in `ccw_edge_kwargs` but already set as kwarg for "
                        f"edge set index {idx} with `edge_list_kwargs`. Preserving kwargs in `edge_list_kwargs`",
                        stacklevel=2
                    )
                else:
                    collated_kwargs_ccw[k] = ccw_edge_kwargs[k]
            for k in list(all_edge_kwargs.keys()):
                if k in collated_kwargs_ccw.keys():
                    warnings.warn(
                        f"Specified kwarg {k} in `all_edge_kwargs` but already set as kwarg for "
                        f"edge set index {idx} with `edge_list_kwargs` or `ccw_edge_kwargs."
                        f"Disregarding `all_edge_kwargs` here.",
                        stacklevel=2
                    )
                else:
                    collated_kwargs_ccw[k] = all_edge_kwargs[k]

            hp.connect_axes(edges=e, axis_id_1=first_axis_name, axis_id_2=next_axis_name,
                            a2_to_a1=False, **collated_kwargs_ccw)

    return hp


class P2CP:
    """
    Polar Parallel Coordinates Plots (P2CPs).

    Conceptually similar to Hive Plots, P2CPs can be used for any multivariate
    data as opposed to solely for network visualizations. Features of the data are placed on their own axes in the same
    polar setup as Hive Plots, resulting in each representation of a complete data point being a *loop* in the resulting
    figure. For more on the nuances of P2CPs, see `Koplik and Valente, 2021 <https://arxiv.org/abs/2109.10193>`_.
    """

    def __init__(self, data: pd.DataFrame or None = None):
        """
        Initialize P2CP instance.
        """
        # backend tracking of node ids (1d np.ndarray)
        self._node_ids = np.array([])

        # backend ``Node`` instances (list)
        self._nodes = []

        # track the data the user has added
        if data is not None:
            self.set_data(data=data)
        else:
            self.data = None

        # track what axes the user has chosen along with specified vmin and vmax values
        # (e.g. each `self.axes['column_id']` has keys "axis", "vmin", and "vmax")
        self.axes = dict()

        # also track a list, from which will connect the ith to the i+1st axes (plus the last to the first)
        self.axes_list = []

        # backend ``HivePlot`` instance
        self._hiveplot = HivePlot()

        # track tags
        self.tags = []

    def __build_underlying_node_instances(self):
        """
        Build the underlying ``Node`` instances which will become the loops in the eventual P2CP to be visualized.

        .. note::
            This is a hidden method because everything relating to the underlying `HivePlot` instance is unnecessary /
            unintuitive to the user generating P2CPs.

        :return: ``None``.
        """
        node_ids = self.data.index.values
        node_data = self.data.to_dict(orient="records")
        nodes = [Node(unique_id=node_id, data=node_dat)
                 for node_id, node_dat in zip(node_ids, node_data)]

        self._node_ids = node_ids
        self._nodes = nodes

        return None

    def set_data(self, data: pd.DataFrame):
        """
        Add a dataset to the ``P2CP`` instance.

        All P2CP construction will be based on this dataset, which will be stored as ``P2CP.data``.

        :param data: dataframe to add.
        :return: ``None``.
        """
        assert type(data) == pd.DataFrame, \
            "`data` must be pandas DataFrame."

        self.data = data

        # also build the ``Node`` instances we'll need for underlying ``HivePlot`` calls later
        self.__build_underlying_node_instances()

        return None

    def __build_underlying_hiveplot_instance(self):
        """
        Build the underlying ``HivePlot`` instance which will become the eventual P2CP to be visualized.

        .. note::
            This is a hidden method because everything relating to the underlying `HivePlot` instance is unnecessary /
            unintuitive to the user generating P2CPs.

        :return: ``None``.
        """
        hp = HivePlot()
        hp.add_nodes(self._nodes)
        axes = [self.axes[k]["axis"] for k in self.axes.keys()]
        hp.add_axes(axes)
        for axis_id in hp.axes.keys():
            # make sure to *sort* on axes without any "\nrepeat" in there for the repeat axes' names
            sorting_variable = axis_id.split("\nRepeat")[0]
            # put *all* the nodes on each axis
            hp.place_nodes_on_axis(axis_id=axis_id, unique_ids=self._node_ids,
                                   sorting_feature_to_use=sorting_variable,
                                   vmin=self.axes[axis_id]["vmin"],
                                   vmax=self.axes[axis_id]["vmax"])
        self._hiveplot = hp

        return None

    def set_axes(self, columns: List or np.ndarray, angles: List or None = None,
                 vmins: List or None = None, vmaxes: List or None = None,
                 axis_kwargs: List or None = None,
                 overwrite_previously_set_axes: bool = True, start_angle: float = 0):
        r"""
        Set the axes that will be used in the eventual P2CP visualization.

        :param columns: column names from ``P2CP.data`` to use. Note, these need not be unique, as repeat axes may be
            desired. By default, repeat column names will be internally renamed to name + ``"\nRepeat"``.
        :param angles: corresponding angles (in degrees) to set for each desired axis. Default ``None`` sets the angles
            evenly spaced over 360 degrees, starting at ``start_angle`` degrees for the first axis and moving
            counterclockwise.
        :param vmins: list of ``float`` values (or ``None`` values) specifying the vmin for each axis, where the ith
            index value corresponds to the ith axis set by ``columns``. A ``None`` value infers the global min for that
            axis. Default ``None`` uses the global min for all axes.
        :param vmaxes: list of ``float`` values (or ``None`` values) specifying the vmax for each axis, where the ith
            index value corresponds to the ith axis set by ``columns``. A ``None`` value infers the global max for that
            axis. Default ``None`` uses the global max for all axes.
        :param axis_kwargs: list of dictionaries of additional kwargs that will be used for the underlying ``Axis``
            instances that will be created for each column. Only relevant if you want to change the positioning / length
            of an axis with the ``start`` and ``end`` parameters. For more on these kwargs, see the documentation for
            ``hiveplotlib.Axis``. Note, if you want to add these kwargs for only a subset of the desired axes, you can
            skip adding kwargs for specific columns by putting a ``None`` at those indices in your ``axis_kwargs``
            input.
        :param overwrite_previously_set_axes: Whether to overwrite any previously decided axes. Default ``True``
            overwrites any existing axes.
        :param start_angle: if ``angles`` is ``None``, sets the starting angle from which we place the axes around the
            origin counterclockwise.
        :return: ``None``.
        """
        num_columns = np.array(columns).size

        for c in columns:
            assert c in self.data.columns, \
                f"Column {c} not in `P2CP.data`, cannot set axis as non-existent variable."

        if angles is not None:
            assert num_columns == np.array(angles).size, \
                "`columns` and `angles` not the same size."
        # build out evenly-spaced `angles` if not provided
        else:
            spacing = 360 / num_columns
            angles = np.arange(start_angle, start_angle + num_columns * spacing, spacing)
            # make sure we're still in [0, 360)
            angles = np.mod(angles, 360)

        if vmins is None:
            vmins = [None] * num_columns
        else:
            assert np.array(vmins).size == num_columns, \
                "`vmins` and `columns` not the same size."

        if vmaxes is None:
            vmaxes = [None] * num_columns
        else:
            assert np.array(vmaxes).size == num_columns, \
                "`vmaxes` and `columns` not the same size."

        if axis_kwargs is None:
            axis_kwargs = [dict()] * num_columns
        else:
            assert np.array(axis_kwargs).size == num_columns, \
                "`axis_kwargs` and `columns` not the same size."
            # turn any `None values to empty dicts
            for i, kw in enumerate(axis_kwargs):
                if kw is None:
                    axis_kwargs[i] = dict()

        # overwrite previously set axes
        if overwrite_previously_set_axes:
            self.axes = dict()
            self.axes_list = []

        for c, a, kw, vmin, vmax in zip(columns, angles, axis_kwargs, vmins, vmaxes):
            if c in self.axes.keys():
                c += "\nRepeat"
            self.axes[c] = dict()
            self.axes[c]["axis"] = Axis(axis_id=c, angle=a, **kw)
            self.axes[c]["vmin"] = vmin
            self.axes[c]["vmax"] = vmax

            self.axes_list.append(c)

        # rebuild the underlying ``HivePlot`` instance
        self.__build_underlying_hiveplot_instance()

        # all edges get scrapped, so no tags remain
        self.tags = []

        return None

    def build_edges(self, indices: List or np.ndarray or str = "all", tag: Hashable or None = None,
                    num_steps: int = 100, **edge_kwargs) -> Hashable:
        """
        Construct the loops of the P2CP for the specified subset of ``indices``.

        These index values correspond to the indices of the ``pandas`` dataframe ``P2CP.data``.

        .. note::
            Specifying ``indices="all"`` draws the curves for the entire dataframe.

        :param indices: which indices of the underlying dataframe to draw on the P2CP. Note, "all" draws the entire
            dataframe.
        :param tag: tag corresponding to specified indices. If ``None`` is provided, the tag will be set as the lowest
            unused integer starting at 0 amongst the tags.
        :param num_steps: number of points sampled along a given Bézier curve. Larger numbers will result in smoother
            curves when plotting later, but slower rendering.
        :param edge_kwargs: additional ``matplotlib`` keyword arguments that will be applied to edges constructed for
            the referenced indices.
        :return: the unique, ``Hashable`` tag used for the constructed edges.
        """
        # "edges" in P2CPs in the network context are to oneself
        if type(indices) == str and indices == "all":
            indices = self._node_ids

        if tag is None:
            # only need to find a unique tag if we've created edges already
            if len(list(self._hiveplot.edges.keys())) > 0:
                # same tags generated over all axes with P2CPs, just need to check over any pair
                tag = self._hiveplot._find_unique_tag(from_axis_id=self.axes_list[0],
                                                      to_axis_id=self.axes_list[1])
            else:
                tag = 0
        edges = np.c_[indices, indices]
        for i, _ in enumerate(self.axes_list):
            first_axis = i
            second_axis = (i + 1) % len(self.axes_list)
            self._hiveplot.connect_axes(edges=edges, tag=tag,
                                        axis_id_1=self.axes_list[first_axis], axis_id_2=self.axes_list[second_axis],
                                        a2_to_a1=False, num_steps=num_steps, **edge_kwargs)
        self.tags.append(tag)

        return tag

    def add_edge_kwargs(self, tag: Hashable or None = None, **edge_kwargs):
        """
        Add edge kwargs to a tag of Bézier curves previously constructed with ``P2CP.build_edges()``.

        For a given tag of curves for which edge kwargs were already set, any redundant edge kwargs specified by this
        method call will overwrite the previously set kwargs.

        .. note::
            Expected to have previously called ``P2CP.build_edges()`` before calling this method, for the tag of
            interest. However, if no tags were ever set (e.g. there's only 1 tag of curves), then no tag is necessary
            here.

        :param tag: which subset of curves to modify kwargs for. Note, if no tag is specified (e.g. ``tag=None``), it is
            presumed there is only one tag to look over and that will be inferred. If no tag is specified and there are
            multiple tags to choose from, a ``ValueError`` will be raised.
        :param edge_kwargs: additional ``matplotlib`` keyword arguments that will be applied to edges constructed for
            the referenced indices.
        :return: ``None``.
        """
        if tag is None:
            assert len(self.tags) == 1, \
                f"No `tag` specified but multiple tags exist for this `P2CP` instance ({self.tags}). Cannot infer " + \
                "which tag to modify, please specify one of the tags with the `tag` parameter."
            tag = self.tags[0]

        else:
            assert tag in self.tags, \
                "`tag` not in previously-generated tags, be sure to construct edges with `P2CP.build_edges()` first."

        for i, _ in enumerate(self.axes_list):
            first_axis = i
            second_axis = (i + 1) % len(self.axes_list)
            self._hiveplot.add_edge_kwargs(axis_id_1=self.axes_list[first_axis],
                                           axis_id_2=self.axes_list[second_axis],
                                           tag=tag, a2_to_a1=False, **edge_kwargs)

        return None

    def reset_edges(self, tag: Hashable or None = None):
        """
        Drop the constructed edges with the specified ``tag``.

        .. note::
            If no tags were ever set (e.g. there's
            only 1 tag of curves), then no tag is necessary here.

        :param tag: which subset of curves to delete. Note, if no tag is specified (e.g. ``tag=None``), then all curves
            will be deleted.
        :return: ``None``.
        """
        if tag is None:
            self._hiveplot.reset_edges()

        else:
            for i, _ in enumerate(self.axes_list):
                first_axis = i
                second_axis = (i + 1) % len(self.axes_list)
                self._hiveplot.reset_edges(axis_id_1=self.axes_list[first_axis],
                                           axis_id_2=self.axes_list[second_axis],
                                           tag=tag, a2_to_a1=False)

        return None

    def copy(self) -> "P2CP":
        """
        Return a copy of the ``P2CP`` instance.

        :return: ``P2CP`` instance.
        """
        return deepcopy(self)

    def to_json(self) -> str:
        """
        Return the information from the axes, point placement on each axis, and edges in Cartesian space as JSON.

        This allows users to visualize P2CPs with arbitrary libraries, even outside of python.

        The dictionary structure of the resulting JSON will consist of two top-level keys:

        "axes" - contains the information for plotting each axis, plus the points on each axis in Cartesian space.

        "edges" - contains the information for plotting the discretized edges in Cartesian space broken up by tag
        values, plus the corresponding unique IDs of points that go with each tag, as well as any kwargs that were set
        for plotting each set of points in a given tag.

        :return: JSON output of axis, point, and edge information.
        """
        # axis endpoints and node placements (both in Cartesian space).
        axis_node_dict = dict()

        for axis in self._hiveplot.axes:
            # endpoints of axis in Cartesian space
            start, end = self._hiveplot.axes[axis].start, self._hiveplot.axes[axis].end

            temp_dict = dict(start=start, end=end,
                             points=self._hiveplot.axes[axis].node_placements.loc[:, ["unique_id", "x", "y"]]
                             .to_dict(orient="list")
                             )
            axis_node_dict[axis] = temp_dict

        edge_info = deepcopy(self._hiveplot.edges)

        # edge ids, discretized curves (in Cartesian space), and kwargs
        new_dict = dict()
        # want to loop over the nested tags, not the axes like with hive plots
        #  (since every point in a tag is a complete loop)
        #  so let's just grab the first axis pair we can find and grab those tags, then loop over the tags instead
        temp_first_axis = list(edge_info.keys())[0]
        temp_second_axis = list(edge_info[temp_first_axis].keys())[0]

        for i, tag in enumerate(edge_info[temp_first_axis][temp_second_axis]):
            new_dict[tag] = dict()
            # ids and edge kwargs will be the same on every axis by construction of the P2CP
            # ids map to themselves in hive plot backend, so let's just store a single id for each
            new_dict[tag]["ids"] = [j[0] for j in edge_info[temp_first_axis][temp_second_axis][tag]["ids"].tolist()]
            new_dict[tag]["edge_kwargs"] = edge_info[temp_first_axis][temp_second_axis][tag]["edge_kwargs"]
            new_dict[tag]["curves"] = dict()
            for a0 in edge_info:
                new_dict[tag]["curves"][a0] = dict()
                for a1 in edge_info[a0]:
                    new_dict[tag]["curves"][a0][a1] = dict()
                    # curves have nan values, must revise to `None` then coax to list
                    arr = edge_info[a0][a1][tag]["curves"]
                    temp = arr.astype("O")
                    temp[np.where(np.isnan(arr))] = None
                    new_dict[tag]["curves"][a0][a1] = temp.tolist()

        collated_output = dict(axes=axis_node_dict,
                               edges=new_dict)

        return json.dumps(collated_output)


def p2cp_n_axes(data: pd.DataFrame,
                indices: List or str = "all", split_on: Hashable or List or None = None,
                axes: List or None = None,
                vmins: List or None = None, vmaxes: List or None = None,
                orient_angle: float = 0,
                all_edge_kwargs: dict or None = None, indices_list_kwargs: list or None = None) -> P2CP:
    """
    Generate a ``P2CP`` instance with an arbitrary number of axes for an arbitrary dataframe.

    Can specify a desired subset of column names, each of which will become an axis in the resulting P2CP.
    Default grabs all columns in the dataframe, unless ``split_on`` is a column name, in which case that specified
    column will be excluded from the list of axes in the final ``P2CP`` instance. Note, repeat axes (e.g. repeated
    column names) are allowed here.

    Axes will be added in counterclockwise order. Axes will all be the same length and position from the origin.

    In deciding what edges of ``data`` get drawn (and how they get drawn), the user has several options. The default
    behavior plots all data points in ``data`` with the same keyword arguments. If one instead wanted to plot a subset
    of data points, one can provide a ``list`` of a subset of indices from the dataframe to the ``indices`` parameter.

    If one wants to plot multiple *sets* of edges in different styles, there are two means of doing this. The more
    automated means is to split on the unique values of a column in the provided ``data``. By specifying
    a column name to the ``split_on`` parameter, data will be added in chunks according to the unique values of the
    specified column. If one instead includes a list of values corresponding to the records in ``data``, data will
    be added according to the unique values of this provided list.
    Each subset of ``data`` corresponding to a unique column value will be given a separate tag, with the
    tag being the unique column value. Note, however, this only works when ``indices="all"``. If one prefers to split
    indices manually, one can instead provide a list of lists to the ``indices`` parameter, allowing for arbitrary
    splitting of the data. Regardless of how one chooses to split the data, one can then assign different keyword
    arguments to each subset of data.

    Changes to all the edge kwargs can be affected with the ``all_edge_kwargs`` parameter. If providing multiple sets
    of edges though in one of the ways discussed above, one can also provide unique kwargs for each set
    of edges by specifying a corresponding ``list`` of dictionaries of kwargs with the ``indices_list_kwargs``
    parameter.

    Specific edge kwargs can also be changed later by running the ``add_edge_kwargs()`` method on the returned ``P2CP``
    instance. If one only added a single set of indices (e.g. ``indices="all"`` or ``indices`` was provided as a flat
    list of index values), then this method can simply be called with kwargs. However, if multiple subsets of edges were
    specified, then one will need to be precise about which ``tag`` of edge kwargs to change. If multiple sets were
    provided via the ``indices`` parameter, then the resulting ``tag`` for each subset will correspond to the index
    value in the list of lists in ``indices``. If instead ``split_on_column`` was specified as not ``None``, then tags
    will be the unique values in the specified column / list of values. Regardless of splitting methodology, existing
    tags can be found under the returned ``P2CP.tags``.

    There is a hierarchy to these kwarg arguments. That is, if redundant / overlapping kwargs are provided for
    different kwarg parameters, a warning will be raised and priority will be given according to the below hierarchy:

    ``indices_list_kwargs`` > ``all_edge_kwargs``.

    :param data: dataframe to add.
    :param indices: ``list`` of index values from the index of the added dataframe ``data``. Default "all" creates edges
        for every row in ``data``, but a ``list`` input creates edges for only the specified subset. Alternatively,
        one can provide a *list of lists* of indices, which will allow for plotting different sets of edges with
        different kwargs. These subsets will be added to the resulting ``P2CP`` instance with tags corresponding to
        the index value in ``indices``.
    :param split_on: column name from ``data`` or list of values corresponding to the records of ``data``.
        If specified as not ``None``, the resulting ``P2CP`` instance will split data according to unique values with
        respect to the column of ``data`` / the list of provided values, with each subset of data given a tag of the
        unique value corresponding to each subset. When specifying a column in ``data``, this column will be excluded
        from consideration if ``axes`` is ``None``. Note: this subsetting can only be run when ``indices="all"``.
        Default ``None`` plots all the records in ``data`` with the same line kwargs.
    :param axes: list of ``Hashable`` column names in ``data``. Each column name will be assigned to a separate axis in
        the resulting ``P2CP`` instance, built out in counterclockwise order. Default ``None`` grabs all columns in the
        dataframe, unless ``split_on`` is a column name, in which case that specified column will be excluded from
        the list of axes in the final ``P2CP`` instance. Note, repeat axes (e.g. repeated column names) are allowed
        here.
    :param vmins: list of ``float`` values (or ``None`` values) specifying the vmin for each axis, where the ith index
        value corresponds to the ith index axis in ``axes`` (e.g. the ith axis of the resulting ``P2CP``
        instance). A ``None`` value infers the global min for that axis. Default ``None`` uses the global min for
        all the axes.
    :param vmaxes: list of ``float`` values (or ``None`` values) specifying the vmax for each axis, where the ith index
        value corresponds to the ith index axis in ``axes`` (e.g. the ith axis of the resulting ``P2CP``
        instance). A ``None`` value infers the global max for that axis. Default ``None`` uses the global max for
        all the axes.
    :param orient_angle: rotates all axes counterclockwise from their initial angles (default 0 degrees).
    :param all_edge_kwargs: kwargs for all edges. Default ``None`` specifies no additional kwargs.
    :param indices_list_kwargs: list of dictionaries of kwargs for each element of ``indices`` when ``indices`` is a
        list of lists or ``split_on`` is not ``None``. The ith set of kwargs in ``indices_list_kwargs`` will only
        be applied to index values corresponding to the ith list in ``indices`` or to index values which have the ith
        unique value in a sorted list of unique values in ``split_on``. Default ``None`` provides no additional
        kwargs. Note, this list must be same length as ``indices`` or the same number of values as the number of unique
        values in ``split_on``.
    :return: ``P2CP`` instance.
    """
    # make sure kwarg arguments are correct
    if all_edge_kwargs is None:
        all_edge_kwargs = dict()

    # default assumption, we are not splitting on a column unless explicitly ruled in later
    split_on_column = False

    # check if we have list of lists input
    #  if every element is size one, it's just a list of indices
    if indices == "all":
        if split_on is not None:
            if type(split_on) == list or type(split_on) == np.ndarray:
                assert len(split_on) == data.shape[0], \
                    "If `split_on` is list-like, must have the same number of values as records in `data`"
                tags = sorted(list(np.unique(split_on)))
                indices = [list(np.where(split_on == t)[0]) for t in tags]
            else:
                split_on_column = True
                split_dict = indices_for_unique_values(df=data, column=split_on)
                tags = sorted(list(split_dict.keys()))
                indices = [list(split_dict[t]) for t in tags]
            if indices_list_kwargs is None:
                indices_list_kwargs = [dict() for _ in tags]
            else:
                assert len(indices) == len(indices_list_kwargs), \
                    "Must provide same number of sets of edges " + \
                    f"(currently unique splits specified by `split_on`={split_on} is " + \
                    f"{len(indices)}) as edge kwargs" + \
                    f"(currently len(indices_list_kwargs) = {len(indices_list_kwargs)}"
        else:
            tags = [None]
            indices = [data.index.values]
            if indices_list_kwargs is None:
                indices_list_kwargs = [dict()]
            assert len(indices_list_kwargs) == 1, \
                "Only 1 set of indices to plot, so can only accept one set of index kwargs"
    else:
        is_list_of_lists = [np.array(i).size for i in indices]
        is_list_of_lists = list(set(is_list_of_lists))
        if is_list_of_lists != [1]:
            assert split_on is None, \
                "You can only specify `split_on` when you are not providing list of lists inputs to `indices`."
            tags = [i for i, _ in enumerate(indices)]
            if indices_list_kwargs is not None:
                assert len(indices) == len(indices_list_kwargs), \
                    "Must provide same number of sets of edges " + \
                    f"(currently len(indices) = {len(indices)}) as edge kwargs" + \
                    f"(currently len(indices_list_kwargs) = {len(indices_list_kwargs)}"
                for idx, k in enumerate(indices_list_kwargs):
                    if k is None:
                        indices_list_kwargs[idx] = dict()
            else:
                indices_list_kwargs = [dict() for _ in indices]
        else:
            tags = [None]
            indices = [indices]
            indices_list_kwargs = [dict()]

    extra_warning_message = ""
    if axes is None:
        axes = data.columns.values
        # drop the splitting column if used
        if split_on_column:
            axes = np.delete(axes, np.where(axes == split_on))
            extra_warning_message += "\n(One axis was removed because it is already used by `split_on`)"

    if vmins is not None:
        assert len(axes) == len(vmins), \
            "Must specify a vmin (`vmins`) for every axis (`axes`). " + \
            f"Currently have {len(vmins)} vmins specified and {len(axes)} axes." + extra_warning_message

    if vmaxes is not None:
        assert len(axes) == len(vmaxes), \
            "Must specify a vmax (`vmaxes`) for every axis (`axes`). " + \
            f"Currently have {len(vmaxes)} vmaxes specified and {len(axes)} axes." + extra_warning_message

    p2cp = P2CP(data=data)
    p2cp.set_axes(columns=axes, angles=None,
                  vmins=vmins, vmaxes=vmaxes,
                  start_angle=orient_angle)

    for i, ind in enumerate(indices):
        # resolve kwarg priorities
        collated_kwargs = indices_list_kwargs[i].copy()
        for k in list(all_edge_kwargs.keys()):
            if k in collated_kwargs.keys():
                warnings.warn(
                    f"Specified kwarg {k} in `all_edge_kwargs` but already set as kwarg for "
                    f"indices list index {i} with `indices_list_kwargs`. "
                    f"Disregarding `all_edge_kwargs` here.",
                    stacklevel=2
                )
            else:
                collated_kwargs[k] = all_edge_kwargs[k]

        p2cp.build_edges(indices=ind, tag=tags[i], **collated_kwargs)

    return p2cp
