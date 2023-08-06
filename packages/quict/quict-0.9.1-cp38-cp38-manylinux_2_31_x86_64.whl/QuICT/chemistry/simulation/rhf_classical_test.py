#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/9/11 18:20
# @Author  : Xiaoquan Xu
# @File    : rhf_classical_simulation.py

import os
import numpy as np
import scipy.linalg as splin

from QuICT.chemistry.simulation.parametertensor import *
from QuICT.chemistry.simulation.moleculardata import MolecularData
from QuICT.chemistry.simulation.rhf_objective import RHFObjective

DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + '/molecular_data'


def rhf_classical_simulation(n_atoms, distance, data_dir=None):
    if data_dir is None:
        data_dir = DATA_DIR
    data_dir += "/hydrogen_chains"
    data_dir += "/h_" + str(n_atoms) + "_sto-3g"
    data_dir += "/bond_distance_" + str(distance)
    molfile = data_dir + "/H" + str(n_atoms)
    molfile += "_sto-3g_singlet_linear_r-" + str(distance)
    moldata = MolecularData(molfile)

    S = np.load(data_dir + "/overlap.npy")
    Hcore = np.load(data_dir + "/h_core.npy")
    TEI = np.einsum("psqr", np.load(data_dir + "/tei.npy"))  # (1, 1, 0, 0)

    _, X = splin.eigh(Hcore, S)
    obi = obi_basis_rotation(Hcore, X)
    tbi = tbi_basis_rotation(TEI, X)
    # print(tbi)
    molecular_hamiltonian = generate_hamiltonian(moldata.nuclear_repulsion, obi, tbi)
    # print(molecular_hamiltonian.const)
    # print(molecular_hamiltonian.obi)
    # print(molecular_hamiltonian.tbi)
    # print(moldata.n_electrons)

    rhf_objective = RHFObjective(molecular_hamiltonian, moldata.n_electrons)
    result = rhf_objective.minimization()

    return rhf_objective, moldata, result, obi, tbi


if __name__ == "__main__":
    rhf_objective, moldata, result, obi, tbi = rhf_classical_simulation(6, 1.3)
    assert moldata.n_orbitals == 6
    assert moldata.n_electrons == 6
    assert moldata.one_body_integrals is None
    assert moldata.two_body_integrals is None

    assert result['fun'] == -2.924060484972225
    assert result['success'] is True
    assert result['nit'] == 7

    rhf_objective, moldata, result, obi, tbi = rhf_classical_simulation(3, 2.5)
    # actually H_3 is H_3_plus
    assert result['fun'] == -0.8062049864970052
    assert result['success'] is True
    assert result['nit'] == 2
