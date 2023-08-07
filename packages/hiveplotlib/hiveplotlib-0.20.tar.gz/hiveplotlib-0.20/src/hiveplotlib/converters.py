# Gary Koplik
# gary<dot>koplik<at>geomdata<dot>com
# December, 2021
# converters.py

"""
Converters from various data structures to ``hiveplotlib``-ready structures.
"""


from hiveplotlib import Node
import numpy as np
from typing import Tuple

# say the graph type instead of calling `nx.Graph` to keep networkx dep out of this file.
NetworkXGraph = "networkx.classes.graph.Graph instance"


def networkx_to_nodes_edges(graph: NetworkXGraph) -> Tuple[Node, np.ndarray]:
    """
    Take a ``networkx`` graph and return ``hiveplotlib``-friendly data structures.

    Specifically, returns a list of ``hiveplotlib.Node`` instances and an ``(n, 2)`` ``np.ndarray`` of
    edges. These outputs can be fed directly into :py:func:`~hiveplotlib.hive_plot_n_axes()`

    :param graph: ``networkx`` graph.
    :return: ``list`` of ``Node`` instances, ``(n, 2)`` ``np.ndarray`` of edges.
    """
    nodes = [Node(unique_id=i, data=data) for i, data in list(graph.nodes.data())]
    edges = np.array(graph.edges)
    return nodes, edges
