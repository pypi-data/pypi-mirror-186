#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/9/12 12:09
# @Author  : Xiaoquan Xu
# @File    : parametertensor.py

import itertools as it
import numpy as np
from numpy import einsum

from QuICT.chemistry.operator.fermion_operator import FermionOperator


def obi_basis_rotation(obi, R):
    """
    Change the basis of a one-body integrals matrix

    Args:
        obi(Ndarray: n*n): one-body integrals of i^ j
        R(Ndarray: n*n): rotation matrix

    Returns:
        Ndarray: n*n one-body integrals of i^ j after rotation
    """
    return einsum("pi,pq,qj->ij", R.conj(), obi, R)


def tbi_basis_rotation(tbi, R):
    """
    Change the basis of a two-body integrals matrix

    Args:
        tbi(Ndarray: n*n*n*n): two-body integrals of i^ j^ s t
        R(Ndarray: n*n): rotation matrix

    Returns:
        Ndarray: n*n*n*n two-body integrals of i^ j^ s t after rotation
    """
    return einsum("pi,qj,pquv,us,vt->ijst", R.conj(), R.conj(), tbi, R, R)


class ParameterTensor:
    """
    Class for the parameters or Hamiltonian

    Attributes:
        const(complex): For a parameter tensor, it should be set to 1
            for multiplying with a Hamitonian
        obi(n*n ndarray): Represent the coefficients of terms of the form
            a^dagger_i a_j, i.e. (1, 0)
        tbi(n*n*n*n ndarray): Represent the coefficients of terms of the form
            a^dagger_i a^dagger_j a_k a_l, i.e. (1, 1, 0, 0)
    """
    def __init__(self, const, obi, tbi):
        self.const = const
        self.obi = obi
        self.tbi = tbi

    def get_fermion_operator(self):
        """
        Transform a Hamiltonian into a fermion-operator polymonial
        """
        n_qubits = self.obi.shape[0]
        fermion_operator = FermionOperator([], self.const)
        for index in it.product(range(n_qubits), repeat=2):
            fermion_operator += FermionOperator(list(zip(index, (1, 0))), self.obi[index])
        for index in it.product(range(n_qubits), repeat=4):
            fermion_operator += FermionOperator(list(zip(index, (1, 1, 0, 0))), self.tbi[index])
        return fermion_operator

    def expectation(self, other):
        """
        Multiply coefficient matrix with hamitonian
        """
        expectation = self.const * other.const
        expectation += np.sum(self.obi * other.obi)
        expectation += np.sum(self.tbi * other.tbi)
        return expectation


def generate_hamiltonian(const, obi, tbi, EQ_TOLERANCE=1.0E-12):
    """
    Double the dimension of obi and tbi,
    then generate an interaction operator as Hamiltonian
    """
    n = obi.shape[0]
    n_qubits = 2 * n
    new_obi = np.zeros((n_qubits, n_qubits))
    new_tbi = np.zeros((n_qubits, n_qubits, n_qubits, n_qubits))

    for p in range(n):
        for q in range(n):
            new_obi[2 * p, 2 * q] = obi[p, q]
            new_obi[2 * p + 1, 2 * q + 1] = obi[p, q]

    for p in range(n):
        for q in range(n):
            for r in range(n):
                for s in range(n):
                    # Mixed spin
                    new_tbi[2 * p, 2 * q + 1, 2 * r + 1, 2 * s] = tbi[p, q, r, s] / 2.
                    new_tbi[2 * p + 1, 2 * q, 2 * r, 2 * s + 1] = tbi[p, q, r, s] / 2.

                    # Same spin
                    new_tbi[2 * p, 2 * q, 2 * r, 2 * s] = tbi[p, q, r, s] / 2.
                    new_tbi[2 * p + 1, 2 * q + 1, 2 * r + 1, 2 * s + 1] = tbi[p, q, r, s] / 2.

    # Truncate.
    new_obi[np.absolute(new_obi) < EQ_TOLERANCE] = 0.
    new_tbi[np.absolute(new_tbi) < EQ_TOLERANCE] = 0.

    return ParameterTensor(const, new_obi, new_tbi)
