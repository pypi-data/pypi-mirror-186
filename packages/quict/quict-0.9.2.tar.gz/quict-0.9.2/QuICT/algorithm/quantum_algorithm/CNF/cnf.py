# -*- coding:utf8 -*-
# @TIME    : 2022/7/
# @Author  : Cheng Guo
# @File    :

import math
import numpy as np
from QuICT.core.gate import *
from QuICT.core.gate.backend.mct.mct_linear_dirty_aux import MCTLinearHalfDirtyAux
from QuICT.core.gate.backend.mct.mct_one_aux import MCTOneAux
from QuICT.qcda.optimization.commutative_optimization import *


class CNFSATOracle:
    def __init__(self, simu=None):
        self.simulator = simu

    def circuit(self) -> CompositeGate:
        return self._cgate

    def run(
        self, cnf_file: str, ancilla_qubits_num: int = 3, dirty_ancilla: int = 0
    ) -> int:
        """Run CNF algorithm

        Args:
            cnf_file (str): The file path
            ancilla_qubits_num (int): >= 3
            dirty_ancilla (int): 0 for clean and >0 for dirty
        """
        # check if Aux > 2
        assert ancilla_qubits_num > 2, "Need at least 3 auxiliary qubit."

        # Step 1: Read CNF File
        variable_number, clause_number, CNF_data = self.read_CNF(cnf_file)

        # Step 2: Construct Circuit
        self._cgate = CompositeGate()
        p = math.floor((ancilla_qubits_num + 1) / 2)
        depth = math.ceil(math.log(clause_number, p))
        target = variable_number
        if clause_number == 1:
            controls = CNF_data[1]
            controls_abs = []
            controls_X = []
            current_Aux = target + 1
            for i in range(len(controls)):
                if controls[i] < 0:
                    controls_abs.append(-controls[i] - 1)
                if controls[i] > 0:
                    controls_abs.append(controls[i] - 1)
                    controls_X.append(controls[i] - 1)
            for i in range(len(controls_X)):
                X | self._cgate(controls_X[i])
            X | self._cgate(target)
            if controls_abs != []:
                MCTOneAux().execute(len(controls_abs) + 2) | self._cgate(
                    controls_abs + [target, current_Aux]
                )

            for i in range(len(controls_X)):
                X | self._cgate(controls_X[i])
        else:
            if dirty_ancilla == 0:
                if clause_number < p + 1:
                    controls_abs = []
                    for j in range(clause_number):
                        controls_abs.append(variable_number + j + 1)
                        self.clause(
                            CNF_data,
                            variable_number,
                            ancilla_qubits_num,
                            j + 1,
                            j + 1,
                            variable_number + j + 1,
                            depth - 1,
                            depth,
                        )
                    if controls_abs != []:
                        MCTOneAux().execute(len(controls_abs) + 2) | self._cgate(
                            controls_abs + [target, target - 1]
                        )
                    else:
                        X | self._cgate(target)
                    for j in range(clause_number):
                        self.clause(
                            CNF_data,
                            variable_number,
                            ancilla_qubits_num,
                            j + 1,
                            j + 1,
                            variable_number + j + 1,
                            depth - 1,
                            depth,
                        )
                else:
                    block_len = math.ceil(clause_number / p)
                    block_number = math.ceil(clause_number / block_len)
                    controls = []

                    for j in range(block_number):
                        self.clause(
                            CNF_data,
                            variable_number,
                            ancilla_qubits_num,
                            j * block_len + 1,
                            np.minimum((j + 1) * block_len, clause_number),
                            variable_number + ancilla_qubits_num - p + 1 + j,
                            depth - 1,
                            depth,
                        )
                        controls.append(
                            variable_number + ancilla_qubits_num - p + 1 + j
                        )

                    current_Aux = variable_number + 1
                    if controls != []:
                        MCTOneAux().execute(len(controls) + 2) | self._cgate(
                            controls + [target, current_Aux]
                        )

                    for j in range(block_number):
                        self.clause(
                            CNF_data,
                            variable_number,
                            ancilla_qubits_num,
                            j * block_len + 1,
                            np.minimum((j + 1) * block_len, clause_number),
                            variable_number + ancilla_qubits_num - p + 1 + j,
                            depth - 1,
                            depth,
                        )
            else:  # dirty_ancilla =1
                if clause_number < p + 1:
                    controls_abs = []
                    for j in range(clause_number):
                        controls_abs.append(variable_number + j + 1)
                        self.clause(
                            CNF_data,
                            variable_number,
                            ancilla_qubits_num,
                            j + 1,
                            j + 1,
                            variable_number + j + 1,
                            depth - 1,
                            depth,
                        )
                    if controls_abs != []:
                        MCTOneAux().execute(len(controls_abs) + 2) | self._cgate(
                            controls_abs + [target, target - 1]
                        )

                    for j in range(clause_number):
                        self.clause(
                            CNF_data,
                            variable_number,
                            ancilla_qubits_num,
                            j + 1,
                            j + 1,
                            variable_number + j + 1,
                            depth - 1,
                            depth,
                        )
                else:
                    if clause_number == 2:  # to do

                        CCX | self._cgate(
                            [
                                variable_number + ancilla_qubits_num - 1,
                                variable_number + ancilla_qubits_num,
                                target,
                            ]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            ancilla_qubits_num,
                            1,
                            1,
                            variable_number + ancilla_qubits_num - 1,
                            depth - 1,
                            depth,
                        )

                        CCX | self._cgate(
                            [
                                variable_number + ancilla_qubits_num - 1,
                                variable_number + ancilla_qubits_num,
                                target,
                            ]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            ancilla_qubits_num,
                            clause_number,
                            clause_number,
                            variable_number + ancilla_qubits_num,
                            depth - 1,
                            depth,
                        )

                        CCX | self._cgate(
                            [
                                variable_number + ancilla_qubits_num - 1,
                                variable_number + ancilla_qubits_num,
                                target,
                            ]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            ancilla_qubits_num,
                            1,
                            1,
                            variable_number + ancilla_qubits_num - 1,
                            depth - 1,
                            depth,
                        )

                        CCX | self._cgate(
                            [
                                variable_number + ancilla_qubits_num - 1,
                                variable_number + ancilla_qubits_num,
                                target,
                            ]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            ancilla_qubits_num,
                            clause_number,
                            clause_number,
                            variable_number + ancilla_qubits_num,
                            depth - 1,
                            depth,
                        )

                    else:
                        block_len = math.ceil(clause_number / p)
                        block_number = math.ceil(clause_number / block_len)
                        current_depth = depth
                        # even
                        if block_number == 2:
                            CCX | self._cgate(
                                [
                                    variable_number + ancilla_qubits_num - 1,
                                    variable_number + ancilla_qubits_num,
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                1,
                                block_len,
                                variable_number + ancilla_qubits_num - 1,
                                depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    variable_number + ancilla_qubits_num - 1,
                                    variable_number + ancilla_qubits_num,
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                block_len + 1,
                                clause_number,
                                variable_number + ancilla_qubits_num,
                                depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    variable_number + ancilla_qubits_num - 1,
                                    variable_number + ancilla_qubits_num,
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                1,
                                block_len,
                                variable_number + ancilla_qubits_num - 1,
                                depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    variable_number + ancilla_qubits_num - 1,
                                    variable_number + ancilla_qubits_num,
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                block_len + 1,
                                clause_number,
                                variable_number + ancilla_qubits_num,
                                depth - 1,
                                depth,
                            )

                        else:  # block_number > 2
                            c = []
                            for i in range(
                                variable_number,
                                variable_number + ancilla_qubits_num + 1,
                            ):
                                if i != target:
                                    c.append(i)

                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - block_number],
                                    c[ancilla_qubits_num - 2 * (block_number - 1)],
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                1,
                                block_len,
                                c[ancilla_qubits_num - block_number],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - block_number],
                                    c[ancilla_qubits_num - 2 * (block_number - 1)],
                                    target,
                                ]
                            )

                            # Control bit variable_ Number+Aux - (block_number-1)+2 - j
                            # put a clause, another control bit
                            # (will be the same as the previous target in this for)
                            # and the target will rise in turn
                            for j in range(1, block_number - 2):
                                CCX | self._cgate(
                                    [
                                        c[
                                            ancilla_qubits_num
                                            - (block_number - 1)
                                            + j
                                            - 1
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            + j
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            - 1
                                            + j
                                        ],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    ancilla_qubits_num,
                                    1 + j * block_len,
                                    (1 + j) * block_len,
                                    c[ancilla_qubits_num - (block_number - 1) + j - 1],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[
                                            ancilla_qubits_num
                                            - (block_number - 1)
                                            + j
                                            - 1
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            + j
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            - 1
                                            + j
                                        ],
                                    ]
                                )

                                # topPhase
                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - 2],
                                    c[ancilla_qubits_num - 1],
                                    c[ancilla_qubits_num - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                1 + (block_number - 2) * block_len,
                                (block_number - 1) * block_len,
                                c[ancilla_qubits_num - 2],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - 2],
                                    c[ancilla_qubits_num - 1],
                                    c[ancilla_qubits_num - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                1 + (block_number - 1) * block_len,
                                clause_number,
                                c[ancilla_qubits_num - 1],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - 2],
                                    c[ancilla_qubits_num - 1],
                                    c[ancilla_qubits_num - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                1 + (block_number - 2) * block_len,
                                (block_number - 1) * block_len,
                                c[ancilla_qubits_num - 2],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - 2],
                                    c[ancilla_qubits_num - 1],
                                    c[ancilla_qubits_num - 2 - (block_number - 1)],
                                ]
                            )

                            for j in range(block_number - 3, 0, -1):
                                CCX | self._cgate(
                                    [
                                        c[
                                            ancilla_qubits_num
                                            - (block_number - 1)
                                            + j
                                            - 1
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            + j
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            - 1
                                            + j
                                        ],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    ancilla_qubits_num,
                                    1 + j * block_len,
                                    (1 + j) * block_len,
                                    c[ancilla_qubits_num - (block_number - 1) + j - 1],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[
                                            ancilla_qubits_num
                                            - (block_number - 1)
                                            + j
                                            - 1
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            + j
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            - 1
                                            + j
                                        ],
                                    ]
                                )

                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - block_number],
                                    c[ancilla_qubits_num - 2 * (block_number - 1)],
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                1,
                                block_len,
                                c[ancilla_qubits_num - block_number],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - block_number],
                                    c[ancilla_qubits_num - 2 * (block_number - 1)],
                                    target,
                                ]
                            )

                            # repeat
                            for j in range(1, block_number - 2):
                                CCX | self._cgate(
                                    [
                                        c[
                                            ancilla_qubits_num
                                            - (block_number - 1)
                                            + j
                                            - 1
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            + j
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            - 1
                                            + j
                                        ],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    ancilla_qubits_num,
                                    1 + j * block_len,
                                    (1 + j) * block_len,
                                    c[ancilla_qubits_num - (block_number - 1) + j - 1],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[
                                            ancilla_qubits_num
                                            - (block_number - 1)
                                            + j
                                            - 1
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            + j
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            - 1
                                            + j
                                        ],
                                    ]
                                )

                                # topPhase
                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - 2],
                                    c[ancilla_qubits_num - 1],
                                    c[ancilla_qubits_num - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                1 + (block_number - 2) * block_len,
                                (block_number - 1) * block_len,
                                c[ancilla_qubits_num - 2],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - 2],
                                    c[ancilla_qubits_num - 1],
                                    c[ancilla_qubits_num - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                1 + (block_number - 1) * block_len,
                                clause_number,
                                c[ancilla_qubits_num - 1],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - 2],
                                    c[ancilla_qubits_num - 1],
                                    c[ancilla_qubits_num - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                ancilla_qubits_num,
                                1 + (block_number - 2) * block_len,
                                (block_number - 1) * block_len,
                                c[ancilla_qubits_num - 2],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[ancilla_qubits_num - 2],
                                    c[ancilla_qubits_num - 1],
                                    c[ancilla_qubits_num - 2 - (block_number - 1)],
                                ]
                            )

                            for j in range(block_number - 3, 0, -1):
                                CCX | self._cgate(
                                    [
                                        c[
                                            ancilla_qubits_num
                                            - (block_number - 1)
                                            + j
                                            - 1
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            + j
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            - 1
                                            + j
                                        ],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    ancilla_qubits_num,
                                    1 + j * block_len,
                                    (1 + j) * block_len,
                                    c[ancilla_qubits_num - (block_number - 1) + j - 1],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[
                                            ancilla_qubits_num
                                            - (block_number - 1)
                                            + j
                                            - 1
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            + j
                                        ],
                                        c[
                                            ancilla_qubits_num
                                            - 2 * (block_number - 1)
                                            - 1
                                            + j
                                        ],
                                    ]
                                )

    def read_CNF(self, cnf_file):
        # file analysis

        variable_number = 0
        clause_number = 0
        CNF_data = []
        f = open(cnf_file, "r")
        for line in f.readlines():
            new = line.strip().split()
            int_new = []
            if new[0] == "p":
                variable_number = int(new[2])
                clause_number = int(new[3])
            else:
                for x in new:
                    if (x != "0") and (int(x) not in int_new):
                        int_new.append(int(x))
                        if (-int(x)) in int_new:
                            int_new = []
                            break

            CNF_data.append(int_new)

        f.close()
        return variable_number, clause_number, CNF_data

    def clause(
        self,
        CNF_data,
        variable_number: int,
        Aux: int,
        StartID: int,
        EndID: int,
        target: int,
        current_depth: int,
        depth: int,
    ):

        p = math.floor((Aux + 1) / 2)
        if StartID == EndID:  # n= variable_number + Aux + 1
            controls = CNF_data[StartID]
            controls_abs = []
            controls_X = []
            for i in range(len(controls)):
                if controls[i] < 0:
                    controls_abs.append(-controls[i] - 1)
                if controls[i] > 0:
                    controls_abs.append(controls[i] - 1)
                    controls_X.append(controls[i] - 1)
            for i in range(len(controls_X)):
                X | self._cgate(controls_X[i])
            X | self._cgate(target)

            d = set(range(variable_number + 1 + Aux))
            d.remove(target)
            for j in controls_abs:
                d.remove(j)
            d = list(d)
            if controls_abs != []:
                MCTLinearHalfDirtyAux().execute(
                    len(controls_abs), (1 + variable_number + Aux)
                ) | self._cgate(controls_abs + d + [target])

            for i in range(len(controls_X)):
                X | self._cgate(controls_X[i])
        else:  # StartID != EndID
            if (EndID - StartID) == 1:  # StartID +1 == EndID
                if ((depth - current_depth) % 2) == 1:  # odd

                    CCX | self._cgate([variable_number + 1, variable_number, target])
                    self.clause(
                        CNF_data,
                        variable_number,
                        Aux,
                        StartID,
                        StartID,
                        variable_number + 1,
                        current_depth - 1,
                        depth,
                    )

                    CCX | self._cgate([variable_number + 1, variable_number, target])
                    self.clause(
                        CNF_data,
                        variable_number,
                        Aux,
                        EndID,
                        EndID,
                        variable_number,
                        current_depth - 1,
                        depth,
                    )

                    CCX | self._cgate([variable_number + 1, variable_number, target])
                    self.clause(
                        CNF_data,
                        variable_number,
                        Aux,
                        StartID,
                        StartID,
                        variable_number + 1,
                        current_depth - 1,
                        depth,
                    )

                    CCX | self._cgate([variable_number + 1, variable_number, target])
                    self.clause(
                        CNF_data,
                        variable_number,
                        Aux,
                        EndID,
                        EndID,
                        variable_number,
                        current_depth - 1,
                        depth,
                    )

                # even    target in {variable_number + ancilla_qubits_num - p + 1 + j}
                else:

                    CCX | self._cgate(
                        [variable_number + Aux - 1, variable_number + Aux, target]
                    )
                    self.clause(
                        CNF_data,
                        variable_number,
                        Aux,
                        StartID,
                        StartID,
                        variable_number + Aux - 1,
                        current_depth - 1,
                        depth,
                    )

                    CCX | self._cgate(
                        [variable_number + Aux - 1, variable_number + Aux, target]
                    )
                    self.clause(
                        CNF_data,
                        variable_number,
                        Aux,
                        EndID,
                        EndID,
                        variable_number + Aux,
                        current_depth - 1,
                        depth,
                    )

                    CCX | self._cgate(
                        [variable_number + Aux - 1, variable_number + Aux, target]
                    )
                    self.clause(
                        CNF_data,
                        variable_number,
                        Aux,
                        StartID,
                        StartID,
                        variable_number + Aux - 1,
                        current_depth - 1,
                        depth,
                    )

                    CCX | self._cgate(
                        [variable_number + Aux - 1, variable_number + Aux, target]
                    )
                    self.clause(
                        CNF_data,
                        variable_number,
                        Aux,
                        EndID,
                        EndID,
                        variable_number + Aux,
                        current_depth - 1,
                        depth,
                    )

            else:  # EndID - StartID > 1
                if (
                    EndID - StartID
                ) < p:  # if block_number == 1 and EndID - StartID > 1

                    c = []
                    for i in range(variable_number, variable_number + Aux + 1):
                        if i != target:
                            c.append(i)

                    if ((depth - current_depth) % 2) == 1:

                        CCX | self._cgate(
                            [c[EndID - StartID], c[2 * (EndID - StartID) - 1], target]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            StartID,
                            StartID,
                            c[EndID - StartID],
                            current_depth - 1,
                            depth,
                        )
                        CCX | self._cgate(
                            [c[EndID - StartID], c[2 * (EndID - StartID) - 1], target]
                        )

                        for j in range(1, EndID - StartID - 1):
                            CCX | self._cgate(
                                [
                                    c[(EndID - StartID) - j],
                                    c[2 * (EndID - StartID) - 1 - j],
                                    c[2 * (EndID - StartID) - j],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + j,
                                StartID + j,
                                c[(EndID - StartID) - j],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[(EndID - StartID) - j],
                                    c[2 * (EndID - StartID) - 1 - j],
                                    c[2 * (EndID - StartID) - j],
                                ]
                            )

                            # topPhase
                        CCX | self._cgate([c[1], c[0], c[EndID - StartID + 1]])
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            (EndID - 1),
                            EndID - 1,
                            c[1],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate([c[1], c[0], c[EndID - StartID + 1]])
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            EndID,
                            EndID,
                            c[0],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate([c[1], c[0], c[EndID - StartID + 1]])
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            (EndID - 1),
                            EndID - 1,
                            c[1],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate([c[1], c[0], c[EndID - StartID + 1]])

                        # downPhase
                        for j in range(EndID - StartID - 2, 0, -1):
                            CCX | self._cgate(
                                [
                                    c[(EndID - StartID) - j],
                                    c[2 * (EndID - StartID) - 1 - j],
                                    c[2 * (EndID - StartID) - j],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + j,
                                StartID + j,
                                c[(EndID - StartID) - j],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[(EndID - StartID) - j],
                                    c[2 * (EndID - StartID) - 1 - j],
                                    c[2 * (EndID - StartID) - j],
                                ]
                            )

                        CCX | self._cgate(
                            [c[EndID - StartID], c[2 * (EndID - StartID) - 1], target]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            StartID,
                            StartID,
                            c[EndID - StartID],
                            current_depth - 1,
                            depth,
                        )
                        CCX | self._cgate(
                            [c[EndID - StartID], c[2 * (EndID - StartID) - 1], target]
                        )

                        # repeat....

                        # Restore each location
                        # Control bit variable_ Number+Aux - (EndID StartID)+2 - j put a clause, another control bit
                        # (will be the same as the previous target in this for) and the target will rise in turn
                        for j in range(1, EndID - StartID - 1):
                            CCX | self._cgate(
                                [
                                    c[(EndID - StartID) - j],
                                    c[2 * (EndID - StartID) - 1 - j],
                                    c[2 * (EndID - StartID) - j],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + j,
                                StartID + j,
                                c[(EndID - StartID) - j],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[(EndID - StartID) - j],
                                    c[2 * (EndID - StartID) - 1 - j],
                                    c[2 * (EndID - StartID) - j],
                                ]
                            )

                            # topPhase
                        CCX | self._cgate([c[1], c[0], c[EndID - StartID + 1]])
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            (EndID - 1),
                            EndID - 1,
                            c[1],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate([c[1], c[0], c[EndID - StartID + 1]])
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            EndID,
                            EndID,
                            c[0],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate([c[1], c[0], c[EndID - StartID + 1]])
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            (EndID - 1),
                            EndID - 1,
                            c[1],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate([c[1], c[0], c[EndID - StartID + 1]])

                        # downPhase
                        for j in range(EndID - StartID - 2, 0, -1):
                            CCX | self._cgate(
                                [
                                    c[(EndID - StartID) - j],
                                    c[2 * (EndID - StartID) - 1 - j],
                                    c[2 * (EndID - StartID) - j],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + j,
                                StartID + j,
                                c[(EndID - StartID) - j],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[(EndID - StartID) - j],
                                    c[2 * (EndID - StartID) - 1 - j],
                                    c[2 * (EndID - StartID) - j],
                                ]
                            )

                    else:  # even
                        CCX | self._cgate(
                            [
                                c[Aux - 1 - EndID + StartID],
                                c[Aux - 2 * (EndID - StartID)],
                                target,
                            ]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            StartID,
                            StartID,
                            c[Aux - 1 - EndID + StartID],
                            current_depth - 1,
                            depth,
                        )
                        CCX | self._cgate(
                            [
                                c[Aux - 1 - EndID + StartID],
                                c[Aux - 2 * (EndID - StartID)],
                                target,
                            ]
                        )

                        for j in range(1, EndID - StartID - 1):
                            CCX | self._cgate(
                                [
                                    c[Aux - (EndID - StartID) + j - 1],
                                    c[Aux - 2 * (EndID - StartID) + j],
                                    c[Aux - 2 * (EndID - StartID) - 1 + j],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + j,
                                StartID + j,
                                c[Aux - (EndID - StartID) + j - 1],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[Aux - (EndID - StartID) + j - 1],
                                    c[Aux - 2 * (EndID - StartID) + j],
                                    c[Aux - 2 * (EndID - StartID) - 1 + j],
                                ]
                            )

                            # topPhase
                        CCX | self._cgate(
                            [c[Aux - 2], c[Aux - 1], c[Aux - 2 - EndID + StartID]]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            (EndID - 1),
                            EndID - 1,
                            c[Aux - 2],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate(
                            [c[Aux - 2], c[Aux - 1], c[Aux - 2 - EndID + StartID]]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            EndID,
                            EndID,
                            c[Aux - 1],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate(
                            [c[Aux - 2], c[Aux - 1], c[Aux - 2 - EndID + StartID]]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            (EndID - 1),
                            EndID - 1,
                            c[Aux - 2],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate(
                            [c[Aux - 2], c[Aux - 1], c[Aux - 2 - EndID + StartID]]
                        )

                        for j in range(EndID - StartID - 2, 0, -1):
                            CCX | self._cgate(
                                [
                                    c[Aux - (EndID - StartID) + j - 1],
                                    c[Aux - 2 * (EndID - StartID) + j],
                                    c[Aux - 2 * (EndID - StartID) - 1 + j],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + j,
                                StartID + j,
                                c[Aux - (EndID - StartID) + j - 1],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[Aux - (EndID - StartID) + j - 1],
                                    c[Aux - 2 * (EndID - StartID) + j],
                                    c[Aux - 2 * (EndID - StartID) - 1 + j],
                                ]
                            )

                        CCX | self._cgate(
                            [
                                c[Aux - 1 - EndID + StartID],
                                c[Aux - 2 * (EndID - StartID)],
                                target,
                            ]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            StartID,
                            StartID,
                            c[Aux - 1 - EndID + StartID],
                            current_depth - 1,
                            depth,
                        )
                        CCX | self._cgate(
                            [
                                c[Aux - 1 - EndID + StartID],
                                c[Aux - 2 * (EndID - StartID)],
                                target,
                            ]
                        )

                        for j in range(1, EndID - StartID - 1):
                            CCX | self._cgate(
                                [
                                    c[Aux - (EndID - StartID) + j - 1],
                                    c[Aux - 2 * (EndID - StartID) + j],
                                    c[Aux - 2 * (EndID - StartID) - 1 + j],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + j,
                                StartID + j,
                                c[Aux - (EndID - StartID) + j - 1],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[Aux - (EndID - StartID) + j - 1],
                                    c[Aux - 2 * (EndID - StartID) + j],
                                    c[Aux - 2 * (EndID - StartID) - 1 + j],
                                ]
                            )

                            # topPhase
                        CCX | self._cgate(
                            [c[Aux - 2], c[Aux - 1], c[Aux - 2 - EndID + StartID]]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            (EndID - 1),
                            EndID - 1,
                            c[Aux - 2],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate(
                            [c[Aux - 2], c[Aux - 1], c[Aux - 2 - EndID + StartID]]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            EndID,
                            EndID,
                            c[Aux - 1],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate(
                            [c[Aux - 2], c[Aux - 1], c[Aux - 2 - EndID + StartID]]
                        )
                        self.clause(
                            CNF_data,
                            variable_number,
                            Aux,
                            (EndID - 1),
                            EndID - 1,
                            c[Aux - 2],
                            current_depth - 1,
                            depth,
                        )

                        CCX | self._cgate(
                            [c[Aux - 2], c[Aux - 1], c[Aux - 2 - EndID + StartID]]
                        )

                        for j in range(EndID - StartID - 2, 0, -1):
                            CCX | self._cgate(
                                [
                                    c[Aux - (EndID - StartID) + j - 1],
                                    c[Aux - 2 * (EndID - StartID) + j],
                                    c[Aux - 2 * (EndID - StartID) - 1 + j],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + j,
                                StartID + j,
                                c[Aux - (EndID - StartID) + j - 1],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[Aux - (EndID - StartID) + j - 1],
                                    c[Aux - 2 * (EndID - StartID) + j],
                                    c[Aux - 2 * (EndID - StartID) - 1 + j],
                                ]
                            )

                else:  # EndID-StartID > p-1  block number >1
                    block_len = math.ceil((EndID - StartID + 1) / p)
                    block_number = math.ceil((EndID - StartID + 1) / block_len)
                    if block_number == 2:
                        # odd  target :variable_number + ancilla_qubits_num - p + 1 + j
                        if ((depth - current_depth) % 2) == 1:

                            CCX | self._cgate(
                                [variable_number + 1, variable_number, target]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID,
                                StartID + block_len - 1,
                                variable_number + 1,
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [variable_number + 1, variable_number, target]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + block_len,
                                EndID,
                                variable_number,
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [variable_number + 1, variable_number, target]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID,
                                StartID + block_len - 1,
                                variable_number + 1,
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [variable_number + 1, variable_number, target]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + block_len,
                                EndID,
                                variable_number,
                                current_depth - 1,
                                depth,
                            )
                        else:  # 当前偶数层

                            CCX | self._cgate(
                                [
                                    variable_number + Aux - 1,
                                    variable_number + Aux,
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID,
                                StartID + block_len - 1,
                                variable_number + Aux - 1,
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    variable_number + Aux - 1,
                                    variable_number + Aux,
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + block_len,
                                EndID,
                                variable_number + Aux,
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    variable_number + Aux - 1,
                                    variable_number + Aux,
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID,
                                StartID + block_len - 1,
                                variable_number + Aux - 1,
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    variable_number + Aux - 1,
                                    variable_number + Aux,
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + block_len,
                                EndID,
                                variable_number + Aux,
                                current_depth - 1,
                                depth,
                            )
                    else:
                        # block number >2
                        c = []
                        for i in range(variable_number, variable_number + Aux + 1):
                            if i != target:
                                c.append(i)
                        if ((depth - current_depth) % 2) == 1:

                            CCX | self._cgate(
                                [
                                    c[block_number - 1],
                                    c[2 * (block_number - 1) - 1],
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID,
                                StartID + block_len - 1,
                                c[block_number - 1],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[block_number - 1],
                                    c[2 * (block_number - 1) - 1],
                                    target,
                                ]
                            )

                            # control bit variable_number + Aux - (block_number-1) + 2 -j
                            # put clause, another control bit and target accension in accordance
                            for j in range(1, block_number - 2):
                                CCX | self._cgate(
                                    [
                                        c[(block_number - 1) - j],
                                        c[2 * (block_number - 1) - 1 - j],
                                        c[2 * (block_number - 1) - j],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    Aux,
                                    StartID + j * block_len,
                                    StartID - 1 + (j + 1) * block_len,
                                    c[(block_number - 1) - j],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[(block_number - 1) - j],
                                        c[2 * (block_number - 1) - 1 - j],
                                        c[2 * (block_number - 1) - j],
                                    ]
                                )

                                # topPhase
                            CCX | self._cgate([c[1], c[0], c[block_number]])
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 2) * block_len,
                                StartID + (block_number - 1) * block_len - 1,
                                c[1],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate([c[1], c[0], c[block_number]])
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 1) * block_len,
                                EndID,
                                c[0],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate([c[1], c[0], c[block_number]])
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 2) * block_len,
                                StartID + (block_number - 1) * block_len - 1,
                                c[1],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate([c[1], c[0], c[block_number]])

                            # downPhase
                            for j in range(block_number - 1 - 2, 0, -1):
                                CCX | self._cgate(
                                    [
                                        c[(block_number - 1) - j],
                                        c[2 * (block_number - 1) - 1 - j],
                                        c[2 * (block_number - 1) - j],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    Aux,
                                    StartID + j * block_len,
                                    StartID - 1 + (j + 1) * block_len,
                                    c[(block_number - 1) - j],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[(block_number - 1) - j],
                                        c[2 * (block_number - 1) - 1 - j],
                                        c[2 * (block_number - 1) - j],
                                    ]
                                )

                            CCX | self._cgate(
                                [
                                    c[block_number - 1],
                                    c[2 * (block_number - 1) - 1],
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID,
                                StartID + block_len - 1,
                                c[block_number - 1],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[block_number - 1],
                                    c[2 * (block_number - 1) - 1],
                                    target,
                                ]
                            )

                            # repeat....

                            # 还原各个位置
                            # 控制位variable_number + Aux - (block_number-1) + 2 -j 放 clause
                            # 另一个 控制位(将与此for内的前一个target 相同)并和target 依次上升
                            for j in range(1, block_number - 1 - 1):
                                CCX | self._cgate(
                                    [
                                        c[(block_number - 1) - j],
                                        c[2 * (block_number - 1) - 1 - j],
                                        c[2 * (block_number - 1) - j],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    Aux,
                                    StartID + j * block_len,
                                    StartID - 1 + (j + 1) * block_len,
                                    c[(block_number - 1) - j],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[(block_number - 1) - j],
                                        c[2 * (block_number - 1) - 1 - j],
                                        c[2 * (block_number - 1) - j],
                                    ]
                                )

                                # topPhase
                            CCX | self._cgate([c[1], c[0], c[block_number]])
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 2) * block_len,
                                StartID + (block_number - 1) * block_len - 1,
                                c[1],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate([c[1], c[0], c[block_number]])
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 1) * block_len,
                                EndID,
                                c[0],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate([c[1], c[0], c[block_number]])
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 2) * block_len,
                                StartID + (block_number - 1) * block_len - 1,
                                c[1],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate([c[1], c[0], c[block_number]])

                            # downPhase
                            for j in range(block_number - 1 - 2, 0, -1):
                                CCX | self._cgate(
                                    [
                                        c[(block_number - 1) - j],
                                        c[2 * (block_number - 1) - 1 - j],
                                        c[2 * (block_number - 1) - j],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    Aux,
                                    StartID + j * block_len,
                                    StartID - 1 + (j + 1) * block_len,
                                    c[(block_number - 1) - j],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[(block_number - 1) - j],
                                        c[2 * (block_number - 1) - 1 - j],
                                        c[2 * (block_number - 1) - j],
                                    ]
                                )

                        else:  # even
                            CCX | self._cgate(
                                [
                                    c[Aux - block_number],
                                    c[Aux - 2 * (block_number - 1)],
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID,
                                StartID - 1 + block_len,
                                c[Aux - block_number],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[Aux - block_number],
                                    c[Aux - 2 * (block_number - 1)],
                                    target,
                                ]
                            )

                            for j in range(1, block_number - 2):
                                CCX | self._cgate(
                                    [
                                        c[Aux - (block_number - 1) + j - 1],
                                        c[Aux - 2 * (block_number - 1) + j],
                                        c[Aux - 2 * (block_number - 1) - 1 + j],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    Aux,
                                    StartID + j * block_len,
                                    StartID - 1 + (1 + j) * block_len,
                                    c[Aux - (block_number - 1) + j - 1],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[Aux - (block_number - 1) + j - 1],
                                        c[Aux - 2 * (block_number - 1) + j],
                                        c[Aux - 2 * (block_number - 1) - 1 + j],
                                    ]
                                )

                                # topPhase
                            CCX | self._cgate(
                                [
                                    c[Aux - 2],
                                    c[Aux - 1],
                                    c[Aux - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 2) * block_len,
                                StartID + (block_number - 1) * block_len - 1,
                                c[Aux - 2],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[Aux - 2],
                                    c[Aux - 1],
                                    c[Aux - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 1) * block_len,
                                EndID,
                                c[Aux - 1],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[Aux - 2],
                                    c[Aux - 1],
                                    c[Aux - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 2) * block_len,
                                StartID + (block_number - 1) * block_len - 1,
                                c[Aux - 2],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[Aux - 2],
                                    c[Aux - 1],
                                    c[Aux - 2 - (block_number - 1)],
                                ]
                            )

                            for j in range(block_number - 3, 0, -1):
                                CCX | self._cgate(
                                    [
                                        c[Aux - (block_number - 1) + j - 1],
                                        c[Aux - 2 * (block_number - 1) + j],
                                        c[Aux - 2 * (block_number - 1) - 1 + j],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    Aux,
                                    StartID + j * block_len,
                                    StartID - 1 + (1 + j) * block_len,
                                    c[Aux - (block_number - 1) + j - 1],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[Aux - (block_number - 1) + j - 1],
                                        c[Aux - 2 * (block_number - 1) + j],
                                        c[Aux - 2 * (block_number - 1) - 1 + j],
                                    ]
                                )

                            CCX | self._cgate(
                                [
                                    c[Aux - block_number],
                                    c[Aux - 2 * (block_number - 1)],
                                    target,
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID,
                                StartID - 1 + block_len,
                                c[Aux - block_number],
                                current_depth - 1,
                                depth,
                            )
                            CCX | self._cgate(
                                [
                                    c[Aux - block_number],
                                    c[Aux - 2 * (block_number - 1)],
                                    target,
                                ]
                            )

                            # re
                            for j in range(1, block_number - 1 - 1):
                                CCX | self._cgate(
                                    [
                                        c[Aux - (block_number - 1) + j - 1],
                                        c[Aux - 2 * (block_number - 1) + j],
                                        c[Aux - 2 * (block_number - 1) - 1 + j],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    Aux,
                                    StartID + j * block_len,
                                    StartID - 1 + (1 + j) * block_len,
                                    c[Aux - (block_number - 1) + j - 1],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[Aux - (block_number - 1) + j - 1],
                                        c[Aux - 2 * (block_number - 1) + j],
                                        c[Aux - 2 * (block_number - 1) - 1 + j],
                                    ]
                                )

                                # topPhase
                            CCX | self._cgate(
                                [
                                    c[Aux - 2],
                                    c[Aux - 1],
                                    c[Aux - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 2) * block_len,
                                StartID + (block_number - 1) * block_len - 1,
                                c[Aux - 2],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[Aux - 2],
                                    c[Aux - 1],
                                    c[Aux - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 1) * block_len,
                                EndID,
                                c[Aux - 1],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[Aux - 2],
                                    c[Aux - 1],
                                    c[Aux - 2 - (block_number - 1)],
                                ]
                            )
                            self.clause(
                                CNF_data,
                                variable_number,
                                Aux,
                                StartID + (block_number - 2) * block_len,
                                StartID + (block_number - 1) * block_len - 1,
                                c[Aux - 2],
                                current_depth - 1,
                                depth,
                            )

                            CCX | self._cgate(
                                [
                                    c[Aux - 2],
                                    c[Aux - 1],
                                    c[Aux - 2 - (block_number - 1)],
                                ]
                            )

                            for j in range(block_number - 3, 0, -1):
                                CCX | self._cgate(
                                    [
                                        c[Aux - (block_number - 1) + j - 1],
                                        c[Aux - 2 * (block_number - 1) + j],
                                        c[Aux - 2 * (block_number - 1) - 1 + j],
                                    ]
                                )
                                self.clause(
                                    CNF_data,
                                    variable_number,
                                    Aux,
                                    StartID + j * block_len,
                                    StartID - 1 + (1 + j) * block_len,
                                    c[Aux - (block_number - 1) + j - 1],
                                    current_depth - 1,
                                    depth,
                                )
                                CCX | self._cgate(
                                    [
                                        c[Aux - (block_number - 1) + j - 1],
                                        c[Aux - 2 * (block_number - 1) + j],
                                        c[Aux - 2 * (block_number - 1) - 1 + j],
                                    ]
                                )
