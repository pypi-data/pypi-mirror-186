import cupy as cp
import numpy as np
import torch


from QuICT.ops.utils import LinAlgLoader
from QuICT.algorithm.quantum_machine_learning.utils.gate_tensor import *


class GpuSimulator:
    """A GPU simulator for gradient propagation."""

    def __init__(self):
        self.algorithm = LinAlgLoader(
            device="GPU",
            enable_gate_kernel=True,
            enable_multigpu_gate_kernel=False,
        )

    def forward(self, ansatz, state=None):
        """The Forward Propagation process of an ansatz.
           Only for GPU simulations that need to return gradients.

        Args:
            ansatz (Ansatz): Ansatz that needs to be simulated.
            state (torch.Tensor, optional): The initial state vector.
                Defaults to None, which means |0>.

        Returns:
            torch.Tensor: The state vector.
        """
        n_qubits = ansatz.n_qubits

        if state is None:
            state = torch.zeros(1 << n_qubits, dtype=torch.complex128).to(ansatz.device)
            state[0] = 1
        else:
            if isinstance(state, np.ndarray):
                state = torch.from_numpy(state).to(ansatz.device)
            else:
                state = state.clone()
        assert state.shape[0] == 1 << n_qubits

        params = torch.stack(ansatz.trainable_pargs)
        state = Applygate.apply(state, ansatz, params, self.algorithm, n_qubits)

        return state

    def measure_prob(self, qid, state):
        """Measure the probability that a qubit has a value of 0 and 1 according to the state.

        Args:
            qid (int): The index of the qubit.
            state (torch.Tensor): The state vector.

        Returns:
            list: The probabilities of qubit with given index to be 0 and 1.
        """
        n_qubits = int(np.log2(state.shape[0]))
        assert 0 <= qid <= n_qubits
        index = n_qubits - 1 - qid
        prob_1 = MeasureProb.apply(index, state, self.algorithm, n_qubits)
        prob = [1 - prob_1, prob_1]
        return prob


def _apply_normal_matrix(
    gate: BasicGateTensor, default_parameters, algorithm, n_qubits, fp
):
    # Get gate's parameters
    assert gate.matrix_type == MatrixType.normal
    args_num = gate.controls + gate.targets
    gate_args = gate.cargs + gate.targs
    matrix = (
        cp.from_dlpack(gate.matrix.clone())
        if fp
        else cp.from_dlpack(gate.gradient.clone())
    )

    # Deal with 1-qubit normal gate e.g. H
    if args_num == 1:
        index = n_qubits - 1 - gate_args[0]
        algorithm.normal_targ(index, matrix, *default_parameters)
    elif args_num == 2:  # Deal with 2-qubits control normal gate e.g. CH
        if gate.controls == gate.targets:
            c_index = n_qubits - 1 - gate.carg
            t_index = n_qubits - 1 - gate.targ
            algorithm.normal_ctargs(c_index, t_index, matrix, *default_parameters)
        elif gate.targets == 2:  # Deal with 2-qubits unitary gate
            indexes = [n_qubits - 1 - index for index in gate_args]
            algorithm.normal_targs(indexes, matrix, *default_parameters)
        else:
            raise KeyError("Quantum gate cannot only have control qubits.")


def _apply_normal_normal_matrix(
    gate: BasicGateTensor, default_parameters, algorithm, n_qubits, fp
):
    assert gate.matrix_type == MatrixType.normal_normal
    t_indexes = [n_qubits - 1 - targ for targ in gate.targs]
    matrix = (
        cp.from_dlpack(gate.matrix.clone())
        if fp
        else cp.from_dlpack(gate.gradient.clone())
    )
    algorithm.normal_normal_targs(t_indexes, matrix, *default_parameters)


def _apply_diagonal_normal_matrix(
    gate: BasicGateTensor, default_parameters, algorithm, n_qubits, fp
):
    assert gate.matrix_type == MatrixType.diag_normal
    t_indexes = [n_qubits - 1 - targ for targ in gate.targs]
    matrix = (
        cp.from_dlpack(gate.matrix.clone())
        if fp
        else cp.from_dlpack(gate.gradient.clone())
    )
    algorithm.diagonal_normal_targs(t_indexes, matrix, *default_parameters)


def _apply_diagonal_matrix(
    gate: BasicGateTensor, default_parameters, algorithm, n_qubits, fp
):
    # Get gate's parameters
    assert gate.matrix_type in [MatrixType.diagonal, MatrixType.diag_diag]
    args_num = gate.controls + gate.targets
    gate_args = gate.cargs + gate.targs
    matrix = (
        cp.from_dlpack(gate.matrix.clone())
        if fp
        else cp.from_dlpack(gate.gradient.clone())
    )

    # Deal with 1-qubit diagonal gate, e.g. Rz
    if args_num == 1:
        index = n_qubits - 1 - gate.targ
        algorithm.diagonal_targ(index, matrix, *default_parameters)
    elif args_num == 2:  # Deal with 2-qubit diagonal gate, e.g. CRz
        if gate.controls == gate.targets:
            c_index = n_qubits - 1 - gate.carg
            t_index = n_qubits - 1 - gate.targ
            algorithm.diagonal_ctargs(c_index, t_index, matrix, *default_parameters)
        elif gate.targets == 2:
            indexes = [n_qubits - 1 - index for index in gate_args]
            algorithm.diagonal_targs(indexes, matrix, *default_parameters)
        else:
            raise KeyError("Quantum gate cannot only have control qubits.")
    else:  # [CCRz]
        c_indexes = [n_qubits - 1 - carg for carg in gate.cargs]
        t_index = n_qubits - 1 - gate.targ
        algorithm.diagonal_more(c_indexes, t_index, matrix, *default_parameters)


def _apply_swap_matrix(gate: BasicGateTensor, default_parameters, algorithm, n_qubits):
    # Get gate's parameters
    assert gate.matrix_type == MatrixType.swap
    args_num = gate.controls + gate.targets
    gate_args = gate.cargs + gate.targs

    if args_num == 1:  # Deal with X Gate
        index = n_qubits - 1 - gate.targ
        algorithm.swap_targ(index, *default_parameters)
    elif args_num == 2:  # Deal with Swap Gate
        t_indexes = [n_qubits - 1 - targ for targ in gate_args]
        algorithm.swap_targs(t_indexes, *default_parameters)
    else:  # CSwap
        t_indexes = [n_qubits - 1 - targ for targ in gate.targs]
        c_index = n_qubits - 1 - gate.carg
        algorithm.swap_tmore(t_indexes, c_index, *default_parameters)


def _apply_reverse_matrix(
    gate: BasicGateTensor, default_parameters, algorithm, n_qubits
):
    # Get gate's parameters
    assert gate.matrix_type == MatrixType.reverse
    args_num = gate.controls + gate.targets
    gate_args = gate.cargs + gate.targs
    matrix = cp.from_dlpack(gate.matrix.clone())

    if args_num == 1:  # Deal with 1-qubit reverse gate, e.g. Y
        index = n_qubits - 1 - gate_args[0]
        algorithm.reverse_targ(index, matrix, *default_parameters)
    elif args_num == 2:  # only consider 1 control qubit + 1 target qubit
        c_index = n_qubits - 1 - gate_args[0]
        t_index = n_qubits - 1 - gate_args[1]
        algorithm.reverse_ctargs(c_index, t_index, matrix, *default_parameters)
    else:  # CCX
        c_indexes = [n_qubits - 1 - carg for carg in gate.cargs]
        t_index = n_qubits - 1 - gate.targ
        algorithm.reverse_more(c_indexes, t_index, *default_parameters)


def _apply_control_matrix(
    gate: BasicGateTensor, default_parameters, algorithm, n_qubits
):
    # Get gate's parameters
    assert gate.matrix_type == MatrixType.control
    args_num = gate.controls + gate.targets
    gate_args = gate.cargs + gate.targs
    matrix = cp.from_dlpack(gate.matrix.clone()).get()

    if args_num == 1:  # Deal with 1-qubit control gate, e.g. S
        index = n_qubits - 1 - gate_args[0]
        val = matrix[1, 1]
        algorithm.control_targ(index, val, *default_parameters)
    elif args_num == 2:  # Deal with 2-qubit control gate, e.g. CZ
        c_index = n_qubits - 1 - gate_args[0]
        t_index = n_qubits - 1 - gate_args[1]
        val = matrix[3, 3]
        algorithm.control_ctargs(c_index, t_index, val, *default_parameters)


def apply_gate(gate, default_parameters, algorithm, fp):
    """(GPU) Apply a tensor gate to a state vector.

    Args:
        gate (BasicGateTensor): The tensor quantum gate.
        default_parameters (tuple): _description_
        algorithm (LinAlgLoader): _description_
        fp (bool): Whether it is forward propagation. True if forward propagation, False if back propagation.

    Returns:
        torch.tensor: The state vector.
    """
    cupy_state = default_parameters[0]
    n_qubits = default_parameters[1]
    # Deal with quantum gate with more than 3 qubits.
    if (
        gate.type in [GateType.unitary, GateType.qft, GateType.iqft]
        and gate.targets >= 3
    ):
        matrix = cp.from_dlpack(gate.matrix.clone())
        matrix = matrix.reshape(
            1 << (gate.controls + gate.targets), 1 << (gate.controls + gate.targets)
        )
        cupy_state = algorithm.matrix_dot_vector(
            cupy_state, n_qubits, matrix, gate.cargs + gate.targs, True
        )
        state_out = torch.from_dlpack(cupy_state)
        return state_out

    matrix_type = gate.matrix_type
    # [H, SX, SY, SW, U2, U3, Rx, Ry] 2-bits [CH, ] 2-bits[targets] [unitary]
    if matrix_type == MatrixType.normal:
        _apply_normal_matrix(gate, default_parameters, algorithm, n_qubits, fp)
    # [Rz, Phase], 2-bits [CRz, Rzz], 3-bits [CCRz]
    elif matrix_type in [MatrixType.diagonal, MatrixType.diag_diag]:
        _apply_diagonal_matrix(gate, default_parameters, algorithm, n_qubits, fp)
    # [X] 2-bits [swap] 3-bits [CSWAP]
    elif matrix_type == MatrixType.swap:
        assert fp is True
        _apply_swap_matrix(gate, default_parameters, algorithm, n_qubits)
    # [Y] 2-bits [CX, CY] 3-bits: [CCX]
    elif matrix_type == MatrixType.reverse:
        assert fp is True
        _apply_reverse_matrix(gate, default_parameters, algorithm, n_qubits)
    # [S, sdg, Z, U1, T, tdg] # 2-bits [CZ, CU1]
    elif matrix_type == MatrixType.control:
        assert fp is True
        _apply_control_matrix(gate, default_parameters, algorithm, n_qubits)
    # [Rxx, Ryy]
    elif matrix_type == MatrixType.normal_normal:
        _apply_normal_normal_matrix(gate, default_parameters, algorithm, n_qubits, fp)
    # [Rzx]
    elif matrix_type == MatrixType.diag_normal:
        _apply_diagonal_normal_matrix(gate, default_parameters, algorithm, n_qubits, fp)

    state_out = torch.from_dlpack(cupy_state)
    return state_out


class Applygate(torch.autograd.Function):
    """The custom autograd function for applying a tensor gate to a state vector."""

    @staticmethod
    def forward(ctx, state, ansatz, pargs, algorithm, n_qubits):
        """The Forward Propagation process of an ansatz."""
        pargs = pargs.flatten()
        pargs_ptr = ansatz.trainable_pargs_ptr
        grads = [None] * pargs.shape[0]

        for gate in ansatz.gates:
            if gate.type == GateType.measure:
                continue
            cupy_state = cp.from_dlpack(state.clone())
            default_parameters = (cupy_state, n_qubits, True)
            state_out = apply_gate(gate, default_parameters, algorithm, True)

            for i in range(len(grads)):
                idx = (
                    pargs_ptr.index(gate.pargs.data_ptr())
                    if gate.pargs.requires_grad
                    else None
                )
                # fx = A * B: grad = 0
                if i != idx and grads[i] is None:
                    continue

                # fx = Gate * state(x): grad = Gate * grad_pre
                elif i != idx and grads[i] is not None:
                    cupy_grad = cp.from_dlpack(grads[i].conj().clone())
                    default_parameters = (cupy_grad, n_qubits, True)
                    grads[i] = apply_gate(
                        gate, default_parameters, algorithm, True
                    ).conj()

                # fx = Gate(x) * state: grad = Gate'(x) * state
                elif i == idx and grads[i] is None:
                    cupy_state = cp.from_dlpack(state.clone())
                    default_parameters = (cupy_state, n_qubits, True)
                    grads[idx] = apply_gate(
                        gate, default_parameters, algorithm, False
                    ).conj()

                # fx = Gate(x) * state(x): grad = Gate'(x) * state(x) + Gate(x) * grad_pre
                else:
                    cupy_state = cp.from_dlpack(state.clone())
                    default_parameters = (cupy_state, n_qubits, True)
                    grad1 = apply_gate(
                        gate, default_parameters, algorithm, False
                    ).conj()
                    cupy_grad = cp.from_dlpack(grads[idx].conj().clone())
                    default_parameters = (cupy_grad, n_qubits, True)
                    grad2 = apply_gate(gate, default_parameters, algorithm, True).conj()
                    grads[idx] = grad1 + grad2
            state = state_out

        # Turn None to zeros
        for i in range(len(grads)):
            if grads[i] is None:
                grads[i] = torch.zeros(1 << n_qubits, dtype=state.dtype).to(
                    state.device
                )

        grads = torch.stack(grads)
        ctx.save_for_backward(grads)
        return state

    @staticmethod
    def backward(ctx, grad_output):
        """The Backward Propagation process of an ansatz."""
        (grad,) = ctx.saved_tensors
        grad = grad_output * grad
        return None, None, grad.real, None, None


prob_grad_single_kernel = cp.RawKernel(
    r"""
    #include <cupy/complex.cuh>
    extern "C" __global__
    void ProbGradSingle(const int index, complex<float>* vec) {
        int label = blockDim.x * blockIdx.x + threadIdx.x;
        const int offset = 1 << index;

        int _0 = (label & ((1 << index) - 1)) + (label >> index << (index + 1));
        int _1 = _0 + offset;

        vec[_0] = 0.0;
        vec[_1] = 2.0 * vec[_1];
    }
    """,
    "ProbGradSingle",
)


prob_grad_double_kernel = cp.RawKernel(
    r"""
    #include <cupy/complex.cuh>
    extern "C" __global__
    void ProbGradDouble(const int index, complex<double>* vec) {
        int label = blockDim.x * blockIdx.x + threadIdx.x;
        const int offset = 1 << index;

        int _0 = (label & ((1 << index) - 1)) + (label >> index << (index + 1));
        int _1 = _0 + offset;

        vec[_0] = 0.0;
        vec[_1] = 2.0 * vec[_1];
    }
    """,
    "ProbGradDouble",
)


def measured_prob_grad(index, cupy_state, n_qubits):
    # Kernel function preparation
    task_number = 1 << (n_qubits - 1)
    thread_per_block = min(256, task_number)
    block_num = task_number // thread_per_block
    kernel_functions = (
        prob_grad_double_kernel
        if cupy_state.dtype == np.complex128
        else prob_grad_single_kernel
    )
    kernel_functions((block_num,), (thread_per_block,), (index, cupy_state))
    cp.cuda.Device().synchronize()

    grad = torch.from_dlpack(cupy_state)
    return grad


class MeasureProb(torch.autograd.Function):
    """The custom autograd function for measuring a qubit according to the state vector."""

    @staticmethod
    def forward(ctx, index, state, algorithm, n_qubits):
        """The Forward Propagation process of measuring the probability."""
        ctx.index = index
        ctx.state = state
        ctx.n_qubits = n_qubits

        cupy_state = cp.from_dlpack(state.detach().clone())
        prob = algorithm.measured_prob_calculate(
            index, cupy_state, n_qubits, all_measured=False, sync=True
        )
        prob = torch.from_dlpack(prob)
        return 1.0 - prob

    @staticmethod
    def backward(ctx, grad_output):
        """The Backward Propagation process of measuring the probability."""
        cupy_state = cp.from_dlpack(ctx.state.detach().clone())
        grad = measured_prob_grad(ctx.index, cupy_state, ctx.n_qubits)
        grad = grad_output * grad
        return None, grad, None, None
