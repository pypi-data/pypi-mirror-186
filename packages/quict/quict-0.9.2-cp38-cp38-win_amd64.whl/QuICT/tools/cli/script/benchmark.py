import sys
import time
import itertools

from QuICT.simulation import Simulator
from QuICT.tools import Logger
from QuICT.tools.circuit_library import CircuitLib


logger = Logger("CLI_Benchmark")


def benchmark(gpu_enable: bool):
    max_qubits = list(range(10, 21, 2))
    max_qubits_dm = list(range(5, 11, 1))
    circuit_library = CircuitLib()

    circuits = circuit_library.get_random_circuit("ustc", qubits_interval=max_qubits)
    circuits_dm = circuit_library.get_random_circuit("ustc", qubits_interval=max_qubits_dm)

    logger.info("Using USTC Instruction Set for building benchamrk quantum circuits")

    backend_list = ["state_vector", "density_matrix"]
    device_list = ["CPU"]
    if gpu_enable:
        device_list.append("GPU")

    for backend, device in itertools.product(backend_list, device_list):
        logger.info(f"Simulation with backend {backend} and device {device}")
        simulator = Simulator(device, backend)
        if backend == "state_vector":
            circuits_list = circuits
        else:
            circuits_list = circuits_dm

        # pre-compile
        _ = simulator.run(circuits_list[0])

        for cir in circuits_list:
            size, width = cir.size(), cir.width()

            if size // width == 20:
                start_time = time.time()
                _ = simulator.run(cir)
                end_time = time.time()

                spending_times = round(end_time - start_time, 2)
                logger.info(
                    f"Simulating {width} qubits circuits and {size} quantum gates using {spending_times} seconds."
                )


if __name__ == "__main__":
    enable_gpu = True if sys.argv[1] == "True" else False

    benchmark(enable_gpu)
