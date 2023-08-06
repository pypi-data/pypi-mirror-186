import itertools
from typing import List

from .backward_match import BackwardMatch
from .forward_match import ForwardMatch
from .matching_dag_circuit import Match, MatchingDAGCircuit


class TemplateMatching:
    """
    [1] Iten, R., Moyard, R., Metger, T., Sutter, D. and Woerner, S., 2020.
    Exact and practical pattern matching for quantum circuit optimization.
    `arXiv:1909.05270 <https://arxiv.org/abs/1909.05270>`
    """

    @classmethod
    def _qubit_fixing(cls,
                      circuit: MatchingDAGCircuit,
                      template: MatchingDAGCircuit,
                      c_node_id: int,
                      t_node_id: int,
                      cnt: int):
        """
        Heuristic qubit algorithm. It will explore `cnt` more gate (if possible)
        and return the set of qubits these gates act on.
        """

        t_successors = template.all_successors(t_node_id)
        c_successors = circuit.all_successors(c_node_id)

        if len(t_successors) > (template.size - t_node_id - 1) / 2:
            # explore backwards
            cands = sorted(c_successors)
        else:
            # explore forwards
            cands = sorted(set(range(circuit.size)) - set(c_successors), reverse=True)

        ret = set(circuit.get_node(c_node_id).qargs)
        for cand in cands[: cnt]:
            cur = ret | set(circuit.get_node(cand).qargs)
            if len(cur) > template.width:
                break
            ret = cur
        return list(ret)

    @classmethod
    def execute(cls,
                circuit: MatchingDAGCircuit,
                template: MatchingDAGCircuit,
                qubit_fixing_param: List[int] = None,
                prune_param: List[int] = None
                ):
        """
        Execute the template matching algorithm. It match `circuit` with `template` and return
        all maximal matches start from every qubit as a list.

        Heuristic qubit parameters `qubit_fixing_param` is in the form [cnt] where `cnt` is
        the number of additional qubits explored when enumerating the qubit mapping (recommended
        value is 1).

        Heuristic backward match parameter `prune_param` is in the form [D, W]. Backward match
        will prune the search tree when depth=k*D (k = 1, 2, ...) and at most W maximal matching
        scenarios will survive (recommended value is [3, 1]).

        Above two heuristic algorithms will be executed only when the corresponding parameter is
        specified.

        Args:
            circuit(MatchingDAGCircuit): the circuit to match
            template(MatchingDAGCircuit): the template to be matched
            qubit_fixing_param(List[int]): Heuristic qubit parameters
            prune_param(List[int]): Heuristic backward match parameter

        Returns:
            List[Match]: List of matches
        """

        match_set = set()

        # enumerate the starting node of template
        for t_node_id in range(template.size):
            # enumerate the starting node of circuit
            for c_node_id in range(circuit.size):
                t_node = template.get_node(t_node_id)
                c_node = circuit.get_node(c_node_id)
                if not t_node.compare_with(c_node):
                    continue

                # heuristically fixed qubits
                fixed_q = cls._qubit_fixing(circuit, template, c_node_id, t_node_id, *qubit_fixing_param) \
                    if qubit_fixing_param else []

                # enumerate free qubits
                all_free_q = set(range(circuit.width)) - set(fixed_q)
                for free_q in itertools.combinations(all_free_q, template.width - len(fixed_q)):
                    q_set = list(free_q) + fixed_q
                    # enumerate permutation
                    for mapping in itertools.permutations(q_set, template.width):
                        if not t_node.compare_with(c_node, mapping):
                            continue

                        forward_match = ForwardMatch.execute(
                            circuit, template, c_node_id, t_node_id, list(mapping))

                        match_list = BackwardMatch.execute(
                            circuit, template, forward_match, c_node_id, t_node_id, list(mapping), prune_param)
                        match_set.update(match_list)

        return list(match_set)
