import numpy as np
import torch

from QuICT.algorithm.quantum_machine_learning.utils import GpuSimulator
from QuICT.algorithm.quantum_machine_learning.utils import Hamiltonian


class VQENet(torch.nn.Module):
    """Variational Quantum Eigensolver algorithm.

    VQE <https://arxiv.org/abs/1304.3061> is a quantum algorithm that uses a variational
    technique to find the minimum eigenvalue of the Hamiltonian of a given system.
    """

    def __init__(
        self,
        n_qubits: int,
        p: int,
        hamiltonian: Hamiltonian,
        device=torch.device("cuda:0"),
    ):
        """Initialize a VQENet instance.

        Args:
            n_qubits (int): The number of qubits.
            p (int): The number of layers of the network.
            hamiltonian (Hamiltonian): The hamiltonian for a specific task.
            device (torch.device, optional): The device to which the VQANet is assigned.
                Defaults to torch.device("cuda:0").
        """
        super().__init__()
        self.n_qubits = n_qubits
        self.p = p
        self.hamiltonian = hamiltonian
        self.device = device
        self.simulator = GpuSimulator()
        self.define_network()

    def define_network(self):
        """Define the network construction.

        Raises:
            NotImplementedError: to be completed
        """
        raise NotImplementedError

    def loss_func(self, state):
        """The loss function for VQE, which aims to minimize the expectation of H.

        Args:
            state (torch.Tensor): The state vector.

        Returns:
            torch.Tensor: Loss, which is equal to the expectation of H.
        """
        if isinstance(state, np.ndarray):
            state = torch.from_numpy(state).to(self.device)
        assert state.shape[0] == 1 << self.n_qubits

        ansatz_list = self.hamiltonian.construct_hamiton_ansatz(
            self.n_qubits, self.device
        )
        coefficients = self.hamiltonian.coefficients
        state_vector = torch.zeros(1 << self.n_qubits, dtype=torch.complex128).to(
            self.device
        )
        for coeff, ansatz in zip(coefficients, ansatz_list):
            sv = ansatz.forward(state)
            state_vector += coeff * sv
        loss = torch.sum(state.conj() * state_vector).real

        return loss
