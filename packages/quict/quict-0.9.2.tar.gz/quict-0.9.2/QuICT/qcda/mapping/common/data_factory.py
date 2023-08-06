import os
from os import path as osp
from typing import Dict, List, Tuple, Union

import networkx as nx
from numba import njit
import numpy as np

from QuICT.core import *


@njit
def _floyd(n: int, dist: np.ndarray, _inf: int) -> np.ndarray:
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for i in range(n):
        for j in range(n):
            if dist[i][j] >= _inf:
                dist[i][j] = 0
    return dist


class DataFactory:
    def __init__(
        self,
        topo: Union[str, Layout],
        max_gate_num: int,
        data_dir: str = None,
    ) -> None:
        if data_dir is None:
            data_dir = osp.dirname(osp.realpath(__file__))
            data_dir = osp.join(data_dir, "data")
        self._data_dir = data_dir
        self._topo_dir = osp.join(data_dir, "topo")

        self._max_gate_num = max_gate_num

        self._topo_names = None

        # Topo attr cache def
        # These attributes maps are lazily initialized for faster start up.
        self._topo_map = {}
        self._topo_graph_map = {}
        self._topo_edge_map = {}
        self._topo_edge_mat_map = {}
        self._topo_qubit_num_map = {}
        self._topo_dist_map = {}

        if isinstance(topo, str):
            self._cur_topo = self.topo_map[topo]
        elif isinstance(topo, Layout):
            self._cur_topo = topo
        else:
            raise TypeError("Only support layout name or Layout object.")
        assert self._cur_topo is not None

    @property
    def topo_names(self) -> List[str]:
        if self._topo_names is None:
            self._topo_names = []
            for _, _, filenames in os.walk(self._topo_dir):
                for name in filenames:
                    self._topo_names.append(name.split(".")[0])
        return self._topo_names

    @property
    def topo_graph_map(self) -> Dict[str, nx.Graph]:
        if len(self._topo_graph_map) == 0:
            self._reset_attr_cache()
        return self._topo_graph_map

    @property
    def topo_edge_map(self) -> Dict[str, List[Tuple[int, int]]]:
        if len(self._topo_edge_map) == 0:
            self._reset_attr_cache()
        return self._topo_edge_map

    @property
    def topo_qubit_num_map(self) -> Dict[str, int]:
        if len(self._topo_qubit_num_map) == 0:
            self._reset_attr_cache()
        return self._topo_qubit_num_map

    @property
    def topo_dist_map(self) -> Dict[str, np.ndarray]:
        if len(self._topo_dist_map) == 0:
            self._reset_attr_cache()
        return self._topo_dist_map

    @property
    def topo_edge_mat_map(self) -> Dict[str, np.ndarray]:
        if len(self._topo_edge_mat_map) == 0:
            self._reset_attr_cache()
        return self._topo_edge_mat_map

    @property
    def topo_map(self) -> Dict[str, Layout]:
        if len(self._topo_map) == 0:
            self._reset_attr_cache()
        return self._topo_map

    def _reset_attr_cache(self):
        for topo_name in self.topo_names:
            topo_path = osp.join(self._topo_dir, f"{topo_name}.json")
            topo = Layout.load_file(topo_path)
            self._topo_map[topo_name] = topo
            topo_graph = self.get_topo_graph(topo)
            self._topo_graph_map[topo_name] = topo_graph
            self._topo_qubit_num_map[topo_name] = topo.qubit_number
            self._topo_dist_map[topo_name] = self.get_topo_dist(topo_graph=topo_graph)

            topo_edge = self.get_topo_edges(topo_graph=topo_graph)
            topo_adj_mat_thin = np.zeros(
                (topo.qubit_number, topo.qubit_number), dtype=int
            )
            for u, v in topo_graph.edges:
                topo_adj_mat_thin[u][v] = 1
            self._topo_edge_map[topo_name] = topo_edge
            self._topo_edge_mat_map[topo_name] = topo_adj_mat_thin

    @classmethod
    def get_topo_graph(cls, topo: Layout) -> nx.Graph:
        """Build tha graph representation of a topology.

        Args:
            topo (Layout): Topology to be built.

        Returns:
            nx.Graph: Graph representation.
        """
        g = nx.Graph()
        for i in range(topo.qubit_number):
            g.add_node(i)
        for edge in topo:
            g.add_edge(edge.u, edge.v)
        return g

    @classmethod
    def get_topo_dist(cls, topo_graph: nx.Graph) -> np.ndarray:
        _inf = nx.number_of_nodes(topo_graph) + 5
        n = nx.number_of_nodes(topo_graph)
        dist = np.empty((n, n), dtype=np.int)
        dist[:, :] = _inf
        for u, v in topo_graph.edges:
            dist[u][v] = 1
            dist[v][u] = 1
        dist = _floyd(n, dist, _inf)
        return dist

    @classmethod
    def get_topo_edges(cls, topo_graph: nx.Graph) -> List[Tuple[int, int]]:
        topo_edge = []
        for u, v in topo_graph.edges:
            topo_edge.append((u, v))
        return topo_edge
