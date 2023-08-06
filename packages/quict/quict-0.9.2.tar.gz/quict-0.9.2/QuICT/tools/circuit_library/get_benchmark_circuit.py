import random
import numpy as np

from QuICT.core import Circuit
from QuICT.core.gate import *


class BenchmarkCircuitBuilder:
    """
    A class fetch QuICT benchmark circuits.

     Args:
        width(int): number of qubits
        size(int): number of gates
        random_params (bool, optional): whether random parameter or use default parameter. Defaults to True.
    """
    @staticmethod
    def parallelized_circuit_build(width: int, size: int, random_params: bool = True):
        typelist = [GateType.rz, GateType.cx]
        prob = [0.8, 0.2]

        gate_indexes = list(range(2))
        qubits_indexes = list(range(width))
        shuffle_qindexes = qubits_indexes[:]
        random.shuffle(shuffle_qindexes)

        cir = Circuit(width)
        while cir.size() < size:
            rand_type = np.random.choice(gate_indexes, p=prob)
            gate_type = typelist[rand_type]
            gate = GATE_TYPE_TO_CLASS[gate_type]()

            if random_params and gate.params:
                gate.pargs = list(np.random.uniform(0, 2 * np.pi, gate.params))

            gsize = gate.controls + gate.targets
            if gsize > len(shuffle_qindexes):
                continue

            gate & shuffle_qindexes[:gsize] | cir

            if gsize == len(shuffle_qindexes):
                shuffle_qindexes = qubits_indexes[:]
                random.shuffle(shuffle_qindexes)
            else:
                shuffle_qindexes = shuffle_qindexes[gsize:]

        return cir

    @staticmethod
    def serialized_circuit_build(width: int, size: int, random_params: bool = True):
        cir = Circuit(width)
        qubit_indexes = list(range(width))
        qubit = random.choice(qubit_indexes)
        qubit_indexes.remove(qubit)

        while cir.size() < size:
            qubit_new = random.choice(qubit_indexes)
            qubits_list = [qubit, qubit_new]
            random.shuffle(qubits_list)
            CX & (qubits_list) | cir

        return cir

    @staticmethod
    def entangled_circuit_build(width: int, size: int, random_params: bool = True):
        def _pattern1():
            cgate = CompositeGate()
            qubit_indexes = list(range(width))
            qubit_extra = []
            for _ in range(width):
                if len(qubit_indexes) > 1:
                    qubit_index = random.sample(qubit_indexes, 2)
                    CX & (qubit_index) | cgate
                    qubit_extra.append(qubit_index)
                    qubit_indexes = list(set(qubit_indexes) - set(qubit_index))
                elif len(qubit_indexes) == 1:
                    for i in range(len(qubit_extra)):
                        q_collect = random.choice(qubit_extra[i])
                        CX & ([qubit_indexes[0], q_collect]) | cgate
                    break
                else:
                    break

            return cgate

        def _pattern2():
            cgate = CompositeGate()
            qubit_indexes = list(range(width))
            result = [qubit_indexes[i:i + 2] for i in range(0, len(qubit_indexes), 2)]
            for i in range(len(result)):
                if len(result[i]) == 2:
                    CX & (result[i]) | cgate

            result = [qubit_indexes[i + 1:i + 3] for i in range(0, len(qubit_indexes), 2)]
            for i in range(len(result)):
                if len(result[i]) == 2:
                    CX & (result[i]) | cgate
                else:
                    break

            return cgate

        cir = Circuit(width)
        while cir.size() < size:
            cgate = random.choice([_pattern1(), _pattern2()])
            cgate | cir

        return cir

    @staticmethod
    def mediate_measure_circuit_build(width: int, size: int, random_params: bool = True):
        typelist = [GateType.rz, GateType.cx]
        prob = [0.8, 0.2]

        def flat_build():
            cgate = CompositeGate()
            qubits_indexes = list(range(width))
            random.shuffle(qubits_indexes)
            while len(qubits_indexes) > 0:
                if len(qubits_indexes) == 1:
                    Rz & qubits_indexes.pop() | cgate
                else:
                    gate_type = np.random.choice(typelist, p=prob)
                    gate = GATE_TYPE_TO_CLASS[gate_type]()
                    gate_size = gate.controls + gate.targets
                    gate & qubits_indexes[:gate_size] | cgate
                    qubits_indexes = qubits_indexes[gate_size:]

            return cgate

        cir = Circuit(width)
        flat_build() | cir
        cir.random_append(size - 2 * width, typelist, random_params, prob)
        flat_build() | cir

        idxes = random.sample(list(range(width, size - width)), k=width)
        for i in range(width):
            mgate = Measure & i
            cir.replace_gate(idxes[i], mgate)

        return cir
