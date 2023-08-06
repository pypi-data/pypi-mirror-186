import sys
import time
import itertools

from QuICT.simulation import Simulator
from QuICT.simulation.state_vector import ConstantStateVectorSimulator
from QuICT.tools import Logger, LogFormat
from QuICT.tools.circuit_library import CircuitLib


logger = Logger("CLI_Benchmark", LogFormat.zero)


def benchmark(gpu_enable: bool):
    # Convert qubits from str into List[int]
    alg_list = ["adder", "grover", "maxcut"]
    max_qubits = 10
    circuit_library = CircuitLib()
    simulation = ConstantStateVectorSimulator()

    for alg in alg_list:
        circuits = circuit_library.get_algorithm_circuit(alg, qubits_interval=max_qubits)
        for cir in circuits:
            start_time = time.time()
            _ = simulation.run(cir)
            end_time = time.time()

            logger.info(f"Spending Time: {end_time - start_time}; with {cir.name}")

    max_qubits = list(range(10, 20, 4))
    max_qubits_dm = list(range(5, 10, 2))
    circuit_library = CircuitLib()

    circuits = circuit_library.get_random_circuit("ustc", qubits_interval=max_qubits)
    circuits_dm = circuit_library.get_random_circuit("ustc", qubits_interval=max_qubits_dm)

    backend_list = ["state_vector", "density_matrix", "unitary"]
    device_list = ["CPU"]
    if gpu_enable:
        device_list.append("GPU")

    for backend, device in itertools.product(backend_list, device_list):
        simulator = Simulator(device, backend)
        if backend == "state_vector" or circuit_path is not None:
            circuits_list = circuits
        else:
            circuits_list = circuits_dm

        for cir in circuits_list:
            start_time = time.time()
            _ = simulator.run(cir)
            end_time = time.time()

            logger.info(f"Spending Time: {end_time - start_time}; with {cir.name} and backend {backend}, {device}")


if __name__ == "__main__":
    enable_gpu = sys.argv[1]

    # if type_ == "algorithm":
    #     alg_benchmark()
    # else:
    #     simulation_benchmark(*sys.argv[2:])
