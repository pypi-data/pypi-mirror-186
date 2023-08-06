# qcompute package
from QCompute import *
from QCompute.QPlatform.QOperation import FixedGate
# qiskit package
from qiskit import IBMQ
from qiskit import QuantumCircuit
from qiskit import transpile

from QuICT.core import Circuit
from QuICT.core.gate import *
from QuICT.simulation.remote import RemoteSimulator


class QuantumLeafSimulator(RemoteSimulator):
    """ The QCompute simulator, used to connect the remote simulator by QCompute.

    Args:
        token ([str]): The token to connect the QCompute simulator.
        backend ([str]): The backend for the remote simulator.
        shots ([int]): The running times; must be a positive integer.
    """

    __BACKEND = [   # simulators
        'cloud_aer_at_bd',
        'cloud_baidu_sim2_earth',
        'cloud_baidu_sim2_heaven',
        'cloud_baidu_sim2_lake',
        'cloud_baidu_sim2_thunder',
        'cloud_baidu_sim2_water',
        'cloud_baidu_sim2_wind',
        'cloud_iopcas'  # QPU
    ]

    __GATES = [
        FixedGate.ID,
        FixedGate.X,
        FixedGate.Y,
        FixedGate.Z,
        FixedGate.H,
        FixedGate.S,
        FixedGate.SDG,
        FixedGate.T,
        FixedGate.TDG,
        FixedGate.CX,
        FixedGate.CY,
        FixedGate.CZ,
        FixedGate.CH,
        FixedGate.SWAP,
        FixedGate.CCX,
        FixedGate.CSWAP
    ]

    def __init__(self, token: str, backend: str = 'cloud_aer_at_bd', shots: int = 1):
        RemoteSimulator.__init__(self, backend, shots)
        if backend not in QuantumLeafSimulator.__BACKEND:
            raise ValueError(
                f"Unsupportted backend in QuantumLeaf Simulator. Please use one of {self.__BACKEND}."
            )

        # Create qcompute backend
        Define.hubToken = token
        self._env = QEnv()

    def _initial_circuit(self, circuit: Circuit, use_previous: bool = False):
        """ Initial QCompute's quantum circuit from QuICT circuit.

        Args:
            circuit ([Circuit]): The QuICT circuit.
            use_previous ([bool]): Using previous vector state or not, default to False.

        Raises:
            ValueError: Unsupportted quantum gate

        Returns:
            [object]: The QCompute simulator.
        """
        if use_previous:
            qubits = self._env.Q
        else:
            qubits = self._env.Q.createList(circuit.width())

        gates = circuit.gates
        for gate in gates:
            if isinstance(gate, IDGate):
                targ = gate.targ
                FixedGate.ID(qubits[targ])
            elif isinstance(gate, XGate):
                targ = gate.targ
                FixedGate.X(qubits[targ])
            elif isinstance(gate, YGate):
                targ = gate.targ
                FixedGate.Y(qubits[targ])
            elif isinstance(gate, ZGate):
                targ = gate.targ
                FixedGate.Z(qubits[targ])
            elif isinstance(gate, HGate):
                targ = gate.targ
                FixedGate.H(qubits[targ])
            elif isinstance(gate, SGate):
                targ = gate.targ
                FixedGate.S(qubits[targ])
            elif isinstance(gate, SDaggerGate):
                targ = gate.targ
                FixedGate.SDG(qubits[targ])
            elif isinstance(gate, TGate):
                targ = gate.targ
                FixedGate.T(qubits[targ])
            elif isinstance(gate, TDaggerGate):
                targ = gate.targ
                FixedGate.TDG(qubits[targ])
            elif isinstance(gate, CXGate):
                carg = gate.carg
                targ = gate.targ
                FixedGate.CX(qubits[carg], qubits[targ])
            elif isinstance(gate, CYGate):
                carg = gate.carg
                targ = gate.targ
                FixedGate.CY(qubits[carg], qubits[targ])
            elif isinstance(gate, CZGate):
                carg = gate.carg
                targ = gate.targ
                FixedGate.CZ(qubits[carg], qubits[targ])
            elif isinstance(gate, CHGate):
                carg = gate.carg
                targ = gate.targ
                FixedGate.CH(qubits[carg], qubits[targ])
            elif isinstance(gate, SwapGate):
                targs = gate.targs
                FixedGate.SWAP(qubits[targs[0]], qubits[targs[1]])
            elif isinstance(gate, CCXGate):
                cargs = gate.cargs
                targ = gate.targ
                FixedGate.CCX(qubits[cargs[0]], qubits[cargs[1]], qubits[targ])
            elif isinstance(gate, CSwapGate):
                carg = gate.carg
                targs = gate.targs
                FixedGate.CSWAP(qubits[carg], qubits[targs[0]], qubits[targs[1]])
            elif isinstance(gate, MeasureGate):
                targ = gate.targ
                MeasureZ([qubits[targ]], [targ])
            else:
                raise ValueError("Unsupportted quantum gate in QuantumLeaf Simulator.")

        return self._env

    def run(self, circuit, use_previous):
        """ start simulator with given circuit

        Args:
            circuit (Circuit): The quantum circuits.
            use_previous (bool, optional): Using the previous state vector. Defaults to False.

        return:
            [data]: The experience result.
        """
        self._env.backend(self._backend)
        env = self._initial_circuit(circuit, use_previous)
        result = env.commit(self._shots)

        return result

    def get_gates(self):
        """ The supportted quantum gates in QCompute.

        Returns:
            [dict]: quantum gates with matrix.
        """
        gates = {}
        for gate in QuantumLeafSimulator.__GATES:
            gates[gate.name] = gate.getMatrix()

        return gates


class QiskitSimulator(RemoteSimulator):
    """ The Qiskit simulator, used to connect the remote simulator by Qiskit.

    Args:
        token ([str]): The token to connect the Qiskit simulator.
        backend ([str]): The backend for the remote simulator.
        shots ([int]): The running times; must be a positive integer.
    """

    __BACKEND = [
        'ibmq_qasm_simulator',
        'ibmq_kolkata',
        'ibmq_mumbai',
        'ibmq_dublin',
        'ibmq_hanoi',
        'ibmq_cairo',
        'ibmq_manhattan',
        'ibmq_brooklyn',
        'ibmq_toronto',
        'ibmq_sydney',
        'ibmq_guadalupe',
        'ibmq_casablanca',
        'ibmq_lagos',
        'ibmq_nairobi',
        'ibmq_santiago',
        'ibmq_manila',
        'ibmq_bogota',
        'ibmq_jakarta',
        'ibmq_quito',
        'ibmq_belem',
        'ibmq_lima',
        'ibmq_armonk',
    ]

    def __init__(self, token, backend: str = 'ibmq_qasm_simulator', shots: int = 1):
        RemoteSimulator.__init__(self, backend, shots)
        if backend not in QiskitSimulator.__BACKEND:
            raise ValueError(
                f"Unsupportted backend in Qiskit Simulator. Please use one of {self.__BACKEND}."
            )

        # create qiskit backend
        self._provider = IBMQ.enable_account(token)
        self._backend = self._provider.get_backend(backend)

    def _initial_circuit(self, circuit, use_previous: bool = False):
        """ Initial Qiskit's quantum circuit from QuICT circuit.

        Args:
            circuit ([Circuit]): The QuICT circuit.
            use_previous ([bool]): Using previous vector state or not, default to False.

        Returns:
            [object]: The Qiskit circuit.
        """
        qasm_str = circuit.qasm()
        translated_circuit = QuantumCircuit.from_qasm_str(qasm_str)
        compiled_circuit = transpile(translated_circuit, self._backend)

        return compiled_circuit

    def run(self, circuit, use_previous):
        """ start simulator with given circuit

        Args:
            circuit (Circuit): The quantum circuits.
            use_previous (bool, optional): Using the previous state vector. Defaults to False.

        return:
            [data]: The experience result.
        """
        compiled_circuit = self._initial_circuit(circuit, use_previous)
        result = self._backend.run(compiled_circuit, shots=self._shots)

        return result.result().data()
