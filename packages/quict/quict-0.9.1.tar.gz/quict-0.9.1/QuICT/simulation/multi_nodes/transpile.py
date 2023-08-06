import numpy as np

from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.core.operator import DataSwitch, DataSwitchType, DeviceTrigger, Multiply, SpecialGate


ALL_PENTY = 0.5
HALF_PENTY = 2
CARG_PENTY = 3
PROB_ADD = 1


class Transpile:
    """ Transpile the circuit by the number of devices.

    Args:
        ndev (int): The number of devices.
        cost_threshold (int, optional): The cost of exchanged splited qubits. Defaults to 3.
    """
    @property
    def ndev(self) -> int:
        """ Return the number of devices """
        return self._ndev

    @ndev.setter
    def ndev(self, ndev: int):
        self._ndev = ndev
        self._split_qb_num = int(np.log2(ndev))

    @property
    def cost_threshold(self) -> int:
        """ Return the cost of exchanged splited qubits. """
        return self._cost_threshold

    @cost_threshold.setter
    def cost_threshold(self, cost_threshold: int):
        self._cost_threshold = cost_threshold

    def __init__(self, ndev: int, cost_threshold: int = 3):
        self._ndev = ndev
        self._cost_threshold = cost_threshold
        self._split_qb_num = int(np.log2(ndev))
        assert 2 ** self._split_qb_num == self._ndev

    def _args_adjust(self, gate_args, outer_qubit_indexes: list, inner_qubit_indexes: list):
        """ Get the updated gate args """
        inner_arg, outer_arg = [], []
        for garg in gate_args:
            if garg in outer_qubit_indexes:
                outer_arg.append((outer_qubit_indexes.index(garg), garg))
            else:
                inner_arg.append(inner_qubit_indexes.index(garg))

        return inner_arg, outer_arg

    def _transpile(self, gates_by_depth: list, split_qubits: list, layer_intervals: list) -> Circuit:
        """ Generate the distributed circuit through the dynamic splited qubits.

        Args:
            gates_by_depth (list): The list of gates at same layers in circuit.
            split_qubits (list): The splited qubits' indexes for each layer intervals
            layer_intervals (list): The layer intervals, which have the same splited qubits

        Returns:
            Circuit: The distributed circuit.
        """
        inner_qubits = self._qubits - self._split_qb_num    # The qubits' number of the transpile circuit
        qubits_indexes = set(range(self._qubits))
        transpiled_circuit = Circuit(inner_qubits)
        start_point = 0
        for interval_idx, point in enumerate(layer_intervals):
            current_outer_qubits = split_qubits[interval_idx]   # The splited qubits' indexes in current interval
            if isinstance(current_outer_qubits, int):
                current_outer_qubits = [current_outer_qubits]

            # Currently inner qubits' indexes
            inner_qubit_indexes = list(qubits_indexes.difference(current_outer_qubits))
            for gates in gates_by_depth[start_point:point]:     # Deal with all gates in current layer interval
                for gate in gates:
                    if gate.type in [GateType.id, GateType.barrier]:
                        continue

                    gate_args = gate.cargs + gate.targs
                    inner_args, outer_arg = self._args_adjust(gate_args, current_outer_qubits, inner_qubit_indexes)
                    if len(outer_arg) == 0:
                        if gate.matrix_type == MatrixType.special:
                            SpecialGate(gate.type, inner_args) | transpiled_circuit
                        else:
                            gate = gate & inner_args
                            gate | transpiled_circuit

                        continue

                    # Deal with gate has qubits in splited qubits
                    if len(gate_args) == 1:
                        device_trigger = self._single_qubit_gate_transpile(gate, outer_arg[0])
                    elif len(gate_args) == 2:
                        device_trigger = self._double_qubits_gate_transpile(gate, inner_args, outer_arg)
                    else:
                        raise ValueError("Only supportted transpilt for gate less than 2 qubits.")

                    device_trigger | transpiled_circuit

            start_point = point
            # Deal with exchange inner qubits and outer qubits
            if interval_idx != len(layer_intervals) - 1 and split_qubits[interval_idx + 1] != current_outer_qubits[0]:
                updated_inner_args = inner_qubit_indexes.index(split_qubits[interval_idx + 1])
                self._split_qubit_exchange(1, inner_qubits - 1 - updated_inner_args) | transpiled_circuit
                perm_gate = self._permutation(current_outer_qubits[0], split_qubits[interval_idx + 1])
                perm_gate.build_gate() | transpiled_circuit

        return transpiled_circuit

    def _split_qubit_exchange(self, old_qubit_index: int, new_split_qubit: int) -> DeviceTrigger:
        """ Generate the DataSwitch about exchanged splited qubits for each device.

        Args:
            old_qubit_index (int): The index of splited qubit which has been replaced
            new_split_qubit (int): The index of new splited qubit.
        """
        dev_mapping = {}
        for index in range(self._ndev):
            splited_cgate = CompositeGate()
            dest = index ^ old_qubit_index
            _0_1 = int(index < dest)
            DataSwitch(dest, DataSwitchType.ctarg, {new_split_qubit: _0_1}) | splited_cgate

            dev_mapping[index] = splited_cgate

        return DeviceTrigger(dev_mapping)

    def _permutation(self, old, new) -> PermGate:
        """ Permutation State Vector after exchanged inner qubits and outer qubits """
        based_range = list(range(self._qubits))
        based_range.remove(old)
        based_range[based_range.index(new)] = old

        # re-order the based range by its indexes
        minimal_indexes = np.argsort(based_range)
        for idx, mini_idx in enumerate(minimal_indexes):
            based_range[mini_idx] = idx

        return Perm(self._qubits - self._split_qb_num, based_range)

    def _single_qubit_gate_transpile(
        self,
        gate: BasicGate,
        outer_qubits_indexes: tuple
    ) -> DeviceTrigger:
        """ Deal with single-qubits gate which in the outer qubit.

        Args:
            gate (BasicGate): The quantum gate.
            outer_qubits_indexes (tuple): The index
        """
        matrix_type = gate.matrix_type
        split_idx = 1 << (outer_qubits_indexes[0])

        dev_mapping = {}
        for index in range(self._ndev):
            _0_1 = index & split_idx
            destination = index ^ split_idx
            splited_cgate = CompositeGate()
            # Normal 1-qubit gates
            if matrix_type == MatrixType.normal:
                DataSwitch(destination, DataSwitchType.half) | splited_cgate
                gate | splited_cgate(0)
                DataSwitch(destination, DataSwitchType.half) | splited_cgate
            # diagonal 1-qubit gates
            elif matrix_type == MatrixType.diagonal:
                value = gate.matrix[_0_1, _0_1]
                Multiply(value) | splited_cgate
            # swap 1-qubit gates [x]
            elif matrix_type == MatrixType.swap:
                DataSwitch(destination, DataSwitchType.all) | splited_cgate
            # reverse 1-qubit gates
            elif matrix_type == MatrixType.reverse:
                value = gate.matrix[int(not _0_1), _0_1]
                Multiply(value) | splited_cgate
                DataSwitch(destination, DataSwitchType.all) | splited_cgate
            # Controlled 1-qubit gates [Z, U1, T, T_dagger, S, S_dagger]
            elif matrix_type == MatrixType.control:
                if _0_1:
                    Multiply(gate.matrix[1, 1]) | splited_cgate
            else:
                SpecialGate(gate.type, outer_qubits_indexes[1], split_idx) | splited_cgate

            dev_mapping[index] = splited_cgate

        return DeviceTrigger(dev_mapping)

    def _double_qubits_gate_transpile(
        self,
        gate: BasicGate,
        inner_args: list,
        outer_args: list
    ):
        """ Deal with double-qubits gate which in the outer qubit.

        Args:
            gate (BasicGate): The quantum gate
            inner_args (list): The gate's qubit indexes which in the inner qubits
            outer_args (list): The gate's qubit indexes which in the outer qubits

        Returns:
            _type_: _description_
        """
        t_qubits = self._qubits - self._split_qb_num
        gate_args, matrix_type = gate.cargs + gate.targs, gate.matrix_type
        double_exceed = len(outer_args) == 2
        if len(outer_args) == 2:
            outer_qubit_idx = [1 << idx for idx, _ in outer_args]
        else:
            intersect_qubit_idx = gate_args.index(outer_args[0][1])
            outer_qubit_idx = 1 << outer_args[0][0]
            inner_args = inner_args[0]

        dev_mapping = {}
        for index in range(self._ndev):
            splited_cgate = CompositeGate()
            # 2-qubits diagonal gate [1, 1, a, b]
            if matrix_type == MatrixType.diagonal:
                if double_exceed:   # both args in splited
                    if index & outer_qubit_idx[0]:
                        value = gate.matrix[3, 3] if index & outer_qubit_idx[1] else gate.matrix[2, 2]
                        Multiply(value) | splited_cgate
                elif intersect_qubit_idx == 0:  # carg in splited
                    if index & outer_qubit_idx:
                        Unitary(gate.target_matrix, MatrixType.diagonal) | splited_cgate(inner_args)
                else:
                    value = gate.matrix[3, 3] if index & outer_qubit_idx else gate.matrix[2, 2]
                    control_matrix = np.array([[1, 0], [0, value]], dtype=np.complex128)
                    Unitary(control_matrix, MatrixType.control) | splited_cgate(inner_args)
            # controlled 2-qubits gate [1, 1, 1, a]
            elif matrix_type == MatrixType.control:
                value = gate.matrix[3, 3]
                control_matrix = np.array([[1, 0], [0, value]], dtype=np.complex128)
                if double_exceed:
                    if (index & outer_qubit_idx[0]) and (index & outer_qubit_idx[1]):
                        Multiply(value) | splited_cgate
                else:
                    if index & outer_qubit_idx:
                        Unitary(control_matrix, MatrixType.control) | splited_cgate(inner_args)
            # diagonal 2-qubits gate [a, b, c, d]
            elif matrix_type == MatrixType.diag_diag:
                if double_exceed:
                    control_index = 2 if index & outer_qubit_idx[0] else 0
                    if index & outer_qubit_idx[1]:
                        control_index += 1

                    value = gate.matrix[control_index, control_index]
                    Multiply(value) | splited_cgate
                elif intersect_qubit_idx == 0:
                    matrix = gate.matrix[2:, 2:] if index & outer_qubit_idx else gate.matrix[:2, :2]
                    Unitary(matrix, MatrixType.diagonal) | splited_cgate(inner_args)
                else:
                    _1 = 1 if index & outer_qubit_idx else 0
                    matrix = np.identity(2, dtype=np.complex128)
                    matrix[[0, 1], [0, 1]] = gate.matrix[[_1, _1 + 2], [_1, _1 + 2]]
                    Unitary(matrix) | splited_cgate(inner_args)
            # control-reverse 2-qubits gate [1, 1, b, a]
            elif matrix_type == MatrixType.reverse:
                if double_exceed:
                    if index & outer_qubit_idx[0]:
                        value = gate.matrix[2, 3] if index & outer_qubit_idx[1] else gate.matrix[3, 2]
                        Multiply(value) | splited_cgate
                        DataSwitch(index ^ outer_qubit_idx[1], DataSwitchType.all) | splited_cgate
                elif intersect_qubit_idx == 0:
                    if index & outer_qubit_idx:
                        matrix = gate.matrix[2:, 2:]
                        Unitary(matrix, MatrixType.reverse) | splited_cgate(inner_args)
                else:
                    matrix = np.identity(2, dtype=np.complex128)
                    matrix[1, 1] = gate.matrix[2, 3] if index & outer_qubit_idx else gate.matrix[3, 2]
                    Unitary(matrix) | splited_cgate(inner_args)
                    DataSwitch(
                        index ^ outer_qubit_idx,
                        DataSwitchType.ctarg,
                        {t_qubits - 1 - inner_args: 1}
                    ) | splited_cgate
            # control-normal 2-qubits gate [CH, CU3]
            elif matrix_type == MatrixType.normal:
                if double_exceed:
                    if index & outer_qubit_idx[0]:
                        DataSwitch(index ^ outer_qubit_idx[1], DataSwitchType.half) | splited_cgate
                        Unitary(gate.matrix[2:, 2:]) | splited_cgate(0)
                        DataSwitch(index ^ outer_qubit_idx[1], DataSwitchType.half) | splited_cgate
                elif intersect_qubit_idx == 0:
                    if index & outer_qubit_idx:
                        Unitary(gate.matrix[2:, 2:]) | splited_cgate(inner_args)
                else:
                    dest = index ^ outer_qubit_idx
                    DataSwitch(
                        dest,
                        DataSwitchType.ctarg,
                        {t_qubits - 1 - inner_args: int(index < dest)}
                    ) | splited_cgate
                    if index & outer_qubit_idx:
                        Unitary(gate.matrix[2:, 2:]) | splited_cgate(inner_args)
                    DataSwitch(
                        dest,
                        DataSwitchType.ctarg,
                        {t_qubits - 1 - inner_args: int(index < dest)}
                    ) | splited_cgate
            # Swap gate [swap]
            elif matrix_type == MatrixType.swap:
                if double_exceed:
                    control_index = 2 if index & outer_qubit_idx[0] else 0
                    if index & outer_qubit_idx[1]:
                        control_index += 1

                    if control_index in [1, 2]:
                        destination = index ^ (sum(outer_qubit_idx))
                        DataSwitch(destination, DataSwitchType.all)
                else:
                    dest = index ^ outer_qubit_idx
                    DataSwitch(
                        dest,
                        DataSwitchType.ctarg,
                        {t_qubits - 1 - inner_args: int(index < dest)}
                    ) | splited_cgate
            # Diagonal * Matrix [Fsim]
            elif matrix_type == MatrixType.ctrl_normal:
                if double_exceed:
                    if index & outer_qubit_idx[0] and index & outer_qubit_idx[1]:
                        Multiply(gate.matrix[-1, -1]) | splited_cgate
                    elif index & outer_qubit_idx[0] or index & outer_qubit_idx[1]:
                        destination = index ^ (sum(outer_qubit_idx))
                        DataSwitch(destination, DataSwitchType.half) | splited_cgate
                        Unitary(gate.matrix[2:, 2:]) | splited_cgate(0)
                        DataSwitch(destination, DataSwitchType.half) | splited_cgate
                else:
                    dest = index ^ outer_qubit_idx
                    DataSwitch(
                        dest,
                        DataSwitchType.ctarg,
                        {t_qubits - 1 - inner_args: 0}
                    ) | splited_cgate
                    if index & outer_qubit_idx:
                        matrix = np.identity(2, dtype=np.complex128)
                        matrix[1, 1] = gate.matrix[3, 3]
                        Unitary(matrix, MatrixType.control) | splited_cgate(inner_args)
                    else:
                        Unitary(gate.matrix[1:3, 1:3]) | splited_cgate(inner_args)
                    DataSwitch(
                        dest,
                        DataSwitchType.ctarg,
                        {t_qubits - 1 - inner_args: 0}
                    ) | splited_cgate
            # Matrix * Matrix [Rxx, Ryy]
            elif matrix_type == MatrixType.normal_normal:
                outside_matrix = gate.matrix[[0, 0, 3, 3], [0, 3, 0, 3]].reshape(2, 2)
                inside_matrix = gate.matrix[1:3, 1:3]
                if double_exceed:
                    destination = index ^ (sum(outer_qubit_idx))
                    DataSwitch(destination, DataSwitchType.half) | splited_cgate
                    matrix = outside_matrix if abs(index - destination) < sum(outer_qubit_idx) else inside_matrix
                    Unitary(matrix) | splited_cgate(0)
                    DataSwitch(destination, DataSwitchType.half) | splited_cgate
                else:
                    dest = index ^ outer_qubit_idx
                    DataSwitch(
                        dest,
                        DataSwitchType.ctarg,
                        {t_qubits - 1 - inner_args: 1}
                    ) | splited_cgate

                    matrix = inside_matrix if index & outer_qubit_idx else outside_matrix
                    Unitary(matrix) | splited_cgate(inner_args)
                    DataSwitch(
                        dest,
                        DataSwitchType.ctarg,
                        {t_qubits - 1 - inner_args: 1}
                    ) | splited_cgate

            dev_mapping[index] = splited_cgate

        return DeviceTrigger(dev_mapping)

    def _gate_switch_cost_generator(self, gates_by_depth: list) -> np.ndarray:
        """ Depending on the gates' type, calculated the switched cost for each gates.

        Args:
            gates_by_depth (list): The list of gates at same layers in circuit.

        Returns:
            ndarray: The switch cost table contains the switched cost of each gates, shape is [# of qubits, # of layers]
        """
        data_switch_cost_matrix = np.zeros((self._qubits, self._depth), dtype=np.int32)
        for idx, depth_gates in enumerate(gates_by_depth):
            for gate in depth_gates:
                gate_matrix_type = gate.matrix_type
                gate_args = gate.cargs + gate.targs
                if gate_matrix_type == MatrixType.normal:
                    if gate.controls == 0:
                        data_switch_cost_matrix[gate_args, idx] += HALF_PENTY
                    else:
                        data_switch_cost_matrix[gate.targs, idx] += CARG_PENTY
                elif gate_matrix_type == MatrixType.reverse:
                    if gate.controls == 1:
                        data_switch_cost_matrix[gate.targs, idx] += CARG_PENTY
                elif gate_matrix_type == MatrixType.swap:
                    if gate.targets > 1:
                        data_switch_cost_matrix[gate_args[-1], idx] += CARG_PENTY
                elif gate_matrix_type in [MatrixType.ctrl_normal, MatrixType.normal_normal]:
                    data_switch_cost_matrix[gate_args, idx] += CARG_PENTY
                elif gate.type in [GateType.measure, GateType.reset]:
                    data_switch_cost_matrix[gate_args, idx] += PROB_ADD

        return data_switch_cost_matrix

    def _split_qubits(self, cost_matrix: np.ndarray):
        """ Depending on the switch cost table, selected the best way to minimize the cost of
        switch data in the distributed environment.

        Args:
            cost_matrix (np.ndarray): The switch cost table contains the switched cost of each gates,
                shape is [# of qubits, # of layers]
        """
        # divided the cost matrix by longest period with switched cost less than cost_threshold
        qubit_num, gate_depth = cost_matrix.shape
        period_interval = []                # record cost matrix's period interval
        sum_cost_by_longest_period = []     # record the sum of period interval of cost matrix
        period_idx = 0
        while period_idx < gate_depth - 1:
            longest_period_idx = 0
            for qubit in range(qubit_num):
                switch_cost = 0
                for idx in range(period_idx, gate_depth, 1):
                    switch_cost += cost_matrix[qubit, idx]
                    if switch_cost > self._cost_threshold:
                        break

                if idx > longest_period_idx:
                    longest_period_idx = idx

            switch_cost = np.sum(cost_matrix[:, period_idx:longest_period_idx], axis=1)
            sum_cost_by_longest_period.append(switch_cost)

            period_idx = longest_period_idx
            period_interval.append(period_idx)

        if gate_depth == 1:
            period_interval.append(gate_depth)
            sum_cost_by_longest_period.append(np.sum(cost_matrix, axis=1))
        else:
            period_interval[-1] += 1

        # find the smallest cost through the sum_cost_by_longest_period
        sum_cost_by_longest_period = np.array(sum_cost_by_longest_period, dtype=np.int32)
        period_qubit_selection = [int(np.argmin(sum_cost_by_longest_period[0]))]
        for sum_cost in sum_cost_by_longest_period[1:]:
            current_minarg = int(np.argmin(sum_cost))
            if current_minarg != period_qubit_selection[-1]:      # required switch split qubits
                # deal with add switch cost threshold
                if sum_cost[period_qubit_selection[-1]] < sum_cost[current_minarg] + self._cost_threshold:
                    current_minarg = period_qubit_selection[-1]
                # deal with switch back cost
                elif len(period_qubit_selection) >= 2 and period_qubit_selection[-2] == current_minarg:
                    start_idx = len(period_qubit_selection) - 2
                    previous_cost = np.sum(sum_cost_by_longest_period[start_idx:start_idx + 2, current_minarg])
                    current_cost = np.sum(
                        sum_cost_by_longest_period[start_idx:start_idx + 2, period_qubit_selection[-2:]]
                    ) + 2 * self._cost_threshold
                    if previous_cost <= current_cost:
                        period_qubit_selection[-1] = current_minarg

            period_qubit_selection.append(current_minarg)

        return period_interval, period_qubit_selection

    def run(self, circuit: Circuit):
        """ Depending on the device number in Transpile, generated the distributed circuit which
        have the necessary DataSwitch and DeviceTrigger operator.

        Args:
            circuit (Circuit): The quantum circuit

        Returns:
            Circuit, List[int]: The distributed circuit and split qubit indexes
        """
        # step 1: run GateDecomposition to avoid Unitary with large qubits and other special gates
        circuit.gate_decomposition()
        self._qubits = circuit.width()
        self._depth = circuit.depth()

        # step 2: order the circuit's gates by depth
        depth_gate = circuit.get_gates_order_by_depth()

        # step 3: decided split qubits by depth gates
        cost_matrix = self._gate_switch_cost_generator(depth_gate)
        split_qubit_intervals, selected_qubit_per_intervals = self._split_qubits(cost_matrix)

        # step 4: transpile circuit by split qubits [add op.data_swap, change gate]
        transpiled_circuits = self._transpile(depth_gate, selected_qubit_per_intervals, split_qubit_intervals)

        return transpiled_circuits, selected_qubit_per_intervals[-1]
