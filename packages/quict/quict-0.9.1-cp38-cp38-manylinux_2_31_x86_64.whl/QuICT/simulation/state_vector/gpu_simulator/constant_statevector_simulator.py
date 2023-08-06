#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/6/28 下午4:50
# @Author  : Kaiqi Li
# @File    : constant_statevecto_simulator

from typing import Union
import numpy as np
import cupy as cp

from QuICT.core import Circuit
from QuICT.core.operator import Trigger
from QuICT.core.gate import BasicGate, CompositeGate
from QuICT.core.utils import GateType, MatrixType
from QuICT.ops.utils import LinAlgLoader
from QuICT.ops.gate_kernel import float_multiply, complex_multiply
from QuICT.simulation.utils import GateMatrixs
from QuICT.tools.exception.core import ValueError, TypeError, GateQubitAssignedError
from QuICT.tools.exception.simulation import (
    SampleBeforeRunError, GateTypeNotImplementError, StateVectorUnmatchedError, GateAlgorithmNotImplementError
)


class ConstantStateVectorSimulator:
    """
    The simulator for qubits' vector state.

    Args:
        circuit (Circuit): The quantum circuit.
        precision (str): The precision for the state vector, one of [single, double]. Defaults to "double".
        gpu_device_id (int): The GPU device ID.
        matrix_aggregation (bool): Using quantum gate matrix's aggregation to optimize running speed.
        sync (bool): Sync mode or Async mode.
    """
    __PRECISION = ["single", "double"]

    @property
    def circuit(self):
        return self._circuit

    @circuit.setter
    def circuit(self, circuit):
        self._circuit = circuit

    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, vec):
        with cp.cuda.Device(self._device_id):
            if type(vec) is np.ndarray:
                self._vector = cp.array(vec)
            else:
                self._vector = vec

    @property
    def device(self):
        return self._device_id

    def __init__(
        self,
        precision: str = "double",
        gpu_device_id: int = 0,
        matrix_aggregation: bool = True,
        sync: bool = True
    ):
        if precision not in self.__PRECISION:
            raise ValueError("StateVectorSimulation.precision", "[single, double]", precision)

        self._precision = np.complex128 if precision == "double" else np.complex64
        self._device_id = gpu_device_id
        self._sync = sync

        # Optimization
        self._using_matrix_aggregation = matrix_aggregation

        # Initial simulator with limit_qubits
        self._algorithm = LinAlgLoader(device="GPU", enable_gate_kernel=True, enable_multigpu_gate_kernel=False)
        # Set gpu id
        cp.cuda.runtime.setDevice(self._device_id)

    def initial_circuit(self, circuit: Circuit):
        """ Initial the qubits, quantum gates and state vector by given quantum circuit. """
        self._circuit = circuit
        self._qubits = int(circuit.width())
        self._pipeline = []

        if self._precision != circuit._precision:
            circuit.convert_precision()

        self._pipeline = circuit.gates

        # Initial GateMatrix if matrix_aggregation is True
        if self._using_matrix_aggregation:
            self.gateM_optimizer = GateMatrixs(self._precision, self._device_id)
            self.gateM_optimizer.build(self._pipeline)

    def _get_gate_matrix(self, gate: BasicGate):
        """ Return the gate's matrix in GPU. """
        if self._using_matrix_aggregation:
            return self.gateM_optimizer.get_target_matrix(gate)
        else:
            return cp.array(gate.matrix, dtype=self._precision)

    def initial_state_vector(self, all_zeros: bool = False):
        """ Initial qubits' vector states. """
        vector_size = 1 << int(self._qubits)
        self._vector = cp.zeros(vector_size, dtype=self._precision)
        if not all_zeros:
            self._vector.put(0, self._precision(1))

    def run(
        self,
        circuit: Circuit,
        state_vector: Union[np.ndarray, cp.ndarray] = None,
        use_previous: bool = False,
        gpu_out: bool = True
    ) -> np.ndarray:
        """ start simulator with given circuit

        Args:
            circuit (Circuit): The quantum circuits.
            state_vector (ndarray): The initial state vector.
            use_previous (bool, optional): Using the previous state vector. Defaults to False.
            record_runtime_measured (bool, optional): Record qubits' measured state during the simulation.

        Returns:
            [array]: The state vector.
        """
        self.initial_circuit(circuit)
        if state_vector is not None:
            assert 2 ** self._qubits == state_vector.size, \
                StateVectorUnmatchedError("The state vector should has the same qubits with the circuit.")
            self.vector = cp.array(state_vector, dtype=self._precision)
        elif not use_previous:
            self.initial_state_vector()

        idx = 0
        while idx < len(self._pipeline):
            gate = self._pipeline[idx]
            idx += 1
            if isinstance(gate, BasicGate):
                self.apply_gate(gate)
            elif isinstance(gate, Trigger):
                self.apply_trigger(gate, idx)
            else:
                raise TypeError("StateVectorSimulation.run.circuit", "[BasicGate, Trigger]". type(gate))

        if not gpu_out:
            return self.vector.get()
        else:
            return self.vector

    def apply_gate(self, gate: BasicGate):
        """ Depending on the given quantum gate, apply the target algorithm to calculate the state vector.

        Args:
            gate (Gate): the quantum gate in the circuit.
        """
        matrix_type = gate.matrix_type
        gate_type = gate.type
        default_parameters = (self._vector, self._qubits, self._sync)
        if (
            gate_type == GateType.id or
            gate_type == GateType.barrier or
            gate.is_identity()
        ):
            return

        # Deal with quantum gate with more than 3 qubits.
        if (
            gate_type in [GateType.unitary, GateType.qft, GateType.iqft, GateType.perm_fx] and
            gate.targets >= 3
        ):
            matrix = self._get_gate_matrix(gate)
            matrix = matrix.reshape(1 << (gate.controls + gate.targets), 1 << (gate.controls + gate.targets))
            self._vector = self._algorithm.matrix_dot_vector(
                self._vector,
                self._qubits,
                matrix,
                gate.cargs + gate.targs,
                self._sync
            )

            return

        # [H, Hy, SX, SY, SW, U2, U3, Rx, Ry] 2-bits [CH, ] 2-bits[Rzx, targets, unitary]
        if matrix_type == MatrixType.normal:
            self.apply_normal_matrix(gate)
        # [Rz, Phase], 2-bits [CRz, Rzz], 3-bits [CCRz]
        elif matrix_type in [MatrixType.diagonal, MatrixType.diag_diag]:
            self.apply_diagonal_matrix(gate)
        # [X] 2-bits [swap, iswap, iswapdg, sqiswap] 3-bits [CSWAP]
        elif matrix_type == MatrixType.swap:
            self.apply_swap_matrix(gate)
        # [Y] 2-bits [CX, CY] 3-bits: [CCX]
        elif matrix_type == MatrixType.reverse:
            self.apply_reverse_matrix(gate)
        # [S, sdg, Z, U1, T, tdg] # 2-bits [CZ, CU1]
        elif matrix_type == MatrixType.control:
            self.apply_control_matrix(gate)
        # [FSim]
        elif matrix_type == MatrixType.ctrl_normal:
            t_indexes = [self._qubits - 1 - targ for targ in gate.targs]
            matrix = self._get_gate_matrix(gate)
            self._algorithm.ctrl_normal_targs(
                t_indexes,
                matrix,
                *default_parameters
            )
        # [Rxx, Ryy]
        elif matrix_type == MatrixType.normal_normal:
            t_indexes = [self._qubits - 1 - targ for targ in gate.targs]
            matrix = self._get_gate_matrix(gate)
            self._algorithm.normal_normal_targs(
                t_indexes,
                matrix,
                *default_parameters
            )
        # [Rzx]
        elif matrix_type == MatrixType.diag_normal:
            t_indexes = [self._qubits - 1 - targ for targ in gate.targs]
            matrix = self._get_gate_matrix(gate)
            self._algorithm.diagonal_normal_targs(
                t_indexes,
                matrix,
                *default_parameters
            )
        # [Measure, Reset]
        elif gate_type in [GateType.measure, GateType.reset]:
            index = self._qubits - 1 - gate.targ
            prob = self.get_measured_prob(index).get()
            self.apply_specialgate(index, gate_type, prob)
        # [Perm]
        elif gate_type == GateType.perm:
            args = gate.cargs + gate.targs
            if len(args) == self._qubits:
                mapping = np.array(gate.pargs, dtype=np.int32)
            else:
                mapping = np.arange(self._qubits, dtype=np.int32)
                for idx, parg in enumerate(gate.pargs):
                    mapping[args[idx]] = args[parg]

            self._algorithm.VectorPermutation(
                self._vector,
                mapping,
                changeInput=True,
                gpu_out=False,
                sync=self._sync
            )
        # unsupported quantum gates
        else:
            raise GateTypeNotImplementError(f"Unsupported Gate Type and Matrix Type: {gate_type} {matrix_type}.")

    def apply_normal_matrix(self, gate: BasicGate):
        # Get gate's parameters
        args_num = gate.controls + gate.targets
        gate_args = gate.cargs + gate.targs
        matrix = self._get_gate_matrix(gate)
        default_parameters = (self._vector, self._qubits, self._sync)

        # Deal with 1-qubit normal gate e.g. H
        if args_num == 1:
            index = self._qubits - 1 - gate_args[0]
            self._algorithm.normal_targ(
                index,
                matrix,
                *default_parameters
            )
        elif args_num == 2:     # Deal with 2-qubits control normal gate e.g. CH
            if gate.controls == gate.targets:
                c_index = self._qubits - 1 - gate.carg
                t_index = self._qubits - 1 - gate.targ
                self._algorithm.normal_ctargs(
                    c_index,
                    t_index,
                    matrix,
                    *default_parameters
                )
            elif gate.targets == 2:     # Deal with 2-qubits unitary gate
                indexes = [self._qubits - 1 - index for index in gate_args]
                self._algorithm.normal_targs(
                    indexes,
                    matrix,
                    *default_parameters
                )
            else:
                raise GateQubitAssignedError("Quantum gate cannot only have control qubits.")

    def apply_diagonal_matrix(self, gate: BasicGate):
        # Get gate's parameters
        args_num = gate.controls + gate.targets
        gate_args = gate.cargs + gate.targs
        matrix = self._get_gate_matrix(gate)
        default_parameters = (self._vector, self._qubits, self._sync)

        # Deal with 1-qubit diagonal gate, e.g. Rz
        if args_num == 1:
            index = self._qubits - 1 - gate.targ
            self._algorithm.diagonal_targ(
                index,
                matrix,
                *default_parameters
            )
        elif args_num == 2:     # Deal with 2-qubit diagonal gate, e.g. CRz
            if gate.controls == gate.targets:
                c_index = self._qubits - 1 - gate.carg
                t_index = self._qubits - 1 - gate.targ
                self._algorithm.diagonal_ctargs(
                    c_index,
                    t_index,
                    matrix,
                    *default_parameters
                )
            elif gate.targets == 2:
                indexes = [self._qubits - 1 - index for index in gate_args]
                self._algorithm.diagonal_targs(
                    indexes,
                    matrix,
                    *default_parameters
                )
            else:
                raise GateQubitAssignedError("Quantum gate cannot only have control qubits.")
        else:   # [CCRz]
            assert gate.type == GateType.ccrz, \
                GateAlgorithmNotImplementError(f"State Vector Simulator cannot deal with {gate.type} currently.")
            c_indexes = [self._qubits - 1 - carg for carg in gate.cargs]
            t_index = self._qubits - 1 - gate.targ
            self._algorithm.diagonal_more(
                c_indexes,
                t_index,
                matrix,
                *default_parameters
            )

    def apply_swap_matrix(self, gate: BasicGate):
        # Get gate's parameters
        args_num = gate.controls + gate.targets
        gate_args = gate.cargs + gate.targs
        default_parameters = (self._vector, self._qubits, self._sync)

        if args_num == 1:       # Deal with X Gate
            index = self._qubits - 1 - gate.targ
            self._algorithm.swap_targ(
                index,
                *default_parameters
            )
        elif args_num == 2:     # Deal with Swap Gate
            if gate.targets != 2:
                raise GateAlgorithmNotImplementError(f"State Vector Simulator cannot deal with {gate.type} currently.")

            t_indexes = [self._qubits - 1 - targ for targ in gate_args]
            self._algorithm.swap_targs(
                t_indexes,
                self._get_gate_matrix(gate),
                *default_parameters
            )
        else:   # CSwap
            assert gate.type == GateType.cswap, \
                GateAlgorithmNotImplementError(f"State Vector Simulator cannot deal with {gate.type} currently.")
            t_indexes = [self._qubits - 1 - targ for targ in gate.targs]
            c_index = self._qubits - 1 - gate.carg
            self._algorithm.swap_tmore(
                t_indexes,
                c_index,
                *default_parameters
            )

    def apply_reverse_matrix(self, gate: BasicGate):
        # Get gate's parameters
        args_num = gate.controls + gate.targets
        gate_args = gate.cargs + gate.targs
        matrix = self._get_gate_matrix(gate)
        default_parameters = (self._vector, self._qubits, self._sync)

        if args_num == 1:   # Deal with 1-qubit reverse gate, e.g. Y
            index = self._qubits - 1 - gate_args[0]
            self._algorithm.reverse_targ(
                index,
                matrix,
                *default_parameters
            )
        elif args_num == 2:   # only consider 1 control qubit + 1 target qubit
            if gate.targets == 2:
                raise GateAlgorithmNotImplementError(f"State Vector Simulator cannot deal with {gate.type} currently.")

            c_index = self._qubits - 1 - gate_args[0]
            t_index = self._qubits - 1 - gate_args[1]
            self._algorithm.reverse_ctargs(
                c_index,
                t_index,
                matrix,
                *default_parameters
            )
        else:   # CCX
            assert gate.type == GateType.ccx, \
                GateAlgorithmNotImplementError(f"State Vector Simulator cannot deal with {gate.type} currently.")
            c_indexes = [self._qubits - 1 - carg for carg in gate.cargs]
            t_index = self._qubits - 1 - gate.targ
            self._algorithm.reverse_more(
                c_indexes,
                t_index,
                *default_parameters
            )

    def apply_control_matrix(self, gate: BasicGate):
        # Get gate's parameters
        args_num = gate.controls + gate.targets
        gate_args = gate.cargs + gate.targs
        default_parameters = (self._vector, self._qubits, self._sync)

        if args_num == 1:       # Deal with 1-qubit control gate, e.g. S
            index = self._qubits - 1 - gate_args[0]
            val = gate.matrix[1, 1]
            self._algorithm.control_targ(
                index,
                val,
                *default_parameters
            )
        elif args_num == 2:     # Deal with 2-qubit control gate, e.g. CZ
            if gate.targets == 2:
                raise GateAlgorithmNotImplementError(f"State Vector Simulator cannot deal with {gate.type} currently.")

            c_index = self._qubits - 1 - gate_args[0]
            t_index = self._qubits - 1 - gate_args[1]
            val = gate.matrix[3, 3]
            self._algorithm.control_ctargs(
                c_index,
                t_index,
                val,
                *default_parameters
            )
        else:
            raise GateAlgorithmNotImplementError(f"State Vector Simulator cannot deal with {gate.type} currently.")

    def apply_trigger(self, op: Trigger, current_idx: int) -> CompositeGate:
        """ Deal with the Operator <Trigger>.

        Args:
            op (Trigger): The operator Trigger
            current_idx (int): the index of Trigger in Circuit
        """
        for targ in op.targs:
            index = self._qubits - 1 - targ
            prob = self.get_measured_prob(index).get()
            _ = self.apply_specialgate(index, GateType.measure, prob)

        mapping_cgate = op.mapping(int(self._circuit[op.targs]))
        if isinstance(mapping_cgate, CompositeGate):
            # optimized composite gate's matrix
            if self._using_matrix_aggregation:
                self.gateM_optimizer.build(mapping_cgate.gates)

            # Check for checkpoint
            cp = mapping_cgate.checkpoint
            position = current_idx if cp is None else self._circuit.find_position(cp)
            self._pipeline = self._pipeline[:position] + mapping_cgate.gates + \
                self._pipeline[position:]

    def apply_multiply(self, value: Union[float, np.complex]):
        """ Deal with Operator <Multiply>

        Args:
            value (Union[float, complex]): The multiply value apply to state vector.
        """
        default_parameters = (self._vector, self._qubits, self._sync)
        if isinstance(value, float):
            float_multiply(value, *default_parameters)
        else:
            if self._precision == np.complex64:
                value = np.complex64(value)

            complex_multiply(value, *default_parameters)

    def apply_zeros(self):
        """ Set state vector to be zero. """
        self._vector = cp.zeros_like(self.vector)

    def get_measured_prob(self, index: int, all_measured: bool = False) -> cp.ndarray:
        """ Return the probability of measured qubit with given index to be 0

        Args:
            index (int): The given qubit index
            all_measured (bool): Calculate measured probability with all state vector,
                only using with Multi-Node Simulation.
        """
        return self._algorithm.measured_prob_calculate(
            index,
            self._vector,
            self._qubits,
            all_measured=all_measured,
            sync=self._sync
        )

    def apply_specialgate(self, index: int, type: GateType, prob: float = None):
        """ Apply Measure/Reset gate in to simulator

        Args:
            index (int): The given qubit index
            type (GateType): the gate type of special gate
            prob (float): The given probability of measured the target qubit into 1

        Returns:
            [float]: The target qubit's measured value or reset value, <0 or <1
        """
        if type == GateType.measure:
            result = int(self._algorithm.apply_measuregate(
                index,
                self._vector,
                self._qubits,
                prob,
                self._sync
            ))
            self._circuit.qubits[self._qubits - 1 - index].measured = result
        elif type == GateType.reset:
            result = self._algorithm.apply_resetgate(
                index,
                self._vector,
                self._qubits,
                prob,
                self._sync
            )
        else:
            raise ValueError("StateVectorSimulator.apply_specialgate", "[measure, reset]", type)

        return result

    def sample(self, shots: int = 1) -> list:
        """ Sample the measured result from current state vector, please initial Circuit first

        Args:
            shots (int): The sample times of current state vector.

        Returns:
            List[int]: The measured result list with length equal to 2 ** self.qubits
        """
        assert (self._circuit is not None), \
            SampleBeforeRunError("StateVectorSimulation sample without run any circuit.")
        original_sv = self._vector.copy()
        state_list = [0] * (1 << self._qubits)
        lastcall_per_qubit = self._circuit.get_lastcall_for_each_qubits()
        measured_idx = [
            i for i in range(self._qubits)
            if lastcall_per_qubit not in [GateType.reset, GateType.measure]
        ]

        for _ in range(shots):
            for m_id in measured_idx:
                index = self._qubits - 1 - m_id
                prob = self.get_measured_prob(index).get()
                _ = self.apply_specialgate(index, GateType.measure, prob)

            state_list[int(self._circuit.qubits)] += 1
            self._vector = original_sv.copy()

        return state_list
