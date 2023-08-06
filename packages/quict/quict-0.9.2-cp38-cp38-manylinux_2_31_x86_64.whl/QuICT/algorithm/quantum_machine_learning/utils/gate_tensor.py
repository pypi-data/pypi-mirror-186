import copy
from typing import Union

import numpy as np
import torch

from QuICT.core.gate import *
from QuICT.core.utils import SPECIAL_GATE_SET, GateType


class BasicGateTensor(object):
    """the abstract SuperClass of all basic tensor quantum gate

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
        pargs(torch.Tensor): the parameters
        parg(read only): the first object of pargs

        type(GateType, read only): gate's type described by GateType

        matrix(torch.Tensor): the unitary matrix of the quantum gate act on targets
    """

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def matrix(self) -> torch.Tensor:
        return self._matrix

    @matrix.setter
    def matrix(self, matrix) -> torch.Tensor:
        self._matrix = matrix

    @property
    def target_matrix(self) -> torch.Tensor:
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
        assert isinstance(controls, int)
        self._controls = controls

    @property
    def cargs(self):
        return self._cargs

    @cargs.setter
    def cargs(self, cargs: Union[list, int]):
        if isinstance(cargs, int):
            cargs = [cargs]

        assert len(cargs) == len(set(cargs)), "Duplicated control qubit indexes."
        self._cargs = cargs

    @property
    def targets(self) -> int:
        return self._targets

    @targets.setter
    def targets(self, targets: int):
        assert isinstance(targets, int)
        self._targets = targets

    @property
    def targs(self):
        return self._targs

    @targs.setter
    def targs(self, targs: list):
        if isinstance(targs, int):
            targs = [targs]

        assert len(targs) == len(set(targs)), "Duplicated target qubit indexes."
        assert not set(self._cargs) & set(
            targs
        ), "Same qubit indexes in control and target."
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
    def pargs(self, pargs: torch.Tensor):
        if isinstance(pargs, torch.Tensor):
            self._pargs = pargs if pargs.dim() > 0 else pargs.unsqueeze(0)
        elif isinstance(pargs, list):
            self._pargs = torch.tensor(pargs).to(self.device)
        elif isinstance(pargs, np.array):
            self._pargs = torch.from_numpy(pargs).to(self.device)
        else:
            self._pargs = torch.tensor([pargs]).to(self.device)
        assert self._pargs.shape[0] == self.params

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
    def device(self):
        return self._device

    def __init__(
        self,
        controls: int,
        targets: int,
        params: int,
        type: GateType,
        matrix_type: MatrixType = MatrixType.normal,
        device=torch.device("cuda:0"),
    ):
        self._matrix = None

        self._controls = controls
        self._targets = targets
        self._params = params
        self._device = device
        self._cargs = []  # list of int
        self._targs = []  # list of int
        self._pargs = torch.tensor([]).to(device)

        assert isinstance(type, GateType)
        self._type = type
        self._matrix_type = matrix_type
        self._precision = torch.complex128
        self._name = "-".join([str(type), "", ""])

        self.assigned_qubits = []  # list of qubits

    def __call__(self):
        """give parameters for the gate, and give parameters by "()", and parameters should be one of int/float/complex

        Some Examples are like this:

        Rz(np.pi / 2)           | qubit

        *Important*: There is no parameters for current quantum gate.

        Returns:
            BasicGateTensor: the gate after filled by parameters
        """
        return self.copy()

    def __eq__(self, other):
        assert isinstance(other, BasicGateTensor)
        if (
            self.type != other.type
            or (self.cargs + self.targs) != (other.cargs + other.targs)
            or not torch.allclose(self.matrix, other.matrix)
        ):
            return False

        return True

    def to(self, device: torch.device):
        """Move the tensor quantum gate to specify device.

        Args:
            device (torch.device): cpu or cuda device.

        Returns:
            BasicGateTensor: the gate on the specified device.
        """
        self._pargs = self._pargs.to(device)
        if self._matrix is not None:
            self._matrix = self._matrix.to(device)
        return self.copy()

    def update_name(self, qubit_id: str, circuit_idx: int = None):
        """Updated gate's name with the given information

        Args:
            qubit_id (str): The qubit's ID.
            circuit_idx (int, optional): The gate's order index in the circuit. Defaults to None.
        """
        qubit_id = qubit_id[:6]
        name_parts = self.name.split("-")
        name_parts[1] = qubit_id

        if circuit_idx is not None:
            name_parts[2] = str(circuit_idx)

        self.name = "-".join(name_parts)

    def change_pargs(self, pargs: list):
        if isinstance(pargs, list):
            pargs = torch.tensor(pargs).to(self._device)
        else:
            pargs = pargs.detach().to(self._device)
        parg_gate_dict = {
            "GateType.rx": Rx_tensor,
            "GateType.ry": Ry_tensor,
            "GateType.rz": Rz_tensor,
            "GateType.gphase": GPhase_tensor,
            "GateType.rxx": Rxx_tensor,
            "GateType.ryy": Ryy_tensor,
            "GateType.rzz": Rzz_tensor,
            "GateType.rzx": Rzx_tensor,
        }
        type_str = self._name[: self._name.find("-")]
        new_gate = parg_gate_dict[type_str](pargs).to(self._device)
        new_gate._targs = self._targs
        new_gate._cargs = self._cargs
        return new_gate

    def __str__(self):
        """get gate information"""
        gate_info = {
            "name": self.name,
            "controls": self.controls,
            "control_bit": self.cargs,
            "targets": self.targets,
            "target_bit": self.targs,
            "parameters": self.pargs,
        }

        return str(gate_info)

    def copy(self):
        """return a copy of this gate

        Returns:
            gate(BasicGateTensor): a copy of this gate
        """
        class_name = str(self.__class__.__name__)
        gate = globals()[class_name]()

        if gate.type in SPECIAL_GATE_SET:
            gate.controls = self.controls
            gate.targets = self.targets
            gate.params = self.params

        gate.pargs = self.pargs
        gate.targs = copy.deepcopy(self.targs)
        gate.cargs = copy.deepcopy(self.cargs)

        if self.assigned_qubits:
            gate.assigned_qubits = copy.deepcopy(self.assigned_qubits)
            gate.update_name(gate.assigned_qubits[0].id)

        return gate

    def permit_element(self, element):
        """judge whether the type of a parameter is int/float/complex

        for a quantum gate, the parameter should be int/float/complex

        Args:
            element: the element to be judged

        Returns:
            bool: True if the type of element is int/float/complex/torch.Tensor
        """
        if not isinstance(element, (int, float, complex, torch.Tensor)):
            raise TypeError(self.type, "int/float/complex/torch.Tensor", type(element))
        return True


class HGate(BasicGateTensor):
    """Hadamard gate"""

    def __init__(self):
        super().__init__(controls=0, targets=1, params=0, type=GateType.h)

        self.matrix = torch.tensor(
            [[1 / np.sqrt(2), 1 / np.sqrt(2)], [1 / np.sqrt(2), -1 / np.sqrt(2)]],
            dtype=self._precision,
        ).to(self.device)

    @property
    def gradient(self):
        raise AttributeError(
            "Only parametric gates with trainable parameters have attribute 'gradient'"
        )


H_tensor = HGate()


class HYGate(BasicGateTensor):
    """Self-inverse gate"""

    def __init__(self):
        super().__init__(controls=0, targets=1, params=0, type=GateType.hy)

        self.matrix = torch.tensor(
            [[1 / np.sqrt(2), -1j / np.sqrt(2)], [1j / np.sqrt(2), -1 / np.sqrt(2)]],
            dtype=self._precision,
        ).to(self.device)

    @property
    def gradient(self):
        raise AttributeError(
            "Only parametric gates with trainable parameters have attribute 'gradient'"
        )


Hy_tensor = HYGate()


class CXGate(BasicGateTensor):
    """controlled-X gate"""

    def __init__(self):
        super().__init__(
            controls=1,
            targets=1,
            params=0,
            type=GateType.cx,
            matrix_type=MatrixType.reverse,
        )

        self.matrix = torch.tensor(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]],
            dtype=self._precision,
        ).to(self.device)

        self._target_matrix = torch.tensor([[0, 1], [1, 0]], dtype=self._precision).to(
            self.device
        )

    @property
    def target_matrix(self):
        return self._target_matrix

    @property
    def gradient(self):
        raise AttributeError(
            "Only parametric gates with trainable parameters have attribute 'gradient'"
        )


CX_tensor = CXGate()


class XGate(BasicGateTensor):
    """Pauli-X gate"""

    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type=GateType.x,
            matrix_type=MatrixType.swap,
        )

        self.matrix = torch.tensor([[0, 1], [1, 0]], dtype=self._precision).to(
            self.device
        )

    @property
    def gradient(self):
        raise AttributeError(
            "Only parametric gates with trainable parameters have attribute 'gradient'"
        )


X_tensor = XGate()


class YGate(BasicGateTensor):
    """Pauli-Y gate"""

    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type=GateType.y,
            matrix_type=MatrixType.reverse,
        )

        self.matrix = torch.tensor([[0, -1j], [1j, 0]], dtype=self._precision).to(
            self.device
        )

    @property
    def gradient(self):
        raise AttributeError(
            "Only parametric gates with trainable parameters have attribute 'gradient'"
        )


Y_tensor = YGate()


class ZGate(BasicGateTensor):
    """Pauli-Z gate"""

    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type=GateType.z,
            matrix_type=MatrixType.control,
        )

        self.matrix = torch.tensor([[1, 0], [0, -1]], dtype=self._precision).to(
            self.device
        )

    @property
    def gradient(self):
        raise AttributeError(
            "Only parametric gates with trainable parameters have attribute 'gradient'"
        )


Z_tensor = ZGate()


class RxGate(BasicGateTensor):
    """Rotation around the x-axis gate"""

    def __init__(self, params=torch.tensor([np.pi / 2])):
        super().__init__(controls=0, targets=1, params=1, type=GateType.rx)

        self.pargs = params

    def __call__(self, alpha):
        self.permit_element(alpha)

        return (
            RxGate(alpha)
            if isinstance(alpha, torch.Tensor)
            else RxGate(torch.tensor([alpha]))
        )

    @property
    def matrix(self):
        matrix = torch.zeros([2, 2], dtype=self._precision).to(self.device)
        matrix[0, 0] = torch.cos(self.parg / 2)
        matrix[0, 1] = -1j * torch.sin(self.parg / 2)
        matrix[1, 0] = -1j * torch.sin(self.parg / 2)
        matrix[1, 1] = torch.cos(self.parg / 2)

        return matrix

    @property
    def gradient(self):
        gradient = torch.zeros([2, 2], dtype=self._precision).to(self.device)
        gradient[0, 0] = -torch.sin(self.parg / 2) / 2
        gradient[0, 1] = -1j * torch.cos(self.parg / 2) / 2
        gradient[1, 0] = -1j * torch.cos(self.parg / 2) / 2
        gradient[1, 1] = -torch.sin(self.parg / 2) / 2

        return gradient


Rx_tensor = RxGate()


class RyGate(BasicGateTensor):
    """Rotation around the y-axis gate"""

    def __init__(self, params=torch.tensor([np.pi / 2])):
        super().__init__(controls=0, targets=1, params=1, type=GateType.ry)

        self.pargs = params

    def __call__(self, alpha):
        self.permit_element(alpha)

        return (
            RyGate(alpha)
            if isinstance(alpha, torch.Tensor)
            else RyGate(torch.tensor([alpha]))
        )

    @property
    def matrix(self):
        matrix = torch.zeros([2, 2], dtype=self._precision).to(self.device)
        matrix[0, 0] = torch.cos(self.parg / 2)
        matrix[0, 1] = -torch.sin(self.parg / 2)
        matrix[1, 0] = torch.sin(self.parg / 2)
        matrix[1, 1] = torch.cos(self.parg / 2)

        return matrix

    @property
    def gradient(self):
        gradient = torch.zeros([2, 2], dtype=self._precision).to(self.device)
        gradient[0, 0] = -torch.sin(self.parg / 2) / 2
        gradient[0, 1] = -torch.cos(self.parg / 2) / 2
        gradient[1, 0] = torch.cos(self.parg / 2) / 2
        gradient[1, 1] = -torch.sin(self.parg / 2) / 2

        return gradient


Ry_tensor = RyGate()


class RzGate(BasicGateTensor):
    """Rotation around the z-axis gate"""

    def __init__(self, params=torch.tensor([np.pi / 2])):
        super().__init__(
            controls=0,
            targets=1,
            params=1,
            type=GateType.rz,
            matrix_type=MatrixType.diagonal,
        )

        self.pargs = params

    def __call__(self, alpha):
        self.permit_element(alpha)

        return (
            RzGate(alpha)
            if isinstance(alpha, torch.Tensor)
            else RzGate(torch.tensor([alpha]))
        )

    @property
    def matrix(self):
        matrix = torch.zeros([2, 2], dtype=self._precision).to(self.device)
        matrix[0, 0] = torch.exp(-self.parg / 2 * 1j)
        matrix[1, 1] = torch.exp(self.parg / 2 * 1j)

        return matrix

    @property
    def gradient(self):
        gradient = torch.zeros([2, 2], dtype=self._precision).to(self.device)
        gradient[0, 0] = -1j * torch.exp(-self.parg / 2 * 1j) / 2
        gradient[1, 1] = 1j * torch.exp(self.parg / 2 * 1j) / 2

        return gradient


Rz_tensor = RzGate()


class GlobalPhaseGate(BasicGateTensor):
    """Phase gate"""

    def __init__(self, params=torch.tensor([0])):
        super().__init__(
            controls=0,
            targets=1,
            params=1,
            type=GateType.gphase,
            matrix_type=MatrixType.diagonal,
        )
        self._qasm_name = "phase"
        self.pargs = params

    def __call__(self, alpha):
        """Set parameters for the gate.

        Args:
            alpha (int/float/complex): The parameter for gate

        Raises:
            TypeError: param not one of int/float/complex

        Returns:
            BasicGate: The gate with parameters
        """
        self.permit_element(alpha)

        return (
            GlobalPhaseGate(alpha)
            if isinstance(alpha, torch.Tensor)
            else GlobalPhaseGate(torch.tensor([alpha]))
        )

    @property
    def matrix(self):
        return torch.tensor(
            [[torch.exp(self.parg * 1j), 0], [0, torch.exp(self.parg * 1j)]],
            dtype=self._precision,
        ).to(self.device)

    @property
    def gradient(self):
        raise AttributeError(
            "Only parametric gates with trainable parameters have attribute 'gradient'"
        )

    def inverse(self):
        _Phase = self.copy()
        _Phase.pargs = [-self.parg]

        return _Phase


GPhase_tensor = GlobalPhaseGate()


class RxxGate(BasicGateTensor):
    """Rxx Gate (rotation about XX)"""

    def __init__(self, params=torch.tensor([np.pi / 2])):
        super().__init__(
            controls=0,
            targets=2,
            params=1,
            type=GateType.rxx,
            matrix_type=MatrixType.normal_normal,
        )

        self.pargs = params

    def __call__(self, alpha):
        self.permit_element(alpha)

        return (
            RxxGate(alpha)
            if isinstance(alpha, torch.Tensor)
            else RxxGate(torch.tensor([alpha]))
        )

    @property
    def matrix(self):
        matrix = torch.zeros([4, 4], dtype=self._precision).to(self.device)
        matrix[0, 0] = matrix[1, 1] = matrix[2, 2] = matrix[3, 3] = torch.cos(
            self.parg / 2
        )
        matrix[0, 3] = matrix[3, 0] = matrix[1, 2] = matrix[2, 1] = (
            -torch.sin(self.parg / 2) * 1j
        )

        return matrix

    @property
    def gradient(self):
        gradient = torch.zeros([4, 4], dtype=self._precision).to(self.device)
        gradient[0, 0] = gradient[1, 1] = gradient[2, 2] = gradient[3, 3] = (
            -torch.sin(self.parg / 2) / 2
        )
        gradient[0, 3] = gradient[3, 0] = gradient[1, 2] = gradient[2, 1] = (
            -torch.cos(self.parg / 2) * 1j / 2
        )

        return gradient


Rxx_tensor = RxxGate()


class RyyGate(BasicGateTensor):
    """Ryy Gate (rotation about YY)"""

    def __init__(self, params=torch.tensor([np.pi / 2])):
        super().__init__(
            controls=0,
            targets=2,
            params=1,
            type=GateType.ryy,
            matrix_type=MatrixType.normal_normal,
        )

        self.pargs = params

    def __call__(self, alpha):
        self.permit_element(alpha)

        return (
            RyyGate(alpha)
            if isinstance(alpha, torch.Tensor)
            else RyyGate(torch.tensor([alpha]))
        )

    @property
    def matrix(self):
        matrix = torch.zeros([4, 4], dtype=self._precision).to(self.device)
        matrix[0, 0] = matrix[1, 1] = matrix[2, 2] = matrix[3, 3] = torch.cos(
            self.parg / 2
        )
        matrix[0, 3] = matrix[3, 0] = torch.sin(self.parg / 2) * 1j
        matrix[1, 2] = matrix[2, 1] = -torch.sin(self.parg / 2) * 1j

        return matrix

    @property
    def gradient(self):
        gradient = torch.zeros([4, 4], dtype=self._precision).to(self.device)
        gradient[0, 0] = gradient[1, 1] = gradient[2, 2] = gradient[3, 3] = (
            -torch.sin(self.parg / 2) / 2
        )
        gradient[0, 3] = gradient[3, 0] = torch.cos(self.parg / 2) * 1j / 2
        gradient[1, 2] = gradient[2, 1] = -torch.cos(self.parg / 2) * 1j / 2

        return gradient


Ryy_tensor = RyyGate()


class RzzGate(BasicGateTensor):
    """Rzz Gate (rotation about ZZ)"""

    def __init__(self, params=torch.tensor([np.pi / 2])):
        super().__init__(
            controls=0,
            targets=2,
            params=1,
            type=GateType.rzz,
            matrix_type=MatrixType.diag_diag,
        )

        self.pargs = params

    def __call__(self, alpha):
        self.permit_element(alpha)

        return (
            RzzGate(alpha)
            if isinstance(alpha, torch.Tensor)
            else RzzGate(torch.tensor([alpha]))
        )

    @property
    def matrix(self):
        matrix = torch.zeros([4, 4], dtype=self._precision).to(self.device)
        matrix[0, 0] = torch.exp(-self.parg / 2 * 1j)
        matrix[1, 1] = torch.exp(self.parg / 2 * 1j)
        matrix[2, 2] = torch.exp(self.parg / 2 * 1j)
        matrix[3, 3] = torch.exp(-self.parg / 2 * 1j)

        return matrix

    @property
    def gradient(self):
        gradient = torch.zeros([4, 4], dtype=self._precision).to(self.device)
        gradient[0, 0] = -1j * torch.exp(-self.parg / 2 * 1j) / 2
        gradient[1, 1] = 1j * torch.exp(self.parg / 2 * 1j) / 2
        gradient[2, 2] = 1j * torch.exp(self.parg / 2 * 1j) / 2
        gradient[3, 3] = -1j * torch.exp(-self.parg / 2 * 1j) / 2

        return gradient


Rzz_tensor = RzzGate()


class RzxGate(BasicGateTensor):
    """Rzx Gate (rotation about ZX)"""

    def __init__(self, params=torch.tensor([np.pi / 2])):
        super().__init__(
            controls=0,
            targets=2,
            params=1,
            type=GateType.rzx,
            matrix_type=MatrixType.diag_normal,
        )

        self.pargs = params

    def __call__(self, alpha):
        self.permit_element(alpha)

        return (
            RzxGate(alpha)
            if isinstance(alpha, torch.Tensor)
            else RzxGate(torch.tensor([alpha]))
        )

    @property
    def matrix(self):
        matrix = torch.zeros([4, 4], dtype=self._precision).to(self.device)
        matrix[0, 0] = matrix[1, 1] = matrix[2, 2] = matrix[3, 3] = torch.cos(
            self.parg / 2
        )
        matrix[0, 1] = matrix[1, 0] = -torch.sin(self.parg / 2) * 1j
        matrix[2, 3] = matrix[3, 2] = torch.sin(self.parg / 2) * 1j

        return matrix

    @property
    def gradient(self):
        gradient = torch.zeros([4, 4], dtype=self._precision).to(self.device)
        gradient[0, 0] = gradient[1, 1] = gradient[2, 2] = gradient[3, 3] = (
            -torch.sin(self.parg / 2) / 2
        )
        gradient[0, 1] = gradient[1, 0] = -torch.cos(self.parg / 2) * 1j / 2
        gradient[2, 3] = gradient[3, 2] = torch.cos(self.parg / 2) * 1j / 2

        return gradient


Rzx_tensor = RzxGate()


class MeasureGate(BasicGateTensor):
    """z-axis Measure gate

    Measure one qubit along z-axis.
    After acting on the qubit(circuit flush), the qubit get the value 0 or 1
    and the amplitude changed by the result.
    """

    def __init__(self):
        super().__init__(
            controls=0,
            targets=1,
            params=0,
            type=GateType.measure,
            matrix_type=MatrixType.special,
        )

    @property
    def matrix(self):
        raise Exception("try to get the matrix of measure gate")

    @property
    def gradient(self):
        raise AttributeError(
            "Only parametric gates with trainable parameters have attribute 'gradient'"
        )


Measure_tensor = MeasureGate()
