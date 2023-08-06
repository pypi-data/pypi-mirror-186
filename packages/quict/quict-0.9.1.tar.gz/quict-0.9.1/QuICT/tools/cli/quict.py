#!/home/likaiqi/.conda/envs/env_kq/bin/python

from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from copy import deepcopy


QUICT_DESCRIBE = """
   ___            ___    ____   _____
  / _ \   _   _  |_ _|  / ___| |_   _|
 | | | | | | | |  | |  | |       | |
 | |_| | | |_| |  | |  | |___    | |
  \__\_\  \___/  |___|  \____|   |_|


Welcome to QuICT Command Line Interface.

Using 'quict --help' to get the documents about QuICT CLI.
Using 'quict --version' to get the version of QuICT.
"""


def cli_construct():
    parser = ArgumentParser(
        prog="quict",
        description=QUICT_DESCRIBE,
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('--version', action='version', version='QuICT CLI 1.0', help="Show the current version.")
    subparsers = parser.add_subparsers()

    # Build env management
    from QuICT.tools.cli.blueprint.remote import login, logout, register, unsubscribe

    # Login
    login_sp = subparsers.add_parser(
        name="login",
        description="Login to QuICT Cloud System.",
        help="Login to QuICT Cloud System.",
    )
    login_sp.add_argument(
        "username", type=str,
        help="The username used to login."
    )
    login_sp.add_argument(
        "password", type=str,
        help="The password of user."
    )
    login_sp.set_defaults(func=login)

    # Logout
    logout_sp = subparsers.add_parser(
        name="logout",
        description="Logout from the QuICT.",
        help="Logout from the QuICT."
    )
    logout_sp.set_defaults(func=logout)

    # Register
    register_sp = subparsers.add_parser(
        name="register",
        description="User Register for QuICT Cloud System.",
        help="User Register",
    )
    register_sp.add_argument(
        "username", type=str,
        help="The username used."
    )
    register_sp.add_argument(
        "password", type=str,
        help="The password for user."
    )
    register_sp.add_argument(
        "email", type=str,
        help="The email address for registed user."
    )
    register_sp.set_defaults(func=register)

    # unsubscribe
    unsubscribe_sp = subparsers.add_parser(
        name="unsubscribe",
        description="Unsubscribe user to QuICT Cloud System.",
        help="Unsubscribe to QuICT Cloud System.",
    )
    unsubscribe_sp.add_argument(
        "username", type=str,
        help="The username used to unsubscribe."
    )
    unsubscribe_sp.add_argument(
        "password", type=str,
        help="The password of user."
    )
    unsubscribe_sp.set_defaults(func=unsubscribe)

    # Circuit
    circuit_sp = subparsers.add_parser(
        name="circuit",
        description="Manage the local circuit library.",
        help="get quantum circuit qasm."
    )
    circuit_cli_construct(circuit_sp)

    # Local Mode's Job
    local_sp = subparsers.add_parser(
        name="local",
        description="Local Modes QuICT Job Management",
        help="QuICT job's management in Local Mode."
    )
    job_cli_construct(local_sp, mode="local")

    # Local Mode's Job
    remote_sp = subparsers.add_parser(
        name="remote",
        description="Remote Modes QuICT Job Management.",
        help="QuICT job's management in Remote Mode."
    )
    job_cli_construct(remote_sp, mode="remote")

    # Benchmark
    benchmark_sp = subparsers.add_parser(
        name="benchmark",
        description="QuICT Benchmark",
        help="QuICT benchmark"
    )
    benchmark_cli_construct(benchmark_sp)

    return parser.parse_args()


def circuit_cli_construct(circuit_sp: ArgumentParser):
    """ Build circuit module in CLI

    Args:
        circuit_sp (ArgumentParser): Circuit Parser
    """
    from QuICT.tools.cli.blueprint.circuit import (
        get_random_circuit, get_algorithm_circuit, store_quantum_circuit,
        delete_quantum_circuit, list_quantum_circuit
    )

    subparser = circuit_sp.add_subparsers()
    # quict circuit get_random
    get_random = subparser.add_parser(
        name="get_random",
        description="Get random circuit.",
        help="get random circuit"
    )
    get_random.add_argument(
        "-i", "--instruction_set",
        choices=["ctrl_unitary", "diag", "single_bit", "ctrl_diag", "google", "ibmq", "ionq", "ustc", "nam", "origin"],
        nargs="?", default="nam",
        help="Choice the instrcution set for random circuit."
    )
    get_random.add_argument(
        "-q", "--qubits",
        nargs="+", type=int, default=[5],
        help="The number of qubits."
    )
    get_random.add_argument(
        "-ms", "--max_size",
        type=int, default=None,
        help="The maximum number of quantum gates."
    )
    get_random.add_argument(
        "-md", "--max_depth",
        type=int, default=None,
        help="The maximum number of circuit depth."
    )
    get_random.add_argument(
        "output_path",
        nargs="?", default=".",
        help="The output path, default to be current path."
    )
    get_random.set_defaults(func=get_random_circuit)

    # quict circuit get_algorithm
    get_algorithm = subparser.add_parser(
        name="get_algorithm",
        description="Get quantum algorithm's circuit.",
        help="get quantum algorithm's circuit, for some algorithm, may have qubits limitation."
    )
    get_algorithm.add_argument(
        "alg", nargs="?",
        choices=["adder", "clifford", "cnf", "grover", "maxcut", "qft", "qnn", "quantum_walk", "vqe"], default="qft",
        help="The quantum algorithm."
    )
    get_algorithm.add_argument(
        "-q", "--qubits",
        nargs="+", type=int, default=5,
        help="The number of qubits' number."
    )
    get_algorithm.add_argument(
        "output_path",
        nargs="?", default=".",
        help="The output path, default to be current path."
    )
    get_algorithm.set_defaults(func=get_algorithm_circuit)

    # quict circuit add
    add = subparser.add_parser(
        name="add",
        description="Store quantum circuit qasm.",
        help="store quantum circuit qasm"
    )
    add.add_argument(
        "name", type=str,
        help="The name of quantum circuit."
    )
    add.add_argument(
        "file", nargs="?",
        type=str, default=".",
        help="The path of qasm file."
    )
    add.set_defaults(func=store_quantum_circuit)

    # quict circuit delete
    delete = subparser.add_parser(
        name="delete",
        description="delete quantum circuit.",
        help="delete the quantum circuit"
    )
    delete.add_argument(
        "name", type=str,
        help="The name of quantum circuit."
    )
    delete.set_defaults(func=delete_quantum_circuit)

    # quict circuit list
    list_cir = subparser.add_parser(
        name="list",
        description="list all customed quantum circuit.",
        help="list all customed quantum circuit."
    )
    list_cir.set_defaults(func=list_quantum_circuit)


def job_cli_construct(mode_sp: ArgumentParser, mode: str):
    """ Build Job module [include remote and local mode] in CLI

    Args:
        mode_sp (ArgumentParser): Job Mode Parser
        mode (str): mode description, one of [local, remote]
    """
    from QuICT.tools.cli.blueprint.job import get_template

    if mode == "local":
        from QuICT.tools.cli.blueprint.job import (
            start_job, stop_job, restart_job, delete_job, status_job, list_jobs
        )
    elif mode == "remote":
        from QuICT.tools.cli.blueprint.remote import start_job, delete_job, status_job, list_jobs

    mode_subparser = mode_sp.add_subparsers()
    job_sp = mode_subparser.add_parser(
        name="job",
        description="QuICT Jobs Management.",
        help="QuICT job's related tools."
    )

    # quict job get_template
    subparser = job_sp.add_subparsers()
    get_templates = subparser.add_parser(
        name="get_template",
        description="Get job template.",
        help="Get job's template."
    )
    get_templates.add_argument(
        "output_path", nargs="?", default=".",
        help="The output path, default to be current path."
    )
    get_templates.set_defaults(func=get_template)

    # quict job start
    start = subparser.add_parser(
        name="start",
        description="Start the job.",
        help="start the job."
    )
    start.add_argument(
        "file", type=str,
        help="The path of jobs file, could be a directory or some file path.",
    )
    start.set_defaults(func=start_job)

    # quict job status
    status = subparser.add_parser(
        name="status",
        description="check the job's status.",
        help="check the job."
    )
    status.add_argument(
        "name", type=str,
        help="The name of target job."
    )
    status.set_defaults(func=status_job)

    if mode == "local":
        # quict job stop
        stop = subparser.add_parser(
            name="stop",
            description="stop a job.",
            help="stop a job."
        )
        stop.add_argument(
            "name", type=str,
            help="The name of target job."
        )
        stop.set_defaults(func=stop_job)

        # quict job restart
        restart = subparser.add_parser(
            name="restart",
            description="restart a stopped job.",
            help="restart a stopped job."
        )
        restart.add_argument(
            "name", type=str,
            help="The name of target job."
        )
        restart.set_defaults(func=restart_job)

    # quict job delete
    delete = subparser.add_parser(
        name="delete",
        description="delete the job.",
        help="delete the job."
    )
    delete.add_argument(
        "name", type=str,
        help="The name of target job."
    )
    delete.set_defaults(func=delete_job)

    # quict job list
    list_job = subparser.add_parser(
        name="list",
        description="list all jobs.",
        help="list all jobs."
    )
    list_job.set_defaults(func=list_jobs)


def benchmark_cli_construct(benchmark_sp: ArgumentParser):
    """ Build Benchmark Module in CLI

    Args:
        benchmark_sp (ArgumentParser): Benchmark Parser
    """
    from QuICT.tools.cli.blueprint.benchmark import benchmark

    benchmark_sp.add_argument(
        "--gpu", action="store_true",
        help="The name of target job."
    )
    benchmark_sp.set_defaults(func=benchmark)


def _decompose_namespace(args: Namespace):
    mapping_args = vars(deepcopy(args))
    del mapping_args["func"]

    return mapping_args


def main():
    args = cli_construct()
    map_args = _decompose_namespace(args)
    args.func(**map_args)


if __name__ == "__main__":
    main()
