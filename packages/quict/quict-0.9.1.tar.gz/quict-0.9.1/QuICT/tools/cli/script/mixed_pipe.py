import sys

from QuICT.tools.cli.script.qcda import qcda_start
from QuICT.tools.cli.script.simulation import simulation_start


def start_pipeline(**kwargs):
    simulation_related = {}
    for key in ["shots", "device", "backend", "precision"]:
        simulation_related[key] = kwargs[key]
        del kwargs[key]

    # Run QCDA process first
    qcda_start(**kwargs)

    # Run Simulation with optimized circuit from QCDA process
    output_path = kwargs['output_path']
    opt_cirpath = f"{output_path}/opt_circuit.qasm"
    simulation_start(circuit_path=opt_cirpath, output_path=output_path, **simulation_related)


if __name__ == "__main__":
    raw_args = sys.argv[1:]
    dict_args = dict([arg.split('=', maxsplit=1) for arg in raw_args])

    start_pipeline(**dict_args)
