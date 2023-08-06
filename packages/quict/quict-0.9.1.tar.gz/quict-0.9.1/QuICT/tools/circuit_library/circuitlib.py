import os
import shutil
from typing import Union, List

from QuICT.core import Circuit
from QuICT.core.gate import GateType
from QuICT.lib.qasm.exceptions import QasmError
from QuICT.tools import Logger
from QuICT.tools.interface import OPENQASMInterface
from .circuit_lib_sql import CircuitLibDB
from .get_benchmark_circuit import BenchmarkCircuitBuilder


logger = Logger("QuICT_Circuit_Library")


class CircuitLib:
    """
    A class handling QuICT circuit library.

    Args:
        output_type (str, optional): one of [circuit, qasm, file]. Defaults to "circuit".
        output_path (str, optional): The path to store qasm file if output type is file.
            Defaults to the current working path.
    """

    __DEFAULT_TYPE = ["template", "random", "algorithm", "benchmark", "instructionset"]
    __DEFAULT_CLASSIFY = {
        "random": [
            "aspen-4", "ourense", "rochester", "sycamore", "tokyo",
            "ctrl_unitary", "diag", "single_bit", "ctrl_diag",
            "google", "ibmq", "ionq", "ustc", "nam", "origin"
        ],
        "algorithm": ["adder", "clifford", "cnf", "grover", "maxcut", "qft", "qnn", "quantum_walk", "vqe"],
        "benchmark": ["highly_entangled", "highly_parallelized", "highly_serialized", "mediate_measure"],
    }
    __DEFAULT_GATESET_for_RANDOM = {
        "google": [[GateType.fsim], [GateType.sx, GateType.sy, GateType.sw, GateType.rx, GateType.ry]],
        "ibmq": [[GateType.cx], [GateType.rz, GateType.sx, GateType.x]],
        "ionq": [[GateType.rxx], [GateType.rx, GateType.ry, GateType.rz]],
        "ustc": [[GateType.cx], [GateType.rx, GateType.ry, GateType.rz, GateType.h, GateType.x]],
        "nam": [[GateType.cx], [GateType.h, GateType.rz]],
        "origin": [[GateType.cx], [GateType.u3]],
        "ctrl_diag": [[GateType.crz, GateType.cu1, GateType.cz], []],
        "ctrl_unitary": [[GateType.cx, GateType.cy, GateType.ch, GateType.cu3], []],
        "diag": [[], [
            GateType.t, GateType.rz, GateType.z, GateType.sdg, GateType.tdg, GateType.u1, GateType.s, GateType.id
        ]],
        "single_bit": [[], [
            GateType.x, GateType.y, GateType.z, GateType.u1, GateType.u2, GateType.u3, GateType.tdg,
            GateType.sdg, GateType.h, GateType.s, GateType.t, GateType.rx, GateType.ry, GateType.rz
        ]],
        "unitary": [[GateType.swap], [GateType.y, GateType.rx, GateType.ry, GateType.u2, GateType.u3]]
    }
    __LIB_PATH = os.path.join(
        os.path.dirname(__file__),
        '../../lib/circuitlib'
    )

    def __init__(
        self,
        output_type: str = "circuit",
        output_path: str = '.'
    ):
        self._output_type = output_type
        self._output_path = output_path
        logger.debug(f"Initial Circuit Library with output {self._output_type}.")

        self._db = CircuitLibDB()
        if output_type == "file":
            if not os.path.isdir(output_path):
                os.makedirs(output_path)

    @property
    def size(self) -> int:
        return self._db.size()

    def _get_circuit_from_qasm(self, file_path: str) -> Circuit:
        """ Load Circuit from a qasm file. """
        qasm = OPENQASMInterface.load_file(file_path)
        if not qasm.valid_circuit:
            logger.warn("Failure to load circuit from qasm.")
            raise QasmError("Missing input file")

        split_path = file_path.split('/')
        cir_name, cir_classify, cir_type  = split_path[-1:-4:-1]
        cir_name = os.path.splitext(cir_name)[0]
        qasm.circuit.name = "+".join([cir_type, cir_classify, cir_name])
        return qasm.circuit

    def _get_string_from_qasm(self, file_path: str) -> str:
        """ Return qasm string from qasm file. """
        return open(file_path, 'r').read()

    def _copy_qasm_file(self, file_path: str):
        """ Copy target qasm file to the given output path. """
        shutil.copy(file_path, self._output_path)

    def _get_all(self, folder: str, files: list) -> Union[List, None]:
        """ Load all qasm files in the list of files.

        Args:
            folder (str): The path of the qasm folder
            files (list): the list of file names

        Returns:
            List[(Circuit|string)]: _description_
        """
        circuit_all = []
        for file in files:
            file_path = os.path.join(folder, file[0])
            if self._output_type == "circuit":
                circuit_all.append(self._get_circuit_from_qasm(file_path))
            elif self._output_type == "qasm":
                circuit_all.append(self._get_string_from_qasm(file_path))
            else:
                self._copy_qasm_file(file_path)

        return circuit_all

    def _get_circuit_from_benchmark(self, classify, width, size):
        if classify == "highly_entangled":
            circuit = BenchmarkCircuitBuilder.entangled_circuit_build(width, size)
        elif classify == "highly_parallelized":
            circuit = BenchmarkCircuitBuilder.parallelized_circuit_build(width, size)
        elif classify == "highly_serialized":
            circuit = BenchmarkCircuitBuilder.serialized_circuit_build(width, size)
        else:
            circuit = BenchmarkCircuitBuilder.mediate_measure_circuit_build(width, size)

        return circuit

    def _get_all_from_generator(
        self,
        type: str,
        classify: str,
        gateset: list,
        prob: list,
        qubits_interval: Union[list, int],
        max_size: int = None,
        max_depth: int = None
    ):
        if isinstance(qubits_interval, int):
            qubits_interval = list(range(2, qubits_interval + 1))

        circuit_list = []
        size_interval = [3, 5, 10, 20]
        for width in qubits_interval:
            for size in size_interval:
                if max_size is not None and size * width > max_size:
                    continue

                if type == "random":
                    circuit = Circuit(width)
                    circuit.random_append(size * width, gateset, True, prob)
                    depth = circuit.depth()
                else:
                    circuit = self._get_circuit_from_benchmark(classify, width, size * width)
                    depth = circuit.depth()

                if max_depth is None or depth <= max_depth:
                    circuit.name = "+".join([type, classify, f"w{width}_s{size * width}_d{depth}"])
                    circuit_list.append(circuit)

        if self._output_type == "circuit":
            return circuit_list
        elif self._output_type == "qasm":
            return [circuit.qasm() for circuit in circuit_list]
        else:
            for circuit in circuit_list:
                output_file = os.path.join(self._output_path, f"{circuit.name}.qasm")
                circuit.qasm(output_file)

    def get_template_circuit(
        self,
        qubits_interval: Union[list, int] = None,
        max_size: int = None,
        max_depth: int = None,
        typelist: list = None
    ) -> Union[List[Union[Circuit, str]], None]:
        """
        Get template circuits in QuICT circuit library. A template will be loaded if
        it satisfies the following restrictions:
            1. the circuit in the given classify.
            2. its number of qubits <= `max_width`,
            3. its number of gates <= `max_size`,
            4. its depth <= `max_depth`.
            5. its gates' types are in `typelist`

        Restrictions will be ignored if not specified.

        Args:
            qubits_interval (Union[List, int], optional): The interval of qubit number, if it givens an interger,
                it equals to the interval of [2, qubits_interval]. The qubits' number range is [1, 5].
            max_size(int): max number of gates, range is [2, 6].
            max_depth(int): max depth of circuit, range is [2, 9].
            typelist(Iterable[GateType]): list of allowed gate types

        Returns:
            (List[Circuit | String] | None): Return the list of output circuit order by output_type.
        """
        path = os.path.join(self.__LIB_PATH, "template")
        files = self._db.circuit_filter("template", "template", qubits_interval, max_size, max_depth)

        ret = self._get_all(path, files)

        if typelist is not None:
            filtered = []
            for each in ret:
                if all([g.type in typelist for g in each.gates]):
                    filtered.append(each)
            ret = filtered

        return ret

    def get_random_circuit(
        self,
        classify: str,
        qubits_interval: Union[list, int],
        max_size: int = None,
        max_depth: int = None
    ) -> Union[List[Union[Circuit, str]], None]:
        """Get random circuits in QuICT circuit library. A template will be loaded if
        it satisfies the following restrictions:
            1. the circuit in the given classify.
            2. its number of qubits <= `max_width`,
            3. its number of gates <= `max_size`,
            4. its depth <= `max_depth`.

        Restrictions will be ignored if not specified.

        Args:
            classify (str): one of ["aspen-4", "ourense", "rochester", "sycamore", "tokyo", \
                "ctrl_unitary", "diag", "single_bits", "ctrl_diag", "google", "ibmq", "ionq", "ustc", "nam", "origin"]
            qubits_interval (Union[List, int], optional): The interval of qubit number, if it givens an interger,
                it equals to the interval of [2, qubits_interval].
            max_size(int): max number of gates.
            max_depth(int): max depth of circuit.

        Returns:
            (List[Circuit | String] | None): Return the list of output circuit order by output_type.
        """
        assert classify in self.__DEFAULT_CLASSIFY['random'], "error classify."
        if classify in self.__DEFAULT_CLASSIFY['random'][:5]:
            path = os.path.join(self.__LIB_PATH, 'random', classify)
            files = self._db.circuit_filter("random", classify, qubits_interval, max_size, max_depth)

            return self._get_all(path, files)
        else:   # Generate random circuit with given limitation
            gate_2q, gate_1q = self.__DEFAULT_GATESET_for_RANDOM[classify]
            if len(gate_2q) > 0 and len(gate_1q) > 0:
                prob = [0.2 / len(gate_2q)] * len(gate_2q) + [0.8 / len(gate_1q)] * len(gate_1q)
            else:
                prob = None

            return self._get_all_from_generator(
                "random", classify, gate_2q + gate_1q, prob, qubits_interval, max_size, max_depth
            )

    def get_algorithm_circuit(
        self,
        classify: str,
        qubits_interval: Union[list, slice] = None,
        max_size: int = None,
        max_depth: int = None
    ) -> Union[List[Union[Circuit, str]], None]:
        """ Get algorithm circuits in QuICT circuit library. A template will be loaded if
        it satisfies the following restrictions:
            1. the circuit in the given classify.
            2. its number of qubits <= `max_width`,
            3. its number of gates <= `max_size`,
            4. its depth <= `max_depth`.

        Restrictions will be ignored if not specified.

        Args:
            classify (str): one of ["adder", "clifford", "grover", "qft", "vqe"]
            qubits_interval (Union[List, int], optional): The interval of qubit number, if it givens an interger,
                it equals to the interval of [2, qubits_interval].
            max_size(int): max number of gates.
            max_depth(int): max depth of circuit.

        Returns:
            (List[Circuit | String] | None): Return the list of output circuit order by output_type.
        """
        assert classify in self.__DEFAULT_CLASSIFY['algorithm'], "error classify."
        path = os.path.join(self.__LIB_PATH, 'algorithm', classify)
        files = self._db.circuit_filter("algorithm", classify, qubits_interval, max_size, max_depth)

        return self._get_all(path, files)

    def get_benchmark_circuit(
        self,
        classify: str,
        qubits_interval: Union[list, int] = None,
        max_size: int = None,
        max_depth: int = None
    ) -> Union[List[Union[Circuit, str]], None]:
        """ Get experiment circuits in QuICT circuit library. A template will be loaded if
        it satisfies the following restrictions:
            1. the circuit in the given classify.
            2. its number of qubits <= `max_width`,
            3. its number of gates <= `max_size`,
            4. its depth <= `max_depth`.

        Restrictions will be ignored if not specified.

        Args:
            classify (str): one of ["highly_entangled", "highly_parallelized", "highly_serialized", "mediate_measure"]
            qubits_interval (Union[List, int], optional): The interval of qubit number, if it givens an interger,
                it equals to the interval of [2, qubits_interval].
            max_size(int): max number of gates.
            max_depth(int): max depth of circuit.

        Returns:
            (List[Circuit | String] | None): Return the list of output circuit order by output_type.
        """
        assert classify in self.__DEFAULT_CLASSIFY['benchmark'], "error experiment classify."
        # Generate benchmark circuit with given limitation
        return self._get_all_from_generator("benchmark", classify, [], [], qubits_interval, max_size, max_depth)

    def get_circuit(
        self,
        type: str,
        classify: str = "template",
        qubits_interval: Union[list, int] = None,
        max_size: int = None,
        max_depth: int = None
    ) -> Union[List[Union[Circuit, str]], None]:
        """Get the target circuits from QuICT Circuit Library.

        Args:
            type (str): The type of circuits, one of [template, random, algorithm, benchmark].
            classify (str, optional): The classify of selected circuit's type.
                For template circuit's type, classify must be template;
                For random circuit's type, classify is one of
                    [aspen-4, ourense, rochester, sycamore, tokyo, ctrl_unitary, diag, single_bit, ctrl_diag,
                     google, ibmq, ionq, ustc, nam, origin]
                For algorithm circuit's type, classify is one of
                    [adder, clifford, grover, qft, vqe, cnf, maxcut]
                For benchmark circuit's type, classify is one of
                    [highly_entangled, highly_parallelized, highly_serialized, mediate_measure]

            qubits_interval (Union[List, int], optional): The interval of qubit number, if it givens an interger,
                it equals to the interval of [1, qubits_interval].
            max_size (int, optional): upper bound of circuit size. If None, no limitation on size, default to None.
            max_depth (int, optional): upper bound of circuit depth. If None, no limitation on depth, default to None.

            WARNING: qubits_interval need to be assigned for getting random circuit and benchmark circuit.

        Returns:
            (List[Circuit | String] | None): Return the list of output circuit order by output_type.
        """
        if type not in self.__DEFAULT_TYPE:
            raise KeyError("error_type")

        if type != "template" and classify not in self.__DEFAULT_CLASSIFY[type]:
            raise KeyError("error matched")

        if type == "template":
            return self.get_template_circuit(qubits_interval, max_size, max_depth)
        elif type == "random":
            return self.get_random_circuit(classify, qubits_interval, max_size, max_depth)
        elif type == "algorithm":
            return self.get_algorithm_circuit(classify, qubits_interval, max_size, max_depth)
        else:
            return self.get_benchmark_circuit(classify, qubits_interval, max_size, max_depth)
