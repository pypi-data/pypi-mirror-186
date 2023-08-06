from collections import defaultdict
from typing import Dict, List, Union

import numpy as np


class Graph:
    """ The graph descript position space and action space for quantum random walk """
    @property
    def position(self) -> int:
        return self._nodes

    @property
    def position_qubits(self) -> int:
        return int(np.ceil(np.log2(self._nodes)))

    @property
    def action_space(self) -> int:
        return len(self._edges[0])

    @property
    def action_qubits(self) -> int:
        if self._operators is None:
            return int(np.ceil(np.log2(self.action_space)))
        else:
            shape = self._operators[0][0].shape
            return int(np.ceil(np.log2(shape[0])))

    @property
    def edges(self) -> dict:
        return self._edges

    @property
    def operators(self) -> dict:
        return self._operators

    @property
    def switched_time(self) -> int:
        return self._switched_time

    def __init__(
        self,
        position: int,
        edges: Union[List, Dict] = None,
        operators: Union[List, Dict] = None,
        switched_time: int = -1
    ):
        """ Initial the random walk graph.

        Args:
            position (int): The number of graph's nodes.
            edges (Union[List, Dict], optional): The edges of each node. Defaults to None.
            operators (Union[List, Dict], optional): The operators of each node. Defaults to None.
            switched_time (int, optional): The number of steps of each coin operator in the nodes.
                Defaults to -1, means not switch coin operator.
        """
        self._nodes = position
        self._switched_time = switched_time
        self._edges = defaultdict(list)
        if edges is not None:
            iterator = enumerate(edges) if isinstance(edges, list) else edges.items()
            for idx, edge in iterator:
                assert isinstance(edge, list)
                self._edges[idx] = edge

        self._operators = defaultdict(list) if operators is not None else operators
        if operators is not None:
            iterator = enumerate(operators) if isinstance(operators, list) else operators.items()
            assert len(iterator) == self._nodes, "The number of operators should equal to position"
            for idx, operator in iterator:
                assert self.operator_validation(operator), "The operator should be 1 or more unitary matrix."
                self._operators[idx] = operator if isinstance(operator, list) else [operator]

    def __str__(self):
        return str(self._edges) + "\nOperators: " + str(self._operators)

    def operator_validation(self, operator: Union[List, np.ndarray]) -> bool:
        """ Validate the operators """
        if isinstance(operator, np.ndarray):
            return self._operator_validation(operator)

        for op in operator:
            if not self._operator_validation(op):
                return False

        return True

    def _operator_validation(self, operator: np.ndarray):
        shape = operator.shape
        log2_shape = int(np.ceil(np.log2(shape[0])))

        return (
            shape[0] == shape[1] and
            shape[0] == (1 << log2_shape) and
            np.allclose(np.eye(shape[0]), operator.dot(operator.T.conj()))
        )

    def add_operator(self, u: int, operator: Union[List, np.ndarray]):
        """ Add operator to a vector. """
        assert u >= 0 and u <= self._nodes
        assert self.operator_validation(operator), "The operator should be 1 or more unitary matrix."
        if isinstance(operator, np.ndarray):
            operator = [operator]

        for op in operator:
            self._operators[u].append(op)

    def add_edge(self, u: int, v: int):
        """ Add edge """
        assert u >= 0 and u <= self._nodes
        assert v >= 0 and v <= self._nodes

        if v not in self._edges[u]:
            self._edges[u].append(v)

    def del_edge(self, u: int, v: int):
        """ Remove edge """
        assert u >= 0 and u <= self._nodes
        assert v >= 0 and v <= self._nodes

        if v in self._edges[u]:
            self._edges[u].remove(v)

    def validation(self) -> bool:
        """ Validate that all vectors has same number of edges. """
        edge_size = len(self._edges[0])
        for edge in self._edges.values():
            if len(edge) != edge_size:
                return False

        return True
