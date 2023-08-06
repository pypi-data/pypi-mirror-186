import cupy as cp
import random
import numpy as np
import torch

from QuICT.algorithm.quantum_machine_learning.utils.gate_tensor import *
from QuICT.algorithm.quantum_machine_learning.utils import apply_gate
from QuICT.core.gate import *
from QuICT.ops.utils import LinAlgLoader


class Ansatz:
    """The Ansatz class, which is similar to Circuit but support the auto-grad of Pytorch."""

    @property
    def n_qubits(self):
        return self._n_qubits

    @property
    def device(self):
        return self._device

    @property
    def gates(self):
        return self._gates

    @property
    def trainable_pargs(self):
        return self._trainable_pargs

    @property
    def trainable_pargs_ptr(self):
        return self._trainable_pargs_ptr

    def __init__(self, n_qubits, circuit=None, device=torch.device("cuda:0")):
        """Initialize an empty Ansatz or from a Circuit.

        Args:
            n_qubits (int): The number of qubits.
            circuit (Circuit, optional): Initialize an Ansatz from a Circuit. Defaults to None.
            device (torch.device, optional): The device to which the Ansatz is assigned.
                Defaults to torch.device("cuda:0").
        """
        self._n_qubits = n_qubits if circuit is None else circuit.width()
        self._device = device
        self._gates = [] if circuit is None else self._gate_to_tensor(circuit.gates)
        self._trainable_pargs = []
        self._trainable_pargs_ptr = []
        self._algorithm = (
            None
            if device.type == "cpu"
            else LinAlgLoader(
                device="GPU",
                enable_gate_kernel=True,
                enable_multigpu_gate_kernel=False,
            )
        )

    def __add__(self, other):
        """Add the gates of an ansatz into the ansatz."""
        ansatz = Ansatz(
            n_qubits=max(self._n_qubits, other._n_qubits), device=self._device
        )
        for gate in self._gates:
            gate.to(self._device)
            gate.update_name("ansatz", len(ansatz._gates))
            ansatz._gates.append(gate)
            if gate.pargs.requires_grad:
                ansatz._trainable_pargs.append(gate.pargs)
                ansatz._trainable_pargs_ptr.append(gate.pargs.data_ptr())

        for other_gate in other._gates:
            other_gate.to(self._device)
            other_gate.update_name("ansatz", len(ansatz._gates))
            ansatz._gates.append(other_gate)
            if other_gate.pargs.requires_grad:
                ansatz._trainable_pargs.append(other_gate.pargs)
                ansatz._trainable_pargs_ptr.append(other_gate.pargs.data_ptr())
        return ansatz

    def _gate_to_tensor(self, gates):
        """Copy the Circuit gates to Ansatz tensor gates."""
        gates_tensor = []
        for gate in gates:
            gate_tensor = BasicGateTensor(
                gate.controls, gate.targets, gate.params, gate.type, device=self._device
            )
            gate_tensor.pargs = torch.tensor(copy.deepcopy(gate.pargs)).to(self._device)
            gate_tensor.targs = copy.deepcopy(gate.targs)
            gate_tensor.cargs = copy.deepcopy(gate.cargs)
            gate_tensor.matrix = torch.from_numpy(gate.matrix).to(self._device)
            gate_tensor.assigned_qubits = copy.deepcopy(gate.assigned_qubits)
            if gate.assigned_qubits:
                gate_tensor.update_name(gate.assigned_qubits[0].id)
            gates_tensor.append(gate_tensor)

        return gates_tensor

    def add_gate(self, gate, act_bits: Union[int, list] = None):
        """Add a gate into the ansatz.

        Args:
            gate (BasicGateTensor): The tensor quantum gate.
            act_bits (Union[int, list], optional): The targets the gate acts on.
                Defaults to None, which means the gate will act on each qubit of the ansatz.
        """
        assert isinstance(gate.type, GateType)
        if gate.type == GateType.unitary:
            assert isinstance(gate.matrix, torch.Tensor)
            assert self._gate_validation(gate)

        if act_bits is None:
            for qid in range(self._n_qubits):
                new_gate = gate.to(self._device)
                new_gate.targs = [qid]
                new_gate.update_name("ansatz", len(self._gates))
                if new_gate.pargs.requires_grad:
                    ptr = new_gate.pargs.data_ptr()
                    if ptr not in self._trainable_pargs_ptr:
                        self._trainable_pargs.append(new_gate.pargs)
                        self._trainable_pargs_ptr.append(ptr)
                self._gates.append(new_gate)
        else:
            new_gate = gate.to(self._device)
            if isinstance(act_bits, int):
                new_gate.targs = act_bits
            else:
                assert len(act_bits) == new_gate.controls + new_gate.targets
                new_gate.cargs = act_bits[: new_gate.controls]
                new_gate.targs = act_bits[new_gate.controls:]
            new_gate.update_name("ansatz", len(self._gates))
            if new_gate.pargs.requires_grad:
                ptr = new_gate.pargs.data_ptr()
                if ptr not in self._trainable_pargs_ptr:
                    self._trainable_pargs.append(new_gate.pargs)
                    self._trainable_pargs_ptr.append(ptr)
            self._gates.append(new_gate)

    def _gate_validation(self, gate):
        """Validate the gate."""

        gate_matrix = gate.matrix
        shape = gate_matrix.shape
        log2_shape = int(np.ceil(np.log2(shape[0])))

        return (
            shape[0] == shape[1]
            and shape[0] == (1 << log2_shape)
            and torch.allclose(
                torch.eye(shape[0], dtype=gate.precision).to(self._device),
                torch.mm(gate_matrix, gate_matrix.T.conj()).to(self._device),
            )
        )

    def _apply_gate_gpu(self, state: torch.Tensor, gate: BasicGateTensor):
        """(GPU) Apply a tensor gate to a state vector.

        Args:
            state (torch.Tensor): The initial state vector.
            gate (BasicGateTensor): The tensor quantum gate.

        Returns:
            torch.Tensor: The state vector.
        """
        assert state.is_cuda, "Must use GPU."
        cupy_state = cp.from_dlpack(state.detach().clone())
        default_parameters = (cupy_state, self._n_qubits, True)
        state_out = apply_gate(gate, default_parameters, self._algorithm, True)
        return state_out

    def _apply_gate_cpu(self, state, gate_tensor, act_bits):
        """(CPU) Apply a tensor gate to a state vector.

        Args:
            state (torch.Tensor): The initial state vector.
            gate_tensor (BasicGateTensor): The tensor quantum gate.
            act_bits (list): The targets the gate acts on.

        Returns:
            torch.Tensor: The state vector.
        """
        # Step 1: Relabel the qubits and calculate their corresponding index values.
        act_bits = [self._n_qubits - 1 - act_bits[i] for i in range(len(act_bits))]
        bits_idx = [1 << i for i in range(self._n_qubits)]
        act_bits_idx = list(np.array(bits_idx)[act_bits])
        act_bits_idx.reverse()
        inact_bits_idx = list(set(bits_idx) - set(act_bits_idx))

        # Step 2: Get the first set of action indices.
        _act_idx = [0]
        for i in range(len(act_bits_idx)):
            for j in range(len(_act_idx)):
                _act_idx.append(act_bits_idx[i] + _act_idx[j])
        _act_idx = torch.tensor(_act_idx).to(self._device)

        # Step 3: Get the following action indices.
        offsets = [0]
        for i in range(len(inact_bits_idx)):
            for j in range(len(offsets)):
                offsets.append(inact_bits_idx[i] + offsets[j])

        for offset in offsets:
            act_idx = _act_idx + offset * torch.ones(
                len(_act_idx), dtype=torch.int64
            ).to(self._device)

            # Step 4: Apply the gate on the action indices of the state.
            action_state = state.index_select(0, act_idx).reshape((act_idx.shape[0], 1))
            action_result = torch.mm(gate_tensor, action_state).reshape(
                act_idx.shape[0]
            )

            # Step 5: Refill the state vector according to the action indices.
            for i in range(len(act_idx)):
                state[act_idx[i]] = action_result[i]

        return state

    def _apply_measuregate(self, qid, state):
        """Apply a Measure gate to a state vector.

        Args:
            qid (int): The index of the measured qubit.
            state (torch.Tensor): The initial state vector.

        Returns:
            torch.Tensor: The state vector after measurement.
            list: The probabilities of measured qubit with given index to be 0 and 1.
        """
        index = self._n_qubits - 1 - qid
        bits_idx = [1 << i for i in range(self._n_qubits)]
        act_bit = 1 << index
        act_bits_idx = list(set(bits_idx) - set([act_bit]))

        idx_0 = [0]
        idx_1 = [act_bit]
        for i in range(len(act_bits_idx)):
            for j in range(len(idx_0)):
                idx = act_bits_idx[i] + idx_0[j]
                idx_0.append(idx)
                idx_1.append(idx + act_bit)

        # Calculate probabilities
        prob_0 = torch.sum(torch.abs(state[idx_0]) * torch.abs(state[idx_0]))

        _0 = random.random() < prob_0
        if _0:
            # The measured state of the qubit is |0>.
            alpha = 1 / torch.sqrt(prob_0)
            for idx in idx_1:
                state[idx] = 0
            for idx in idx_0:
                state[idx] *= alpha

        else:
            # The measured state of the qubit is |1>.
            alpha = 1 / torch.sqrt(1 - prob_0)
            for idx in idx_0:
                state[idx] = 0
            for idx in idx_1:
                state[idx] *= alpha

        return state

    def measure_prob(self, qid, state):
        """Measure the probability that a qubit has a value of 0 and 1 according to the state.

        Args:
            qid (int): The index of the qubit.
            state (torch.Tensor): The state vector.

        Returns:
            list: The probabilities of qubit with given index to be 0 and 1.
        """
        index = self._n_qubits - 1 - qid
        bits_idx = [1 << i for i in range(self._n_qubits)]
        act_bit = 1 << index
        act_bits_idx = list(set(bits_idx) - set([act_bit]))

        idx_0 = [0]
        for i in range(len(act_bits_idx)):
            for j in range(len(idx_0)):
                idx = act_bits_idx[i] + idx_0[j]
                idx_0.append(idx)

        # Calculate probabilities
        prob_0 = torch.sum(torch.abs(state[idx_0]) * torch.abs(state[idx_0]))
        return [prob_0, 1 - prob_0]

    def forward(self, state_vector=None):
        """The Forward Propagation process of an ansatz.
           Only for GPU simulations that do not need to return gradients or CPU simulations.

        Args:
            state_vector (np.array/torch.Tensor, optional): The initial state vector.
                Defaults to None, which means |0>.

        Returns:
            torch.Tensor: The state vector.
        """
        if state_vector is None:
            state = torch.zeros(1 << self._n_qubits, dtype=torch.complex128).to(
                self._device
            )
            state[0] = 1
        else:
            if isinstance(state_vector, np.ndarray):
                state = torch.from_numpy(state_vector).to(self._device)
            else:
                state = state_vector.clone()
        assert state.shape[0] == 1 << self._n_qubits

        for gate in self._gates:
            # Measure gate
            if gate.type == GateType.measure:
                state = self._apply_measuregate(gate.targ, state.clone())
            else:
                # CPU
                if self._device.type == "cpu":
                    gate_tensor = gate.matrix.to(self._device)
                    act_bits = gate.cargs + gate.targs
                    state = self._apply_gate_cpu(state, gate_tensor, act_bits)
                # GPU
                else:
                    assert (
                        len(self._trainable_pargs)
                        == len(self._trainable_pargs_ptr)
                        == 0
                    ), "Only ansatz without trainable parameters could use ansatz.forward()."
                    state = self._apply_gate_gpu(state, gate)

        return state
