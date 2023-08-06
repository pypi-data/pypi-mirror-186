import torch
import torch.nn as nn

from QuICT.algorithm.quantum_machine_learning.ansatz_library import QNNLayer
from QuICT.algorithm.quantum_machine_learning.utils import Ansatz
from QuICT.algorithm.quantum_machine_learning.utils.gate_tensor import *
from QuICT.algorithm.quantum_machine_learning.utils.encoding import *
from QuICT.algorithm.quantum_machine_learning.utils import GpuSimulator
from QuICT.core import Circuit
from QuICT.core.gate import *


class QuantumNet(nn.Module):
    def __init__(
        self,
        data_qubits,
        layers=["XX", "ZZ"],
        encoding="qubit",
        device=torch.device("cuda:0"),
    ):
        """Initialize a QuantumNet instance.

        Args:
            data_qubits (int): The index of the readout qubit.
            layers (list, optional): The list of types of QNN layers.
                Currently only supports XX, YY, ZZ, and ZX. Defaults to ["XX", "ZZ"].
            encoding (str, optional): The encoding method to encode the image as quantum ansatz.
                Only support qubit encoding and amplitude encoding. Defaults to "qubit".
            device (torch.device, optional): The device to which the model is assigned.
                Defaults to torch.device("cuda:0").
        """
        super(QuantumNet, self).__init__()
        assert encoding in ["qubit", "amplitude"]
        self._layers = layers
        self._device = device
        self._data_qubits = data_qubits
        if encoding == "qubit":
            self._encoding = Qubit(data_qubits, device)
        elif encoding == "amplitude":
            self._encoding = Amplitude(data_qubits, device)
        self._n_qubits = self._data_qubits + 1
        self._simulator = GpuSimulator()
        self._pqc = QNNLayer(
            list(range(self._data_qubits)), self._data_qubits, device=self._device
        )
        self._define_params()

    def forward(self, X):
        """The forward propagation process of QuantumNet.

        Args:
            X (torch.Tensor): The input images.

        Returns:
            torch.Tensor: Classification result. The predicted probabilities that the images belongs to class 1.
        """
        Y_pred = torch.zeros([X.shape[0]], device=self._device)
        for i in range(X.shape[0]):
            self._encoding.encoding(X[i])
            data_ansatz = self._encoding.ansatz
            model_ansatz = self._construct_ansatz()
            ansatz = data_ansatz + model_ansatz
            if self._device.type == "cpu":
                state = ansatz.forward()
                prob = ansatz.measure_prob(self._data_qubits, state)
            else:
                state = self._simulator.forward(ansatz)
                prob = self._simulator.measure_prob(self._data_qubits, state)
            assert prob is not None, "There is no Measure Gate on the readout qubit."
            Y_pred[i] = prob[1]
        return Y_pred

    def _define_params(self):
        """Define the network parameters to be trained."""
        self.params = nn.Parameter(
            torch.rand(len(self._layers), self._data_qubits, device=self._device),
            requires_grad=True,
        )

    def _construct_ansatz(self):
        """Build the model ansatz."""
        model_ansatz = Ansatz(self._n_qubits, device=self._device)
        model_ansatz.add_gate(X_tensor, self._data_qubits)
        model_ansatz.add_gate(H_tensor, self._data_qubits)
        model_ansatz += self._pqc(self._layers, self.params)
        model_ansatz.add_gate(H_tensor, self._data_qubits)
        return model_ansatz

    def _construct_circuit(self):
        """Build the model circuit."""
        model_circuit = Circuit(self._n_qubits)
        X | model_circuit(self._data_qubits)
        H | model_circuit(self._data_qubits)
        sub_circuit = self._pqc.circuit_layer(self._layers, self.params)
        model_circuit.extend(sub_circuit.gates)
        H | model_circuit(self._data_qubits)
        return model_circuit
