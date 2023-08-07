# Gary Koplik
# gary<dot>koplik<at>geomdata<dot>com
# December, 2021
# datasets.py

"""
Quick example datasets for use in ``hiveplotlib``.

For Hive Plots, many excellent network datasets are available online, including many graphs that can be generated using
`networkx <https://networkx.org/documentation/stable/reference/generators.html>`_ and
`pytorch-geometric <https://pytorch-geometric.readthedocs.io/en/latest/notes/data_cheatsheet.html#>`_.
The `Stanford Large Network Dataset Collection <https://snap.stanford.edu/data/>`_ is also a great general source of
network datasets. If working with ``networkx`` graphs,
users can also take advantage of the ``hiveplotlib.converters.networkx_to_nodes_edges()`` method to quickly get those
graphs into a ``hiveplotlib``-ready format.

For Polar Parallel Coordinates Plots (P2CPs), many datasets are available through packages including
`statsmodels <https://www.statsmodels.org/stable/datasets/index.html>`_ and
`scikit-learn <https://scikit-learn.org/stable/datasets.html>`_.
"""

import numpy as np
import pandas as pd


def four_gaussian_blobs_3d(num_points: int = 50, noise: float = 0.5,
                           random_seed: int = 0):
    """
    Generate a ``pandas`` dataframe of four Gaussian blobs in 3d.

    This dataset serves as a simple example for showing 3d viz using Polar Parallel Coordinates Plots (P2CPs) instead
    of 3d plotting.

    :param num_points: number of points in each blob.
    :param noise: noisiness of Gaussian blobs.
    :param random_seed: random seed to generate consistent data between calls.
    :return: ``(num_points * 4, 4)`` ``pd.DataFrame`` of X, Y, Z, and blob labels.
    """
    # dimension of data (e.g. 3 => 3d data)
    dim = 3

    # keeping a subset of the corner blobs to plot
    corners_to_keep = [0, 1, 2, 4]

    # name of the features we will create for each set of data generated below
    feature_names = ["X", "Y", "Z", "Label"]

    # set seed for consistent data
    rng = np.random.default_rng(random_seed)

    # build list of arrays of Gaussian blobs at each corner of a cube
    b_list = []
    coords = []
    for i in [0, 5]:
        for j in [0, 5]:
            for k in [0, 5]:
                b = rng.normal(scale=noise,
                               size=num_points * dim).reshape(num_points, dim)
                b[:, 0] += i
                b[:, 1] += j
                b[:, 2] += k
                b = np.c_[b, np.repeat(len(b_list), b.shape[0])]
                b_list.append(b)
                coords.append((i, j, k))

    # put our 4 blobs of interest into a single dataframe
    df = pd.DataFrame(np.row_stack([b_list[i] for i in corners_to_keep]),
                      columns=feature_names)

    # make the labels ints
    df.Label = df.Label.astype(int)
    # replace the 4s with 3s so our labels are just range(4)
    df.Label.values[df.Label.values == 4] = 3

    return df
