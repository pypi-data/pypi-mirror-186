from typing import Dict, List, Tuple

from QuICT.core import *
from QuICT.core.gate import *

from .dag import DAG


class OptimizingTemplate:
    """
    Circuit template used in AutoOptimization.
    """
    def __init__(self, template: DAG, replacement: DAG = None,
                 anchor: int = 0, weight: int = 1, phase: float = 0):
        """
        Args:
            template(DAG): template circuit
            replacement(DAG): replacement circuit
            anchor(int): starting qubit of comparison with `template`
            weight(int): weight of this template
            phase(float): global phase. exp(`phase` * pi) * `replacement` == `template`
        """
        self.template = template
        self.replacement = replacement
        self.anchor = anchor
        self.weight = weight
        self.phase = phase

    def compare(self, other: Tuple[DAG.Node, int], flag_enabled=False, dummy_rz=False):
        """
        Compare the other circuit with template.
        This circuit will start from the first gate on qubit `anchor`.
        The other circuit will start from (node, wire) defined by `other`.

        Args:
            other: the start point of the other circuit
            flag_enabled(bool): Whether consider `flag` field. If true,
                nodes already with FLAG_VISITED will be
                skipped. Nodes in the matching will be set FLAG_VISITED.

        Returns:
            Dict[int, DAG.Node]: mapping from id(node of this circuit) to
                matched node in the other circuit. If not matched, return None.
        """
        return self.template.compare_circuit(other, self.anchor, flag_enabled, dummy_rz)

    def get_replacement(self, mapping):
        """
        Get a copy of replacement circuit.

        Args:
            mapping(Dict[int, DAG.Node]): the mapping found by `compare` method.
        Returns:
            DAG: a copy of replacement.
        """
        return self.replacement.copy()

    def replace(self, mapping: Dict[int, DAG.Node]):
        """
        Replace by `mapping`.

        Args:
            mapping(Dict[int, DAG.Node]): mapping from id(template node) to
                the matched node in the original circuit.
        """
        replacement = self.get_replacement(mapping)
        new_mapping = {}
        for qubit_ in range(replacement.width()):
            t_node, t_qubit = self.template.start_nodes[qubit_].successors[0]
            p_node, p_qubit = mapping[id(t_node)].predecessors[t_qubit]
            r_node = replacement.start_nodes[qubit_]
            new_mapping[id(r_node)] = (p_node, p_qubit)

            t_node, t_qubit = self.template.end_nodes[qubit_].predecessors[0]
            s_node, s_qubit = mapping[id(t_node)].successors[t_qubit]
            r_node = replacement.end_nodes[qubit_]
            new_mapping[id(r_node)] = (s_node, s_qubit)
        DAG.replace_circuit(new_mapping, replacement)

    def regrettable_replace(self, mapping: Dict[int, DAG.Node]):
        """
        Replace by `mapping`, but can undo later.

        Args:
            mapping(Dict[int, DAG.Node]): mapping from id(template node) to
                the matched node in the original circuit.
        Returns:
            Tuple[DAG, Dict[int, Tuple[DAG.Node, int]]]: (old circuit, mapping).
                Information needed to undo the replacing.
        """

        replacement = self.get_replacement(mapping)
        original = DAG(Circuit(replacement.width()),
                       build_toffoli=replacement.build_toffoli)

        new_mapping = {}
        undo_mapping = {}
        for qubit_ in range(replacement.width()):
            t_node, t_qubit = self.template.start_nodes[qubit_].successors[0]
            p_node, p_qubit = mapping[id(t_node)].predecessors[t_qubit]
            r_node = replacement.start_nodes[qubit_]
            new_mapping[id(r_node)] = (p_node, p_qubit)
            undo_mapping[id(original.start_nodes[qubit_])] = (p_node, p_qubit)

            t_node, t_qubit = self.template.end_nodes[qubit_].predecessors[0]
            s_node, s_qubit = mapping[id(t_node)].successors[t_qubit]
            r_node = replacement.end_nodes[qubit_]
            new_mapping[id(r_node)] = (s_node, s_qubit)
            undo_mapping[id(original.end_nodes[qubit_])] = (s_node, s_qubit)

        DAG.replace_circuit(new_mapping, replacement, erase_old=False)

        for qubit_ in range(replacement.width()):
            t_node, t_qubit = self.template.start_nodes[qubit_].successors[0]
            t_node = mapping[id(t_node)]
            original.start_nodes[qubit_].connect(0, t_qubit, t_node)

            t_node, t_qubit = self.template.end_nodes[qubit_].predecessors[0]
            t_node = mapping[id(t_node)]
            t_node.connect(t_qubit, 0, original.end_nodes[qubit_])

        return original, undo_mapping

    @staticmethod
    def undo_replace(original, undo_mapping):
        """
        Undo replacing.

        Args:
            original(DAG): return value of `regrettable_replace`
            undo_mapping(Dict[int, Tuple[DAG.Node, int]]): return value of `regrettable_replace`
        """
        DAG.replace_circuit(undo_mapping, original)

    def replace_all(self, dag: DAG):
        """
        Find all `template` in the `dag` and replace them with `replacement`.

        Args:
            dag(DAG): circuit to replace.
        """

        dag.reset_flag()

        matched = []
        for node in dag.topological_sort():
            mapping = self.compare((node, -1), flag_enabled=True, dummy_rz=True)
            if not mapping:
                continue
            matched.append(mapping)

        for mapping in matched:
            self.replace(mapping)

        dag.global_phase = np.mod(dag.global_phase + len(matched) * self.phase, 2 * np.pi)
        return len(matched)


class ParameterizedTemplate(OptimizingTemplate):
    """
    Circuit template with Rz gates.
    """
    def __init__(self, template: DAG, replacement: DAG = None,
                 anchor: int = 0, weight: int = 1, phase: float = 0, param_order: List[int] = None):
        super().__init__(template, replacement, anchor, weight, phase)

        self.rz_list = list(filter(lambda g: g.gate_type == GateType.rz, template.topological_sort()))
        self.param_order = list(range(len(self.rz_list))) if param_order is None else param_order

    def get_replacement(self, mapping):
        """
        Get a copy of circuit `replacement`. Set Rz phases in the copy by `param_order`.

        Args:
            mapping(Dict[int, DAG.Node]): the mapping found by `compare` method.
        Returns:
            DAG: a copy of replacement.
        """
        replacement = self.replacement.copy()
        r_rz_list = list(filter(lambda g: g.gate_type == GateType.rz, replacement.topological_sort()))
        for idx, rz in zip(self.param_order, r_rz_list):
            rz.params = mapping[id(self.rz_list[idx])].params.copy()
            if np.isclose(float(rz.params[0]), 0):
                rz.erase()
        return replacement


def get_circuit_from_list(n_qubit, gate_list):
    circ = Circuit(n_qubit)
    for Gate_, qubit_ in gate_list:
        Gate_ | circ(qubit_)
    return circ


def reverse_order(order):
    rev = [0] * len(order)
    for idx, val in enumerate(order):
        rev[val] = idx
    return rev


def generate_hadamard_gate_templates() -> List[OptimizingTemplate]:
    # FIXME weight is count of hadamard gates
    tpl_list = [
        [1, 2, 0, [[H, 0], [H, 0]], []],
        [1, 1, +np.pi / 4, [[H, 0], [S, 0], [H, 0]], [[S_dagger, 0], [H, 0], [S_dagger, 0]]],
        [1, 1, -np.pi / 4, [[H, 0], [S_dagger, 0], [H, 0]], [[S, 0], [H, 0], [S, 0]]],
        [2, 4, 0, [[H, 0], [H, 1], [CX, [0, 1]], [H, 0], [H, 1]], [[CX, [1, 0]]]],
        [2, 2, 0, [[H, 1], [S, 1], [CX, [0, 1]], [S_dagger, 1], [H, 1]], [[S_dagger, 1], [CX, [0, 1]], [S, 1]]],
        [2, 2, 0, [[H, 1], [S_dagger, 1], [CX, [0, 1]], [S, 1], [H, 1]], [[S, 1], [CX, [0, 1]], [S_dagger, 1]]],
        [1, 2, 0, [[X, 0], [X, 0]], []]
    ]

    ret = []
    for n_qubit, weight, phase, tpl, rpl in tpl_list:
        tpl_circ = get_circuit_from_list(n_qubit, tpl)
        rpl_circ = get_circuit_from_list(n_qubit, rpl)
        ret.append(OptimizingTemplate(DAG(tpl_circ), DAG(rpl_circ), weight=weight, phase=phase))
    return ret


def generate_single_qubit_gate_templates() -> List[OptimizingTemplate]:
    tpl_list = [
        [2, 1, [[H, 1], [CX, [0, 1]], [H, 1]]],
        [2, 1, [[CX, [0, 1]], [Rz(0), 1], [CX, [0, 1]]]],
        [2, 0, [[CX, [0, 1]]]],
        [3, 0, [[CX, [1, 0]], [CX, [0, 2]], [CX, [1, 0]]]],
        [1, 0, [[H, 0], [X, 0], [H, 0]]]
    ]

    ret = []
    for n_qubit, anchor, tpl in tpl_list:
        tpl_circ = get_circuit_from_list(n_qubit, tpl)
        ret.append(OptimizingTemplate(DAG(tpl_circ), anchor=anchor))
    return ret


def generate_cnot_targ_templates() -> List[OptimizingTemplate]:
    tpl_list = [
        [2, 1, [[CX, [0, 1]]]],
        [2, 0, [[H, 0], [CX, [0, 1]], [H, 0]]],
        [1, 0, [[X, 0]]]
    ]

    ret = []
    for n_qubit, anchor, tpl in tpl_list:
        tpl_circ = get_circuit_from_list(n_qubit, tpl)
        ret.append(OptimizingTemplate(DAG(tpl_circ), anchor=anchor))
    return ret


def generate_cnot_ctrl_templates() -> List[OptimizingTemplate]:
    tpl_list = [
        [2, 0, [[CX, [0, 1]]]],
        [1, 0, [[Rz(0), 0]]]
    ]

    ret = []
    for n_qubit, anchor, tpl in tpl_list:
        tpl_circ = get_circuit_from_list(n_qubit, tpl)
        ret.append(OptimizingTemplate(DAG(tpl_circ), anchor=anchor))
    return ret


def generate_gate_preserving_rewrite_template() -> List[ParameterizedTemplate]:
    tpl_list = [
        [3, [2, 1, 0],
         [[CX, [0, 2]], [Rz(1), 2], [CX, [1, 2]], [Rz(2), 2], [CX, [0, 2]], [Rz(3), 2], [CX, [1, 2]]],
         [[CX, [1, 2]], [Rz(3), 2], [CX, [0, 2]], [Rz(2), 2], [CX, [1, 2]], [Rz(1), 2], [CX, [0, 2]]]
         ],
        [3, [1, 0],
         [[CX, [0, 2]], [Rz(1), 2], [CX, [1, 2]], [Rz(2), 2], [CX, [1, 2]]],
         [[CX, [1, 2]], [CX, [0, 2]], [Rz(2), 2], [CX, [1, 2]], [Rz(1), 2]]
         ]
    ]

    ret = []
    for n_qubit, order, tpl, rpl in tpl_list:
        tpl_circ = get_circuit_from_list(n_qubit, tpl)
        rpl_circ = get_circuit_from_list(n_qubit, rpl)
        ret.append(ParameterizedTemplate(DAG(tpl_circ), DAG(rpl_circ), param_order=order))
        ret.append(ParameterizedTemplate(DAG(rpl_circ), DAG(tpl_circ), param_order=reverse_order(order)))
        return ret


def generate_gate_reducing_rewrite_template() -> List[ParameterizedTemplate]:
    tpl_list = [
        [4, 2, [2, 1, 0, 3],
         [[CX, [2, 1]], [CX, [0, 3]], [CX, [1, 3]], [Rz(1), 3], [CX, [1, 3]], [CX, [2, 3]],
          [Rz(2), 3], [CX, [0, 3]], [Rz(3), 3], [CX, [1, 3]], [Rz(4), 3], [CX, [2, 3]], [CX, [1, 3]]],
         [[CX, [2, 3]], [Rz(3), 3], [CX, [0, 3]], [Rz(2), 3], [CX, [1, 3]], [Rz(1), 3],
          [CX, [0, 3]], [CX, [2, 3]], [Rz(4), 3], [CX, [1, 3]], [CX, [2, 1]]]
         ],
        [4, 2, [0, 2, 4, 3, 1],
         [[CX, [2, 1]], [Rz(1), 3], [CX, [2, 3]], [Rz(2), 3], [CX, [1, 3]], [Rz(3), 3], [CX, [1, 3]],
          [CX, [0, 3]], [Rz(4), 3], [CX, [2, 3]], [CX, [1, 3]], [Rz(5), 3], [CX, [0, 3]], [CX, [1, 3]]],
         [[Rz(1), 3], [CX, [1, 3]], [Rz(3), 3], [CX, [2, 3]], [CX, [0, 3]], [Rz(5), 3],
          [CX, [1, 3]], [Rz(4), 3], [CX, [0, 3]], [Rz(2), 3], [CX, [2, 3]], [CX, [2, 1]]]
         ],
        [4, 1, [2, 1, 0, 3],
         [[CX, [2, 1]], [CX, [0, 3]], [CX, [1, 3]], [Rz(1), 3], [CX, [1, 3]], [CX, [2, 3]],
          [Rz(2), 3], [CX, [0, 3]], [Rz(3), 3], [CX, [1, 3]], [Rz(4), 3]],
         [[CX, [2, 3]], [Rz(3), 3], [CX, [0, 3]], [Rz(2), 3], [CX, [1, 3]], [Rz(1), 3],
          [CX, [0, 3]], [CX, [2, 3]], [Rz(4), 3], [CX, [2, 1]]]
         ],
        [4, 2, [1, 2, 3, 0],
         [[CX, [2, 1]], [CX, [1, 3]], [CX, [2, 3]], [Rz(1), 3], [CX, [1, 3]], [Rz(2), 3], [CX, [0, 3]],
          [Rz(3), 3], [CX, [2, 3]], [CX, [1, 3]], [Rz(4), 3], [CX, [0, 3]], [CX, [1, 3]]],
         [[CX, [2, 3]], [Rz(2), 3], [CX, [0, 3]], [Rz(3), 3], [CX, [1, 3]], [Rz(4), 3],
          [CX, [0, 3]], [CX, [2, 3]], [Rz(1), 3], [CX, [1, 3]], [CX, [2, 1]]]
         ],
        [4, 2, [1, 2, 3, 0],
         [[CX, [2, 1]], [CX, [2, 3]], [CX, [1, 3]], [Rz(1), 3], [CX, [1, 3]], [Rz(2), 3],
          [CX, [0, 3]], [Rz(3), 3], [CX, [2, 3]], [CX, [1, 3]], [Rz(4), 3], [CX, [0, 3]], [CX, [1, 3]]],
         [[CX, [2, 3]], [Rz(2), 3], [CX, [0, 3]], [Rz(3), 3], [CX, [1, 3]], [Rz(4), 3],
          [CX, [0, 3]], [CX, [2, 3]], [Rz(1), 3], [CX, [1, 3]], [CX, [2, 1]]]
         ],
    ]

    ret = []
    for n_qubit, weight, order, tpl, rpl in tpl_list:
        tpl_circ = get_circuit_from_list(n_qubit, tpl)
        rpl_circ = get_circuit_from_list(n_qubit, rpl)
        ret.append(ParameterizedTemplate(DAG(tpl_circ), DAG(rpl_circ), weight=weight, param_order=order))
    return ret
