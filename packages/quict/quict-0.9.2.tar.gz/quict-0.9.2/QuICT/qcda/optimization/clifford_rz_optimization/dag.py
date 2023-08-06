from collections import deque
from collections.abc import Iterable
from itertools import chain
from typing import Dict, List, Set, Tuple

from QuICT.core import *
from QuICT.core.gate import *
from QuICT.core.gate.gate_builder import GATE_TYPE_TO_CLASS

from .symbolic_phase import SymbolicPhase, SymbolicPhaseVariable


class DAG(Iterable):
    """
    DAG representation of a quantum circuit that indicates the commutative
    relations between gates. Iterate over a DAG will gate a sequence of
    BasicGate's in topological order.
    """

    class Node:
        """
        DAG node class.
        """

        __slots__ = ['predecessors', 'successors', 'flag', 'qubit_id', 'size', 'qubit_loc', 'qubit_flag',
                     'gate_type', '_params', 'poly_phase']

        FLAG_DEFAULT = 0
        FLAG_VISITED = 1
        FLAG_ERASED = -1
        FLAG_IN_QUE = 2
        FLAG_TO_ERASE = 3

        def __init__(self, gate_: BasicGate = None, qubit_=0):
            """
            Args:
                gate_(BasicGate): Gate represented by this node
                qubit_(int): the actual qubit the gate sits on (used only when `gate_` is None)
            """
            self.gate_type = gate_.type if gate_ is not None else None
            self._params = gate_.pargs.copy() if gate_ is not None else []

            # the actual qubit the i-th wire of the gate act on
            self.qubit_loc = [qubit_] if gate_ is None else list(chain(gate_.cargs, gate_.targs))
            # inverse mapping of self.qubit_loc
            self.qubit_id = {qubit_: 0} if gate_ is None else {qubit_: i for i, qubit_ in enumerate(self.qubit_loc)}

            self.size = len(self.qubit_id)
            self.predecessors: List[Tuple[DAG.Node, int]] = [(None, 0)] * self.size
            self.successors: List[Tuple[DAG.Node, int]] = [(None, 0)] * self.size

            # temp variables used for optimization algorithms
            self.qubit_flag = [self.FLAG_DEFAULT] * self.size
            self.flag = self.FLAG_DEFAULT
            self.poly_phase = None

        @property
        def params(self):
            return self._params

        @params.setter
        def params(self, args):
            assert type(args) == list, 'assignment of params must be a list'
            self._params = args

        def get_gate(self):
            """
            Get a copy of corresponding gate of the node

            Returns:
                BasicGate: corresponding gate
            """

            return GATE_TYPE_TO_CLASS[self.gate_type]()(*self.params) & self.qubit_loc \
                if self.gate_type is not None else None

        def add_forward_edge(self, qubit_, node):
            """
            Add an edge from self to node. Make sure qubit_id is up to date.

            Args:
                qubit_(int): the actual qubit this edge sit on
                node(DAG.Node): the node this edge point to
            """
            u_id = self.qubit_id[qubit_]
            v_id = node.qubit_id[qubit_]
            self.successors[u_id] = (node, v_id)
            node.predecessors[v_id] = (self, u_id)

        def connect(self, forward_qubit, backward_qubit, node):
            """
            Connect (self, forward_qubit) to (node, backward_qubit)

            Args:
                forward_qubit(int): the wire this edge points from
                backward_qubit(int): the wire this edge points to
                node(DAG.Node):  the node this edge points to
            """
            self.successors[forward_qubit] = (node, backward_qubit)
            node.predecessors[backward_qubit] = (self, forward_qubit)

        def append(self, forward_qubit, backward_qubit, node):
            """
            Insert a (node, backward_qubit) after (self, forward_qubit)

            Args:
                forward_qubit(int): the wire this edge points from
                backward_qubit(int): the wire this edge points to
                node(DAG.Node):  the node this edge points to
            """
            s_node, s_qubit = self.successors[forward_qubit]
            self.connect(forward_qubit, backward_qubit, node)
            node.connect(backward_qubit, s_qubit, s_node)

        def erase(self):
            """
            erase this node from the DAG. It will:
            1. set this node as FLAG_ERASED
            2. remove pointers between it and adjacent nodes
            """
            self.flag = self.FLAG_ERASED
            for qubit_ in range(self.size):
                p_node, p_qubit = self.predecessors[qubit_]
                n_node, n_qubit = self.successors[qubit_]
                if p_node:
                    p_node.connect(p_qubit, n_qubit, n_node)
                elif n_node:
                    n_node.predecessors[qubit_] = (None, 0)
            self.predecessors = None
            self.successors = None

    class VirtualNode(Node):
        """
        Virtual DAG node. When we want to temporarily insert a node into a DAG
        but not actually change the DAG structure, we can create a virtual node.
        """
        def __init__(self, gate_: BasicGate, predecessors, successors):
            """
            Args:
                gate_(BasicGate): the gate
                predecessors(List[Tuple[DAG.Node, int]]): predecessors of this node
                successors(List[Tuple[DAG.Node, int]]): successors of this node
            """
            super().__init__(gate_=gate_)
            self.predecessors = predecessors
            self.successors = successors

    def __init__(self, gates: Circuit, build_toffoli=True):
        """
        Args:
            gates(Circuit): Circuit represented by this DAG
        """

        self._width = gates.width()

        self.start_nodes = [self.Node(qubit_=i) for i in range(self._width)]
        self.end_nodes = [self.Node(qubit_=i) for i in range(self._width)]
        self.global_phase = 0
        self.has_symbolic_rz = False
        self.init_size = self._build_graph(gates, build_toffoli)
        self.build_toffoli = build_toffoli

    def width(self):
        """
        Get number of qubits of this circuit
        Returns:
            int: Number of qubits
        """
        return self._width

    @staticmethod
    def _build_ccz(gate_):
        """CCX decomposition described in Nam et.al."""
        cgate = CompositeGate()
        with cgate:
            CX & [1, 2]
            T_dagger & 2
            CX & [0, 2]
            T & 2
            CX & [1, 2]
            T_dagger & 2
            CX & [0, 2]
            CX & [0, 1]
            T_dagger & 1
            CX & [0, 1]
            T & 0
            T & 1
            T & 2

        args = gate_.cargs + gate_.targs
        if len(args) == gate_.controls + gate_.targets:
            cgate & args
        return cgate.gates

    def _build_graph(self, gates: Circuit, build_toffoli):
        node_cnt = 0
        cur_nodes = self.start_nodes.copy()

        var_cnt = 0
        for idx, gate_ in enumerate(gates.gates):
            # decouple ccx building with dag
            if build_toffoli and (gate_.type == GateType.ccx or gate_.type == GateType.ccz):
                self.has_symbolic_rz = True
                gate_list = self._build_ccz(gate_)
                if gate_.type == GateType.ccx:
                    gate_list = [H & gate_.targ] + gate_list + [H & gate_.targ]

                node_cnt += len(gate_list)

                # create a new phase variable
                var = SymbolicPhaseVariable(var_cnt)
                var_cnt += 1

                # represent phase of T/Tdg gates with this variable
                for each in gate_list:
                    node = self.Node(each)
                    if node.gate_type == GateType.t:
                        node.gate_type = GateType.rz
                        node.params = [SymbolicPhase() + var]
                        self.global_phase += var / 2
                    elif node.gate_type == GateType.tdg:
                        node.gate_type = GateType.rz
                        node.params = [SymbolicPhase() - var]
                        self.global_phase -= var / 2

                    for qubit_ in list(chain(each.cargs, each.targs)):
                        cur_nodes[qubit_].add_forward_edge(qubit_, node)
                        cur_nodes[qubit_] = node
            else:
                node_cnt += 1
                node = self.Node(gate_)
                for qubit_ in list(chain(gate_.cargs, gate_.targs)):
                    cur_nodes[qubit_].add_forward_edge(qubit_, node)
                    cur_nodes[qubit_] = node

        for qubit_ in range(self._width):
            cur_nodes[qubit_].add_forward_edge(qubit_, self.end_nodes[qubit_])

        return node_cnt

    def get_circuit(self):
        """
        Generate circuit net list from this DAG.

        Returns:
            Circuit: Circuit equivalent to this DAG
        """

        circ = Circuit(self._width)
        mapping = {(id(node), 0): qubit_ for qubit_, node in enumerate(self.start_nodes)}
        for node in self.topological_sort():
            for qubit_ in range(node.size):
                pred, qubit2 = node.predecessors[qubit_]
                mapping[(id(node), qubit_)] = mapping[(id(pred), qubit2)]

            node.get_gate() | circ([mapping[(id(node), qubit_)] for qubit_ in range(node.size)])

        if not np.isclose(float(self.global_phase), 0):
            GPhase(self.global_phase) | circ(0)
        return circ

    def topological_sort(self, include_dummy=False):
        """
        Iterate over nodes in this DAG in topological order (ignore start nodes)

        Returns:
            Iterator[DAG.Node]: nodes in topological order
        """

        edge_count = {}
        queue = deque(self.start_nodes)
        while len(queue) > 0:
            cur = queue.popleft()
            if cur.gate_type is not None or include_dummy:
                yield cur
            for nxt, _ in cur.successors:
                if nxt is None:
                    continue
                if id(nxt) not in edge_count:
                    edge_count[id(nxt)] = nxt.size
                edge_count[id(nxt)] -= 1
                if edge_count[id(nxt)] == 0:
                    queue.append(nxt)

    @staticmethod
    def topological_sort_sub_circuit(prev_node, succ_node):
        """
        Sort the sub circuit between prev_node and succ_node in topological order.

        Returns:
            Iterator[DAG.Node]: nodes in topological order
        """
        end_set = set()
        for node_, qubit_ in filter(lambda x: x is not None, succ_node):
            end_set.add(id(node_))

        edge_count = {}
        queue = deque()
        for each in prev_node:
            if each is None:
                continue
            node_, qubit_ = each
            nxt, nxt_q = node_.successors[qubit_]
            if id(nxt) in end_set:
                continue

            if id(nxt) not in edge_count:
                edge_count[id(nxt)] = nxt.size
            edge_count[id(nxt)] -= 1
            if edge_count[id(nxt)] == 0:
                queue.append(nxt)

        while len(queue) > 0:
            cur = queue.popleft()
            yield cur

            for nxt, nxt_q in cur.successors:
                if nxt is None or id(nxt) in end_set:
                    continue
                if id(nxt) not in edge_count:
                    edge_count[id(nxt)] = nxt.size
                edge_count[id(nxt)] -= 1
                if edge_count[id(nxt)] == 0:
                    queue.append(nxt)

    def reset_flag(self):
        """
        Set flag of all nodes to FLAG_DEFAULT
        """
        for node in self.start_nodes:
            node.flag = node.FLAG_DEFAULT
            node.qubit_flag = [node.FLAG_DEFAULT] * node.size
        for node in self.end_nodes:
            node.flag = node.FLAG_DEFAULT
            node.qubit_flag = [node.FLAG_DEFAULT] * node.size
        for node in self.topological_sort():
            node.flag = node.FLAG_DEFAULT
            node.qubit_flag = [node.FLAG_DEFAULT] * node.size

    def set_qubit_loc(self):
        """
        Update qubit_loc of all nodes.
        """

        mapping = {(id(node), 0): qubit_ for qubit_, node in enumerate(self.start_nodes)}
        for i, node in enumerate(self.start_nodes):
            node.qubit_loc[0] = i
            node.qubit_id = {i: 0}
        for i, node in enumerate(self.end_nodes):
            node.qubit_loc[0] = i
            node.qubit_id = {i: 0}

        for node in self.topological_sort():
            for qubit_ in range(node.size):
                pred, qubit2 = node.predecessors[qubit_]
                mapping[(id(node), qubit_)] = mapping[(id(pred), qubit2)]
                node.qubit_loc[qubit_] = mapping[(id(node), qubit_)]

            node.qubit_id = {qubit_: i for i, qubit_ in enumerate(node.qubit_loc)}

    def compare_circuit(self, other: Tuple[Node, int], anchor_qubit: int,
                        flag_enabled: bool = False, dummy_rz: bool = False):
        """
        Compare this circuit with another circuit.
        This circuit starts from the first gate on the `anchor_qubit`.
        The other starts from (gate, wire) defined by variable `other`.
        Param values (such as phases in Rz) ignored.

        Args:
            other(Tuple[Node, int]): start point of the other circuit
            anchor_qubit(int): start point of this circuit.
            flag_enabled(bool): Whether consider `flag` field. If true,
                nodes already with FLAG_VISITED will be
                skipped. Nodes in the matching will be set FLAG_VISITED.
            dummy_rz(bool): Enable dummy_rz feature: when there is a rz is `self`
            but not in `other`, create a virtual Rz(0) in `other` to match them.

        Returns:
            Dict[int, DAG.Node]: mapping from id(node of this circuit) to
                matched node in the other circuit. If not matched, return None.
        """
        t_node, t_qubit = self.start_nodes[anchor_qubit].successors[0]
        o_node, o_qubit = other[0], (t_qubit if other[1] == -1 else other[1])
        if o_node.gate_type is None:
            return None

        if o_node.gate_type != t_node.gate_type or (t_qubit != o_qubit) or (o_node.flag and flag_enabled):
            return None

        mapping = {id(t_node): o_node}
        queue = deque([(t_node, o_node)])
        while len(queue) > 0:
            u, v = queue.popleft()
            for neighbors in ['predecessors', 'successors']:
                for qubit_ in range(u.size):
                    u_nxt, u_qubit = getattr(u, neighbors)[qubit_]
                    if not u_nxt.gate_type:
                        continue

                    v_nxt, v_qubit = getattr(v, neighbors)[qubit_]
                    if id(u_nxt) in mapping:
                        if dummy_rz and isinstance(mapping[id(u_nxt)], DAG.VirtualNode):
                            continue
                        if id(mapping[id(u_nxt)]) != id(v_nxt) or u_qubit != v_qubit:
                            return None
                        continue

                    # v_nxt fails to match u_nxt
                    if not v_nxt.gate_type or (v_nxt.flag and flag_enabled) or \
                            u_nxt.gate_type != v_nxt.gate_type or u_qubit != v_qubit:
                        # if u_nxt is a rz, put a virtual node in v_nxt
                        if dummy_rz and u_nxt.gate_type == GateType.rz:
                            vnode = DAG.VirtualNode(
                                Rz(0),
                                [(v, qubit_)] if neighbors == 'successors' else [(v_nxt, v_qubit)],
                                [(v_nxt, v_qubit)] if neighbors == 'successors' else [(v, qubit_)]
                            )
                            mapping[id(u_nxt)] = vnode
                            queue.append((u_nxt, vnode))
                            continue
                        return None

                    mapping[id(u_nxt)] = v_nxt
                    queue.append((u_nxt, v_nxt))

        if flag_enabled:
            for each in mapping.values():
                each.flag = DAG.Node.FLAG_VISITED
        return mapping

    @staticmethod
    def replace_circuit(mapping: Dict[int, Tuple[Node, int]], replacement, erase_old=True):
        """
        Replace a part of this DAG with `replacement` defined by `mapping`.

        Args:
            mapping(Dict[int, Tuple[Node, int]]): mapping from the replacement to this circuit
            replacement: new sub circuit
            erase_old: whether erase old circuit
        """
        replacement: DAG
        erase_queue = deque()
        for qubit_ in range(replacement.width()):
            # first node on qubit_ in replacement circuit
            r_node, r_qubit = replacement.start_nodes[qubit_].successors[0]
            # node previous to the node corresponding to t_node in original circuit
            if id(replacement.start_nodes[qubit_]) not in mapping:
                continue
            p_node, p_qubit = mapping[id(replacement.start_nodes[qubit_])]
            if erase_old:
                erase_queue.append(p_node.successors[p_qubit][0])

            # place r_node after p_node
            p_node.connect(p_qubit, r_qubit, r_node)

        for qubit_ in range(replacement.width()):
            # last node on qubit_ in replacement circuit
            r_node, r_qubit = replacement.end_nodes[qubit_].predecessors[0]
            # node successive to the node corresponding to t_node in original circuit
            if id(replacement.end_nodes[qubit_]) not in mapping:
                continue
            s_node, s_qubit = mapping[id(replacement.end_nodes[qubit_])]
            d_node, d_qubit = s_node.predecessors[s_qubit]
            d_node.successors[d_qubit] = (None, 0)

            # place s_node after r_node
            r_node.connect(r_qubit, s_qubit, s_node)

        if erase_old:
            while len(erase_queue) > 0:
                cur = erase_queue.popleft()
                if cur is None or cur.flag == cur.FLAG_ERASED:
                    continue
                for qubit_ in range(cur.size):
                    erase_queue.append(cur.successors[qubit_][0])

                cur.flag = cur.FLAG_ERASED
                cur.predecessors = None
                cur.successors = None

    @staticmethod
    def _get_reachable_relation(node: Node, qubit_: int) -> Set[Tuple[Tuple[int, int], int]]:
        visited = set()
        queue = deque([(node, qubit_)])
        while len(queue) > 0:
            cur, cur_q = queue.popleft()
            if cur.gate_type is None:
                continue
            nxt, _ = cur.successors[cur_q]
            if id(nxt) not in visited:
                for nxt_q in range(nxt.size):
                    queue.append((nxt, nxt_q))
                visited.add(id(nxt))

        reachable = {((id(node), qubit_), o) for o in visited}
        return reachable

    def get_reachable_relation(self) -> Set[Tuple[Tuple[int, int], int]]:
        """
        Get reachable relation of nodes, namely whether (node A, wire) can reach the other node B.

        Returns:
            Set[Tuple[Tuple[int, int], int]]: Reachable relation ((id(A), wire), id(B))
        """
        reachable = set()
        for each in self.topological_sort(include_dummy=True):
            for qubit_ in range(each.size):
                reachable.update(self._get_reachable_relation(each, qubit_))
        return reachable

    @staticmethod
    def get_reachable_set(node: Node, qubit_: int, succ_node=None):
        """
        Get a set of reachable nodes starting from (node, qubit_)

        Args:
            node(DAG.Node): starting node
            qubit_(int): starting wire
            succ_node(List[Tuple[DAG.Node, int]]): right boundary

        Returns:
            Set[int]: id of reachable nodes
        """
        term_set = set()
        if succ_node is not None:
            for node_, qubit_ in filter(lambda x: x is not None, succ_node):
                term_set.add(id(node_))

        visited = set()
        queue = deque([(node, qubit_)])
        while len(queue) > 0:
            cur, cur_q = queue.popleft()
            if cur.gate_type is None or id(cur) in term_set:
                continue
            nxt, _ = cur.successors[cur_q]
            if id(nxt) not in visited:
                for nxt_q in range(nxt.size):
                    queue.append((nxt, nxt_q))
                visited.add(id(nxt))

        return visited

    @staticmethod
    def _get_sub_circuit_reachable_relation(node, qubit_, term_set):
        visited = set()
        queue = deque([(node, qubit_)])
        while len(queue) > 0:
            cur, cur_q = queue.popleft()
            if id(cur) in term_set:
                continue
            nxt, _ = cur.successors[cur_q]
            if id(nxt) not in visited:
                for nxt_q in range(nxt.size):
                    queue.append((nxt, nxt_q))
                visited.add(id(nxt))

        reachable = {((id(node), qubit_), o) for o in visited}
        return reachable

    @classmethod
    def get_sub_circuit_reachable_relation(cls, prev_node, succ_node):
        """
        Get reachable relation of nodes in the sub circuit,
        namely whether (node A, wire) can reach node B.

        If prev_node[i] and succ_node[i] is None, the sub circuit does not contain qubit i.

        Args:
            prev_node(List[Tuple[DAG.Node, int]]): left bound of the sub circuit.
            succ_node(List[Tuple[DAG.Node, int]]): right bound of the sub circuit.

        Returns:
            Set[Tuple[Tuple[int, int], int]]: Reachable relation ((id(A), wire), id(B))

        """
        term_set = set()
        for node_, qubit_ in filter(lambda x: x is not None, succ_node):
            term_set.add(id(node_))

        reachable = set()
        for each in cls.topological_sort_sub_circuit(prev_node, succ_node):
            for qubit_ in range(each.size):
                reachable.update(cls._get_sub_circuit_reachable_relation(each, qubit_, term_set))
        return reachable

    def append(self, gate_: BasicGate):
        """
        Add a gate after this DAG.

        Args:
            gate_(BasicGate): gate to add
        """
        node_ = self.Node(gate_)
        for wire_, qubit_ in enumerate(node_.qubit_loc):
            p_node, p_qubit = self.end_nodes[qubit_].predecessors[0]
            p_node.successors[p_qubit] = (node_, wire_)
            node_.predecessors[wire_] = (p_node, p_qubit)

            node_.successors[wire_] = (self.end_nodes[qubit_], 0)
            self.end_nodes[qubit_].predecessors[0] = (node_, wire_)

    def extend(self, gates: List[BasicGate]):
        """
        Add a list of gates after this DAG

        Args:
            gates(List[BasicGate]): gates to add
        """
        for each in gates:
            self.append(each)

    def __iter__(self):
        """
        Iterate over gates in this DAG in topological order

        Returns:
            Iterator[BasicGate]: gates in topological order
        """

        for node in self.topological_sort():
            yield node.get_gate()

    def copy(self):
        """
        Get a copy of this circuit

        Returns:
            DAG: a copy
        """
        return DAG(self.get_circuit(), build_toffoli=self.build_toffoli)

    def destroy(self):
        """
        Destroy this DAG.
        """
        que = deque(self.start_nodes)
        while len(que) > 0:
            cur = que.popleft()
            if cur is None or cur.flag == cur.FLAG_ERASED:
                continue
            for qubit_ in range(cur.size):
                que.append(cur.successors[qubit_][0])

            cur.flag = cur.FLAG_ERASED
            cur.predecessors = None
            cur.successors = None
