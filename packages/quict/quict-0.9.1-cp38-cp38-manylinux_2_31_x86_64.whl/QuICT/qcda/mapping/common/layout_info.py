from typing import List, Tuple

import networkx as nx
import numpy as np
from QuICT.core import *
from .data_factory import DataFactory


class LayoutInfo:
    def __init__(self, layout: Layout) -> None:
        self.layout = layout
        self._mask = None
        self._graph = None
        self._dist = None
        self._edges = None

    @property
    def topo_graph(self) -> nx.Graph:
        if self._graph is None:
            self._graph = DataFactory.get_topo_graph(self.layout)
        return self._graph

    @property
    def topo_dist(self) -> np.ndarray:
        if self._dist is None:
            self._dist = DataFactory.get_topo_dist(topo_graph=self.topo_graph)
        return self._dist

    @property
    def topo_edges(self) -> List[Tuple[int, int]]:
        if self._edges is None:
            self._edges = DataFactory.get_topo_edges(topo_graph=self.topo_graph)
        return self._edges
