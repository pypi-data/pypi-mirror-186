#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/08/13 15:30
# @Author  : Xiaoquan Xu
# @File    : fermion_operator.py

"""
A fermion operator is a polynomial of anti-commutative creation-annihilation operators,
which is a useful representation for states and Hamiltonians by second quantization.
"""

from QuICT.chemistry.operator.polynomial_operator import PolynomialOperator


class FermionOperator(PolynomialOperator):
    """
    A fermion operator is a polynomial of anti-commutative creation-annihilation operators,
    which is a useful representation for states and Hamiltonians by second quantization.

    Due to the anti-commutation relation, the polynomial is in fact a multilinear function of
    the ladder operators. In this class, the operator could be represented as below.
    For example, list
    [[[(i, 1), (j, 1), (k, 0), (l, 0)], 1.2], [[(k, 1), (l, 1), (i, 0), (j, 0)], -1.2], ...]
    stands for (1.2 a_i^dagger a_j^dagger a_k a_l - 1.2 a_k^dagger a_l^dagger a_i a_j + ...),
    which could also be parsed as string '1.2 * i^ j^ k l - 1.2 * k^ l^ i j + ...'.

    In the following descriptions, the above list is called list format,
    while the above string is called string format.
    """
    def __init__(self, monomial=None, coefficient=1.):
        """
        Create a monomial of ladder operators with the two given formats.

        Args:
            monomial(list/str): Operator monomial in list/string format
            coefficient(int/float/complex): Coefficient of the monomial
        """
        super().__init__(monomial, coefficient)
        if self.operators == []:
            return
        variables = self.operators[0][0]
        l = len(variables)

        # The variables in a monomial should be in ascending order.
        # Anti-commutation relation for operators on different targets.
        for i in range(l - 1, 0, -1):
            fl = False
            for j in range(i):
                if variables[j][0] > variables[j + 1][0]:
                    variables[j], variables[j + 1] = variables[j + 1], variables[j]
                    coefficient *= -1
                    fl = True
            if not fl:
                break

        # Adjacent identical operators lead to zero operator.
        if any([variables[i] == variables[i + 1] for i in range(l - 1)]):
            self.operators = []
            return

        # Anti-commutation relation for operators on identical targets.
        operators = []
        for i in range(l):
            if i == 0 or variables[i][0] != variables[i - 1][0]:
                k = l
                for j in range(i + 1, l):
                    if variables[j][0] != variables[i][0]:
                        k = j
                        break
                if (k - i) % 2 == 1:
                    operators += [variables[i]]
                elif variables[i][1] == 1:
                    operators += [variables[i], variables[i + 1]]
                else:
                    self.operators = [[operators, coefficient],
                                      [operators + [variables[i + 1], variables[i]], -coefficient]]
                    self *= FermionOperator(variables[k:])  # mul promises the ascending order
                    return
        self.operators = [[operators, coefficient]]

    @classmethod
    def get_polynomial(cls, monomial=None, coefficient=1.):
        '''
        Construct an instance of the same class(i.e. FermionOperator) using the arguments.

        Args:
            monomial(list/str): Operator monomial in list/string format
            coefficient(int/float/complex): Coefficient of the monomial
        '''
        return FermionOperator(monomial, coefficient)

    def analyze_single(self, single_operator):
        """
        Transform a string format of a single operator to a tuple.
        For example,
        '231' -> (231,0); '426^' -> (426,1)

        Args:
            single_operator(str): string format

        Returns:
            tuple: the corresponding tuple in list format
        """
        if single_operator[-1] == '^':
            return (int(single_operator[:-1]), 1)
        else:
            return (int(single_operator), 0)

    @classmethod
    def parse_single(cls, single_operator):
        """
        Transform a tuple format of a single operator to a string.
        For example,
        (21,0) -> '21 '; (88,1) -> '88^ '

        Args:
            single_operator(tuple): list format

        Returns:
            string: the corresponding string format
        """
        return str(single_operator[0]) + ('^ ' if single_operator[1] else ' ')
