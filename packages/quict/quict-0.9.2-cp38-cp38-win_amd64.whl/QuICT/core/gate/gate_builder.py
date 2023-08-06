#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2022/1/14 10:54
# @Author  : Han Yu, Li Kaiqi
# @File    : gate_builder.py

import numpy as np
import random

from QuICT.core.qubit import Qubit, Qureg
from QuICT.core.gate import *
from QuICT.core.utils import GateType
from QuICT.tools.exception.core import GateQubitAssignedError


GATE_TYPE_TO_CLASS = {
    GateType.h: HGate,
    GateType.hy: HYGate,
    GateType.s: SGate,
    GateType.sdg: SDaggerGate,
    GateType.x: XGate,
    GateType.y: YGate,
    GateType.z: ZGate,
    GateType.sx: SXGate,
    GateType.sy: SYGate,
    GateType.sw: SWGate,
    GateType.id: IDGate,
    GateType.u1: U1Gate,
    GateType.u2: U2Gate,
    GateType.u3: U3Gate,
    GateType.rx: RxGate,
    GateType.ry: RyGate,
    GateType.rz: RzGate,
    GateType.t: TGate,
    GateType.tdg: TDaggerGate,
    GateType.phase: PhaseGate,
    GateType.gphase: GlobalPhaseGate,
    GateType.cz: CZGate,
    GateType.cx: CXGate,
    GateType.cy: CYGate,
    GateType.ch: CHGate,
    GateType.crz: CRzGate,
    GateType.cu1: CU1Gate,
    GateType.cu3: CU3Gate,
    GateType.fsim: FSimGate,
    GateType.rxx: RxxGate,
    GateType.ryy: RyyGate,
    GateType.rzz: RzzGate,
    GateType.rzx: RzxGate,
    GateType.swap: SwapGate,
    GateType.iswap: iSwapGate,
    GateType.iswapdg: iSwapDaggerGate,
    GateType.sqiswap: SquareRootiSwapGate,
    GateType.cswap: CSwapGate,
    GateType.ccx: CCXGate,
    GateType.ccz: CCZGate,
    GateType.ccrz: CCRzGate,
    GateType.measure: MeasureGate,
    GateType.reset: ResetGate,
    GateType.barrier: BarrierGate,
    GateType.unitary: UnitaryGate,
    GateType.perm: PermGate,
    GateType.perm_fx: PermFxGate,
    GateType.qft: QFTGate,
    GateType.iqft: IQFTGate
}


def build_gate(
    gate_type: GateType,
    qubits: list,
    params: list = None
):
    """ Build a quantum gate with given parameter

    Args:
        gate_type (GateType): The gate type
        qubits (int/list/Qubit/Qureg): The qubit or qubit index of the gate.
        params (list, optional): The gate's parameters. Defaults to None.

    Returns:
        BasicGate: The quantum gate
    """
    gate = GATE_TYPE_TO_CLASS[gate_type]()
    if params is not None:
        params = params if isinstance(params, list) else [params]
        gate = gate(*params)

    args_number = gate.controls + gate.targets
    if isinstance(qubits, Qubit):
        qubits = Qureg(qubits)
    elif isinstance(qubits, int):
        qubits = [qubits]
    assert len(qubits) == args_number, GateQubitAssignedError(
        "The qubits number should equal to the target quantum gate."
    )

    if isinstance(qubits, Qureg):
        gate.assigned_qubits = qubits
    else:
        gate.cargs = qubits[:gate.controls]
        gate.targs = qubits[gate.controls:]

    return gate


def build_random_gate(
    gate_type: GateType,
    qubits: int,
    random_params: bool = False
):
    """ Build a quantum gate with random qubit and parameter.

    Args:
        gate_type (GateType): The gate type
        qubits (int): the number of qubits
        random_params (bool, optional): whether random parameter or use default parameter. Defaults to False.

    Returns:
        BasicGate: The quantum gate
    """
    gate = GATE_TYPE_TO_CLASS[gate_type]()
    args_number = gate.controls + gate.targets
    choiced_qubits = random.sample(range(qubits), args_number)
    gate.cargs = choiced_qubits[:gate.controls]
    gate.targs = choiced_qubits[gate.controls:]

    if random_params and gate.params:
        gate.pargs = list(np.random.uniform(0, 2 * np.pi, gate.params))

    return gate
