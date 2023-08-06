"""
Optimize Clifford circuits with template matching and symbolic peephole optimization
"""

import itertools
import random

import numpy as np

from QuICT.core import Circuit
from QuICT.core.gate import (CX, CY, CZ, CompositeGate, GateType, H, S,
                             S_dagger, X, Z)
from QuICT.qcda.optimization.commutative_optimization import \
    CommutativeOptimization
from QuICT.qcda.synthesis.gate_transform.transform_rule import (cy2cx_rule,
                                                                cz2cx_rule)
from QuICT.qcda.utility import OutputAligner, PauliOperator


class SymbolicCliffordOptimization(object):
    """
    Implement the Clifford circuit optimization process described in Reference, which
    consists of the following 4 steps:
    1. Partition the circuit into compute and Pauli stages
    2. Apply template matching to the compute stage
    3. Apply symbolic peephole optimization to the compute stage
    4. Optimize the 1-qubit gate count

    Reference:
        https://arxiv.org/abs/2105.02291
    """
    def __init__(self, control_sets=None):
        """
        Args:
            control_sets(list, optional): containing several control_set, which is list of qubit,
                CX coupling control_set and the complement would be decoupled
        """
        assert control_sets is None or isinstance(control_sets, list),\
            TypeError('control_set must be list of qubit')
        self.control_sets = control_sets

    def __repr__(self):
        return 'SymbolicCliffordOptimization()'

    @OutputAligner()
    def execute(self, gates: CompositeGate):
        """
        Args:
            gates(Circuit/CompositeGate): the Clifford Circuit/CompositeGate to be optimized

        Returns:
            CompositeGate: the Clifford CompositeGate after optimization
        """
        width = gates.width()
        if isinstance(gates, Circuit):
            gates = CompositeGate(gates=gates.gates)
        assert isinstance(gates, CompositeGate),\
            TypeError('Invalid input(Circuit/CompositeGate)')
        for gate in gates:
            # FIXME log output here
            if not gate.is_clifford():
                return gates

        if self.control_sets is None:
            self.control_sets = list(itertools.combinations(range(width), 2))

        compute, global_pauli = self.partition(gates, width)

        size = compute.size()
        while True:
            control_set = list(random.choice(self.control_sets))
            compute, global_pauli = self.circular_optimization(compute, width, global_pauli)
            compute = self.cx_reverse(compute, control_set)
            compute, global_pauli = self.circular_optimization(compute, width, global_pauli)
            compute = self.reorder(compute)
            compute = self.symbolic_peephole_optimization(compute, control_set)
            compute, global_pauli = self.circular_optimization(compute, width, global_pauli)
            if compute.size() == size:
                break
            size = compute.size()

        compute.extend(global_pauli.gates(keep_phase=True))
        return compute

    def reorder(self, gates: CompositeGate):
        """
        For CompositeGate with CX, H, S only, reorder gates so that S appears as late as possible
        """
        for gate in gates:
            assert gate.type in [GateType.cx, GateType.h, GateType.s],\
                ValueError('Only CX, H, S gates are allowed in reorder')
        width = gates.width()
        gates_reorder = CompositeGate()
        S_stack = [[] for _ in range(width)]
        for gate in gates:
            if gate.type == GateType.s:
                S_stack[gate.targ].append(gate)
            else:
                gates_reorder.extend(S_stack[gate.targ])
                gates_reorder.append(gate)
                S_stack[gate.targ] = []
        for qubit in range(width):
            gates_reorder.extend(S_stack[qubit])
        return gates_reorder

    def cx_reverse(self, gates: CompositeGate, control_set: list):
        """
        For CX in the CompositeGate, if its target qubit is in the control_set while its control qubit
        is not, the control and target qubit will be reversed by adding H gates.
        """
        gates_reverse = CompositeGate()
        for gate in gates:
            if gate.type == GateType.cx and gate.carg not in control_set and gate.targ in control_set:
                with gates_reverse:
                    H & gate.carg
                    H & gate.targ
                    CX & [gate.targ, gate.carg]
                    H & gate.carg
                    H & gate.targ
            else:
                gates_reverse.append(gate)
        return gates_reverse

    def circular_optimization(self, gates: CompositeGate, width: int, global_pauli: PauliOperator):
        # TODO: More optimization to be added here
        CO = CommutativeOptimization(deparameterization=True)
        while True:
            gates_opt = CO.execute(gates)
            compute, pauli = self.partition(gates_opt, width)
            global_pauli = pauli.combine(global_pauli)
            if compute.size() == gates.size() and gates_opt.size() == gates.size():
                break
            gates = compute
        return compute, global_pauli

    @staticmethod
    def partition(gates: CompositeGate, width=None):
        """
        Partition the CompositeGate into compute and Pauli stages, where compute stage contains
        only CX, H, S, Sdg gates and Pauli stage contains only Pauli gates.

        Args:
            gates(CompositeGate): Clifford CompositeGate
            width(int, optional): width of the CompositeGate

        Returns:
            CompositeGate, PauliOperator: compute stage and Pauli stage
        """
        for gate in gates:
            assert gate.is_clifford(), ValueError('Only Clifford CompositeGate')
        if width is None:
            width = gates.width()
        pauli = PauliOperator([GateType.id for _ in range(width)])

        compute = CompositeGate()
        for gate in gates:
            if gate.is_pauli():
                pauli.combine_one_gate(gate.type, gate.targ)
                continue
            if gate.type == GateType.cx or gate.type == GateType.h or gate.type == GateType.s:
                pauli.conjugate_act(gate)
                compute.append(gate.copy())
                continue
            if gate.type == GateType.sdg:
                pauli.combine_one_gate(GateType.z, gate.targ)
                pauli.conjugate_act(gate.inverse())
                compute.append(gate.inverse())
                continue

        return compute, pauli

    @classmethod
    def symbolic_peephole_optimization(cls, gates: CompositeGate, control_set: list):
        """
        Symbolic Pauli gate gives another expression for controlled Pauli gates.
        By definition, a controlled-U gate CU means:
            if the control qubit is |0>, do nothing;
            if the control qubit is |1>, apply U to the target qubit.
        In general, CU = ∑_v |v><v| ⊗ U^v, where U^v is called a symbolic gate.

        Here we focus only on symbolic Pauli gates and symbolic phase.
        By decoupling CNOT gates with projectors and symbolic Pauli gates, optimization
        rules of 1-qubit gates could be used to optimize Clifford circuits.

        Args:
            gates(CompositeGate): CompositeGate with CX, H, S gates only where the CX coupling control_set
                and the complement must have the control qubit in control_set
            control_set(list): list of qubit, CX coupling control_set and the complement would be decoupled

        Returns:
            CompositeGate: CompositeGate after optimization
        """
        for gate in gates:
            assert gate.type in [GateType.cx, GateType.h, GateType.s],\
                ValueError('Only CX, H, S gates are allowed in this optimization')
            if gate.type == GateType.cx:
                assert not (gate.carg not in control_set and gate.targ in control_set),\
                    ValueError('Coupling CX must have the control qubit in control_set')

        gates_opt = CompositeGate()
        current = CompositeGate()
        control = None
        for gate in gates:
            if current.size() != 0:
                if ((gate.type != GateType.cx and gate.targ != control) or
                   (gate.type == GateType.cx and (gate.carg == control or gate.carg not in control_set))):
                    current.append(gate)
                else:
                    gates_opt.extend(cls.local_symbolic_optimization(current, control))
                    current = CompositeGate()
            if current.size() == 0:
                if (gate.type != GateType.cx or
                   (gate.type == GateType.cx and gate.carg not in control_set)):
                    gates_opt.append(gate)
                else:
                    current.append(gate)
                    control = gate.carg

        if current.size() != 0:
            gates_opt.extend(cls.local_symbolic_optimization(current, control))
        return gates_opt

    @classmethod
    def local_symbolic_optimization(cls, gates: CompositeGate, control: int):
        """
        Inner method for symbolic peephole optimization
        """
        for gate in gates:
            assert gate.targ != control, ValueError('control qubit should not be targeted')

        symbolic_gates = CompositeGate()
        for gate in gates:
            # symbolize coupling cx
            if gate.type == GateType.cx and gate.carg == control:
                symbolic_gates.append(X & gate.targ)
            else:
                symbolic_gates.append(gate)

        # pauli here is symbolic pauli, including symbolic phase
        compute, pauli = cls.partition(symbolic_gates)

        # such partition may cause negative optimization, if so, return the original gates
        if gates.count_2qubit_gate() < compute.count_2qubit_gate() + pauli.hamming_weight:
            return gates

        # restore the symbolic pauli
        for qubit in range(pauli.width):
            if qubit == control:
                assert pauli.operator[qubit] == GateType.id
                continue
            if pauli.operator[qubit] == GateType.x:
                compute.append(CX & [control, qubit])
            if pauli.operator[qubit] == GateType.y:
                compute.extend(cy2cx_rule(CY & [control, qubit]))
            if pauli.operator[qubit] == GateType.z:
                compute.extend(cz2cx_rule(CZ & [control, qubit]))
        # restore the symbolic phase
        if np.isclose(pauli.phase, 1j):
            compute.append(S & control)
        if np.isclose(pauli.phase, -1):
            compute.append(Z & control)
        if np.isclose(pauli.phase, -1j):
            compute.append(S_dagger & control)

        return compute
