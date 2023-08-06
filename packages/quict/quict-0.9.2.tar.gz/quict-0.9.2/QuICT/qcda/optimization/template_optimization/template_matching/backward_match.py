import heapq
from collections import deque
from typing import List, Tuple

from .matching_dag_circuit import (Match, MatchingDAGCircuit, MatchingDAGNode,
                                   NodeInfo)


class MatchingScenario:
    """
    Class for matching scenario in backward searching tree
    """
    def __init__(self, circuit_info, template_info, match, counter):
        """
        Args:
            circuit_info(List[NodeInfo]): node infos of circuit
            template_info(List[NodeInfo]): node infos of template
            match(List[Tuple[int, int]]): current match info
            counter(int): number of gates visited
        """
        self.circuit_info = circuit_info
        self.template_info = template_info
        self.match = match.copy()
        self.counter = counter


class BackwardMatch:
    """
    Class for backward matching.
    """

    @classmethod
    def _calc_gate_indices(cls, circuit: MatchingDAGCircuit):
        """
        Returns:
             List[int]: the list of gate to backward match
        """
        return list(filter(
            lambda i: circuit.get_node(i).matchable(),
            reversed(range(circuit.size))
        ))

    @classmethod
    def _find_candidates(cls, match, template, template_info, t_node_id) -> List[MatchingDAGNode]:
        """
        Find candidate for next match.
        """
        successors = set(template.all_successors(t_node_id))

        matches = {m[0] for m in match}
        ret = sorted(filter(
            lambda x: x not in successors and x not in matches and not template_info[x].is_blocked,
            range(t_node_id + 1, template.size)
        ), reverse=True)

        return [template.get_node(i) for i in ret]

    @classmethod
    def _prune(cls, scenarios: deque, gate_indices, depth, width):
        """
        Heuristic backward matching algorithm.
        """
        counters = [s.counter for s in scenarios]
        if counters.count(max(counters)) == len(counters) and counters[0] < len(gate_indices) \
                and counters[0] % depth == 0:
            ret = deque(heapq.nlargest(width, scenarios, key=lambda s: len(s.match)))
            return ret
        return scenarios

    @classmethod
    def _left_block(cls,
                    circuit: MatchingDAGCircuit,
                    template: MatchingDAGCircuit,
                    scenario: MatchingScenario,
                    c_node_id: int):
        """
        Block a node and all its predecessors in circuit.
        """
        c_info = scenario.circuit_info.copy()
        t_info = scenario.template_info.copy()
        match = scenario.match.copy()
        counter = scenario.counter

        c_info[c_node_id] = NodeInfo(None, True)
        for c_nxt_id in circuit.all_predecessors(c_node_id):
            c_info[c_nxt_id] = NodeInfo(None, True)

        nxt_scenario = MatchingScenario(c_info, t_info, match, counter + 1)
        return nxt_scenario

    @classmethod
    def _right_block(cls,
                     circuit: MatchingDAGCircuit,
                     template: MatchingDAGCircuit,
                     scenario: MatchingScenario,
                     c_node_id: int):
        """
        Block a node and all its successors in circuit.
        """
        c_info = scenario.circuit_info.copy()
        t_info = scenario.template_info.copy()
        match = scenario.match
        counter = scenario.counter

        c_info[c_node_id] = NodeInfo(None, True)

        broken_match = []
        for c_nxt_id in circuit.all_successors(c_node_id):
            t_nxt_id = c_info[c_nxt_id].matched_with
            if t_nxt_id is not None:
                broken_match.append(t_nxt_id)
                t_info[t_nxt_id] = NodeInfo(None, False)
            c_info[c_nxt_id] = NodeInfo(None, True)

        new_match = list(filter(lambda x: x[0] not in broken_match, match))
        nxt_scenario = MatchingScenario(c_info, t_info, new_match, counter + 1)

        return broken_match, nxt_scenario

    @classmethod
    def execute(cls,
                circuit: MatchingDAGCircuit,
                template: MatchingDAGCircuit,
                forward_match: List[Tuple[int, int]],
                c_node_id: int,
                t_node_id: int,
                qubit_mapping: List[int],
                prune_param=None) -> List[Match]:
        """
        Execute backward matching algorithm.

        Args:
            circuit(MatchingDAGCircuit): the circuit to match
            template(MatchingDAGCircuit): the template to be matched
            forward_match(List[Tuple[int, int]]): matches by Forward matching
            c_node_id(int): the starting node of `circuit`
            t_node_id(int): the starting node of `template`
            qubit_mapping(List[int]): qubit mapping
                (qubit i in `temlate` is mapped to qubit_mapping[i] is circuit)
            prune_param(List[int]): heuristic backward matching parameters

        Returns:
            List[Match]: List of maximal matches found
        """

        # the list of id's of gate to match in circuit
        gate_indices = cls._calc_gate_indices(circuit)
        scenarios = deque([
            MatchingScenario(
                circuit.matching_info(),
                template.matching_info(),
                forward_match,
                0
            )
        ])

        # remaining number of gates to match in template (given by the paper, not sure why)
        remain_cnt = template.size - t_node_id - len(forward_match)

        res = []
        while len(scenarios) > 0:
            if prune_param is not None:
                scenarios = cls._prune(scenarios, gate_indices, *prune_param)

            # extract current scenario
            cur_scenario = scenarios.popleft()
            c_info = cur_scenario.circuit_info
            t_info = cur_scenario.template_info
            match = cur_scenario.match
            counter = cur_scenario.counter
            backward_match = list(filter(lambda x: x not in forward_match, match))

            # match found if all nodes in circuit visited or all gates in template matched
            if counter >= len(gate_indices) or len(backward_match) == remain_cnt:
                res.append(Match(match, qubit_mapping))
                continue

            cur_c_node_id = gate_indices[counter]
            cur_c_node: MatchingDAGNode = circuit.get_node(cur_c_node_id)
            if c_info[cur_c_node_id].is_blocked:
                # continue if current node cannot be matched
                nxt_scenario = MatchingScenario(c_info, t_info, match, counter + 1)
                scenarios.append(nxt_scenario)
                continue

            cands = cls._find_candidates(match, template, t_info, t_node_id)
            flag_broken = True  # if all possible matches will break sth
            flag_succeed = False  # if there is possible match

            for cur_t_node in cands:
                # FIXME remove identical matches

                if cur_t_node.compare_with(cur_c_node, qubit_mapping):
                    # option 1.1: match the gate and block unconnected matches
                    cur_c_info = c_info.copy()
                    cur_t_info = t_info.copy()
                    cur_match = match.copy()

                    broken_match = []

                    for block_id in template.all_successors(cur_t_node.id):
                        if cur_t_info[block_id].matched_with is None:
                            cur_t_info[block_id] = NodeInfo(None, True)

                            for t_nxt_id in template.all_successors(block_id):
                                c_nxt_id = cur_t_info[t_nxt_id].matched_with
                                if c_nxt_id is not None:
                                    cur_c_info[c_nxt_id] = NodeInfo(None, True)
                                    broken_match.append(t_nxt_id)
                                cur_t_info[t_nxt_id] = NodeInfo(None, True)

                    flag_broken &= len(broken_match) > 0
                    new_match = list(filter(lambda x: x[0] not in broken_match, cur_match))

                    # check if fixed match is unchanged
                    if (t_node_id, c_node_id) in new_match and \
                            all(map(lambda x: x in new_match, backward_match)):
                        cur_t_info[cur_t_node.id] = NodeInfo(cur_c_node_id, False)
                        cur_c_info[cur_c_node_id] = NodeInfo(cur_t_node.id, False)
                        new_match.append((cur_t_node.id, cur_c_node_id))
                        nxt_scenario = MatchingScenario(cur_c_info, cur_t_info, new_match, counter + 1)
                        scenarios.append(nxt_scenario)

                        flag_succeed = True

            if flag_succeed:
                # option 1.2: right block the node (available if matching succeeded)
                broken_match, nxt_scenario = cls._right_block(circuit, template, cur_scenario, cur_c_node_id)

                if (t_node_id, c_node_id) in nxt_scenario.match and \
                        all(map(lambda x: x in nxt_scenario.match, backward_match)):
                    scenarios.append(nxt_scenario)

                if broken_match and flag_broken:
                    # option 1.3: left block the node (available if all above options break previous matches)
                    nxt_scenario = cls._left_block(circuit, template, cur_scenario, cur_c_node_id)
                    scenarios.append(nxt_scenario)
            else:
                # option 2: if no match found, block it
                c_info[cur_c_node_id] = NodeInfo(None, True)
                following_match = list(filter(
                    lambda i: c_info[i].matched_with is not None,
                    circuit.all_successors(cur_c_node_id)
                ))

                if not following_match or not cur_c_node.predecessors:
                    # option 2.1: if block it affect nothing, do it.
                    nxt_scenario = MatchingScenario(c_info, t_info, match, counter + 1)
                    scenarios.append(nxt_scenario)
                else:
                    # option 2.2: left block it
                    nxt_scenario = cls._left_block(circuit, template, cur_scenario, cur_c_node_id)
                    scenarios.append(nxt_scenario)

                    # option 2.3: right block it
                    broken_match, nxt_scenario = cls._right_block(circuit, template, cur_scenario, cur_c_node_id)
                    if (t_node_id, c_node_id) in nxt_scenario.match and \
                            all(map(lambda x: x in nxt_scenario.match, backward_match)):
                        scenarios.append(nxt_scenario)

        # return distinct matches of maximal length
        max_len = max(len(match) for match in res)
        maximal_res = filter(lambda m: len(m) == max_len, res)
        return list(set(maximal_res))
