"""
Compute the disentangler of Pauli operators (O, O')
"""

import copy
import random
import itertools

import numpy as np

from QuICT.core.gate import build_gate, BasicGate, CompositeGate, GateType, PAULI_GATE_SET, CX, H


class PauliOperator(object):
    """
    Pauli operator is a list of (I, X, Y, Z) with length n, which operates on n qubits.

    In this class, we use a list of GateType to represent the operator, where the GateTypes stand
    for the gates. Despite the operator, the phase is also recorded.
    """
    pauli_list = [GateType.id, GateType.x, GateType.y, GateType.z]
    phase_list = [1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j]

    combine_rules = {
        # I I = I
        (GateType.id, GateType.id): (GateType.id, 1),
        # I X = X
        (GateType.id, GateType.x): (GateType.x, 1),
        # I Y = Y
        (GateType.id, GateType.y): (GateType.y, 1),
        # I Z = Z
        (GateType.id, GateType.z): (GateType.z, 1),
        # X I = X
        (GateType.x, GateType.id): (GateType.x, 1),
        # X X = I
        (GateType.x, GateType.x): (GateType.id, 1),
        # X Y = -iZ
        (GateType.x, GateType.y): (GateType.z, -1j),
        # X Z = iY
        (GateType.x, GateType.z): (GateType.y, 1j),
        # Y I = Y
        (GateType.y, GateType.id): (GateType.y, 1),
        # Y X = iZ
        (GateType.y, GateType.x): (GateType.z, 1j),
        # Y Y = I
        (GateType.y, GateType.y): (GateType.id, 1),
        # Y Z = -iX
        (GateType.y, GateType.z): (GateType.x, -1j),
        # Z I = Z
        (GateType.z, GateType.id): (GateType.z, 1),
        # Z X = -iY
        (GateType.z, GateType.x): (GateType.y, -1j),
        # Z Y = iX
        (GateType.z, GateType.y): (GateType.x, 1j),
        # Z Z = I
        (GateType.z, GateType.z): (GateType.id, 1)
    }

    conjugate_rules = {
        # CX I0 I1 CX = I0 I1
        (GateType.cx, GateType.id, GateType.id): (GateType.id, GateType.id, 1),
        # CX I0 X1 CX = I0 X1
        (GateType.cx, GateType.id, GateType.x): (GateType.id, GateType.x, 1),
        # CX I0 Y1 CX = Z0 Y1
        (GateType.cx, GateType.id, GateType.y): (GateType.z, GateType.y, 1),
        # CX I0 Z1 CX = Z0 Z1
        (GateType.cx, GateType.id, GateType.z): (GateType.z, GateType.z, 1),
        # CX X0 I1 CX = X0 X1
        (GateType.cx, GateType.x, GateType.id): (GateType.x, GateType.x, 1),
        # CX X0 X1 CX = X0 I1
        (GateType.cx, GateType.x, GateType.x): (GateType.x, GateType.id, 1),
        # CX X0 Y1 CX = Y0 Z1
        (GateType.cx, GateType.x, GateType.y): (GateType.y, GateType.z, 1),
        # CX X0 Z1 CX = -Y0 Y1
        (GateType.cx, GateType.x, GateType.z): (GateType.y, GateType.y, -1),
        # CX Y0 I1 CX = Y0 X1
        (GateType.cx, GateType.y, GateType.id): (GateType.y, GateType.x, 1),
        # CX Y0 X1 CX = Y0 I1
        (GateType.cx, GateType.y, GateType.x): (GateType.y, GateType.id, 1),
        # CX Y0 Y1 CX = -X0 Z1
        (GateType.cx, GateType.y, GateType.y): (GateType.x, GateType.z, -1),
        # CX Y0 Z1 CX = X0 Y1
        (GateType.cx, GateType.y, GateType.z): (GateType.x, GateType.y, 1),
        # CX Z0 I1 CX = Z0 I1
        (GateType.cx, GateType.z, GateType.id): (GateType.z, GateType.id, 1),
        # CX Z0 X1 CX = Z0 X1
        (GateType.cx, GateType.z, GateType.x): (GateType.z, GateType.x, 1),
        # CX Z0 Y1 CX = I0 Y1
        (GateType.cx, GateType.z, GateType.y): (GateType.id, GateType.y, 1),
        # CX Z0 Z1 CX = I0 Z1
        (GateType.cx, GateType.z, GateType.z): (GateType.id, GateType.z, 1),
        # H I H = I
        (GateType.h, GateType.id): (GateType.id, 1),
        # H X H = Z
        (GateType.h, GateType.x): (GateType.z, 1),
        # H Y H = -Y
        (GateType.h, GateType.y): (GateType.y, -1),
        # H Z H = X
        (GateType.h, GateType.z): (GateType.x, 1),
        # Sdg I S = I
        (GateType.s, GateType.id): (GateType.id, 1),
        # Sdg X S = Y
        (GateType.s, GateType.x): (GateType.y, 1),
        # Sdg Y S = -X
        (GateType.s, GateType.y): (GateType.x, -1),
        # Sdg Z S = Z
        (GateType.s, GateType.z): (GateType.z, 1),
        # S I Sdg = I
        (GateType.sdg, GateType.id): (GateType.id, 1),
        # S X Sdg = -Y
        (GateType.sdg, GateType.x): (GateType.y, -1),
        # S Y Sdg = X
        (GateType.sdg, GateType.y): (GateType.x, 1),
        # S Z Sdg = Z
        (GateType.sdg, GateType.z): (GateType.z, 1),
        # X I X = I
        (GateType.x, GateType.id): (GateType.id, 1),
        # X X X = X
        (GateType.x, GateType.x): (GateType.x, 1),
        # X Y X = -Y
        (GateType.x, GateType.y): (GateType.y, -1),
        # X Z X = -Z
        (GateType.x, GateType.z): (GateType.z, -1),
        # Y I Y = I
        (GateType.y, GateType.id): (GateType.id, 1),
        # Y X Y = -X
        (GateType.y, GateType.x): (GateType.x, -1),
        # Y Y Y = Y
        (GateType.y, GateType.y): (GateType.y, 1),
        # Y Z Y = -Z
        (GateType.y, GateType.z): (GateType.z, -1),
        # Z I Z = I
        (GateType.z, GateType.id): (GateType.id, 1),
        # Z X Z = -X
        (GateType.z, GateType.x): (GateType.x, -1),
        # Z Y Z = -Y
        (GateType.z, GateType.y): (GateType.y, -1),
        # Z Z Z = Z
        (GateType.z, GateType.z): (GateType.z, 1)
    }

    standardize_rules = {
        (GateType.id, GateType.id): ([], 4),
        (GateType.id, GateType.x): ([GateType.h], 3),
        (GateType.id, GateType.y): ([GateType.s, GateType.h], 3),
        (GateType.id, GateType.z): ([], 3),
        (GateType.x, GateType.id): ([], 2),
        (GateType.x, GateType.x): ([], 1),
        (GateType.x, GateType.y): ([GateType.h, GateType.s, GateType.h], 0),
        (GateType.x, GateType.z): ([], 0),
        (GateType.y, GateType.id): ([GateType.s], 2),
        (GateType.y, GateType.x): ([GateType.h, GateType.s], 0),
        (GateType.y, GateType.y): ([GateType.s], 1),
        (GateType.y, GateType.z): ([GateType.s], 0),
        (GateType.z, GateType.id): ([GateType.h], 2),
        (GateType.z, GateType.x): ([GateType.h], 0),
        (GateType.z, GateType.y): ([GateType.s, GateType.h], 0),
        (GateType.z, GateType.z): ([GateType.h], 1)
    }

    def __init__(self, operator=None, phase=1 + 0j):
        """
        Construct a PauliOperator with a list of GateType

        Args:
            operator(list, optional): the list of GateType representing the PauliOperator
            phase(complex, optional): the global phase of the PauliOperator, ±1 or ±i
        """
        if operator is None:
            self._operator = []
        else:
            assert isinstance(operator, list), TypeError("operator must be list of int(GateType).")
            for gate_type in operator:
                assert gate_type == GateType.id or gate_type in PAULI_GATE_SET,\
                    ValueError("operator must contain Pauli gates only.")
            self._operator = operator
        assert phase in PauliOperator.phase_list, ValueError("phase must be ±1 or ±i")
        self._phase = phase

    def __str__(self):
        string = ''
        for i in range(len(self.operator)):
            if self.operator[i] == GateType.id:
                string += 'I'
            elif self.operator[i] == GateType.x:
                string += 'X'
            elif self.operator[i] == GateType.y:
                string += 'Y'
            elif self.operator[i] == GateType.z:
                string += 'Z'
            else:
                raise ValueError('Invalid GateType')
        return string + ', {}'.format(self.phase)

    @property
    def operator(self) -> list:
        return self._operator

    @operator.setter
    def operator(self, operator: list):
        assert isinstance(operator, list), TypeError("operator must be list of int(GateType).")
        for gate_type in operator:
            assert gate_type == GateType.id or gate_type in PAULI_GATE_SET,\
                ValueError("operator must contain Pauli gates only.")
        self._operator = operator

    @property
    def phase(self) -> complex:
        return self._phase

    @phase.setter
    def phase(self, phase: complex):
        assert phase in PauliOperator.phase_list, ValueError("phase must be ±1 or ±i")
        self._phase = phase

    def gates(self, keep_id=False, keep_phase=False) -> CompositeGate:
        """
        The CompositeGate corresponding to the PauliOperator

        Args:
            keep_id(bool, optional): whether to keep the IDgate in the CompositeGate
            keep_phase(bool, optional): whether to keep the global phase in the CompositeGate

        Returns:
            CompositeGate: The CompositeGate corresponding to the PauliOperator
        """
        gates = CompositeGate()
        for qubit, gate_type in enumerate(self.operator):
            if not keep_id and gate_type == GateType.id:
                continue
            gate = build_gate(gate_type, qubit)
            gates.append(gate)
        if keep_phase and not np.isclose(self.phase, 1 + 0j):
            phase = -1j * np.log(self.phase)
            gate = build_gate(GateType.gphase, 0, phase.real)
            gates.append(gate)
        return gates

    @property
    def width(self) -> int:
        return len(self.operator)

    @property
    def support(self) -> list:
        support = []
        for qubit, operator in enumerate(self.operator):
            if operator != GateType.id:
                support.append(qubit)
        return support

    @property
    def hamming_weight(self) -> int:
        return len(self.support)

    @staticmethod
    def random(width: int):
        """
        Give a random PauliOperator with given width

        Args:
            width(int): the width of the PauliOperator

        Returns:
            PauliOperator: a random PauliOperator with given width
        """
        operator = []
        for _ in range(width):
            operator.append(random.choice(PauliOperator.pauli_list))
        return PauliOperator(operator)

    @staticmethod
    def random_anti_commutative_pair(width):
        op_id = [GateType.id for _ in range(width)]
        # Avoid p1 = identity
        while True:
            p1 = PauliOperator.random(width)
            if p1.operator != op_id:
                break
        # Expectation = 2
        while True:
            p2 = PauliOperator.random(width)
            if not p1.commute(p2):
                break
        return p1, p2

    @staticmethod
    def iterator(width: int):
        """
        Yield all the PauliOperators with given width

        Args:
            width(int): the width of the PauliOperator

        Yields:
            PauliOperator: PauliOperator with given width
        """
        for operator in itertools.product(PauliOperator.pauli_list, repeat=width):
            yield PauliOperator(list(operator))

    def commute(self, other):
        """
        Decide whether two PauliOperators commute or anti-commute

        Args:
            other(PauliOperator): PauliOperator to be checked with self

        Returns:
            boolean: True for commutative or False for anti-commutative
        """
        assert isinstance(other, PauliOperator),\
            TypeError("commute() only checks commutativity between PauliOperators.")
        assert self.width == other.width,\
            ValueError("PauliOperators to be checked must have the same width.")

        res = True
        for qubit in range(self.width):
            if self.operator[qubit] == GateType.id or other.operator[qubit] == GateType.id\
               or self.operator[qubit] == other.operator[qubit]:
                continue
            else:
                res = not res
        return res

    def combine(self, other):
        """
        Compute the PauliOperator after combined with a PauliOperator from the right side.
        Be aware of the order, which would affect the global phase.

        Args:
            other(PauliOperator): the PauliOperator to be combined

        Returns:
            PauliOperator: the combined PauliOperator
        """
        assert isinstance(other, PauliOperator),\
            TypeError("combine() only combines PauliOperators.")
        assert self.width == other.width,\
            ValueError("PauliOperators to be combined must have the same width.")

        self.phase *= other.phase
        for qubit, gate_type in enumerate(other.operator):
            self.combine_one_gate(gate_type, qubit)
        return self

    def combine_one_gate(self, gate_type: GateType, qubit: int):
        """
        Compute the PauliOperator after combined with a Pauli gate from the right side.
        Be aware of the order, which would affect the global phase.

        Args:
            gate_type(GateType): type of the Pauli gate to be combined
            qubit(int): qubit that the Pauli gate acts on
        """
        assert gate_type in PAULI_GATE_SET or gate_type == GateType.id,\
            ValueError('gate to be combined must be a pauli gate')
        assert isinstance(qubit, int) and qubit >= 0 and qubit < self.width,\
            ValueError('qubit out of range')

        self.operator[qubit], phase = PauliOperator.combine_rules[self.operator[qubit], gate_type]
        self.phase *= phase

    def conjugate_act(self, gate: BasicGate):
        """
        Compute the PauliOperator after conjugate action of a clifford gate
        Be aware that the conjugate action means U^-1 P U, where U is the clifford gate
        and P is the PauliOperator. It is important for S gate.

        Args:
            gate(BasicGate): the clifford gate to be acted on the PauliOperator
        """
        assert gate.is_clifford() or gate.type == GateType.id,\
            ValueError("Only conjugate action of Clifford gates here.")
        for targ in gate.cargs + gate.targs:
            assert targ < self.width, ValueError("target of the gate out of range")

        if gate.type == GateType.cx:
            self.operator[gate.carg], self.operator[gate.targ], phase\
                = PauliOperator.conjugate_rules[gate.type, self.operator[gate.carg], self.operator[gate.targ]]
        else:
            self.operator[gate.targ], phase = PauliOperator.conjugate_rules[gate.type, self.operator[gate.targ]]
        self.phase *= phase

    @staticmethod
    def disentangler(pauli_x, pauli_z, target=0) -> CompositeGate:
        """
        For anti-commuting n-qubit Pauli operators O and O', there exists a Clifford circuit L∈C_n
        such that L^(-1) O L = X_j, L^(-1) O' L = Z_j.
        L is referred to as a disentangler for the pair (O, O').

        Args:
            pauli_x(PauliOperator): the PauliOperator to be transformed to X_j
            pauli_z(PauliOperator): the PauliOperator to be transformed to Z_j
            target(int, optional): the j in the X_j, Z_j to be transformed to

        Returns:
            CompositeGate: the disentangler for the pair (O, O')

        Reference:
            https://arxiv.org/abs/2105.02291
        """
        assert isinstance(pauli_x, PauliOperator) and isinstance(pauli_z, PauliOperator),\
            TypeError("disentangler only defined for PauliOperator pairs")
        assert pauli_x.width == pauli_z.width,\
            ValueError('two PauliOperators must be of the same width')
        assert not pauli_x.commute(pauli_z),\
            ValueError('anti-commutative pairs needed for computing disentangler')
        assert isinstance(target, int) and 0 <= target and target < pauli_x.width,\
            ValueError('the target must be integer in the width of the PauliOperators')

        pauli_x = copy.deepcopy(pauli_x)
        pauli_z = copy.deepcopy(pauli_z)

        # Record the qubits in the 5 cases of the standard forms
        XZ = []
        XX = []
        XI = []
        IZ = []
        II = []
        standard_forms = [XZ, XX, XI, IZ, II]

        # Transform the pauli_x and pauli_z to 'standard' forms
        standardizer = CompositeGate()
        for qubit in range(pauli_x.width):
            gates, form = PauliOperator.standardize_rules[pauli_x.operator[qubit], pauli_z.operator[qubit]]
            for gate_type in gates:
                gate = build_gate(gate_type, qubit)
                pauli_x.conjugate_act(gate)
                pauli_z.conjugate_act(gate)
                standardizer.append(gate)
            standard_forms[form].append(qubit)

        # Construct the disentangler of 'standard' pairs with the algorithm given in reference
        disentangler = CompositeGate()
        with disentangler:
            for subset in standard_forms:
                if target in subset:
                    if subset is not XZ:
                        # Swap & [target, XZ[0]]
                        CX & [target, XZ[0]]
                        CX & [XZ[0], target]
                        CX & [target, XZ[0]]
                    if XZ[0] != target:
                        subset.remove(target)
                        subset.append(XZ[0])
                        XZ[0] = target
            for j in XI:
                CX & [target, j]
            for j in IZ:
                CX & [j, target]
            if len(XX) > 0:
                i = XX[0]
                for j in XX[1:]:
                    CX & [i, j]
                CX & [target, i]
                H & i
                CX & [i, target]
            # Anti-commutation gives that len(XZ) is odd
            for k in range((len(XZ) - 1) // 2):
                i = 2 * k + 1
                j = 2 * k + 2
                CX & [XZ[j], XZ[i]]
                CX & [XZ[i], target]
                CX & [target, XZ[j]]

        standardizer.extend(disentangler)

        # Add the last Pauli gate for the phase correction
        for gate in disentangler:
            pauli_x.conjugate_act(gate)
            pauli_z.conjugate_act(gate)
        if pauli_x.phase == 1 and pauli_z.phase == -1:
            gate = build_gate(GateType.x, target)
            standardizer.append(gate)
        if pauli_x.phase == -1 and pauli_z.phase == -1:
            gate = build_gate(GateType.y, target)
            standardizer.append(gate)
        if pauli_x.phase == -1 and pauli_z.phase == 1:
            gate = build_gate(GateType.z, target)
            standardizer.append(gate)

        return standardizer
