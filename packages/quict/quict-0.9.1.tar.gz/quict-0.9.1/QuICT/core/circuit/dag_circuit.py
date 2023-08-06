from collections import Iterable, deque
from typing import Set

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from QuICT.core.gate import BasicGate
from QuICT.tools.exception.core import TypeError


class DAGNode:
    """ The node in DAG Circuit, represent a quantum gate in circuit.

    Args:
        id (int): The unique identity, usually be the quantum gates' index
        gate (BasicGate): The quantum gate
        successors (list, optional): The successors for nodes. Defaults to [].
        predecessors (list, optional): The predecessors for nodes. Defaults to [].
    """
    @property
    def id(self):
        return self._id

    @property
    def gate(self):
        return self._gate

    @property
    def name(self):
        return self._name

    @property
    def cargs(self):
        return self._cargs

    @property
    def targs(self):
        return self._targs

    @property
    def qargs(self):
        return self._qargs

    @property
    def successors(self):
        return self._successors

    @property
    def type(self):
        return self._type

    @successors.setter
    def successors(self, sces: list):
        self._successors = sces

    @property
    def predecessors(self):
        return self._predecessors

    @predecessors.setter
    def predecessors(self, pdces: list):
        self._predecessors = pdces

    def __init__(self, id: int, gate: BasicGate, successors: list = None, predecessors: list = None):
        self._id = id
        self._gate = gate
        self._name = gate.qasm_name
        self._cargs = gate.cargs
        self._targs = gate.targs
        self._qargs = gate.cargs + gate.targs
        self._type = gate.type
        self._successors = [] if successors is None else successors
        self._predecessors = [] if predecessors is None else predecessors

    def append_pred(self, u):
        """
        Append a node id to successors.

        Args:
            u(int): the node
        """
        self._predecessors.append(u)

    def append_succ(self, u):
        """
        Append a node id to predecessors.

        Args:
            u(int): the node
        """

        self._successors.append(u)


class DAGCircuit:
    """ The DAG Circuit using networkx.DiGraph()

    The nodes in the graph represented the quantum gates, and the edges means the two quantum
    gates is non-commutation. In other words, a directed edge between node A with quantum gate GA
    and node B with quantum gate GB, the quantum gate GA does not commute with GB.

    The nodes in the graph have the following attributes:
    'name', 'gate', 'cargs', 'targs', 'qargs', 'successors', 'predecessors'.

    **Reference:**

    [1] Iten, R., Moyard, R., Metger, T., Sutter, D. and Woerner, S., 2020.
    Exact and practical pattern matching for quantum circuit optimization.
    `arXiv:1909.05270 <https://arxiv.org/abs/1909.05270>`_

    Args:
        circuit (Circuit): The quantum circuit.
    """
    @property
    def name(self) -> str:
        return self._name

    @property
    def size(self) -> int:
        return self._size

    @property
    def width(self) -> int:
        return self._width

    @property
    def gates(self):
        for node_id in self.nodes():
            node = self.get_node(node_id)
            yield node.gate

    def __init__(self, circuit, node_type=DAGNode):
        self._circuit = circuit
        self._name = f"DAG_{self._circuit.name}"
        self._size = self._circuit.size()
        self._width = self._circuit.width()
        self._graph = nx.DiGraph()
        self._node_type = node_type
        # Build DAG Circuit
        self._to_dag_circuit()

    ####################################################################
    ############         DAGCircuit Nodes and Edges         ############
    ####################################################################
    def __getitem__(self, item):
        """ to fit the slice operator, overloaded this function.

        get a smaller qureg/qubit from this circuit

        Args:
            item(int/slice): slice passed in.
        Return:
            Qubit/Qureg: the result or slice
        """
        return self.nodes()[item]

    def nodes(self) -> list:
        """ Get all nodes in DAG.

        Returns:
            list: The list of nodes
        """
        return list(self._graph.nodes)

    def add_node(self, node: DAGNode):
        """ Add a node into DAG.

        Args:
            node (DAGNode): The DAG Node
        """
        assert isinstance(node, DAGNode), TypeError("DagCircuit.add_node.node", "DAGNode", type(node))
        if not self._graph.has_node(node.id):
            self._graph.add_node(node.id, node=node)

    def get_node(self, node_id: int):
        """ Get DAG node's data.

        Args:
            node_id (int): the unique identity for node
        """
        return self._graph.nodes[node_id]["node"]

    def edges(self) -> list:
        """ Get all edges in DAG.

        Returns:
            list: The list of edges of DAG.
        """
        return list(self._graph.edges)

    def in_edges(self, node_id: int):
        """ Get all in-edges of node with given node id.

        Args:
            node_id (int): the unique identity for node
        """
        return self._graph.in_edges(node_id)

    def out_edges(self, node_id: int):
        """ Get all out-edges of node with given node id.

        Args:
            node_id (int): the unique identity for node
        """
        return self._graph.out_edges(node_id)

    ####################################################################
    ############                Circuit to DAG              ############
    ####################################################################
    def _to_dag_circuit(self):
        gates = self._circuit.gates
        reachable = np.zeros(shape=(len(gates), ), dtype=bool)
        for idx, g in enumerate(gates):
            assert isinstance(g, BasicGate), "Only support BasicGate in DAGCircuit."
            cur = self._node_type(idx, g)
            self.add_node(cur)
            reachable[: idx] = True
            for prev in reversed(range(idx)):
                if reachable[prev] and not g.commutative(gates[prev]):
                    self.add_edge(prev, idx)
                    reachable[list(self.all_predecessors(prev))] = False

    def _all_reachable(self, start, direction):
        if isinstance(start, int):
            visited = {start}
        elif isinstance(start, Iterable):
            visited = set(start)
        else:
            raise TypeError("DagCircuit.all_successors/predecessors.start", "int/Iterable", type(start))

        que = deque(visited)
        init_visited = visited.copy()
        while len(que) > 0:
            cur_node = self.get_node(que.popleft())
            for node_id in getattr(cur_node, direction):
                if node_id not in visited:
                    que.append(node_id)
                    visited.add(node_id)

        return visited - init_visited

    def all_predecessors(self, start) -> Set[int]:
        """
        Return all predecessors (direct and indirect) of `start`.
        `start` can be a node id (int) or many node ids (Iterable).

        Args:
            start(int/Iterable): the start node(s)

        Returns:
            set: set of predecessors
        """

        return self._all_reachable(start, 'predecessors')

    def all_successors(self, start) -> Set[int]:
        """
        Return all successors (direct and indirect) of `start`.

        Args:
            start(int/Iterable): the start node(s)

        Returns:
            Set[int]: set of successors
        """

        return self._all_reachable(start, 'successors')

    def add_edge(self, u, v):
        """
        Add a directed edge to DAG.

        Args:
            u(int): start node
            v(int): end node
        """

        self._graph.add_edge(u, v)
        self.get_node(u).append_succ(v)
        self.get_node(v).append_pred(u)

    ####################################################################
    ############              DAG_Circuit utils             ############
    ####################################################################
    def draw(self, layout=nx.shell_layout):
        """ Draw a DAG circuit, save as jpg file.

        Args:
            layout (layout, optional): The networkx.layout. Defaults to nx.shell_layout.
        """
        graph_name = f"{self.name}.jpg"
        plt.figure()
        nx.draw(self._graph, pos=layout(self._graph), with_labels=True)
        plt.savefig(graph_name)
