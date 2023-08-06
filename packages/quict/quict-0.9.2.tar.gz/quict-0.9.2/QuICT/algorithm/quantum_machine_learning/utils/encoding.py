from QuICT.algorithm.quantum_machine_learning.utils import Ansatz
from QuICT.algorithm.quantum_machine_learning.utils.gate_tensor import *
from QuICT.core import Circuit
from QuICT.core.gate import *


class Qubit:
    """Qubit encoding for encoding classical image data into quantum circuits."""

    @property
    def circuit(self):
        return self._circuit

    @property
    def ansatz(self):
        return self._ansatz

    def __init__(self, data_qubits, device=torch.device("cuda:0")):
        """The qubit encoding constructor.

        Args:
            data_qubits (int): The number of the data qubits.
            device (str, optional): The device to which the model is assigned.
                Defaults to "cuda:0".
        """
        self._data_qubits = data_qubits
        self._device = device
        self._circuit = None
        self._ansatz = None

    def encoding(self, img, circuit=False):
        """Encode the image as quantum ansatz using qubit encoding.
        One pixel corresponds to one qubit.

        Args:
            img (torch.Tensor): The classical image data.
            circuit (bool): If True, build data circuits at the same time.
                Defaults to False.
        """
        img = img.flatten()
        self._ansatz = Ansatz(self._data_qubits, device=self._device)
        for i in range(img.shape[0]):
            if img[i] == 1:
                self._ansatz.add_gate(X_tensor, i)
        if circuit:
            self._circuit = Circuit(self._data_qubits)
            for i in range(img.shape[0]):
                if img[i] == 1:
                    X | self._circuit(i)


class Amplitude:
    """Amplitude encoding for encoding classical image data into quantum circuits."""

    @property
    def circuit(self):
        return self._circuit

    @property
    def ansatz(self):
        return self._ansatz

    def __init__(self, data_qubits, device=torch.device("cuda:0")):
        """The amplitude encoding constructor.

        Args:
            data_qubits (int): The number of the data qubits.
            device (str, optional): The device to which the model is assigned.
                Defaults to "cuda:0".
        """
        self._data_qubits = data_qubits
        self._device = device
        self._circuit = None
        self._ansatz = None

    def encoding(self, img, circuit=False):
        """Encode the image as quantum ansatz using amplitude encoding."""
        raise NotImplementedError
