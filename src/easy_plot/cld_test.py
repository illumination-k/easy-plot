import networkx as nx
import numpy as np

from easy_plot.cld import adjgraph_from_tukey, get_cld_from_graph

significance = np.matrix(
    [
        [-1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, -1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, -1, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, -1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, -1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, -1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, -1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, -1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, -1],
    ]
)

mat = significance == 0
g = nx.Graph(nx.from_numpy_array(mat))


def test_get_cld_from_graph():
    raise NotImplementedError()
