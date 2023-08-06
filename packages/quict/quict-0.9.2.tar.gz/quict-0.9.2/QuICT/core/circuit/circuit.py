#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2022/1/17 9:41
# @Author  : Han Yu, Kaiqi Li
# @File    : circuit.py
from typing import Union, List
import numpy as np

from QuICT.core.qubit import Qubit, Qureg
from QuICT.core.layout import Layout, SupremacyLayout
from QuICT.core.gate import BasicGate, H, Measure, build_random_gate, build_gate
from QuICT.core.utils import (
    GateType,
    CircuitBased,
    unique_id_generator
)
from QuICT.core.operator import (
    Trigger,
    CheckPoint,
    Operator,
    CheckPointChild,
    NoiseGate
)
from .dag_circuit import DAGCircuit

from QuICT.tools import Logger
from QuICT.tools.exception.core import *


logger = Logger("circuit")


class Circuit(CircuitBased):
    """ Implement a quantum circuit

    Circuit is the core part of the framework.

    Attributes:
        wires(Union[Qureg, int]): the number of qubits for the circuit.
        name(str): the name of the circuit.
        topology(list<tuple<int, int>>):
            The topology of the circuit. When the topology list is empty, it will be seemed as fully connected.
        fidelity(float): the fidelity of the circuit
        ancillae_qubits(list<int>): The indexes of ancilla qubits for current circuit.
    """
    @property
    def qubits(self) -> Qureg:
        return self._qubits

    @property
    def ancillae_qubits(self) -> List[int]:
        return self._ancillae_qubits

    @ancillae_qubits.setter
    def ancillae_qubits(self, ancillae_qubits: List[int]):
        for idx in ancillae_qubits:
            if idx < 0 or idx >= self.width():
                raise IndexExceedError(
                    "circuit.ancillae_qubits", [0, self.width()], idx
                )

            self._ancillae_qubits.append(idx)

    @property
    def topology(self) -> Layout:
        return self._topology

    @topology.setter
    def topology(self, topology: Layout):
        if topology is None:
            self._topology = None
            return

        if not isinstance(topology, Layout):
            raise TypeError(
                "Circuit.topology", "Layout", type(topology)
            )

        if topology.qubit_number != self.width():
            raise ValueError(
                "Circuit.topology.qubit_number", self.width(), topology.qubit_number
            )

        self._topology = topology

    @property
    def fidelity(self) -> float:
        return self._fidelity

    @fidelity.setter
    def fidelity(self, fidelity):
        if fidelity is None:
            self._fidelity = None
            return

        if not isinstance(fidelity, float):
            raise TypeError(
                "Circuit.fidelity", "float", type(fidelity)
            )

        if fidelity < 0 or fidelity > 1.0:
            raise ValueError(
                "Circuit.fidelity", "within [0, 1]", {fidelity}
            )

        self._fidelity = fidelity

    def __init__(
        self,
        wires,
        name: str = None,
        topology: Layout = None,
        fidelity: float = None,
        ancillae_qubits: List[int] = None
    ):
        if name is None:
            name = "circuit_" + unique_id_generator()

        super().__init__(name)
        self._ancillae_qubits = []
        self._topology = None
        self._fidelity = None
        self._checkpoints = []

        if isinstance(wires, Qureg):
            self._qubits = wires
        else:
            self._qubits = Qureg(wires)

        if ancillae_qubits is not None:
            self.ancillae_qubits = ancillae_qubits

        logger.debug(f"Initial Quantum Circuit {name} with {len(self._qubits)} qubits.")
        if topology is not None:
            self.topology = topology
            logger.debug(f"The Layout for Quantum Circuit is {self._topology}.")

        if fidelity is not None:
            self.fidelity = fidelity
            logger.debug(f"The Fidelity for Quantum Circuit is {self.fidelity}.")

    def __del__(self):
        """ release the memory """
        self.gates = None
        self._qubits = None
        self.topology = None
        self.fidelity = None
        logger.debug(f"Delete Quantum Circuit {self._name}.")

    def __or__(self, targets):
        """deal the operator '|'

        Use the syntax "circuit | circuit"
        to add the gate of circuit into the circuit/qureg/qubit

        Note that the order of qubits is that control bits first
        and target bits followed.

        Args:
            targets: the targets the gate acts on, it can have following form,
                1) Circuit
        Raise:
            TypeError: the type of targets is wrong
        """
        if not isinstance(targets, Circuit):
            raise TypeError(
                "Circuit.or", "Circuit", type(targets)
            )

        if not self.qubits == targets.qubits:
            diff_qubits = targets.qubits.diff(self.qubits)
            targets.update_qubit(diff_qubits, is_append=True)

        targets.extend(self.gates)

    ####################################################################
    ############         Circuit Qubits Operators           ############
    ####################################################################
    def __call__(self, indexes: object):
        """ get a smaller qureg from this circuit

        Args:
            indexes: the indexes passed in, it can have follow form:
                1) int
                2) list<int>
                3) Qubit
                4) Qureg
        Returns:
            Qureg: the qureg correspond to the indexes
        Exceptions:
            TypeError: the type of indexes is error.
        """
        if isinstance(indexes, int) or type(indexes) is list:
            indexes = self.qubits(indexes)

        if isinstance(indexes, Qubit):
            indexes = Qureg(indexes)

        if not isinstance(indexes, Qureg):
            raise TypeError(
                "Circuit.call", "int/list[int]/Qubit/Qureg", type(indexes)
            )

        self._pointer = indexes
        return self

    def __getitem__(self, item):
        """ to fit the slice operator, overloaded this function.

        get a smaller qureg/qubit from this circuit

        Args:
            item(int/slice): slice passed in.
        Return:
            Qubit/Qureg: the result or slice
        """
        return self.qubits[item]

    def add_qubit(self, qubits: Union[Qureg, int], is_ancillary_qubit: bool = False):
        """ add additional qubits in circuit.

        Args:
            qubits Union[Qureg, int]: The new qubits.
            is_ancillae_qubit (bool, optional): whether the given qubits is ancillae, default to False.
        """
        if isinstance(qubits, int):
            if qubits <= 0:
                raise IndexExceedError("Circuit.add_qubit", ">= 0", {qubits})

            qubits = Qureg(qubits)

        self._qubits = self._qubits + qubits
        if is_ancillary_qubit:
            self._ancillae_qubits += list(range(self.width() - len(qubits), self.width()))

        logger.debug(f"Quantum Circuit {self._name} add {len(qubits)} qubits.")

    def reset_qubits(self):
        """ Reset all qubits in current circuit. """
        self._qubits.reset_qubits()
        logger.debug(f"Reset qubits' measured result in the Quantum Circuit {self._name}.")

    def remapping(self, qureg: Qureg, mapping: list, circuit_update: bool = False):
        """ Realignment the qubits by the given mapping.

        Args:
            qureg (Qureg): The qubits which need to permutate.
            mapping (list): The order of permutation.
            circuit_update (bool, optional): whether rearrange the qubits in circuit. Defaults to False.
        """
        if not isinstance(qureg, Qureg):
            raise TypeError("Circuit.remapping", "Qureg", type(qureg))

        if len(qureg) != len(mapping):
            raise ValueError("Circuit.remapping.mapping", len(qureg), len(mapping))

        current_index = [self.qubits.index(qubit) for qubit in qureg]
        remapping_index = [current_index[m] for m in mapping]
        remapping_qureg = self.qubits[remapping_index]

        if circuit_update:
            self._qubits = remapping_qureg
            logger.debug(f"The qureg is permutation by the order {mapping}.")

        qureg[:] = remapping_qureg

    ####################################################################
    ############          Circuit Gates Operators           ############
    ####################################################################
    def _add_quantumgate_into_circuit(self, gate: BasicGate, insert_idx: int = -1):
        if insert_idx == -1:
            self.gates.append(gate)
            insert_idx = len(self.gates)
        else:
            self.gates.insert(insert_idx, gate)

        logger.debug(
            f"Add quantum gate {gate.type} with qubit indexes {gate.cargs + gate.targs} " +
            f"with index {insert_idx}."
        )

        # Update gate type dict
        if gate.type in self._gate_type.keys():
            self._gate_type[gate.type] += 1
        else:
            self._gate_type[gate.type] = 1

    def _update_gate_index(self):
        for index, gate in enumerate(self.gates):
            gate_type, gate_qb, gate_idx = gate.name.split('-')

            if int(gate_idx) != index:
                gate.name = '-'.join([gate_type, gate_qb, str(index)])

    def replace_gate(self, idx: int, gate: BasicGate):
        """ Replace the quantum gate in the target index, only accept BasicGate or NoiseGate.

        Args:
            idx (int): The index of replaced quantum gate in circuit.
            gate (BasicGate): The new quantum gate
        """
        assert idx >= 0 and idx < len(self._gates), IndexExceedError(
            "Circuit.replace_gate.idx", [0, len(self._gates)], idx
        )
        assert isinstance(gate, (BasicGate, NoiseGate)), TypeError(
            "Circuit.replace_gate.gate", "[BasicGate, NoiseGate]", type(gate)
        )

        logger.debug(f"The origin gate {self._gates[idx]} is replaced by {gate}")
        self._gates[idx] = gate

    def find_position(self, cp_child: CheckPointChild):
        position = -1
        if cp_child is None:
            return position

        for cp in self._checkpoints:
            if cp.uid == cp_child.uid:
                position = cp.position
                cp.position = cp_child.shift
            elif position != -1:
                # change the related position for backward checkpoint
                cp.position = cp_child.shift

        return position

    def get_DAG_circuit(self) -> DAGCircuit:
        """
        Translate a quantum circuit to a directed acyclic graph
        via quantum gates dependencies (The commutation of quantum gates).

        The nodes in the graph represented the quantum gates, and the edges means the two quantum
        gates is non-commutation. In other words, a directed edge between node A with quantum gate GA
        and node B with quantum gate GB, the quantum gate GA does not commute with GB.

        The nodes in the graph have the following attributes:
        'name', 'gate', 'cargs', 'targs', 'qargs', 'successors', 'predecessors'.

        **Reference:**

        [1] Iten, R., Moyard, R., Metger, T., Sutter, D. and Woerner, S., 2020.
        Exact and practical pattern matching for quantum circuit optimization.
        `arXiv:1909.05270 <https://arxiv.org/abs/1909.05270>`_

        Returns:
            DAGCircuit: A directed acyclic graph represent current quantum circuit
        """
        try:
            return DAGCircuit(self)
        except Exception as e:
            raise CircuitDAGError(e)

    ####################################################################
    ############          Circuit Build Operators           ############
    ####################################################################
    def extend(self, gates: list):
        """ Add list of gates to the circuit

        Args:
            gates(list<BasicGate>): the gate to be added to the circuit
        """
        position = -1
        if not isinstance(gates, list):
            position = self.find_position(gates.checkpoint)
            gates = gates.gates

        for gate in gates:
            if position == -1:
                self.append(gate, is_extend=True)
            else:
                self.append(gate, is_extend=True, insert_idx=position)
                position += 1

        self._pointer = None

    def append(self, op: Union[BasicGate, Operator], is_extend: bool = False, insert_idx: int = -1):
        qureg = self._pointer[:] if self._pointer else None
        if not is_extend:
            self._pointer = None

        if isinstance(op, BasicGate):
            self._add_gate(op, qureg, insert_idx)
        elif isinstance(op, Trigger):
            self._add_trigger(op, qureg)
        elif isinstance(op, CheckPoint):
            self._checkpoints.append(op)
            logger.debug(f"Add an CheckPoint which point to index {op.position}.")
        elif isinstance(op, Operator):
            self._gates.append(op)
            logger.debug(f"Add an operator {type(op)}.")
        else:
            raise TypeError(
                "Circuit.append.gate", "Trigger/BasicGate/NoiseGate", {type(op)}
            )

    def _add_gate(self, gate: BasicGate, qureg: Qureg, insert_idx: int):
        """ add a gate into some qureg

        Args:
            gate(BasicGate)
            qureg(Qureg)
        """
        args_num = gate.controls + gate.targets
        gate_ctargs = gate.cargs + gate.targs
        is_assigned = gate.assigned_qubits or gate_ctargs
        if not qureg:
            if not is_assigned:
                if gate.is_single():
                    self._add_gate_to_all_qubits(gate)
                    return
                elif args_num == self.width():
                    qureg = self.qubits
                else:
                    raise CircuitAppendError(f"{gate.type} need assign qubits to add into circuit.")
            else:
                qureg = self.qubits[gate_ctargs] if gate_ctargs else gate.assigned_qubits
        else:
            if len(qureg) < args_num:
                raise CircuitAppendError("Assigned qubits must larger or equal to gate size.")

            if len(qureg) > args_num and gate_ctargs:
                qureg = qureg[gate_ctargs]

        gate = gate.copy()
        gate.cargs = [self.qubits.index(qureg[idx]) for idx in range(gate.controls)]
        gate.targs = [self.qubits.index(qureg[idx]) for idx in range(gate.controls, gate.controls + gate.targets)]
        gate.assigned_qubits = qureg
        gate.update_name(qureg[0].id, len(self.gates))

        # Add gate into circuit
        self._add_quantumgate_into_circuit(gate, insert_idx)

    def _add_gate_to_all_qubits(self, gate):
        for idx in range(self.width()):
            new_gate = gate.copy()
            new_gate.targs = [idx]
            new_gate.assigned_qubits = self.qubits(idx)
            new_gate.update_name(self.qubits[idx].id, len(self.gates))

            self._add_quantumgate_into_circuit(new_gate)

    def _add_trigger(self, op: Trigger, qureg: Qureg):
        if qureg:
            if len(qureg) != op.targets:
                raise CircuitAppendError("Failure to add Trigger into Circuit, as un-matched qureg.")

            op.targs = [self.qubits.index(qureg[idx]) for idx in range(op.targets)]
        else:
            if not op.targs:
                raise CircuitAppendError("Trigger need assign qubits to add into circuit.")

            for targ in op.targs:
                if targ >= self.width():
                    raise CircuitAppendError("The trigger's target exceed the width of the circuit.")

        self.gates.append(op)
        logger.debug(f"Add an operator Trigger with qubit indexes {op.targs}.")

    def random_append(
        self,
        rand_size: int = 10,
        typelist: list = None,
        random_params: bool = False,
        probabilities: list = None
    ):
        """ add some random gate to the circuit, not include Unitary, Permutation and Permutation_FX Gate.

        Args:
            rand_size(int): the number of the gate added to the circuit
            typelist(list<GateType>): the type of gate, default contains
                Rx, Ry, Rz, Cx, Cy, Cz, CRz, Ch, Rxx, Ryy, Rzz and FSim
            random_params(bool): whether using random parameters for all quantum gates with parameters.
            probabilities: The probability of append for each gates
        """
        if typelist is None:
            typelist = [
                GateType.rx, GateType.ry, GateType.rz,
                GateType.cx, GateType.cy, GateType.crz,
                GateType.ch, GateType.cz, GateType.rxx,
                GateType.ryy, GateType.rzz, GateType.fsim
            ]

        unsupported_gate_type = [GateType.unitary, GateType.perm, GateType.perm_fx]
        if len(set(typelist) & set(unsupported_gate_type)) != 0:
            raise CircuitSpecialAppendError(
                f"{set(typelist) & set(unsupported_gate_type)} is not support in random append."
            )

        if probabilities is not None:
            if not np.isclose(sum(probabilities), 1, atol=1e-6):
                raise ValueError("Circuit.random_append.probabilities", "sum to 1", sum(probabilities))

            if len(probabilities) != len(typelist):
                raise CircuitSpecialAppendError(
                    "The length of probabilities should equal to the length of Gate Typelist."
                )

        logger.debug(f"Random append {rand_size} quantum gates from {typelist} with probability {probabilities}.")
        gate_prob = probabilities
        gate_indexes = list(range(len(typelist)))
        n_qubit = self.width()
        for _ in range(rand_size):
            rand_type = np.random.choice(gate_indexes, p=gate_prob)
            gate_type = typelist[rand_type]
            self.append(build_random_gate(gate_type, n_qubit, random_params))

    def supremacy_append(self, repeat: int = 1, pattern: str = "ABCDCDAB"):
        """
        Add a supremacy circuit to the circuit

        Args:
            repeat(int): the number of two-qubit gates' sequence
            pattern(str): indicate the two-qubit gates' sequence
        """
        qubits = len(self.qubits)
        supremacy_layout = SupremacyLayout(qubits)
        supremacy_typelist = [GateType.sx, GateType.sy, GateType.sw]
        logger.debug(f"Append Supremacy Circuit with mapping pattern sequence {pattern} and repeat {repeat} times.")

        self._add_gate_to_all_qubits(H)

        for i in range(repeat * len(pattern)):
            for q in range(qubits):
                gate_type = supremacy_typelist[np.random.randint(0, 3)]
                self.append(build_gate(gate_type, q))

            current_pattern = pattern[i % (len(pattern))]
            if current_pattern not in "ABCD":
                raise ValueError("Circuit.append_supremacy.pattern", "[A, B, C, D]", current_pattern)

            edges = supremacy_layout.get_edges_by_pattern(current_pattern)
            for e in edges:
                gate_params = [np.pi / 2, np.pi / 6]
                gate_args = [int(e[0]), int(e[1])]
                fgate = build_gate(GateType.fsim, gate_args, gate_params)

                self.append(fgate)

        self._add_gate_to_all_qubits(Measure)

    ####################################################################
    ############                Circuit Utils               ############
    ####################################################################
    def sub_circuit(
        self,
        start: int = 0,
        max_size: int = -1,
        qubit_limit: Union[int, List[int], Qureg] = [],
        gate_limit: List[GateType] = [],
        remove: bool = False
    ):
        """ get a sub circuit

        Args:
            start(int): the start gate's index, default 0
            max_size(int): max size of the sub circuit, default -1 without limit
            qubit_limit(int/list<int>/Qureg): the required qubits' indexes, if [], accept all qubits. default to be [].
            gate_limit(List[GateType]): list of required gate's type, if [], accept all quantum gate. default to be [].
            remove(bool): whether deleting the slice gates from origin circuit, default False
        Return:
            Circuit: the sub circuit
        """
        max_size_for_logger = max_size if max_size == -1 else len(self.gates) - start
        logger.debug(
            f"Get {max_size_for_logger} gates from gate index {start}" +
            f" with target qubits {qubit_limit} and gate limit {gate_limit}."
        )
        if qubit_limit:
            target_qubits = qubit_limit
            if isinstance(qubit_limit, Qureg):
                target_qubits = [self._qubits.index(qubit) for qubit in qubit_limit]
            elif isinstance(qubit_limit, int):
                target_qubits = [qubit_limit]

            for target in target_qubits:
                if target < 0 or target >= self.width():
                    raise IndexExceedError("Circuit.sub_circuit.qubit_limit", [0, self.width()], target)

            set_tqubits = set(target_qubits)

        sub_circuit = Circuit(self.width()) if not qubit_limit else Circuit(len(target_qubits))
        sub_gates = self._gates[:]
        for gate_index in range(start, len(self._gates)):
            gate = sub_gates[gate_index]
            _gate = gate.copy()
            gate_args = set(gate.cargs + gate.targs)
            is_append_in_subc = True
            if (qubit_limit and gate_args & set(set_tqubits) != gate_args):
                is_append_in_subc = False

            if (gate_limit and gate.type not in gate_limit):
                is_append_in_subc = False

            if is_append_in_subc:
                if qubit_limit:
                    _gate.targs = [target_qubits.index(targ) for targ in _gate.targs]
                    _gate.cargs = [target_qubits.index(carg) for carg in _gate.cargs]
                    _gate | sub_circuit
                else:
                    _gate | sub_circuit

                if remove:
                    self._gates.remove(gate)

            if sub_circuit.size() >= max_size and max_size != -1:
                break

        if remove:
            self._update_gate_index()
            logger.warn(f"Remove sub-circuit's gates from quantum circuit {self._name}.")

        return sub_circuit

    def draw(self, method: str = 'matp_auto', filename: str = None):
        """Draw the figure of circuit.

        Args:
            method(str): the method to draw the circuit
                matp_inline: Show the figure interactively but do not save it to file.
                matp_file: Save the figure to file but do not show it interactively.
                matp_auto: Automatically select inline or file mode according to matplotlib backend.
                matp_silent: Return the drawn figure without saving or showing.
                command : command
            filename(str): the output filename without file extensions, default to None.
                If filename is None, it will using matlibplot.show() except matlibplot.backend
                is agg, it will output jpg file named circuit's name.
            get_figure(bool): Whether to return the figure object of matplotlib.

        Returns:
            If method is 'matp_silent', a matplotlib Figure is returned. Note that that figure is created in matplotlib
            Object Oriented interface, which means it must be display with IPython.display.

        Examples:
            >>> from IPython.display import display
            >>> circ = Circuit(5)
            >>> circ.random_append()
            >>> silent_fig = circ.draw(method="matp_silent")
            >>> display(silent_fig)
        """
        from QuICT.tools.drawer import PhotoDrawer, TextDrawing
        import matplotlib

        if method.startswith('matp'):
            if filename is not None:
                if '.' not in filename:
                    filename += '.jpg'

            photo_drawer = PhotoDrawer()
            if method == 'matp_auto':
                save_file = matplotlib.get_backend() == 'agg'
                show_inline = matplotlib.get_backend() != 'agg'
            elif method == 'matp_file':
                save_file = True
                show_inline = False
            elif method == 'matp_inline':
                save_file = False
                show_inline = True
            elif method == 'matp_silent':
                save_file = False
                show_inline = False
            else:
                raise ValueError(
                    "Circuit.draw.matp_method", "[matp_auto, matp_file, matp_inline, matp_silent]", method
                )

            silent = (not show_inline) and (not save_file)
            photo_drawer.run(circuit=self, filename=filename, save_file=save_file)

            if show_inline:
                from IPython.display import display
                display(photo_drawer.figure)
            elif silent:
                return photo_drawer.figure

        elif method == 'command':
            text_drawer = TextDrawing([i for i in range(len(self.qubits))], self.gates)
            if filename is None:
                print(text_drawer.single_string())
                return
            elif '.' not in filename:
                filename += '.txt'

            text_drawer.dump(filename)
        else:
            raise ValueError(
                "Circuit.draw.method", "[matp_auto, matp_file, matp_inline, matp_silent, command]", method
            )
