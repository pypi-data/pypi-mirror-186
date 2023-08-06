import os
import sys

from QuICT.core import Layout
from QuICT.tools import Logger, LogFormat
from QuICT.tools.interface import OPENQASMInterface
from QuICT.tools.circuit_library import CircuitLib
from QuICT.qcda.qcda import QCDA
from QuICT.qcda.synthesis.gate_transform import USTCSet, GoogleSet, IBMQSet, IonQSet, NamSet, OriginSet
from QuICT.qcda.synthesis import GateTransform, CliffordUnidirectionalSynthesizer
from QuICT.qcda.optimization import (
    CliffordRzOptimization, CommutativeOptimization, SymbolicCliffordOptimization,
    TemplateOptimization, CnotWithoutAncilla
)


logger = Logger("QCDA_Local_Mode", LogFormat.full)


iset_mapping = {
    "USTC": USTCSet,
    "Google": GoogleSet,
    "IBMQ": IBMQSet,
    "IonQ": IonQSet,
    "Nam": NamSet,
    "Origin": OriginSet
}


def qcda_start(
    circuit_path: str,
    output_path: str,
    layout_path: str = None,
    methods: str = None,
    instruction_set: str = "Google",
    auto_mode: str = "light",
    para: bool = True,
    depara: bool = False,
    templates: str = ""
):
    if templates:
        width, size, depth = templates.split("+")
        templates = CircuitLib().get_template_circuit(
            int(width), int(size), int(depth)
        )

    method_mapping = {
        "GateTransform": GateTransform(iset_mapping[instruction_set]),
        "Clifford": CliffordUnidirectionalSynthesizer(),
        "CliffordRz": CliffordRzOptimization(auto_mode),
        "Commutative": CommutativeOptimization(para, depara),
        "SymbolicClifford": SymbolicCliffordOptimization(),
        "Template": TemplateOptimization(templates),
        "CNOT": CnotWithoutAncilla()
    }
    logger.debug("Start Run QCDA Job in local mode.")
    logger.debug(
        f"Job Parameters: circuit path: {circuit_path}, methods: {methods}, " +
        f"output path: {output_path}."
    )
    # Get circuit from given path
    circuit = OPENQASMInterface.load_file(circuit_path).circuit
    qcda = QCDA()

    if methods is not None:
        methods = methods.split("+")
        for method in methods:
            qcda.add_method(method_mapping[method])

    if layout_path is not None:
        layout = Layout.load_file(layout_path)
        qcda.add_mapping(layout)

    circuit_opt = qcda.compile(circuit)
    output_path = os.path.join(output_path, 'opt_circuit.qasm')
    circuit_opt.qasm(output_path)

    logger.debug(f"QCDA Job finished, store the result in {output_path}.")


if __name__ == "__main__":
    raw_args = sys.argv[1:]
    dict_args = dict([arg.split('=', maxsplit=1) for arg in raw_args])

    qcda_start(
        **dict_args
    )
