import sys

from QuICT.tools import Logger, LogFormat
from QuICT.simulation import Simulator
from QuICT.tools.interface import OPENQASMInterface


logger = Logger("Simulation_Local_Mode", LogFormat.full)


def simulation_start(
    circuit_path: str,
    shots: str,
    device: str,
    backend: str,
    precision: str,
    output_path: str
):
    logger.info("Start Run Simulation Job in local mode.")
    logger.debug(
        f"Job Parameters: circuit path: {circuit_path}, shots: {shots}, " +
        f"Precision: {precision}, Device: {device}, Backend: {backend}, " +
        f"output_path: {output_path}."
    )
    # Get circuit from given path
    circuit = OPENQASMInterface.load_file(circuit_path).circuit

    # Start Simulator
    simulator = Simulator(
        device=device,
        backend=backend,
        precision=precision,
        output_path=output_path,
        amplitude_record=True
    )
    simulator.run(circuit, shots=int(shots))

    logger.info(f"Simulation Job finished, store the result in {output_path}.")


if __name__ == "__main__":
    raw_args = sys.argv[1:]
    dict_args = dict([arg.split('=', maxsplit=1) for arg in raw_args])
    logger.info(f"{dict_args}")

    simulation_start(
        **dict_args
    )
