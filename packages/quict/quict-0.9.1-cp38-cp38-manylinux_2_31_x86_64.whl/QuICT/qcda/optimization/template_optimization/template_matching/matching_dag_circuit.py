from collections import namedtuple
from collections.abc import Iterable
from functools import cached_property
from typing import List, Set

from QuICT.core import Circuit
from QuICT.core.circuit.dag_circuit import DAGCircuit, DAGNode
from QuICT.core.gate import BasicGate

NodeInfo = namedtuple('NodeInfo', ['matched_with', 'is_blocked'])


class MatchingDAGNode(DAGNode):
    """
    DAG node class tailored for template matching algorithm.
    """

    __slots__ = ['successors_to_visit', 'matched_with', 'is_blocked',
                 '_id', '_gate', '_name', '_cargs', '_targs', '_qargs',
                 '_successors', '_predecessors']

    def __init__(self, id: int, gate: BasicGate):
        self.successors_to_visit = []
        self.matched_with = None
        self.is_blocked = False
        super().__init__(id, gate)

    def pop_successors_to_visit(self):
        """
        Pop the first element of successors_to_visit. If no more, return None.

        Returns:
            int: first element of successors_to_visit
        """

        if not self.successors_to_visit:
            return None

        ret = self.successors_to_visit[0]
        self.successors_to_visit.pop(0)
        return ret

    def matchable(self):
        """
        Returns:
            bool: Whether the node can be matched
        """
        return (not self.is_blocked) and (self.matched_with is None)

    def compare_with(self, other, qubit_mapping=None) -> bool:
        """
        Compare `self` to the node `other` under mapping `qubit_mapping`.
        qubit i of `self` is mapped to qubit qubit_mapping[i] of `other`.
        If `qubit_mapping` is None, only compare gate type.
        The order of control qubits is ignored.

        Args:
            other(MatchingDAGNode): the other node
            qubit_mapping(list): mapping
        """

        if self.name != other.name:
            return False
        if qubit_mapping is not None:
            t_cargs = set(map(lambda x: qubit_mapping[x], self.cargs))
            c_cargs = set(other.cargs)
            if t_cargs != c_cargs:
                return False

            for t_qubit, c_qubit in zip(self.targs, other.targs):
                if qubit_mapping[t_qubit] != c_qubit:
                    return False
        return True

    def node_info(self):
        """
        Return:
            tuple: (the matched node, whether is blocked)
        """
        return NodeInfo(self.matched_with, self.is_blocked)


class MatchingDAGCircuit(DAGCircuit):
    """
        DAG circuit class tailored for template matching algorithm.
    """

    def __init__(self, circuit: Circuit):
        self._successor_cache = {}
        self._predecessor_cache = {}
        super().__init__(circuit, node_type=MatchingDAGNode)

    def init_forward_matching(self, node_id, other_id, s2v_enabled=False):
        """
        Initialize forward matching info.
        Args:
            node_id(int): the start node of forward matching
            other_id(int): the start node of the other circuit to match
            s2v_enabled(bool): whether initialize successors_to_visit
        """
        for nid in self.nodes():
            node = self.get_node(nid)
            if node.id == node_id:
                node.matched_with = other_id
                if s2v_enabled:
                    node.successors_to_visit = sorted(node.successors.copy())
            else:
                node.matched_with = None
                if s2v_enabled:
                    node.successors_to_visit = []
            node.is_blocked = False

    def all_predecessors(self, start, cache_enabled=True) -> Set[int]:
        """
        Return all predecessors (direct and undirect) of `start`.
        `start` can be a node id (int) or many node ids (Iterable).
        Return values of single node query will be cached if `cache_enable` is True

        Args:
            start(int/Iterable): the start node(s)
            cache_enabled(bool): whether use cache

        Returns:
            set: set of predecessors
        """

        if not cache_enabled or isinstance(start, Iterable):
            return self._all_reachable(start, 'predecessors')
        elif isinstance(start, int):
            if start not in self._predecessor_cache:
                self._predecessor_cache[start] = set(self.get_node(start).predecessors)
                for succ in self.get_node(start).predecessors:
                    self._predecessor_cache[start] |= self.all_predecessors(succ)
            return self._predecessor_cache[start]
        else:
            assert False, 'start must be int or iterable objects'

    def all_successors(self, start, cache_enabled=True) -> Set[int]:
        """
        Return all successors (direct and indirect) of `start`.
        `start` can be a node id (int) or many node ids (Iterable).
        Return values of single node query will be cached if `cache_enable` is True.

        Args:
            start(int/Iterable): the start node(s)
            cache_enabled(bool): whether use cache

        Returns:
            Set[int]: set of successors
        """

        if not cache_enabled or isinstance(start, Iterable):
            return self._all_reachable(start, 'successors')
        elif isinstance(start, int):
            if start not in self._successor_cache:
                self._successor_cache[start] = set(self.get_node(start).successors)
                for succ in self.get_node(start).successors:
                    self._successor_cache[start] |= self.all_successors(succ)
            return self._successor_cache[start]
        else:
            assert False, 'start must be int or iterable objects'

    def matching_info(self):
        """
        Returns:
              List[NodeInfo]: matching info used by backward_match
        """
        return [self.get_node(i).node_info() for i in range(self.size)]

    def get_circuit(self):
        """
        Output the circuit of this DAG.

        Returns:
            Circuit: the circuit
        """

        circ = Circuit(self.width)
        for node_id in self.nodes():
            node: MatchingDAGNode = self.get_node(node_id)
            circ.append(node.gate.copy())
        return circ


class Match:
    """
    Class to store matches
    """
    def __init__(self, match: List, qubit_mapping: List):
        self.match = sorted(match)
        self.qubit_mapping = qubit_mapping

    def __len__(self):
        return len(self.match)

    def __hash__(self):
        return hash(tuple(self.match))

    def __str__(self):
        return f'Match({str(self.match)}, {str(self.qubit_mapping)})'

    def __repr__(self):
        return str(self)

    @cached_property
    def template_nodes(self):
        """
        Returns:
            Set[int]: Set of tempalte nodes
        """

        return {m[0] for m in self.match}

    @cached_property
    def circuit_nodes(self):
        """
        Returns:
            Set[int]: Set of circuit nodes
        """

        return {m[1] for m in self.match}
