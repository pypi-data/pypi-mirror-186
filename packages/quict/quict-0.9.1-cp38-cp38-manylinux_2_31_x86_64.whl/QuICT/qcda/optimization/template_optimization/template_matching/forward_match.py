from typing import List, Tuple

from .matching_dag_circuit import MatchingDAGCircuit, MatchingDAGNode


class ForwardMatch:
    """
    Class for forward matching.
    """

    @classmethod
    def _insert_match_nodes(cls, match_nodes: List[MatchingDAGNode], node: MatchingDAGNode):
        """
        Insert a node to `matched_node` list. Then sorted the list in increasing order of
        the first element of `successors_to_visit`.
        """
        if len(node.successors_to_visit) > 0:
            match_nodes.append(node)
            match_nodes.sort(key=lambda n: n.successors_to_visit[0])

    @classmethod
    def _find_candidates(cls,
                         match: List[Tuple[int, int]],
                         template: MatchingDAGCircuit,
                         t_node_id: int) -> List[MatchingDAGNode]:
        """
        Find valid candidates for next match
        """
        match = {match[i][0] for i in range(len(match))}

        block = set()
        for u in match - {t_node_id}:
            for v in template.get_node(u).successors:
                if v not in match:
                    block |= template.all_successors(v)

        id_set = set(template.get_node(t_node_id).successors) - match - block
        return [template.get_node(i) for i in id_set]

    @classmethod
    def execute(cls,
                circuit: MatchingDAGCircuit,
                template: MatchingDAGCircuit,
                c_node_id: int,
                t_node_id: int,
                qubit_mapping: List[int]):
        """
        Execute Forward matching.

        Args:
            circuit(MatchingDAGCircuit): the circuit to match
            template(MatchingDAGCircuit): the template to be matched
            c_node_id(int): the starting node of `circuit`
            t_node_id(int): the starting node of `template`
            qubit_mapping(List[int]): qubit mapping
                (qubit i in `temlate` is mapped to qubit_mapping[i] is circuit)

        Returns:
            List[Tuple[int, int]]: the maximal match (template node id, circuit node id)'s
        """

        # initialize properties
        circuit.init_forward_matching(c_node_id, t_node_id, s2v_enabled=True)
        template.init_forward_matching(t_node_id, c_node_id)

        match = [(t_node_id, c_node_id)]
        match_nodes = [circuit.get_node(c_node_id)]
        while len(match_nodes) > 0:
            # every time match the first element of successors_to_visit of one node
            cur_node: MatchingDAGNode = match_nodes[0]
            match_nodes.pop(0)

            nxt_node_id = cur_node.pop_successors_to_visit()
            if nxt_node_id is None:
                continue
            nxt_node = circuit.get_node(nxt_node_id)

            if cur_node.successors_to_visit:
                cls._insert_match_nodes(match_nodes, cur_node)

            if not nxt_node.matchable():
                continue

            cands: List[MatchingDAGNode] = cls._find_candidates(match, template, cur_node.matched_with)
            success = False
            for t_nxt_node in cands:
                if t_nxt_node.compare_with(nxt_node, qubit_mapping):
                    t_nxt_node.matched_with = nxt_node.id
                    nxt_node.matched_with = t_nxt_node.id
                    match.append((t_nxt_node.id, nxt_node.id))

                    # calc nxt_node.successors_to_visit
                    nxt_node.successors_to_visit = sorted(list(filter(
                        lambda x: circuit.get_node(x).matchable,
                        nxt_node.successors
                    )))
                    # match_nodes.append(nxt_node)
                    cls._insert_match_nodes(match_nodes, nxt_node)

                    success = True
                    break

            if not success:
                # if not succeeded, block the node and all its successors
                nxt_node.is_blocked = True
                for node_id in circuit.all_successors(nxt_node.id):
                    succ_node = circuit.get_node(node_id)

                    succ_node.is_blocked = True
                    # remove matched info
                    if succ_node.matched_with:
                        t = succ_node.matched_with
                        template.get_node(t).matched_with = None
                        succ_node.matched_with = None
                        match.remove((t, succ_node.id))

        return match
