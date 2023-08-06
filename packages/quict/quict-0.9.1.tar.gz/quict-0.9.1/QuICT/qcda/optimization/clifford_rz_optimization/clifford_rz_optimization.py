import time
from collections import deque
from functools import cached_property
from typing import List

from QuICT.qcda.optimization.commutative_optimization import \
    CommutativeOptimization
from QuICT.qcda.utility import OutputAligner

from .dag import DAG
from .symbolic_phase import SymbolicPhase
from .template import *


class CliffordRzOptimization(object):
    """
    Heuristic optimization of circuits in Clifford + Rz.

    [1] Nam, Yunseong, et al. "Automated optimization of large quantum
    circuits with continuous parameters." npj Quantum Information 4.1
    (2018): 1-12.
    """

    _optimize_sub_method = {
        1: "reduce_hadamard_gates",
        2: "cancel_single_qubit_gates",
        3: "cancel_two_qubit_gates",
        4: "merge_rotations",
        5: "float_rotations",
    }
    _optimize_routine = {
        'heavy': [1, 3, 2, 3, 1, 2, 4, 5],
        'light': [1, 3, 2, 3, 1, 2, 4, 3, 2],
    }

    def parameterize_all(self, gates: DAG):
        """
        Convert all applicable Rz gates into T/Tdg/S/Sdg/Z in the circuit.

        Args:
            gates(DAG): DAG of the circuit
        """
        for node in gates.topological_sort():
            if node.gate_type in [GateType.s, GateType.t, GateType.sdg, GateType.tdg, GateType.z]:
                gate_, phase_ = CommutativeOptimization.parameterize(node.get_gate())
                node.gate_type = gate_.type
                node.params = gate_.pargs
                gates.global_phase += phase_

        if not isinstance(gates.global_phase, SymbolicPhase):
            gates.global_phase %= 2 * np.pi
        else:
            gates.global_phase = np.mod(gates.global_phase, 2 * np.pi)

    @cached_property
    def hadamard_templates(self):
        return generate_hadamard_gate_templates()

    @cached_property
    def single_qubit_gate_templates(self):
        return generate_single_qubit_gate_templates()

    @cached_property
    def cnot_targ_template(self):
        return generate_cnot_targ_templates()

    @cached_property
    def cnot_ctrl_template(self):
        return generate_cnot_ctrl_templates()

    @cached_property
    def gate_preserving_rewrite_template(self):
        return generate_gate_preserving_rewrite_template()

    @cached_property
    def gate_reducing_rewrite_template(self):
        return generate_gate_reducing_rewrite_template()

    def deparameterize_all(self, gates: DAG):
        """
        Convert all applicable T/Tdg/S/Sdg/Z into Rz in the circuit.

        Args:
            gates(DAG): DAG of the circuit
        """
        for node in gates.topological_sort():
            if node.gate_type == GateType.rz and not isinstance(node.params[0], SymbolicPhase):
                compo_gate_, phase_ = CommutativeOptimization.deparameterize(node.get_gate())
                if len(compo_gate_.gates) > 1:
                    continue
                node.gate_type = compo_gate_[0].type
                node.params = compo_gate_[0].pargs
                gates.global_phase += phase_

        if not isinstance(gates.global_phase, SymbolicPhase):
            gates.global_phase %= 2 * np.pi
        else:
            gates.global_phase = np.mod(gates.global_phase, 2 * np.pi)

    def reduce_hadamard_gates(self, gates: DAG):
        """
        Reduce hadamard gates in Clifford+Rz circuits by template matching.
        Adjacent X gates will also be cancelled out.

        Args:
            gates(DAG): DAG of the circuit
        Returns:
            int: Number of H gates reduced.
        """
        cnt = 0
        self.deparameterize_all(gates)
        # enumerate templates and replace every occurrence
        for template in self.hadamard_templates:
            cnt += template.replace_all(gates) * template.weight
        self.parameterize_all(gates)
        return cnt

    def cancel_single_qubit_gates(self, gates: DAG):
        """
        Merge Rz gates in Clifford+Rz circuit.
        Args:
            gates(DAG): DAG of the circuit
        Returns:
            int: Number of gates reduced.
        """
        cnt = 0
        for node in list(gates.topological_sort()):
            # enumerate every single qubit gate
            if node.gate_type != GateType.rz or node.flag == node.FLAG_ERASED:
                continue
            # erase the gate if degree = 0
            if np.isclose(float(node.params[0]), 0):
                node.erase()
                cnt += 1
                continue

            # try cancelling while commuting the gate with templates
            # (c_node, c_qubit): the position right before template matching
            c_node, c_qubit = node, 0
            while True:
                # (n_node, n_qubit): the start of template matching
                n_node, n_qubit = c_node.successors[c_qubit]
                # stop if reaching the end of circuit
                if not n_node.gate_type:
                    break

                # if n_node is another rz, merge and erase the original node
                if n_node.gate_type == node.gate_type:
                    n_node.params[0] = n_node.params[0] + node.params[0]
                    node.erase()
                    cnt += 1
                    break

                # template matching
                mapping = None
                for template in self.single_qubit_gate_templates:
                    mapping = mapping or template.compare(c_node.successors[c_qubit])
                    if mapping:
                        # found a sub-circuit that commutes
                        # set (c_node, c_qubit) to be the last position of this sub-circuit
                        c_node, c_qubit = template.template.end_nodes[template.anchor].predecessors[0]
                        c_node = mapping[id(c_node)]
                        break
                # found no templates. commuting fails
                if not mapping:
                    break
        return cnt

    class ReachableSet:
        """
        Data structure that manages the reachable relations in a DAG.

        For a DAG of over 10000 nodes, storing reachable relations between all nodes
        consumes excessive memories. ReachableSet will automatically manage and
        store recently used relations.
        """
        def __init__(self, succ_node=None, max_size=1000000):
            """
            Args:
                  succ_node(List[Tuple[DAG.Node, int]]): right boundary
                  max_size(int): max number of entries stored in this set.
            """
            self.succ_node = succ_node
            self.size = 0
            self.reachable = {}
            self.max_size = max_size

        def query(self, node, qubit_, other):
            """
            Ask whether `(node, qubit_)` can reach the node `other`.

            Args:
                node(DAG.Node): the starting node
                qubit_(int): the starting wire
                other(DAG.Node): the target node

            Returns:
                bool: whether reachable
            """
            key = (id(node), qubit_)
            if key not in self.reachable:
                new_set = DAG.get_reachable_set(node, qubit_, self.succ_node)
                if len(new_set) + self.size > self.max_size:
                    self.reachable.clear()
                self.reachable[key] = new_set
                self.size += len(new_set)

            return id(other) in self.reachable[key]

    def cancel_two_qubit_gates(self, gates: DAG):
        """
        Merge CX gate in Clifford+Rz circuit.

        Args:
            gates(DAG): DAG of the circuit
        Returns:
            int: Number of gates reduced.
        """
        cnt = 0
        reachable = self.ReachableSet()
        for node in list(gates.topological_sort()):
            # enumerate every cnot gate
            if node.flag == DAG.Node.FLAG_ERASED or node.gate_type != GateType.cx:
                continue

            c_ctrl_node, c_ctrl_qubit = node, 0
            c_targ_node, c_targ_qubit = node, 1
            while True:
                n_ctrl_node, n_ctrl_qubit = c_ctrl_node.successors[c_ctrl_qubit]
                n_targ_node, n_targ_qubit = c_targ_node.successors[c_targ_qubit]
                # remove two adjacent cnot gates
                if id(n_ctrl_node) == id(n_targ_node) and n_ctrl_node.gate_type == GateType.cx and \
                        n_ctrl_qubit == 0 and n_targ_qubit == 1:
                    n_ctrl_node.erase()
                    node.erase()
                    cnt += 2
                    break

                # try commuting node with templates anchored in control qubit
                mapping = None
                for template in self.cnot_ctrl_template:
                    mapping = template.compare(c_ctrl_node.successors[c_ctrl_qubit])
                    # After we find a template U after current cnot, there are two cases:
                    # Case 1:        .___.         .___.
                    #         --O----| U |--     --| U |---O--
                    #           |    |___|     =   |___|   |
                    #         --X-----------     ----------X--
                    # Case 2:        .___.         .___.
                    #         --O----|   |--     --|   |---O--
                    #           |    | U |    !=   | U |   |
                    #         --X----|___|--     --|___|---X--
                    # The template only guarantees control node 'O' can be moved across U, so case 2 is invalid.
                    # By further checking whether 'X' can reach any nodes in U, we can exclude case 2.

                    if mapping and all([not reachable.query(c_targ_node, c_targ_qubit, o) for o in mapping.values()]):
                        c_ctrl_node, c_ctrl_qubit = template.template.end_nodes[template.anchor].predecessors[0]
                        c_ctrl_node = mapping[id(c_ctrl_node)]
                        break
                    else:
                        mapping = None
                if mapping:
                    continue

                # try commuting node with templates anchored in target qubit
                for template in self.cnot_targ_template:
                    mapping = template.compare(c_targ_node.successors[c_targ_qubit])
                    # if control node can reach any node in the template, it will block commuting.
                    if mapping and all([not reachable.query(c_ctrl_node, c_ctrl_qubit, o) for o in mapping.values()]):
                        c_targ_node, c_targ_qubit = template.template.end_nodes[template.anchor].predecessors[0]
                        c_targ_node = mapping[id(c_targ_node)]
                        break
                    else:
                        mapping = None
                if not mapping:
                    break
        return cnt

    def _traverse_cnot_rz_circuit(self, anchor, flag_ofs=1):
        flag_visited = flag_ofs + 1
        flag_term = flag_ofs + 2

        anchors = {anchor.qubit_loc[0]: anchor, anchor.qubit_loc[1]: anchor}
        anchor_queue = deque(anchors.keys())

        term_node = {'predecessors': {}, 'successors': {}}
        while len(anchor_queue) > 0:
            anchor_qubit = anchor_queue.popleft()
            for neighbors in ['predecessors', 'successors']:
                c_node = anchors[anchor_qubit]
                c_node.qubit_flag[c_node.qubit_id[anchor_qubit]] = flag_visited
                while True:
                    p_node, p_qubit = getattr(c_node, neighbors)[c_node.qubit_id[anchor_qubit]]
                    if p_node.gate_type is None or p_node.gate_type not in [GateType.cx, GateType.x, GateType.rz]:
                        term_node[neighbors][anchor_qubit] = p_node
                        p_node.qubit_flag = [flag_term] * p_node.size
                        break
                    p_node.qubit_flag[p_qubit] = flag_visited

                    if p_node.gate_type == GateType.cx:
                        o_qubit = p_node.qubit_loc[p_qubit ^ 1]
                        if o_qubit not in anchors:
                            anchors[o_qubit] = p_node
                            anchor_queue.append(o_qubit)
                    c_node = p_node

        for neighbors in ['predecessors', 'successors']:
            prune_queue = deque()
            for anchor_qubit, anchor_node in anchors.items():
                c_node = anchors[anchor_qubit]

                while True:
                    p_node, p_qubit = getattr(c_node, neighbors)[c_node.qubit_id[anchor_qubit]]
                    if p_node.qubit_flag[p_qubit] == flag_term:
                        if id(p_node) != id(term_node[neighbors][anchor_qubit]):
                            prune_queue.append((p_node, p_qubit))
                        break

                    if p_node.gate_type == GateType.cx:
                        o_qubit = p_qubit ^ 1
                        if p_node.qubit_flag[o_qubit] != flag_visited:
                            if o_qubit == 1:  # target out of bound, skip
                                pass
                            else:  # control out of bound, terminate
                                p_node.qubit_flag[p_qubit] = flag_term
                                prune_queue.append((p_node, p_qubit))
                                break
                    c_node = p_node

            while len(prune_queue) > 0:
                c_node, c_qubit = prune_queue.popleft()
                while True:
                    p_node, p_qubit = getattr(c_node, neighbors)[c_qubit]
                    if id(p_node) == id(term_node[neighbors][p_node.qubit_loc[p_qubit]]):
                        break
                    p_node.qubit_flag[p_qubit] = flag_term
                    if p_node.gate_type is not None and p_node.gate_type == GateType.cx:
                        o_qubit = p_qubit ^ 1
                        if p_node.qubit_flag[o_qubit] == flag_visited:
                            if o_qubit == 0:
                                pass
                            else:
                                p_node.qubit_flag[o_qubit] = flag_term
                                prune_queue.append((p_node, o_qubit))
                    c_node, c_qubit = p_node, p_qubit

        left_bound = {}
        anchors = {anchor.qubit_loc[0]: anchor, anchor.qubit_loc[1]: anchor}
        anchor_queue = deque(anchors.keys())
        while len(anchor_queue) > 0:
            anchor_qubit = anchor_queue.popleft()
            for neighbors in ['predecessors', 'successors']:
                c_node = anchors[anchor_qubit]
                while True:
                    p_node, p_qubit = getattr(c_node, neighbors)[c_node.qubit_id[anchor_qubit]]
                    if p_node.qubit_flag[p_qubit] == flag_term:
                        if neighbors == 'predecessors':
                            left_bound[anchor_qubit] = (p_node, p_qubit)
                        break
                    if p_node.gate_type == GateType.cx and all([f == flag_visited for f in p_node.qubit_flag]):
                        o_qubit = p_node.qubit_loc[p_qubit ^ 1]
                        if o_qubit not in anchors:
                            anchors[o_qubit] = p_node
                            anchor_queue.append(o_qubit)
                    c_node = p_node

        edge_count = {}
        queue = deque()
        for node_, qubit_ in left_bound.values():
            s_node, s_qubit = node_.successors[qubit_]
            if s_node.qubit_flag[s_qubit] != flag_term:
                if id(s_node) not in edge_count:
                    edge_count[id(s_node)] = sum([f == flag_visited for f in s_node.qubit_flag])
                edge_count[id(s_node)] -= 1
                if edge_count[id(s_node)] == 0:
                    queue.append(s_node)

        node_list = []
        while len(queue) > 0:
            cur = queue.popleft()
            if cur.gate_type is not None and all([f == flag_visited for f in cur.qubit_flag]):
                cur.flag = cur.FLAG_VISITED
                node_list.append(cur)
            for c_qubit in range(cur.size):
                if cur.qubit_flag[c_qubit] != flag_visited:
                    continue
                s_node, s_qubit = cur.successors[c_qubit]
                if s_node is None or s_node.qubit_flag[s_qubit] == flag_term:
                    continue
                if id(s_node) not in edge_count:
                    edge_count[id(s_node)] = sum([f == flag_visited for f in s_node.qubit_flag])
                edge_count[id(s_node)] -= 1
                if edge_count[id(s_node)] == 0:
                    queue.append(s_node)
        return node_list

    def _parse_cnot_rz_circuit(self, node_list):
        phases = {}
        first_rz = {}
        cur_phases = {}

        for node_ in node_list:
            for qubit_ in node_.qubit_loc:
                if qubit_ not in cur_phases:
                    cur_phases[qubit_] = 1 << (qubit_ + 1)

            if node_.gate_type == GateType.cx:
                cur_phases[node_.qubit_loc[1]] = cur_phases[node_.qubit_loc[1]] ^ cur_phases[node_.qubit_loc[0]]
            elif node_.gate_type == GateType.x:
                cur_phases[node_.qubit_loc[0]] = cur_phases[node_.qubit_loc[0]] ^ 1
            elif node_.gate_type == GateType.rz:
                sign = -1 if cur_phases[node_.qubit_loc[0]] & 1 else 1
                mono = (cur_phases[node_.qubit_loc[0]] >> 1)
                phases[mono] = sign * node_.params[0] + (phases[mono] if mono in phases else 0)
                if mono not in first_rz:
                    first_rz[mono] = (node_, sign)
                else:
                    node_.flag = node_.FLAG_TO_ERASE

        for phase_, pack_ in first_rz.items():
            node_, sign = pack_
            if np.isclose(float(phases[phase_]), 0):
                node_.erase()
            else:
                node_.params = [sign * phases[phase_]]

        cnt = 0
        for node_ in node_list:
            if node_.gate_type != GateType.rz or node_.flag == node_.FLAG_ERASED:
                continue
            if node_.flag == node_.FLAG_TO_ERASE:
                cnt += 1
                node_.erase()
        return cnt

    def merge_rotations(self, gates: DAG):
        """
        Merge Rz gates using phase polynomials.

        Args:
            gates(DAG): DAG of the circuit
        Returns:
            int: Number of gates reduced.
        """
        gates.reset_flag()
        gates.set_qubit_loc()
        cnt = 0
        for idx, anchor_ in enumerate(list(gates.topological_sort())):
            if anchor_.gate_type != GateType.cx or anchor_.flag == anchor_.FLAG_VISITED:
                continue

            node_list = self._traverse_cnot_rz_circuit(anchor_, idx * 2)
            cnt += self._parse_cnot_rz_circuit(node_list)

        return cnt

    def _enumerate_cnot_rz_circuit(self, gates: DAG):
        """
        Iterate over CNOT+Rz sub circuit in Clifford+Rz circuit.
        Isolated Rz gates will be ignored. Each sub circuit is
        described by a tuple (left boundary, right boundary, node count). The boundary is described
        by a list whose i-th element is the tuple (node, wire) on the i-th qubit.

        Args:
            gates(DAG): DAG of the circuit

        Returns:
            Iterator[Tuple[List[DAG.Node, int]], Tuple[List[DAG.Node, int]], int]: CNOT+Rz Sub circuit
        """

        # reset qubit location of nodes in case it is corrupted sub circuit replacement
        gates.set_qubit_loc()
        # reset node flags to FLAG_DEFAULT
        gates.reset_flag()
        for node in gates.topological_sort():
            # enumerate over every unvisited CNOT gate
            if node.flag == node.FLAG_VISITED or node.gate_type != GateType.cx:
                continue

            # set of terminate node's id
            term_node_set = set()
            # encountered CNOT gates during this iteration
            # id -> Tuple[node, bitmask], bitmask(i) represents if node's i-th qubit is reachable
            visited_cnot = {}

            # STEP 1: for each anchored qubit, traverse to the left and right boundary
            anchors = {node.qubit_loc[0]: node, node.qubit_loc[1]: node}
            anchor_queue = deque(anchors.keys())
            while len(anchor_queue) > 0:
                anchor_qubit = anchor_queue.popleft()
                for neighbors in ['predecessors', 'successors']:
                    c_node = anchors[anchor_qubit]
                    while True:
                        p_node, p_qubit = getattr(c_node, neighbors)[c_node.qubit_id[anchor_qubit]]

                        # find a non CNOT+Rz gate. Set it a terminate node
                        if p_node.gate_type is None or p_node.gate_type not in \
                                [GateType.cx, GateType.x, GateType.rz] or p_node.flag == p_node.FLAG_VISITED:
                            term_node_set.add(id(p_node))
                            break

                        if p_node.gate_type == GateType.cx:
                            # encounter a new CNOT gate
                            visited_cnot[id(p_node)] = [p_node, 0b00]
                            # if we encounter a CNOT acting on a new qubit, set it as an anchor node
                            o_qubit = p_node.qubit_loc[p_qubit ^ 1]
                            if o_qubit not in anchors:
                                anchors[o_qubit] = p_node
                                anchor_queue.append(o_qubit)
                                # anchor qubit is regarded as initially reachable
                                visited_cnot[id(p_node)][1] |= 1 << (p_qubit ^ 1)

                        c_node = p_node

            # STEP 2: topologically visit the CNOT node in visited_cnot. Calculate reachable bitmasks.
            cnot_queue = deque([node])
            while len(cnot_queue) > 0:
                anchor_node = cnot_queue.popleft()
                for anchor_qubit in anchor_node.qubit_loc:
                    for neighbors in ['predecessors', 'successors']:
                        c_node = anchor_node
                        while True:
                            c_node.flag = c_node.FLAG_VISITED
                            p_node, p_qubit = getattr(c_node, neighbors)[c_node.qubit_id[anchor_qubit]]
                            if id(p_node) in term_node_set:
                                break
                            if p_node.gate_type == GateType.cx and id(p_node) in visited_cnot:
                                visited_cnot[id(p_node)][1] |= 1 << p_node.qubit_id[anchor_qubit]
                                if visited_cnot[id(p_node)][1] == 0b11 and p_node.flag == p_node.FLAG_DEFAULT:
                                    p_node.flag = p_node.FLAG_IN_QUE
                                    cnot_queue.append(p_node)
                                break
                            if p_node.flag == p_node.FLAG_VISITED:
                                break
                            c_node = p_node

            # If any of the two qubits of one CNOT is not reachable, it cannot be included
            # in the graph. Set it as terminate node.
            for list_ in visited_cnot.values():
                if list_[1] != 0b11:
                    term_node_set.add(id(list_[0]))

            # STEP 3: calculate boundary by traversing each qubit until we encounter a terminate node
            bound = {}
            visited_node = set()
            for neighbors in ['predecessors', 'successors']:
                bound[neighbors]: List[Tuple[DAG.Node, int]] = [None] * gates.width()
                for anchor_qubit, anchor_node in anchors.items():
                    if id(anchor_node) in term_node_set:
                        continue
                    c_node = anchors[anchor_qubit]
                    while True:
                        visited_node.add(id(c_node))
                        p_node, _ = getattr(c_node, neighbors)[c_node.qubit_id[anchor_qubit]]
                        if id(p_node) in term_node_set:
                            bound[neighbors][anchor_qubit] = (c_node, c_node.qubit_id[anchor_qubit])
                            break
                        c_node = p_node
            yield bound['predecessors'], bound['successors'], len(visited_node)

    def assign_symbolic_phases(self, gates: DAG):
        """
        Assign polarity to undetermined T gates in the circuit. Do it greedily to reduce gate count.

        Args:
            gates(DAG): DAG of the circuit
        Returns:
            int: Number of gates reduced.
        """
        if not gates.has_symbolic_rz:
            return 0

        # collect all variables in the circuit
        # label -> (variable, expr list)
        var_dict = {}
        for node_ in gates.topological_sort():
            if node_.gate_type == GateType.rz and isinstance(node_.params[0], SymbolicPhase):
                cur_var_dict = node_.params[0].var_dict
                for label in cur_var_dict:
                    var, _ = cur_var_dict[label]
                    if label not in var_dict:
                        var_dict[label] = [var, []]

                    var_dict[label][1].append(node_.params[0])

        ret = 0
        # greedily assign polarity to each variable
        for var, expr_list in var_dict.values():
            var.phase = np.pi / 4
            t_cnt = sum([np.isclose(expr.evaluate(), 0) for expr in expr_list])
            var.phase = -np.pi / 4
            tdg_cnt = sum([np.isclose(expr.evaluate(), 0) for expr in expr_list])
            if t_cnt >= tdg_cnt:
                var.phase = np.pi / 4

            ret += max(t_cnt, tdg_cnt)

        # replace all symbolic param with actual value
        for node_ in gates.topological_sort():
            if node_.gate_type == GateType.rz and isinstance(node_.params[0], SymbolicPhase):
                node_.params[0] = node_.params[0].evaluate()

        # evaluate global phase
        gates.global_phase = gates.global_phase.evaluate()
        gates.has_symbolic_rz = False
        return ret

    def _change_poly_phase(self, node, qubit_, delta, pos_list=None, pos_cnt=None, history=None):
        """
        Change poly phase of `node` on wire `qubit_` by incremental value `delta`.
        Either `pos_list` or `pos_cnt` should be given.
        """

        # remove old value
        cur = node.poly_phase[qubit_]
        if pos_list:
            old = (node, qubit_, cur & 1)
            pos_list[cur >> 1].remove(old)
        if pos_cnt:
            pos_cnt[cur >> 1] -= 1

        # update and add new value
        node.poly_phase[qubit_] ^= delta
        cur = node.poly_phase[qubit_]
        if pos_list:
            new = (node, qubit_, cur & 1)
            if cur >> 1 not in pos_list:
                pos_list[cur >> 1] = []
            pos_list[cur >> 1].append(new)
        if pos_cnt:
            if cur >> 1 not in pos_cnt:
                pos_cnt[cur >> 1] = 0
            pos_cnt[cur >> 1] += 1

        # record the change in history
        if history is not None:
            history.append((node, qubit_, delta))

    def _erase_from_pos_list(self, node, pos_list):
        """
        Maintain floating position list `pos_list` when erasing `node`.
        """
        for qubit_ in range(node.size):
            cur = node.poly_phase[qubit_]
            old = (node, qubit_, cur & 1)
            pos_list[cur >> 1].remove(old)

    def _check_float_pos(self, node, qubit_, phases, pos_list=None, pos_cnt=None):
        """
        Check whether it is valid to change the poly phase of `node` on wire `qubit_`.
        """
        cur = node.poly_phase[qubit_] >> 1
        if cur not in phases or np.isclose(float(phases[cur]), 0):
            return True
        else:
            if pos_list:
                return len(pos_list[cur]) > 1
            else:
                return pos_cnt[cur] > 1

    def _float_cancel_sub_circuit(self, prev_node, succ_node):
        """
        Do float two qubit cancelling in sub circuit.
        """
        # calculate floating positions
        phases = {}
        cur_phases = {}
        pos_list = {}

        # put right bound into a set
        term_set = set()
        for node_, qubit_ in filter(lambda x: x is not None, succ_node):
            term_set.add(id(node_))

        # STEP 1: calculate poly phase of all positions in the circuit
        for qubit_, pack in enumerate(prev_node):
            if pack is not None:
                node_, wire_ = pack
                cur_phases[qubit_] = 1 << (qubit_ + 1)
                pos_list[1 << qubit_] = [(node_, wire_, 0)]

        rz_cnt = 0
        for node_ in list(DAG.topological_sort_sub_circuit(prev_node, succ_node)):
            if node_.gate_type == GateType.cx:
                cur_phases[node_.qubit_loc[1]] = cur_phases[node_.qubit_loc[1]] ^ cur_phases[node_.qubit_loc[0]]
                node_.poly_phase = [cur_phases[node_.qubit_loc[0]], cur_phases[node_.qubit_loc[1]]]
                for qubit_ in range(2):
                    cur = node_.poly_phase[qubit_]
                    if cur >> 1 not in pos_list:
                        pos_list[cur >> 1] = []
                    pos_list[cur >> 1].append((node_, qubit_, cur & 1))

            elif node_.gate_type == GateType.x:
                cur_phases[node_.qubit_loc[0]] = cur_phases[node_.qubit_loc[0]] ^ 1
                node_.poly_phase = [cur_phases[node_.qubit_loc[0]]]
                cur = node_.poly_phase[0]
                if cur >> 1 not in pos_list:
                    pos_list[cur >> 1] = []
                pos_list[cur >> 1].append((node_, 0, cur & 1))

            elif node_.gate_type == GateType.rz:
                # remove rz gates (later we put it back)
                rz_cnt += 1
                sign = -1 if cur_phases[node_.qubit_loc[0]] & 1 else 1
                mono = (cur_phases[node_.qubit_loc[0]] >> 1)
                phases[mono] = sign * node_.params[0] + (phases[mono] if mono in phases else 0)
                node_.erase()

        # STEP 2: cancel cx gates
        cnt = 0

        reachable = DAG.get_sub_circuit_reachable_relation(prev_node, succ_node)
        for cx in list(DAG.topological_sort_sub_circuit(prev_node, succ_node)):
            if cx.gate_type != GateType.cx or cx.flag == cx.FLAG_ERASED:
                continue

            change_history = []
            success = False
            c_ctrl_node, c_ctrl_qubit = cx, 0
            c_targ_node, c_targ_qubit = cx, 1
            while True:
                n_ctrl_node, n_ctrl_qubit = c_ctrl_node.successors[c_ctrl_qubit]
                n_targ_node, n_targ_qubit = c_targ_node.successors[c_targ_qubit]

                # find cancellation
                if id(n_ctrl_node) == id(n_targ_node) and n_ctrl_node.gate_type == GateType.cx and \
                        n_ctrl_qubit == 0 and n_targ_qubit == 1:

                    # cancellation failed
                    if not self._check_float_pos(cx, 1, phases, pos_list=pos_list):
                        break

                    # cancellation succeeded, maintain pos_list and erase nodes
                    success = True
                    self._erase_from_pos_list(n_ctrl_node, pos_list)
                    self._erase_from_pos_list(cx, pos_list)
                    n_ctrl_node.erase()
                    cx.erase()
                    cnt += 2
                    break

                if id(n_ctrl_node) not in term_set and \
                        n_ctrl_node.gate_type == GateType.cx and \
                        n_ctrl_qubit == 0 and \
                        ((id(c_targ_node), c_targ_qubit), id(n_ctrl_node)) not in reachable:
                    # Case A: share control
                    # ---O--O--
                    # ---|--|--
                    # ---X--|--
                    # ------X--
                    c_ctrl_node, c_ctrl_qubit = n_ctrl_node, n_ctrl_qubit

                elif id(n_targ_node) not in term_set and \
                        n_targ_node.gate_type == GateType.cx and \
                        n_targ_qubit == 1 and \
                        ((id(c_ctrl_node), c_ctrl_qubit), id(n_targ_node)) not in reachable and \
                        self._check_float_pos(cx, 1, phases, pos_list=pos_list):
                    # Case B: share target
                    # ---X--X--
                    # ---|--|--
                    # ---O--|--
                    # ------O--
                    self._change_poly_phase(cx, 1, n_targ_node.poly_phase[0], pos_list=pos_list, history=change_history)
                    self._change_poly_phase(n_targ_node, 1, cx.poly_phase[0], pos_list=pos_list, history=change_history)

                    c_targ_node, c_targ_qubit = n_targ_node, n_targ_qubit

                elif id(n_targ_node) not in term_set and n_targ_node.gate_type == GateType.x and \
                        self._check_float_pos(cx, 1, phases, pos_list=pos_list):
                    # Case C: X gate on target
                    # ---O-----
                    # ---|-----
                    # ---X--X--
                    self._change_poly_phase(cx, 1, 1, pos_list=pos_list, history=change_history)
                    self._change_poly_phase(n_targ_node, 0, cx.poly_phase[0], pos_list=pos_list, history=change_history)

                    c_targ_node, c_targ_qubit = n_targ_node, n_targ_qubit
                else:
                    break

            # undo changes if no cancellation found
            if not success:
                for node_, qubit_, delta_ in reversed(change_history):
                    self._change_poly_phase(node_, qubit_, delta_, pos_list=pos_list)

        # put back Rz
        for mono, phase in phases.items():
            if np.isclose(float(phase), 0):
                continue
            rz_cnt -= 1
            c_node, c_qubit, sign = pos_list[mono][0]
            r_node = DAG.Node(Rz(0) & c_node.qubit_loc[c_qubit])
            r_node.params = [phase if sign == 0 else -phase]
            c_node.append(c_qubit, 0, r_node)
        return cnt + rz_cnt

    def float_cancel_two_qubit_gates(self, gates):
        """
        Merge CX gates in the circuit while considering float positions of Rz gates.

        Args:
            gates(DAG): DAG of the circuit
        Returns:
            int: Number of gates reduced.
        """
        gates.reset_flag()
        gates.set_qubit_loc()
        cnt = 0
        for prev_node, succ_node, node_cnt in list(self._enumerate_cnot_rz_circuit(gates)):
            # the boundary given by enumerate_cnot_rz_circuit is described by internal node of
            # the sub circuit, but PhasePolynomial and replace method need eternal boundary.
            # This conversion is necessary because nodes in eternal boundary may change due to previous iteration.
            for qubit_ in range(gates.width()):
                if prev_node[qubit_] is not None:
                    c_node, c_qubit = prev_node[qubit_]
                    prev_node[qubit_] = c_node.predecessors[c_qubit]
                    c_node, c_qubit = succ_node[qubit_]
                    succ_node[qubit_] = c_node.successors[c_qubit]
            cnt += self._float_cancel_sub_circuit(prev_node, succ_node)
        return cnt

    def _try_float_cancel_sub_circuit(self, prev_node, succ_node):
        """
        Test whether float_cancel_sub_circuit can find cancellation in this sub circuit.
        The difference with `_float_cancel_sub_circuit` is that we do not change the circuit.
        Thus instead of recording every possible floating position, we only record the count of them.
        """

        phases = {}
        cur_phases = {}
        pos_cnt = {}

        # put right bound into a set
        term_set = set()
        for node_, qubit_ in filter(lambda x: x is not None, succ_node):
            term_set.add(id(node_))

        # STEP 1: calculate poly phase of all positions in the circuit
        for qubit_, pack in enumerate(prev_node):
            if pack is not None:
                cur_phases[qubit_] = 1 << (qubit_ + 1)
                pos_cnt[1 << qubit_] = 1

        rz_cnt = 0
        for node_ in list(DAG.topological_sort_sub_circuit(prev_node, succ_node)):
            if node_.gate_type == GateType.cx:
                cur_phases[node_.qubit_loc[1]] = cur_phases[node_.qubit_loc[1]] ^ cur_phases[node_.qubit_loc[0]]
                node_.poly_phase = [cur_phases[node_.qubit_loc[0]], cur_phases[node_.qubit_loc[1]]]
                for qubit_ in range(2):
                    cur = node_.poly_phase[qubit_]
                    if cur >> 1 not in pos_cnt:
                        pos_cnt[cur >> 1] = 0
                    pos_cnt[cur >> 1] += 1

            elif node_.gate_type == GateType.x:
                cur_phases[node_.qubit_loc[0]] = cur_phases[node_.qubit_loc[0]] ^ 1
                node_.poly_phase = [cur_phases[node_.qubit_loc[0]]]
                cur = node_.poly_phase[0]
                if cur >> 1 not in pos_cnt:
                    pos_cnt[cur >> 1] = 0
                pos_cnt[cur >> 1] += 1

            elif node_.gate_type == GateType.rz:
                rz_cnt += 1
                sign = -1 if cur_phases[node_.qubit_loc[0]] & 1 else 1
                mono = (cur_phases[node_.qubit_loc[0]] >> 1)
                phases[mono] = sign * node_.params[0] + (phases[mono] if mono in phases else 0)

        # return True if we can merge some Rz gates
        for phase in phases.values():
            if not np.isclose(float(phase), 0):
                rz_cnt -= 1
        if rz_cnt > 0:
            return True

        # STEP 2: try cx cancellation
        reachable = DAG.get_sub_circuit_reachable_relation(prev_node, succ_node)
        for cx in list(DAG.topological_sort_sub_circuit(prev_node, succ_node)):
            if cx.gate_type != GateType.cx or cx.flag == cx.FLAG_ERASED:
                continue

            change_history = []
            c_ctrl_node, c_ctrl_qubit = cx, 0
            c_targ_node, c_targ_qubit = cx, 1
            while True:
                n_ctrl_node, n_ctrl_qubit = c_ctrl_node.successors[c_ctrl_qubit]
                n_targ_node, n_targ_qubit = c_targ_node.successors[c_targ_qubit]
                if id(n_ctrl_node) == id(n_targ_node) and n_ctrl_node.gate_type == GateType.cx and \
                        n_ctrl_qubit == 0 and n_targ_qubit == 1:
                    if not self._check_float_pos(cx, 1, phases, pos_cnt=pos_cnt):
                        break
                    return True

                if id(n_ctrl_node) not in term_set and n_ctrl_node.gate_type == GateType.rz:
                    # Extra Case 1
                    # --O--Rz--
                    # --|------
                    # --X------
                    c_ctrl_node, c_ctrl_qubit = n_ctrl_node, n_ctrl_qubit
                elif id(n_targ_node) not in term_set and n_targ_node.gate_type == GateType.rz:
                    # Extra Case 2
                    # --O------
                    # --|------
                    # --X--Rz--
                    c_targ_node, c_targ_qubit = n_targ_node, n_targ_qubit
                elif id(n_ctrl_node) not in term_set and \
                        n_ctrl_node.gate_type == GateType.cx and \
                        n_ctrl_qubit == 0 and \
                        ((id(c_targ_node), c_targ_qubit), id(n_ctrl_node)) not in reachable:
                    # Case A: share control
                    # ---O--O--
                    # ---|--|--
                    # ---X--|--
                    # ------X--
                    c_ctrl_node, c_ctrl_qubit = n_ctrl_node, n_ctrl_qubit

                elif id(n_targ_node) not in term_set and \
                        n_targ_node.gate_type == GateType.cx and \
                        n_targ_qubit == 1 and \
                        ((id(c_ctrl_node), c_ctrl_qubit), id(n_targ_node)) not in reachable and \
                        self._check_float_pos(cx, 1, phases, pos_cnt=pos_cnt):
                    # Case B: share target
                    # ---X--X--
                    # ---|--|--
                    # ---O--|--
                    # ------O--
                    self._change_poly_phase(cx, 1, n_targ_node.poly_phase[0], pos_cnt=pos_cnt, history=change_history)
                    self._change_poly_phase(n_targ_node, 1, cx.poly_phase[0], pos_cnt=pos_cnt, history=change_history)

                    c_targ_node, c_targ_qubit = n_targ_node, n_targ_qubit

                elif id(n_targ_node) not in term_set and n_targ_node.gate_type == GateType.x and \
                        self._check_float_pos(cx, 1, phases, pos_cnt=pos_cnt):
                    # Case C: X gate on target
                    # ---O-----
                    # ---|-----
                    # ---X--X--
                    self._change_poly_phase(cx, 1, 1, pos_cnt=pos_cnt, history=change_history)
                    self._change_poly_phase(n_targ_node, 0, cx.poly_phase[0], pos_cnt=pos_cnt, history=change_history)

                    c_targ_node, c_targ_qubit = n_targ_node, n_targ_qubit
                else:
                    break

            for node_, qubit_, delta_ in reversed(change_history):
                self._change_poly_phase(node_, qubit_, delta_, pos_cnt=pos_cnt)

        return False

    def try_float_cancel_two_qubit_gates(self, gates):
        """
        Test whether float_cancel_two_qubit_gates can reduce gate count in the current circuit.

        Args:
            gates(DAG): DAG of the circuit
        Returns:
            bool: whether float_cancel_two_qubit_gates can reduce gate count
        """

        gates.reset_flag()
        gates.set_qubit_loc()
        for prev_node, succ_node, node_cnt in list(self._enumerate_cnot_rz_circuit(gates)):
            # the boundary given by enumerate_cnot_rz_circuit is described by internal node of
            # the sub circuit, but PhasePolynomial and replace method need eternal boundary.
            # This conversion is necessary because nodes in eternal boundary may change due to previous iteration.
            for qubit_ in range(gates.width()):
                if prev_node[qubit_] is not None:
                    c_node, c_qubit = prev_node[qubit_]
                    prev_node[qubit_] = c_node.predecessors[c_qubit]
                    c_node, c_qubit = succ_node[qubit_]
                    succ_node[qubit_] = c_node.successors[c_qubit]
            if self._try_float_cancel_sub_circuit(prev_node, succ_node):
                return True

        return False

    def gate_preserving_rewrite(self, gates):
        """
        Reduce gate count by gate preserving rewrite rules.

        Args:
            gates(DAG): DAG of the circuit
        Returns:
            int: Number of gates reduced.
        """

        cnt = 0
        success = True
        while success:
            success = False
            for template in self.gate_preserving_rewrite_template:
                for node in gates.topological_sort():
                    mapping = template.compare((node, -1), dummy_rz=True)
                    if not mapping:
                        continue
                    original, undo_mapping = template.regrettable_replace(mapping)

                    if self.try_float_cancel_two_qubit_gates(gates):
                        # if rewriting enables cancellation else where, do it and restart template matching
                        cnt += self.float_cancel_two_qubit_gates(gates)
                        success = True
                        break

                    # undo replacing if otherwise
                    template.undo_replace(original, undo_mapping)
                if success:
                    break
        return cnt

    def gate_reducing_rewrite(self, gates):
        """
        Reduce gate count by gate reducing rewrite rules.

        Args:
            gates(DAG): DAG of the circuit
        Returns:
            int: Number of gates reduced.
        """
        cnt = 0
        for template in self.gate_reducing_rewrite_template:
            cnt += template.replace_all(gates) * template.weight
        if cnt:
            cnt += self.float_cancel_two_qubit_gates(gates)
            cnt += self.cancel_two_qubit_gates(gates)
        return cnt

    def float_rotations(self, gates: DAG):
        """
        Reduce gate count by considering float positions of Rz gates.

        Args:
            gates(DAG): DAG of the circuit
        Returns:
            int: Number of gates reduced.
        """
        cnt = 0
        cnt += self.float_cancel_two_qubit_gates(gates)
        cnt += self.gate_preserving_rewrite(gates)
        cnt += self.gate_reducing_rewrite(gates)
        return cnt

    def __init__(self, level='light', optimize_toffoli=True, verbose=False):
        """
        Heuristic optimization of circuits in Clifford + Rz.

        Args:
              level(str): Support 'light' and 'heavy' level. See details in [1]
              optimize_toffoli(bool): whether decompose and optimize ccx/ccz gates into Clifford+rz
              verbose(bool): whether output details of each step

        [1] Nam, Yunseong, et al. "Automated optimization of large quantum
        circuits with continuous parameters." npj Quantum Information 4.1
        (2018): 1-12.
        """
        assert level in self._optimize_routine, Exception(f'unrecognized level {level}')
        self.level = level
        self.verbose = verbose
        self.optimize_toffoli = optimize_toffoli

    def __repr__(self):
        return f'CliffordRzOptimization(level={self.level}, ' \
               f'optimize_toffoli={self.optimize_toffoli})'

    @OutputAligner()
    def execute(self, gates):
        """
        Heuristic optimization of circuits in Clifford + Rz.

        Args:
              gates(Circuit): Circuit to be optimized

        Returns:
            Circuit: The circuit after optimization

        [1] Nam, Yunseong, et al. "Automated optimization of large quantum
        circuits with continuous parameters." npj Quantum Information 4.1
        (2018): 1-12.
        """
        routine = self._optimize_routine[self.level]
        _gates = DAG(gates, self.optimize_toffoli)
        self.parameterize_all(_gates)

        gate_cnt = 0
        round_cnt = 0
        total_time = 0

        while True:
            round_cnt += 1
            if self.verbose:
                print(f'ROUND #{round_cnt}:')

            cnt = 0
            # apply each method in routine
            for step in routine:
                start_time = time.time()
                cur_cnt = getattr(self, self._optimize_sub_method[step])(_gates)
                end_time = time.time()

                if self.verbose:
                    print(f'\t{self._optimize_sub_method[step]}: {cur_cnt} '
                          f'gates reduced, cost {np.round(end_time - start_time, 3)} s')

                cnt += cur_cnt
                total_time += end_time - start_time

            if cnt == 0:
                # assign symbolic t gates for nearly optimized circuit
                start_time = time.time()
                cnt += self.assign_symbolic_phases(_gates)
                end_time = time.time()
                if self.verbose:
                    print(f'\tassign_symbolic_phases: {cnt} '
                          f'gates reduced, cost {np.round(end_time - start_time, 3)} s')

                # stop if nothing can be optimized
                if cnt == 0:
                    break

            gate_cnt += cnt

        self.deparameterize_all(_gates)
        ret = _gates.get_circuit()

        if self.verbose:
            print(f'initially {_gates.init_size} gates, '
                  f'remain {ret.size()} gates, cost {np.round(total_time, 3)} s')
        return ret
