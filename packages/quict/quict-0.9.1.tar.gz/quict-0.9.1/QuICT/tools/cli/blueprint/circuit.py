import os
import shutil

from QuICT.tools import Logger
from QuICT.tools.cli.utils import JobValidation
from QuICT.tools.circuit_library import CircuitLib


logger = Logger("CLI_Circuit_Management")


default_customed_circuit_folder = os.path.join(
    os.path.dirname(__file__),
    "..",
    "circuit"
)


def get_random_circuit(
    qubits: list,
    max_size: int,
    max_depth: int,
    instruction_set: str = "nam",
    output_path: str = '.'
):
    """ Generate the circuit with give parameters and write circuit's qasm into output path.

    Args:
        qubits (list): The list of qubits number.
        size (list): The list of circuit's gate number.
        random_param (bool): whether using random parameters for all quantum gates with parameters.
        instruction_set (str, optional): The given instruction sets. Defaults to "random".
        output_path (str, optional): The output folder. Defaults to current work dir.
    """
    circuit_library = CircuitLib(output_type="file", output_path=output_path)
    circuit_library.get_random_circuit(instruction_set, qubits, max_size, max_depth)


def get_algorithm_circuit(alg: str, qubits: list, output_path: str = "."):
    """ Get the algorithm circuit and write its qasm into output path. """
    circuit_library = CircuitLib(output_type="file", output_path=output_path)
    circuit_library.get_algorithm_circuit(alg, qubits_interval=qubits)


def store_quantum_circuit(name: str, file: str):
    """ Save the given quantum circuit into Quantum Circuit Library. """
    get_folder_name = os.listdir(default_customed_circuit_folder)
    if not name.endswith(".qasm"):
        name += ".qasm"

    if name in get_folder_name:
        logger.warn("Repeat circuits name.")
        return

    # qasm file validation
    _ = JobValidation.get_circuit_info(file)
    shutil.copy(file, f"{default_customed_circuit_folder}/{name}")
    logger.info(f"Successfully add circuit {name} into Circuit Library.")


def delete_quantum_circuit(name: str):
    """ Delete the customed quantum circuit in Circuit Library. """
    get_folder_name = os.listdir(default_customed_circuit_folder)
    if not name.endswith(".qasm"):
        name += ".qasm"

    if name not in get_folder_name:
        logger.warn("No target circuit in Circuit Library.")
        return

    os.remove(f"{default_customed_circuit_folder}/{name}")
    logger.info(f"Successfully remove circuit {name} from Circuit Library.")


def list_quantum_circuit():
    """ List all customed quantum circuit in Circuit Library. """
    circuit_name = os.listdir(default_customed_circuit_folder)
    logger.info(f"There are {len(circuit_name)} in the Circuit Library.")
    if len(circuit_name) > 0:
        logger.info("circuit names: " + ", ".join([cir[:-5] for cir in circuit_name]))
