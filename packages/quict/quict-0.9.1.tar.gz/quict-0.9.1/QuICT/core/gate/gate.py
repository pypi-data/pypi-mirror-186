#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2022/1/17 9:04
# @Author  : Han Yu, Li Kaiqi
# @File    : gate.py
import copy
from typing import Union
import numpy as np

from QuICT.core.utils import (
    GateType, MatrixType, SPECIAL_GATE_SET, DIAGONAL_GATE_SET, CGATE_LIST,
    PAULI_GATE_SET, CLIFFORD_GATE_SET,
    perm_decomposition, matrix_product_to_circuit
)
from QuICT.tools.exception.core import (
    TypeError, ValueError, GateAppendError, GateQubitAssignedError,
    QASMError, GateMatrixError, GateParametersAssignedError
)


class BasicGate(object):
    """ the abstract SuperClass of all basic quantum gate

    All basic quantum gate described in the framework have
    some common attributes and some common functions
    which defined in this class

    Attributes:
        name(str): the name of the gate
        controls(int): the number of the control bits of the gate
        cargs(list<int>): the list of the index of control bits in the circuit
        carg(int, read only): the first object of cargs

        targets(int): the number of the target bits of the gate
        targs(list<int>): the list of the index of target bits in the circuit
        targ(int, read only): the first object of targs

        params(list): the number of the parameter of the gate
        pargs(list): the list of the parameter
        parg(read only): the first object of pargs

        qasm_name(str, read only): gate's name in the OpenQASM 2.0
        type(GateType, read only): gate's type described by GateType

        matrix(np.array): the unitary matrix of the quantum gate act on targets
    """
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def matrix(self) -> np.ndarray:
        return self._matrix

    @matrix.setter
    def matrix(self, matrix) -> np.ndarray:
        self._matrix = matrix

    @property
    def target_matrix(self) -> np.ndarray:
        return self.matrix

    @property
    def type(self):
        return self._type

    @property
    def matrix_type(self):
        return self._matrix_type

    @property
    def controls(self) -> int:
        return self._controls

    @controls.setter
    def controls(self, controls: int):
        assert isinstance(controls, int), TypeError("BasicGate.controls", "int", type(controls))
        self._controls = controls

    @property
    def cargs(self):
        return self._cargs

    @cargs.setter
    def cargs(self, cargs: Union[list, int]):
        if isinstance(cargs, int):
            cargs = [cargs]

        assert len(cargs) == len(set(cargs)), ValueError("BasicGate.cargs", "not have duplicated value", cargs)
        self._cargs = cargs

    @property
    def targets(self) -> int:
        return self._targets

    @targets.setter
    def targets(self, targets: int):
        assert isinstance(targets, int), TypeError("BasicGate.targets", "int", type(targets))
        self._targets = targets

    @property
    def targs(self):
        return self._targs

    @targs.setter
    def targs(self, targs: list):
        if isinstance(targs, int):
            targs = [targs]

        assert len(targs) == len(set(targs)), ValueError("BasicGate.targs", "not have duplicated value", targs)
        assert not set(self._cargs) & set(targs), ValueError(
            "BasicGate.targs", "have no same index with control qubits", set(self._cargs) & set(targs)
        )
        self._targs = targs

    @property
    def params(self) -> int:
        return self._params

    @params.setter
    def params(self, params: int):
        self._params = params

    @property
    def pargs(self):
        return self._pargs

    @pargs.setter
    def pargs(self, pargs: list):
        if isinstance(pargs, list):
            self._pargs = pargs
        else:
            self._pargs = [pargs]

        if len(self._pargs) != self.params:
            raise ValueError("BasicGate.pargs:length", f"equal to gate's parameter number {self._pargs}", len(pargs))

    @property
    def parg(self):
        return self.pargs[0]

    @property
    def carg(self):
        return self.cargs[0]

    @property
    def targ(self):
        return self.targs[0]

    @property
    def precision(self):
        return self._precision

    @property
    def qasm_name(self):
        return self._qasm_name

    def __init__(
        self,
        controls: int,
        targets: int,
        params: int,
        type_: GateType,
        matrix_type: MatrixType = MatrixType.normal
    ):
        self._matrix = None

        self._controls = controls
        self._targets = targets
        self._params = params
        self._cargs = []    # list of int
        self._targs = []    # list of int
        self._pargs = []    # list of float/..

        assert isinstance(type_, GateType), TypeError("BasicGate.type", "GateType", type(type_))
        self._type = type_
        self._matrix_type = matrix_type
        self._precision = np.complex128
        self._qasm_name = str(type_.name)
        self._name = "-".join([str(type_), "", ""])

        self.assigned_qubits = []   # list of qubits

    def __or__(self, targets):
        """deal the operator '|'

        Use the syntax "gate | circuit" or "gate | Composite Gate"
        to add the gate into the circuit or composite gate
        Some Examples are like this:

        X       | circuit
        CX      | circuit([0, 1])
        Measure | CompositeGate

        Note that the order of qubits is that control bits first
        and target bits followed.

        Args:
            targets: the targets the gate acts on, it can have following form,
                1) Circuit
                2) CompositeGate

        Raise:
            TypeError: the type of other is wrong
        """
        try:
            targets.append(self)
        except Exception as e:
            raise GateAppendError(f"Failure to append gate {self.name} to targets, due to {e}")

    def __and__(self, targets):
        """deal the operator '&'

        Use the syntax "gate & int" or "gate & list<int>" to set gate's attribute.
        Special uses when in composite gate's context.

        Some Examples are like this:
        X       & 1
        CX      & [0, 1]

        Note that the order of qubits is that control bits first
        and target bits followed.

        Args:
            targets: the targets the gate acts on, it can have following form,
                1) int
                2) list<int>

        Raise:
            TypeError: the type of targets is wrong
        """
        _gate = self.copy()

        if isinstance(targets, int):
            assert _gate.is_single(), GateQubitAssignedError("The qubits number should equal to the quantum gate.")

            _gate.targs = [targets]
        elif isinstance(targets, list):
            if len(targets) != _gate.controls + _gate.targets:
                raise GateQubitAssignedError("The qubits number should equal to the quantum gate.")

            _gate.cargs = targets[:_gate.controls]
            _gate.targs = targets[_gate.controls:]
        else:
            raise TypeError("BasicGate.&", "int or list<int>", type(targets))

        if CGATE_LIST:
            CGATE_LIST[-1].append(_gate)
        else:
            return _gate

    def __call__(self):
        """ give parameters for the gate, and give parameters by "()", and parameters should be one of int/float/complex

        Some Examples are like this:

        Rz(np.pi / 2)           | qubit
        U3(np.pi / 2, 0, 0)     | qubit

        *Important*: There is no parameters for current quantum gate.

        Returns:
            BasicGate: the gate after filled by parameters
        """
        return self.copy()

    def __eq__(self, other):
        assert isinstance(other, BasicGate), TypeError("BasicGate.==", "BasicGate", type(other))
        if (
            self.type != other.type or
            (self.cargs + self.targs) != (other.cargs + other.targs) or
            not np.allclose(self.matrix, other.matrix)
        ):
            return False

        return True

    def update_name(self, qubit_id: str, circuit_idx: int = None):
        """ Updated gate's name with the given information

        Args:
            qubit_id (str): The qubit's unique ID.
            circuit_idx (int, optional): The gate's order index in the circuit. Defaults to None.
        """
        qubit_id = qubit_id[:6]
        name_parts = self.name.split('-')
        name_parts[1] = qubit_id

        if circuit_idx is not None:
            name_parts[2] = str(circuit_idx)

        self.name = '-'.join(name_parts)

    def __str__(self):
        """ get gate information """
        gate_info = {
            "name": self.name,
            "controls": self.controls,
            "control_bit": self.cargs,
            "targets": self.targets,
            "target_bit": self.targs,
            "parameters": self.pargs
        }

        return str(gate_info)

    def qasm(self):
        """ generator OpenQASM string for the gate

        Return:
            string: the OpenQASM 2.0 describe of the gate
        """
        if self.type in SPECIAL_GATE_SET[4:]:
            raise QASMError(f"The gate do not support qasm, {self.type}")

        qasm_string = self.qasm_name
        if self.params > 0:
            params = [str(parg) for parg in self.pargs]
            params_string = "(" + ", ".join(params) + ")"

            qasm_string += params_string

        ctargs = [f"q[{ctarg}]" for ctarg in self.cargs + self.targs]
        ctargs_string = " " + ', '.join(ctargs) + ";\n"
        qasm_string += ctargs_string

        return qasm_string

    def convert_precision(self):
        """ Convert gate's precision into single precision np.complex64. """
        if self.type in [GateType.measure, GateType.reset, GateType.barrier]:
            return

        self._precision = np.complex64 if self._precision == np.complex128 else np.complex128
        if self.params == 0:
            self._matrix = self.matrix.astype(self._precision)

    def inverse(self):
        """ the inverse of the gate

        Return:
            BasicGate: the inverse of the gate
        """
        return self.copy()

    def commutative(self, goal, eps=1e-7):
        """ decide whether gate is commutative with another gate

        note when the gate is special gates like Unitary, Permutation, Measure and so on, return False.

        Args:
            goal(BasicGate): the target gate
            eps(float): the precision of comparision

        Return:
            bool: True if commutative
        """
        # Check the affected qubits
        self_controls = set(self.cargs)
        self_targets = set(self.targs)
        goal_controls = set(goal.cargs)
        goal_targets = set(goal.targs)
        # If the affected qubits of the gates are completely different, they must commute
        self_qubits = self_controls | self_targets
        goal_qubits = goal_controls | goal_targets
        if len(self_qubits & goal_qubits) == 0:
            return True

        # Ignore all the special gates except for the unitary gates due to the difficulty of getting the matrices
        if (
            (self.is_special() and self.type != GateType.unitary) or
            (goal.is_special() and self.type != GateType.unitary)
        ):
            return False

        # Check the target matrices of the gates
        A = self.target_matrix
        B = goal.target_matrix
        # It means commuting that any of the target matrices is close to identity
        if (
            np.allclose(A, np.identity(1 << self.targets), rtol=eps, atol=eps) or
            np.allclose(B, np.identity(1 << goal.targets), rtol=eps, atol=eps)
        ):
            return True

        # For gates whose number of target qubits is 1, optimized judgment could be used
        if self.targets == 1 and goal.targets == 1:
            # Diagonal target gates commutes with the control qubits
            if (
                (len(self_controls & goal_targets) > 0 and not goal.is_diagonal()) or
                (len(goal_controls & self_targets) > 0 and not self.is_diagonal())
            ):
                return False
            # Compute the target matrix commutation
            if (
                len(goal_targets & self_targets) > 0 and
                not np.allclose(A.dot(B), B.dot(A), rtol=eps, atol=eps)
            ):
                return False

            return True
        # Otherwise, we need to calculate the matrix commutation directly
        else:
            # Collect all the affected qubits and create the converter to the minimal qubits
            qubits = self_qubits | goal_qubits
            qubits_dict = {}
            for idx, x in enumerate(qubits):
                qubits_dict[x] = idx
            # Create two masked gates whose affected qubits are the minimal ones
            self_masked = self.cargs + self.targs
            for i in range(len(self_masked)):
                self_masked[i] = qubits_dict[self_masked[i]]
            goal_masked = goal.cargs + goal.targs
            for i in range(len(goal_masked)):
                goal_masked[i] = qubits_dict[goal_masked[i]]
            # Compute the matrix commutation
            self_matrix = self.expand(list(qubits))
            goal_matrix = goal.expand(list(qubits))
            return np.allclose(self_matrix.dot(goal_matrix), goal_matrix.dot(self_matrix), rtol=eps, atol=eps)

    def is_single(self) -> bool:
        """ judge whether gate is a one qubit gate(excluding special gate like measure, reset, custom and so on)

        Returns:
            bool: True if it is a one qubit gate
        """
        return self.targets + self.controls == 1

    def is_control_single(self) -> bool:
        """ judge whether gate has one control bit and one target bit

        Returns:
            bool: True if it is has one control bit and one target bit
        """
        return self.controls == 1 and self.targets == 1

    def is_clifford(self) -> bool:
        """ judge whether gate's matrix is a Clifford gate

        Returns:
            bool: True if gate's matrix is a Clifford gate
        """
        return self.type in CLIFFORD_GATE_SET

    def is_diagonal(self) -> bool:
        """ judge whether gate's matrix is diagonal

        Returns:
            bool: True if gate's matrix is diagonal
        """
        return (
            self.type in DIAGONAL_GATE_SET or
            (self.type == GateType.unitary and self._is_diagonal())
        )

    def _is_diagonal(self) -> bool:
        return np.allclose(np.diag(np.diag(self.matrix)), self.matrix)

    def is_pauli(self) -> bool:
        """ judge whether gate's matrix is a Pauli gate

        Returns:
            bool: True if gate's matrix is a Pauli gate
        """
        return self.type in PAULI_GATE_SET

    def is_special(self) -> bool:
        """ judge whether gate's is special gate, which is one of
        [Measure, Reset, Barrier, Perm, Unitary, ...]

        Returns:
            bool: True if gate's matrix is special
        """
        return self.type in SPECIAL_GATE_SET

    def is_identity(self) -> bool:
        if self.type in [GateType.reset, GateType.measure, GateType.barrier]:
            return False

        return np.allclose(self.matrix, np.identity(1 << (self.controls + self.targets), dtype=self.precision))

    def expand(self, qubits: Union[int, list]) -> bool:
        """ expand self matrix into the circuit's unitary linear space. If input qubits is integer, please make sure
        the indexes of current gate is within [0, qubits).

        Args:
            qubits Union[int, list]: the total number of qubits of the target circuit or the indexes of expand qubits.
        """
        if isinstance(qubits, int):
            qubits = list(range(qubits))

        qubits_num = len(qubits)
        if qubits_num == self.controls + self.targets:
            return self.matrix

        assert qubits_num > self.controls + self.targets, GateQubitAssignedError(
            "The expand qubits' num should >= gate's qubits num."
        )
        gate_args = self.cargs + self.targs
        if len(gate_args) == 0:     # Deal with not assigned quantum gate
            gate_args = [qubits[i] for i in range(self.controls + self.targets)]

        updated_args = [qubits.index(garg) for garg in gate_args]
        return matrix_product_to_circuit(self.matrix, updated_args, qubits_num)

    def copy(self):
        """ return a copy of this gate

        Returns:
            gate(BasicGate): a copy of this gate
        """
        class_name = str(self.__class__.__name__)
        gate = globals()[class_name]()

        if gate.type in SPECIAL_GATE_SET:
            gate.controls = self.controls
            gate.targets = self.targets
            gate.params = self.params

        if gate.type in [GateType.perm, GateType.unitary, GateType.perm_fx]:
            gate.matrix = self.matrix

        gate.pargs = copy.deepcopy(self.pargs)
        gate.targs = copy.deepcopy(self.targs)
        gate.cargs = copy.deepcopy(self.cargs)

        if self.assigned_qubits:
            gate.assigned_qubits = copy.deepcopy(self.assigned_qubits)
            gate.update_name(gate.assigned_qubits[0].id)

        if self.precision == np.complex64:
            gate.convert_precision()

        return gate

    def permit_element(self, element):
        """ judge whether the type of a parameter is int/float/complex

        for a quantum gate, the parameter should be int/float/complex

        Args:
            element: the element to be judged

        Returns:
            bool: True if the type of element is int/float/complex
        """
        if not isinstance(element, (int, float, complex)):
            tp = type(element)
            if tp == np.int64 or tp == np.float64 or tp == np.complex128:
                return True

            raise TypeError(self.type, "int/float/complex", type(element))


class HGate(BasicGate):
    """ Hadamard gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.h
        )

        self.matrix = np.array([
            [1 / np.sqrt(2), 1 / np.sqrt(2)],
            [1 / np.sqrt(2), -1 / np.sqrt(2)]
        ], dtype=self._precision)


H = HGate()


class HYGate(BasicGate):
    """ Self-inverse gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.hy
        )

        self.matrix = np.array([
            [1 / np.sqrt(2), -1j / np.sqrt(2)],
            [1j / np.sqrt(2), -1 / np.sqrt(2)]
        ], dtype=self._precision)


Hy = HYGate()


class SGate(BasicGate):
    """ S gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.s,
            matrix_type=MatrixType.control
        )

        self.matrix = np.array([
            [1, 0],
            [0, 1j]
        ], dtype=self._precision)

    def inverse(self):
        """ change it be sdg gate"""
        _Sdagger = SDaggerGate()
        _Sdagger.targs = copy.deepcopy(self.targs)
        _Sdagger.assigned_qubits = copy.deepcopy(self.assigned_qubits)

        return _Sdagger


S = SGate()


class SDaggerGate(BasicGate):
    """ The conjugate transpose of Phase gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.sdg,
            matrix_type=MatrixType.control
        )

        self.matrix = np.array([
            [1, 0],
            [0, -1j]
        ], dtype=self._precision)

    def inverse(self):
        """ change it to be s gate """
        _Sgate = SGate()
        _Sgate.targs = copy.deepcopy(self.targs)
        _Sgate.assigned_qubits = copy.deepcopy(self.assigned_qubits)

        return _Sgate


S_dagger = SDaggerGate()


class XGate(BasicGate):
    """ Pauli-X gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.x,
            matrix_type=MatrixType.swap
        )

        self.matrix = np.array([
            [0, 1],
            [1, 0]
        ], dtype=self._precision)


X = XGate()


class YGate(BasicGate):
    """ Pauli-Y gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.y,
            matrix_type=MatrixType.reverse
        )

        self.matrix = np.array([
            [0, -1j],
            [1j, 0]
        ], dtype=self._precision)


Y = YGate()


class ZGate(BasicGate):
    """ Pauli-Z gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.z,
            matrix_type=MatrixType.control
        )

        self.matrix = np.array([
            [1, 0],
            [0, -1]
        ], dtype=self._precision)


Z = ZGate()


class SXGate(BasicGate):
    """ sqrt(X) gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.sx
        )

        self.matrix = np.array([
            [0.5 + 0.5j, 0.5 - 0.5j],
            [0.5 - 0.5j, 0.5 + 0.5j]
        ], dtype=self._precision)

    def inverse(self):
        """ change it be rx gate"""
        _Rx = RxGate([-np.pi / 2])
        _Rx.targs = copy.deepcopy(self.targs)

        return _Rx


SX = SXGate()


class SYGate(BasicGate):
    """ sqrt(Y) gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.sy
        )

        self.matrix = np.array([
            [1 / np.sqrt(2), -1 / np.sqrt(2)],
            [1 / np.sqrt(2), 1 / np.sqrt(2)]
        ], dtype=self._precision)

    def inverse(self):
        """ change it to be ry gate"""
        _Ry = RyGate([-np.pi / 2])
        _Ry.targs = copy.deepcopy(self.targs)

        return _Ry


SY = SYGate()


class SWGate(BasicGate):
    """ sqrt(W) gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.sw
        )

        self.matrix = np.array([
            [1 / np.sqrt(2), -np.sqrt(1j / 2)],
            [np.sqrt(-1j / 2), 1 / np.sqrt(2)]
        ], dtype=self._precision)

    def inverse(self):
        """ change it be U2 gate"""
        _U2 = U2Gate([3 * np.pi / 4, 5 * np.pi / 4])
        _U2.targs = copy.deepcopy(self.targs)

        return _U2


SW = SWGate()


class IDGate(BasicGate):
    """ Identity gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.id,
            matrix_type=MatrixType.diagonal
        )

        self.matrix = np.array([
            [1, 0],
            [0, 1]
        ], dtype=self._precision)


ID = IDGate()


class U1Gate(BasicGate):
    """ Diagonal single-qubit gate """
    def __init__(self, params: list = [np.pi / 2]):
        super().__init__(
            controls=0,
            targets=1,
            params=1,
            type_=GateType.u1,
            matrix_type=MatrixType.control
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return U1Gate([alpha])

    @property
    def matrix(self):
        return np.array([
            [1, 0],
            [0, np.exp(1j * self.pargs[0])]
        ], dtype=self._precision)

    def inverse(self):
        _U1 = self.copy()
        _U1.pargs = [-self.pargs[0]]

        return _U1


U1 = U1Gate()


class U2Gate(BasicGate):
    """ One-pulse single-qubit gate """
    def __init__(self, params: list = [np.pi / 2, np.pi / 2]):
        super().__init__(
            controls=0,
            targets=1,
            params=2,
            type_=GateType.u2
        )

        self.pargs = params

    def __call__(self, alpha, beta):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate
            beta (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        params = [alpha, beta]

        for param in params:
            self.permit_element(param)

        return U2Gate(params)

    @property
    def matrix(self):
        sqrt2 = 1 / np.sqrt(2)
        return np.array([
            [1 * sqrt2,
             -np.exp(1j * self.pargs[1]) * sqrt2],
            [np.exp(1j * self.pargs[0]) * sqrt2,
             np.exp(1j * (self.pargs[0] + self.pargs[1])) * sqrt2]
        ], dtype=self._precision)

    def inverse(self):
        _U2 = self.copy()
        _U2.pargs = [np.pi - self.pargs[1], np.pi - self.pargs[0]]

        return _U2


U2 = U2Gate()


class U3Gate(BasicGate):
    """ Two-pulse single-qubit gate """
    def __init__(self, params: list = [0, 0, np.pi / 2]):
        super().__init__(
            controls=0,
            targets=1,
            params=3,
            type_=GateType.u3
        )

        self.pargs = params

    def __call__(self, alpha, beta, gamma):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate
            beta (int/float/complex): The parameter for gate
            gamma (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        params = [alpha, beta, gamma]

        for param in params:
            self.permit_element(param)

        return U3Gate(params)

    @property
    def matrix(self):
        return np.array([
            [np.cos(self.pargs[0] / 2),
             -np.exp(1j * self.pargs[2]) * np.sin(self.pargs[0] / 2)],
            [np.exp(1j * self.pargs[1]) * np.sin(self.pargs[0] / 2),
             np.exp(1j * (self.pargs[1] + self.pargs[2])) * np.cos(self.pargs[0] / 2)]
        ], dtype=self._precision)

    def inverse(self):
        _U3 = self.copy()
        _U3.pargs = [self.pargs[0], np.pi - self.pargs[2], np.pi - self.pargs[1]]

        return _U3


U3 = U3Gate()


class RxGate(BasicGate):
    """ Rotation around the x-axis gate """
    def __init__(self, params: list = [np.pi / 2]):
        super().__init__(
            controls=0,
            targets=1,
            params=1,
            type_=GateType.rx
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return RxGate([alpha])

    @property
    def matrix(self):
        return np.array([
            [np.cos(self.parg / 2), 1j * -np.sin(self.parg / 2)],
            [1j * -np.sin(self.parg / 2), np.cos(self.parg / 2)]
        ], dtype=self._precision)

    def inverse(self):
        _Rx = self.copy()
        _Rx.pargs = [-self.pargs[0]]

        return _Rx


Rx = RxGate()


class RyGate(BasicGate):
    """ Rotation around the y-axis gate """
    def __init__(self, params: list = [np.pi / 2]):
        super().__init__(
            controls=0,
            targets=1,
            params=1,
            type_=GateType.ry
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return RyGate([alpha])

    @property
    def matrix(self):
        return np.array([
            [np.cos(self.pargs[0] / 2), -np.sin(self.pargs[0] / 2)],
            [np.sin(self.pargs[0] / 2), np.cos(self.pargs[0] / 2)],
        ], dtype=self._precision)

    def inverse(self):
        _Ry = self.copy()
        _Ry.pargs = [-self.pargs[0]]

        return _Ry


Ry = RyGate()


class RzGate(BasicGate):
    """ Rotation around the z-axis gate """
    def __init__(self, params: list = [np.pi / 2]):
        super().__init__(
            controls=0,
            targets=1,
            params=1,
            type_=GateType.rz,
            matrix_type=MatrixType.diagonal
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return RzGate([alpha])

    @property
    def matrix(self):
        return np.array([
            [np.exp(-self.parg / 2 * 1j), 0],
            [0, np.exp(self.parg / 2 * 1j)]
        ], dtype=self._precision)

    def inverse(self):
        _Rz = self.copy()
        _Rz.pargs = [-self.pargs[0]]

        return _Rz


Rz = RzGate()


class TGate(BasicGate):
    """ T gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.t,
            matrix_type=MatrixType.control
        )

        self.matrix = np.array([
            [1, 0],
            [0, 1 / np.sqrt(2) + 1j * 1 / np.sqrt(2)]
        ], dtype=self._precision)

    def inverse(self):
        """ change it be tdg gate"""
        _Tdagger = TDaggerGate()
        _Tdagger.targs = copy.deepcopy(self.targs)
        _Tdagger.assigned_qubits = copy.deepcopy(self.assigned_qubits)

        return _Tdagger


T = TGate()


class TDaggerGate(BasicGate):
    """ The conjugate transpose of T gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.tdg,
            matrix_type=MatrixType.control
        )

        self.matrix = np.array([
            [1, 0],
            [0, 1 / np.sqrt(2) + 1j * -1 / np.sqrt(2)]
        ], dtype=self._precision)

    def inverse(self):
        """ change it to be t gate """
        _Tgate = TGate()
        _Tgate.targs = copy.deepcopy(self.targs)
        _Tgate.assigned_qubits = copy.deepcopy(self.assigned_qubits)

        return _Tgate


T_dagger = TDaggerGate()


class PhaseGate(BasicGate):
    """ Phase gate """
    def __init__(self, params: list = [0]):
        super().__init__(
            controls=0,
            targets=1,
            params=1,
            type_=GateType.phase,
            matrix_type=MatrixType.control
        )

        self.pargs = params
        self._qasm_name = "p"

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return PhaseGate([alpha])

    @property
    def matrix(self):
        return np.array([
            [1, 0],
            [0, np.exp(self.parg * 1j)]
        ], dtype=self._precision)

    def inverse(self):
        _Phase = self.copy()
        _Phase.pargs = [-self.parg]

        return _Phase


Phase = PhaseGate()


class GlobalPhaseGate(BasicGate):
    """ Phase gate """
    def __init__(self, params: list = [0]):
        super().__init__(
            controls=0,
            targets=1,
            params=1,
            type_=GateType.gphase,
            matrix_type=MatrixType.diagonal
        )
        self._qasm_name = "phase"
        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return GlobalPhaseGate([alpha])

    @property
    def matrix(self):
        return np.array([
            [np.exp(self.parg * 1j), 0],
            [0, np.exp(self.parg * 1j)]
        ], dtype=self._precision)

    def inverse(self):
        _Phase = self.copy()
        _Phase.pargs = [-self.parg]

        return _Phase


GPhase = GlobalPhaseGate()


class CZGate(BasicGate):
    """ controlled-Z gate """
    def __init__(self):
        super().__init__(
            controls=1,
            targets=1,
            params=0,
            type_=GateType.cz,
            matrix_type=MatrixType.control
        )

        self.matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -1]
        ], dtype=self._precision)

        self._target_matrix = np.array([
            [1, 0],
            [0, -1]
        ], dtype=self._precision)

    @property
    def target_matrix(self):
        return self._target_matrix


CZ = CZGate()


class CXGate(BasicGate):
    """ controlled-X gate """
    def __init__(self):
        super().__init__(
            controls=1,
            targets=1,
            params=0,
            type_=GateType.cx,
            matrix_type=MatrixType.reverse
        )

        self.matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ], dtype=self._precision)

        self._target_matrix = np.array([
            [0, 1],
            [1, 0]
        ], dtype=self._precision)

    @property
    def target_matrix(self):
        return self._target_matrix


CX = CXGate()


class CYGate(BasicGate):
    """ controlled-Y gate """
    def __init__(self):
        super().__init__(
            controls=1,
            targets=1,
            params=0,
            type_=GateType.cy,
            matrix_type=MatrixType.reverse
        )

        self.matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, -1j],
            [0, 0, 1j, 0]
        ], dtype=self._precision)

        self._target_matrix = np.array([
            [0, -1j],
            [1j, 0]
        ], dtype=self._precision)

    @property
    def target_matrix(self):
        return self._target_matrix


CY = CYGate()


class CHGate(BasicGate):
    """ controlled-Hadamard gate """
    def __init__(self):
        super().__init__(
            controls=1,
            targets=1,
            params=0,
            type_=GateType.ch
        )

        self.matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1 / np.sqrt(2), 1 / np.sqrt(2)],
            [0, 0, 1 / np.sqrt(2), -1 / np.sqrt(2)]
        ], dtype=self._precision)

        self._target_matrix = np.array([
            [1 / np.sqrt(2), 1 / np.sqrt(2)],
            [1 / np.sqrt(2), -1 / np.sqrt(2)]
        ], dtype=self._precision)

    @property
    def target_matrix(self):
        return self._target_matrix


CH = CHGate()


class CRzGate(BasicGate):
    """ controlled-Rz gate """

    def __init__(self, params: list = [np.pi / 2]):
        super().__init__(
            controls=1,
            targets=1,
            params=1,
            type_=GateType.crz,
            matrix_type=MatrixType.diagonal
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return CRzGate([alpha])

    @property
    def matrix(self):
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, np.exp(-self.parg / 2 * 1j), 0],
            [0, 0, 0, np.exp(self.parg / 2 * 1j)]
        ], dtype=self._precision)

    @property
    def target_matrix(self) -> np.ndarray:
        return np.array([
            [np.exp(-self.parg / 2 * 1j), 0],
            [0, np.exp(self.parg / 2 * 1j)]
        ], dtype=self._precision)

    def inverse(self):
        _CRz = self.copy()
        _CRz.pargs = [-self.pargs[0]]

        return _CRz


CRz = CRzGate()


class CU1Gate(BasicGate):
    """ Controlled-U1 gate """
    def __init__(self, params: list = [np.pi / 2]):
        super().__init__(
            controls=1,
            targets=1,
            params=1,
            type_=GateType.cu1,
            matrix_type=MatrixType.control
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return CU1Gate([alpha])

    @property
    def matrix(self):
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, np.exp(1j * self.pargs[0])]
        ], dtype=self._precision)

    @property
    def target_matrix(self) -> np.ndarray:
        return np.array([
            [1, 0],
            [0, np.exp(1j * self.pargs[0])]
        ], dtype=self._precision)

    def inverse(self):
        _CU1 = self.copy()
        _CU1.pargs = [-self.pargs[0]]

        return _CU1

    def build_gate(self):
        from QuICT.core.gate import CompositeGate

        cgate = CompositeGate()
        with cgate:
            CRz(self.parg) & [0, 1]
            U1(self.parg / 2) & 0

        args = self.cargs + self.targs
        if len(args) == self.controls + self.targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


CU1 = CU1Gate()


class CU3Gate(BasicGate):
    """ Controlled-U3 gate """
    def __init__(self, params: list = [np.pi / 2, 0, 0]):
        super().__init__(
            controls=1,
            targets=1,
            params=3,
            type_=GateType.cu3
        )

        self.pargs = params

    def __call__(self, alpha, beta, gamma):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate
            beta (int/float/complex): The parameter for gate
            gamma (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        params = [alpha, beta, gamma]

        for param in params:
            self.permit_element(param)

        return CU3Gate(params)

    @property
    def matrix(self):
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, np.cos(self.pargs[0] / 2), -np.exp(1j * self.pargs[2]) * np.sin(self.pargs[0] / 2)],
            [0, 0, np.exp(1j * self.pargs[1]) * np.sin(self.pargs[0] / 2),
             np.exp(1j * (self.pargs[1] + self.pargs[2])) * np.cos(self.pargs[0] / 2)]
        ], dtype=self._precision)

    @property
    def target_matrix(self) -> np.ndarray:
        return np.array([
            [np.cos(self.pargs[0] / 2), -np.exp(1j * self.pargs[2]) * np.sin(self.pargs[0] / 2)],
            [np.exp(1j * self.pargs[1]) * np.sin(self.pargs[0] / 2),
             np.exp(1j * (self.pargs[1] + self.pargs[2])) * np.cos(self.pargs[0] / 2)]
        ], dtype=self._precision)

    def inverse(self):
        _CU3 = self.copy()
        _CU3.pargs = [self.pargs[0], np.pi - self.pargs[2], np.pi - self.pargs[1]]

        return _CU3

    def build_gate(self):
        from QuICT.qcda.synthesis import UnitaryDecomposition

        assert self.controls + self.targets > 0
        mapping_args = self.cargs + self.targs
        cgate, _ = UnitaryDecomposition().execute(self.matrix)
        if len(mapping_args) == self.controls + self.targets:
            cgate & mapping_args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


CU3 = CU3Gate()


class FSimGate(BasicGate):
    """ fSim gate """
    def __init__(self, params: list = [np.pi / 2, 0]):
        super().__init__(
            controls=0,
            targets=2,
            params=2,
            type_=GateType.fsim,
            matrix_type=MatrixType.ctrl_normal
        )

        self.pargs = params

    def __call__(self, alpha, beta):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate
            beta (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        params = [alpha, beta]
        for param in params:
            self.permit_element(param)

        return FSimGate(params)

    @property
    def matrix(self):
        costh = np.cos(self.pargs[0])
        sinth = np.sin(self.pargs[0])
        phi = self.pargs[1]

        return np.array([
            [1, 0, 0, 0],
            [0, costh, -1j * sinth, 0],
            [0, -1j * sinth, costh, 0],
            [0, 0, 0, np.exp(-1j * phi)]
        ], dtype=self._precision)

    def inverse(self):
        _FSim = self.copy()
        _FSim.pargs = [-self.pargs[0], -self.pargs[1]]

        return _FSim


FSim = FSimGate()


class RxxGate(BasicGate):
    """ Rxx gate """
    def __init__(self, params: list = [0]):
        super().__init__(
            controls=0,
            targets=2,
            params=1,
            type_=GateType.rxx,
            matrix_type=MatrixType.normal_normal
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return RxxGate([alpha])

    @property
    def matrix(self):
        costh = np.cos(self.parg / 2)
        sinth = np.sin(self.parg / 2)

        return np.array([
            [costh, 0, 0, -1j * sinth],
            [0, costh, -1j * sinth, 0],
            [0, -1j * sinth, costh, 0],
            [-1j * sinth, 0, 0, costh]
        ], dtype=self._precision)

    def inverse(self):
        _Rxx = self.copy()
        _Rxx.pargs = [-self.parg]

        return _Rxx

    def build_gate(self):
        from QuICT.core.gate import CompositeGate

        cgate = CompositeGate()
        with cgate:
            H & 0
            H & 1
            CX & [0, 1]
            Rz(self.parg) & 1
            CX & [0, 1]
            H & 0
            H & 1

        args = self.cargs + self.targs
        if len(args) == self.controls + self.targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


Rxx = RxxGate()


class RyyGate(BasicGate):
    """ Ryy gate """
    def __init__(self, params: list = [np.pi / 2]):
        super().__init__(
            controls=0,
            targets=2,
            params=1,
            type_=GateType.ryy,
            matrix_type=MatrixType.normal_normal
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return RyyGate([alpha])

    @property
    def matrix(self):
        costh = np.cos(self.parg / 2)
        sinth = np.sin(self.parg / 2)

        return np.array([
            [costh, 0, 0, 1j * sinth],
            [0, costh, -1j * sinth, 0],
            [0, -1j * sinth, costh, 0],
            [1j * sinth, 0, 0, costh]
        ], dtype=self._precision)

    def inverse(self):
        _Ryy = self.copy()
        _Ryy.pargs = [-self.parg]

        return _Ryy

    def build_gate(self):
        from QuICT.core.gate import CompositeGate

        cgate = CompositeGate()
        with cgate:
            Hy & 0
            Hy & 1
            CX & [0, 1]
            Rz(self.parg) & 1
            CX & [0, 1]
            Hy & 0
            Hy & 1

        args = self.cargs + self.targs
        if len(args) == self.controls + self.targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


Ryy = RyyGate()


class RzzGate(BasicGate):
    """ Rzz gate """
    def __init__(self, params: list = [np.pi / 2]):
        super().__init__(
            controls=0,
            targets=2,
            params=1,
            type_=GateType.rzz,
            matrix_type=MatrixType.diag_diag
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return RzzGate([alpha])

    @property
    def matrix(self):
        expth = np.exp(0.5j * self.parg)
        sexpth = np.exp(-0.5j * self.parg)

        return np.array([
            [sexpth, 0, 0, 0],
            [0, expth, 0, 0],
            [0, 0, expth, 0],
            [0, 0, 0, sexpth]
        ], dtype=self._precision)

    def inverse(self):
        _Rzz = self.copy()
        _Rzz.pargs = [-self.parg]

        return _Rzz

    def build_gate(self):
        from QuICT.core.gate import CompositeGate

        cgate = CompositeGate()
        with cgate:
            CX & [0, 1]
            Rz(self.parg) & 1
            CX & [0, 1]

        args = self.cargs + self.targs
        if len(args) == self.controls + self.targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


Rzz = RzzGate()


class RzxGate(BasicGate):
    """ Rzx gate """
    def __init__(self, params: list = [np.pi / 2]):
        super().__init__(
            controls=0,
            targets=2,
            params=1,
            type_=GateType.rzx,
            matrix_type=MatrixType.diag_normal
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return RzxGate([alpha])

    @property
    def matrix(self):
        costh = np.cos(self.parg / 2)
        sinth = np.sin(self.parg / 2)

        return np.array([
            [costh, -1j * sinth, 0, 0],
            [-1j * sinth, costh, 0, 0],
            [0, 0, costh, 1j * sinth],
            [0, 0, 1j * sinth, costh]
        ], dtype=self._precision)

    def inverse(self):
        _Rzx = self.copy()
        _Rzx.pargs = [-self.parg]

        return _Rzx

    def build_gate(self):
        from QuICT.core.gate import CompositeGate

        cgate = CompositeGate()
        with cgate:
            H & 0
            CX & [0, 1]
            Rz(self.parg) & 1
            CX & [0, 1]
            H & 0

        args = self.cargs + self.targs
        if len(args) == self.controls + self.targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


Rzx = RzxGate()


class MeasureGate(BasicGate):
    """ z-axis Measure gate

    Measure one qubit along z-axis.
    After acting on the qubit(circuit flush), the qubit get the value 0 or 1
    and the amplitude changed by the result.
    """

    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.measure,
            matrix_type=MatrixType.special
        )

    @property
    def matrix(self) -> np.ndarray:
        raise GateMatrixError("try to get the matrix of measure gate")


Measure = MeasureGate()


class ResetGate(BasicGate):
    """ Reset gate

    Reset the qubit into 0 state,
    which change the amplitude
    """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.reset,
            matrix_type=MatrixType.special
        )

    @property
    def matrix(self) -> np.ndarray:
        raise GateMatrixError("try to get the matrix of reset gate")


Reset = ResetGate()


class BarrierGate(BasicGate):
    """ Barrier gate

    In IBMQ, barrier gate forbid the optimization cross the gate,
    It is invalid in out circuit now.
    """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type_=GateType.barrier,
            matrix_type=MatrixType.special
        )

    @property
    def matrix(self) -> np.ndarray:
        raise GateMatrixError("try to get the matrix of barrier gate")


Barrier = BarrierGate()


class SwapGate(BasicGate):
    """ Swap gate

    In the computation, it will not change the amplitude.
    Instead, it change the index of a Tangle.
    """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=2,
            params=0,
            type_=GateType.swap,
            matrix_type=MatrixType.swap
        )

        self.matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ], dtype=np.complex128)

    def build_gate(self):
        from QuICT.core.gate import CompositeGate

        cgate = CompositeGate()
        with cgate:
            CX & [0, 1]
            CX & [1, 0]
            CX & [0, 1]

        args = self.cargs + self.targs
        if len(args) == self.controls + self.targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


Swap = SwapGate()


class iSwapGate(BasicGate):
    """ iSwap gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=2,
            params=0,
            type_=GateType.iswap,
            matrix_type=MatrixType.swap,
        )

        self.matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, 1j, 0],
            [0, 1j, 0, 0],
            [0, 0, 0, 1]
        ], dtype=np.complex128)


iSwap = iSwapGate()


class iSwapDaggerGate(BasicGate):
    """ iSwap gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=2,
            params=0,
            type_=GateType.iswapdg,
            matrix_type=MatrixType.swap,
        )

        self.matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, -1j, 0],
            [0, -1j, 0, 0],
            [0, 0, 0, 1]
        ], dtype=np.complex128)


iSwap_dagger = iSwapDaggerGate()


class SquareRootiSwapGate(BasicGate):
    """ Square Root of iSwap gate """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=2,
            params=0,
            type_=GateType.sqiswap,
            matrix_type=MatrixType.swap,
        )

        self.matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, (1 + 1j) / np.sqrt(2), 0],
            [0, (1 + 1j) / np.sqrt(2), 0, 0],
            [0, 0, 0, 1]
        ], dtype=np.complex128)


sqiSwap = SquareRootiSwapGate()


# PermGate class -- no qasm
class PermGate(BasicGate):
    """ Permutation gate

    A special gate defined in our circuit,
    It can change an n-qubit qureg's amplitude by permutaion,
    the parameter is a 2^n list describes the permutation.
    """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=0,
            params=0,
            type_=GateType.perm,
            matrix_type=MatrixType.special
        )

    def __call__(self, targets: int, params: list):
        """ pass permutation to the gate

        the length of params must be n, and should be a permutation for [0, n) without repeat

        Args:
            targets(int): the number of qubits
            params(list): the permutation parameters

        Returns:
            PermGate: the gate after filled by parameters
        """
        if not isinstance(params, list):
            raise TypeError("PermGate.params", "list", type(params))
        if not isinstance(targets, int):
            raise TypeError("PermGate.targets", "int", type(targets))

        assert len(params) == targets, GateParametersAssignedError("the length of params must equal to targets")

        _gate = self.copy()
        _gate.targets = targets
        _gate.params = targets
        for idx in params:
            if not isinstance(idx, int):
                raise TypeError("PermGate.params.values", "int", type(idx))
            if idx < 0 or idx >= _gate.targets:
                raise ValueError("PermGate.params.values", f"[0, {targets}]", idx)
            if idx in _gate.pargs:
                raise ValueError("PermGate.params.values", "have no duplicated value", idx)

            _gate.pargs.append(idx)

        return _gate

    def inverse(self):
        _gate = self.copy()
        _gate.pargs = [self.targets - 1 - p for p in self.pargs]

        return _gate

    def build_gate(self, targs: list = None):
        from QuICT.core.gate import CompositeGate

        swap_args: list[list[int]] = perm_decomposition(self.pargs[:])
        cgate = CompositeGate()
        with cgate:
            for swap_arg in swap_args:
                Swap & swap_arg

        if targs is not None:
            assert len(targs) == self.targets + self.controls, \
                GateQubitAssignedError("The qubits number should equal to the quantum gate.")
            cgate & targs

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


Perm = PermGate()


class PermFxGate(BasicGate):
    """ act an Fx oracle on a qureg

    This Class is the subClass of PermGate.
    In fact, we calculate the permutation by the parameters.

    """

    def __init__(self):
        super().__init__(
            controls=0,
            targets=0,
            params=0,
            type_=GateType.perm_fx,
            matrix_type=MatrixType.normal
        )

    def __call__(self, n: int, params: list):
        """ pass Fx to the gate

        Args:
            n (int): the number of targets
            params (list[int]): the list of index, and the index represent which should be 1.

        Returns:
            PermFxGate: the gate after filled by parameters
        """
        if not isinstance(params, list) or not isinstance(n, int):
            raise TypeError(f"n must be int {type(n)}, params must be list {type(params)}")

        N = 1 << n
        for p in params:
            if p >= N:
                raise Exception("the params should be less than N")

        _gate = self.copy()
        _gate.params = 1 << (n + 1)
        _gate.targets = n + 1
        for idx in range(1 << _gate.targets):
            if idx >> 1 in params:
                _gate.pargs.append(idx ^ 1)
            else:
                _gate.pargs.append(idx)

        _gate.matrix = self._build_matrix(_gate.targets, _gate.pargs)

        return _gate

    def _build_matrix(self, targets, pargs):
        matrix_ = np.zeros((1 << targets, 1 << targets), dtype=self.precision)
        for idx, p in enumerate(pargs):
            matrix_[idx, p] = 1

        return matrix_


PermFx = PermFxGate()


class UnitaryGate(BasicGate):
    """ Custom gate

    act an unitary matrix on the qureg,
    the parameters is the matrix

    """
    def __init__(self):
        super().__init__(
            controls=0,
            targets=0,
            params=0,
            type_=GateType.unitary
        )

    def __call__(self, params: np.array, matrix_type: MatrixType = MatrixType.normal):
        """ pass the unitary matrix

        Args:
            params(np.array/list): contain 2^n * 2^n elements, which
            form an unitary matrix.

        Returns:
            UnitaryGateGate: the gate after filled by parameters
        """
        _u = UnitaryGate()

        if isinstance(params, list):
            params = np.array(params, dtype=self._precision)

        matrix_size = params.size
        if matrix_size == 0:
            raise GateMatrixError("the list or tuple passed in shouldn't be empty")

        length, width = params.shape
        if length != width:
            N = int(np.log2(matrix_size))
            assert N ^ 2 == matrix_size, GateMatrixError("the shape of unitary matrix should be square.")

            params = params.reshape(N, N)

        n = int(np.log2(params.shape[0]))
        if (1 << n) != params.shape[0]:
            raise GateMatrixError("the length of list should be the square of power(2, n)")

        _u.targets = n
        _u.matrix = params.astype(self._precision)
        if n <= 3:
            _u._validate_matrix_type()
        else:
            _u._matrix_type = matrix_type

        return _u

    def _validate_matrix_type(self):
        if self._is_diagonal():
            is_control = np.allclose(self.matrix[:-1, :-1], np.identity((2 ** self.targets - 1), dtype=self._precision))
            self._matrix_type = MatrixType.control if is_control else MatrixType.diagonal

        if (
            np.allclose(self.matrix[:-2, :-2], np.identity((2 ** self.targets - 2), dtype=self._precision)) and
            np.sum(self.matrix[:-2, -1]) + self.matrix[-1, -1] == 0 and
            np.sum(self.matrix[-1, :-2]) + self.matrix[-2, -2] == 0
        ):
            self._matrix_type = MatrixType.reverse

    def copy(self):
        gate = super().copy()
        gate.matrix = self.matrix

        return gate

    def inverse(self):
        _U = super().copy()
        inverse_matrix = np.array(
            np.mat(self._matrix).reshape(1 << self.targets, 1 << self.targets).H.reshape(1, -1),
            dtype=self._precision
        )
        _U.matrix = inverse_matrix
        _U.targets = self.targets

        return _U

    def build_gate(self):
        from QuICT.qcda.synthesis import UnitaryDecomposition

        assert self.controls + self.targets > 0
        mapping_args = self.cargs + self.targs
        cgate, _ = UnitaryDecomposition().execute(self.matrix)
        cgate & mapping_args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


Unitary = UnitaryGate()


class CCXGate(BasicGate):
    """ Toffoli gate

    When using this gate, it will be showed as a whole gate
    instend of being split into smaller gate

    """
    def __init__(self):
        super().__init__(
            controls=2,
            targets=1,
            params=0,
            type_=GateType.ccx,
            matrix_type=MatrixType.reverse
        )

        self.matrix = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0]
        ], dtype=self._precision)

        self._target_matrix = np.array([
            [0, 1],
            [1, 0]
        ], dtype=self._precision)

    @property
    def target_matrix(self) -> np.ndarray:
        return self._target_matrix

    def build_gate(self):
        from QuICT.core.gate import CompositeGate

        cgate = CompositeGate()
        with cgate:
            H & 2
            CX & [2, 1]
            T_dagger & 1
            CX & [0, 1]
            T & 1
            CX & [2, 1]
            T_dagger & 1
            CX & [0, 1]
            T & 1
            CX & [0, 2]
            T_dagger & 2
            CX & [0, 2]
            T & 0
            T & 2
            H & 2

        args = self.cargs + self.targs
        if len(args) == self.controls + self.targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


CCX = CCXGate()


class CCZGate(BasicGate):
    """ Multi-control Z gate

    When using this gate, it will be showed as a whole gate
    instend of being split into smaller gate

    """
    def __init__(self):
        super().__init__(
            controls=2,
            targets=1,
            params=0,
            type_=GateType.ccz
        )

        self.matrix = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, -1]
        ], dtype=self._precision)

        self._target_matrix = np.array([
            [1, 0],
            [0, -1]
        ], dtype=self._precision)

    @property
    def target_matrix(self) -> np.ndarray:
        return self._target_matrix

    def build_gate(self):
        from QuICT.core.gate import CompositeGate

        cgate = CompositeGate()
        with cgate:
            CX & [2, 1]
            T_dagger & 1
            CX & [0, 1]
            T & 1
            CX & [2, 1]
            T_dagger & 1
            CX & [0, 1]
            T & 1
            CX & [0, 2]
            T_dagger & 2
            CX & [0, 2]
            T & 0
            T & 2

        args = self.cargs + self.targs
        if len(args) == self.controls + self.targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


CCZ = CCZGate()


class CCRzGate(BasicGate):
    """ controlled-Rz gate with two control bits """
    def __init__(self, params: list = [0]):
        super().__init__(
            controls=2,
            targets=1,
            params=1,
            type_=GateType.ccrz,
            matrix_type=MatrixType.diagonal
        )

        self.pargs = params

    def __call__(self, alpha):
        """ Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return CCRzGate([alpha])

    @property
    def matrix(self):
        return np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, np.exp(-self.parg / 2 * 1j), 0],
            [0, 0, 0, 0, 0, 0, 0, np.exp(self.parg / 2 * 1j)]
        ], dtype=self._precision)

    @property
    def target_matrix(self) -> np.ndarray:
        return np.array([
            [np.exp(-self.parg / 2 * 1j), 0],
            [0, np.exp(self.parg / 2 * 1j)]
        ], dtype=self._precision)

    def inverse(self):
        _CCRz = self.copy()
        _CCRz.pargs = -self.parg
        return _CCRz

    def build_gate(self):
        from QuICT.core.gate import CompositeGate

        cgate = CompositeGate()
        with cgate:
            CRz(self.parg / 2) & [1, 2]
            CX & [0, 1]
            CRz(-self.parg / 2) & [1, 2]
            CX & [0, 1]
            CRz(self.parg / 2) & [0, 2]

        args = self.cargs + self.targs
        if len(args) == self.controls + self.targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


CCRz = CCRzGate()


class QFTGate(BasicGate):
    """ QFT gate """
    @property
    def matrix(self) -> np.ndarray:
        if self._matrix is None:
            cgate = self.build_gate()
            self._matrix = cgate.matrix()
        return self._matrix

    def __init__(self, targets: int = 3):
        super().__init__(
            controls=0,
            targets=targets,
            params=0,
            type_=GateType.qft
        )

    def __call__(self, targets: int):
        """ pass the unitary matrix

        Args:
            targets(int): point out the number of bits of the gate

        Returns:
            QFTGate: the QFTGate after filled by target number
        """
        return QFTGate(targets)

    def inverse(self):
        _IQFT = IQFTGate()
        _IQFT.targs = copy.deepcopy(self.targs)
        _IQFT.targets = self.targets
        return _IQFT

    def build_gate(self, targets: int = 0):
        from QuICT.core.gate import CompositeGate

        if targets == 0:
            targets = self.targets

        cgate = CompositeGate()
        with cgate:
            for i in range(targets):
                H & i
                for j in range(i + 1, targets):
                    CU1(2 * np.pi / (1 << j - i + 1)) & [j, i]

        args = self.cargs + self.targs
        if len(args) == targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


QFT = QFTGate()


class IQFTGate(QFTGate):
    """ IQFT gate """
    def __call__(self, targets: int):
        """ pass the unitary matrix

        Args:
            targets(int): point out the number of bits of the gate

        Returns:
            IQFTGate: the IQFTGate after filled by target number
        """
        return IQFTGate(targets)

    def inverse(self):
        _QFT = QFTGate()
        _QFT.targs = copy.deepcopy(self.targs)
        _QFT.targets = self.targets
        return _QFT

    def build_gate(self, targets: int = 0):
        from QuICT.core.gate import CompositeGate

        if targets == 0:
            targets = self.targets

        cgate = CompositeGate()
        with cgate:
            for i in range(targets - 1, -1, -1):
                for j in range(targets - 1, i, -1):
                    CU1(-2 * np.pi / (1 << j - i + 1)) & [j, i]
                H & i

        args = self.cargs + self.targs
        if len(args) == targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


IQFT = IQFTGate()


class CSwapGate(BasicGate):
    """ Fredkin gate

    When using this gate, it will be showed as a whole gate
    instend of being split into smaller gate
    """
    def __init__(self):
        super().__init__(
            controls=1,
            targets=2,
            params=0,
            type_=GateType.cswap,
            matrix_type=MatrixType.swap
        )

        self.matrix = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1]
        ], dtype=self._precision)

        self._target_matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ], dtype=self._precision)

    @property
    def target_matrix(self) -> np.ndarray:
        return self._target_matrix

    def build_gate(self):
        from QuICT.core.gate import CompositeGate

        cgate = CompositeGate()
        with cgate:
            CX & [2, 1]
            H & 2
            CX & [2, 1]
            T_dagger & 1
            CX & [0, 1]
            T & 1
            CX & [2, 1]
            T_dagger & 1
            CX & [0, 1]
            T & 1
            CX & [0, 2]
            T_dagger & 2
            CX & [0, 2]
            T & 0
            T & 2
            H & 2
            CX & [2, 1]

        args = self.cargs + self.targs
        if len(args) == self.controls + self.targets:
            cgate & args

        if self._precision == np.complex64:
            cgate.convert_precision()

        return cgate


CSwap = CSwapGate()
