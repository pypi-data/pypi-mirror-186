# !/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/4/27 2:02 下午
# @Author  : Han Yu
# @File    : _simulator
import numpy as np
from typing import Union

from QuICT.core import Circuit
from QuICT.core.noise import NoiseModel
from QuICT.simulation.state_vector import CircuitSimulator
from QuICT.simulation.unitary import UnitarySimulator
from QuICT.simulation.density_matrix import DensityMatrixSimulation
from QuICT.simulation.utils import Result, options_validation
from QuICT.tools.exception.core import ValueError
from QuICT.tools.exception.simulation import SimulatorOptionsUnmatchedError


class Simulator:
    """ The high-level simulation class, including all QuICT simulator mode.

    Args:
        device (str): The device of the simulator. One of [CPU, GPU]
        backend (str): The backend for the simulator. One of [unitary, state_vector, density_matrix]
        shots (int): The running times; must be a positive integer, default to 1.
        precision (str): The precision of simulator, one of [single, double], default to double.
        circuit_record (bool): whether record circuit's qasm in output, default to False.
        amplitude_record (bool): whether record the amplitude of qubits, default to False.
        **options (dict): other optional parameters for the simulator.
    """

    __DEVICE = ["CPU", "GPU"]
    __BACKEND = ["unitary", "state_vector", "density_matrix"]
    __PRECISION = ["single", "double"]

    def __init__(
        self,
        device: str = "CPU",
        backend: str = "state_vector",
        precision: str = "double",
        circuit_record: bool = False,
        amplitude_record: bool = False,
        output_path: str = None,
        **options
    ):
        assert device in Simulator.__DEVICE, ValueError("Simulator.device", "[CPU, GPU]", device)
        self._device = device
        assert backend in Simulator.__BACKEND, \
            ValueError("Simulator.backend", "[unitary, state_vector, density_matrix]", backend)
        self._backend = backend
        assert precision in Simulator.__PRECISION, ValueError("Simulator.precision", "[single, double]", precision)
        self._precision = precision

        if options_validation(options=options, device=self._device, backend=self._backend):
            self._options = options
        else:
            raise SimulatorOptionsUnmatchedError(
                f"Unmatched options arguments depending on {self._device} and {self._backend}."
            )

        # Result's arguments
        self._result_recorder = Result(
            device, backend, precision, circuit_record, amplitude_record, self._options, output_path
        )

    def _load_simulator(self):
        """ Initial simulator. """
        if self._device == "GPU":
            from QuICT.simulation.state_vector import ConstantStateVectorSimulator

        if self._backend == "state_vector":
            simulator = ConstantStateVectorSimulator(precision=self._precision, **self._options) \
                if self._device == "GPU" else CircuitSimulator(precision=self._precision)
        else:
            if self._backend == "unitary":
                simulator = UnitarySimulator(device=self._device, precision=self._precision)
            else:
                simulator = DensityMatrixSimulation(device=self._device, precision=self._precision)

        return simulator

    def run(
        self,
        circuit: Union[Circuit, np.ndarray],
        shots: int = 1,
        state_vector: np.ndarray = None,
        density_matrix: np.ndarray = None,
        noise_model: NoiseModel = None,
        use_previous: bool = False
    ):
        """ start simulator with given circuit

        Args:
            circuit Union[Circuit, np.ndarray]: The quantum circuits or unitary matrix.
            state_vector (ndarray): The initial state vector.
            density_matrix (ndarray): The initial density matrix.
            noise_model (NoiseModel, optional): The NoiseModel only for density_matrix simulator. Defaults to None.
            use_previous (bool, optional): Using the previous state vector. Defaults to False.

        Yields:
            [dict]: The Result Dict.
        """
        if isinstance(circuit, np.ndarray) and self._backend != "unitary":
            raise SimulatorOptionsUnmatchedError(
                f"The unitary matrix input only allows in the unitary backend, not {self._backend}."
            )

        if (density_matrix is not None or noise_model is not None) and self._backend != "density_matrix":
            raise SimulatorOptionsUnmatchedError(
                "The density matrix and noise model input only allows in the density_matrix backend, " +
                f"not {self._backend}."
            )

        if state_vector is not None and self._backend == "density_matrix":
            raise SimulatorOptionsUnmatchedError(
                "The state vector input is not allowed in the density matrix backend."
            )

        if isinstance(circuit, Circuit):
            self._result_recorder.record_circuit(circuit)

        simulator = self._load_simulator()
        if self._backend == "density_matrix":
            amplitude = simulator.run(circuit, density_matrix, noise_model, use_previous)
        else:
            amplitude = simulator.run(circuit, state_vector, use_previous)

        self._result_recorder.record_amplitude(amplitude)

        sample_result = simulator.sample(shots)
        self._result_recorder.record_sample(sample_result)

        return self._result_recorder.__dict__()
