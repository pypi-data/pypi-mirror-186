#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME    : 2021/08/13 14:30
# @Author  : Xiaoquan Xu
# @File    : polynomial_operator.py

"""
A PolynomialOperator of symbolic operators.
The superClass of FermionOperator and QubitOperator.
"""

import copy


class PolynomialOperator(object):
    """
    A polynomial of symbolic operators.
    The superClass of FermionOperator and QubitOperator.

    In this class, the operator could be represented as below.
    The first parameter in a binary tuple represents the target, while the second one represents the type.
    Two monomials can be merged if and only if their list formats only differ in the coefficient.
    The standardlization for a monomial should be accomplished in __init__ according to specific rules.

    For example, list
    [[[(i, 1), (j, 1), (k, 0), (l, 0)], 1.2], [[(k, 1), (l, 1), (i, 0), (j, 0)], -1.2], ...]
    stands for '1.2 a_i^(1) a_j^(1) a_k^(0) a_l^(0) - 1.2 a_k^(1) a_l^(1) a_i^(0) a_j^(0) + ...',

    In the following descriptions, the above list is called list format,
    while the above string is called string format.
    """
    def __init__(self, monomial=None, coefficient=1.):
        """
        Create a monomial of operators with the two given formats.
        PolynomialOperator() means zero operator, recognized by 'monomial == None'
        QubitOperator('X1') or FermionOperator('1^') or PolynomialOperator([(1,1)]) implies the coefficient is 1
        PolynomialOperator(0) or replacing 0 with some other constant is illegal

        Args:
            monomial(list/str): Operator monomial in list/string format
            coefficient(int/float/complex): Coefficient of the monomial
        """
        if monomial is None or coefficient == 0:       # zero operator
            self.operators = []
            return
        if isinstance(monomial, list):
            variables = copy.deepcopy(monomial)
        elif isinstance(monomial, str):
            variables = []
            for var in monomial.split():
                variables.append(self.analyze_single(var))
        else:
            raise Exception("Illegal type of monomial.")
        self.operators = [[variables, coefficient]]

    @classmethod
    def get_polynomial(cls, monomial=None, coefficient=1.):
        '''
        Construct an instance of the same class using the arguments.
        To be overrided.

        Args:
            monomial(list/str): Operator monomial in list/string format
            coefficient(int/float/complex): Coefficient of the monomial
        '''
        raise Exception("Construction of PolynomialOperator is prohibited.")

    @classmethod
    def analyze_single(cls, single_operator):
        """
        Transform a string format of a single operator to a tuple.
        To be overrided.

        Args:
            single_operator(str): string format

        Returns:
            tuple: the corresponding tuple in list format
        """
        raise Exception("The string format is not recognized.")

    @classmethod
    def parse_single(cls, single_operator):
        """
        Transform a tuple format of a single operator to a string.
        To be overrided.

        Args:
            single_operator(tuple): list format

        Returns:
            string: the corresponding string format
        """
        raise Exception("The string format is not realized.")

    def __add__(self, other):
        """
        Addition of two operators.

        Args:
            other(PolynomialOperator): Operator to be added

        Returns:
            PolynomialOperator: self + other
        """
        ans = self.get_polynomial()
        A = self.operators
        B = other.operators
        ia = ib = 0
        while ia < len(A) and ib < len(B):
            if A[ia][0] == B[ib][0]:
                if A[ia][1] + B[ib][1] != 0:
                    ans.operators += [[copy.deepcopy(A[ia][0]), A[ia][1] + B[ib][1]]]
                ia += 1
                ib += 1
            elif A[ia][0] < B[ib][0]:
                ans.operators += [copy.deepcopy(A[ia])]
                ia += 1
            else:
                ans.operators += [copy.deepcopy(B[ib])]
                ib += 1
        while ia < len(A):
            ans.operators += [copy.deepcopy(A[ia])]
            ia += 1
        while ib < len(B):
            ans.operators += [copy.deepcopy(B[ib])]
            ib += 1
        return ans

    def __iadd__(self, other):
        """
        Implement the '+=' operation.
        """
        ans = self + other
        self.operators = ans.operators
        return self

    def __mul__(self, other):
        """
        Multiplication of two operators or an operator with a number.

        Args:
            other(PolynomialOperator/int/float/complex): multiplier

        Returns:
            PolynomialOperator: self * other
        """
        ans = self.get_polynomial()
        if not isinstance(other, PolynomialOperator):
            ans.operators = [[copy.deepcopy(mono[0]), mono[1] * other] for mono in self.operators]
            return ans
        A = self.operators
        B = other.operators
        for mono_A in A:
            for mono_B in B:
                ans += self.get_polynomial(mono_A[0] + mono_B[0], mono_A[1] * mono_B[1])
        return ans

    def __imul__(self, other):
        """
        Implement the '*=' operation.
        """
        ans = self * other
        self.operators = ans.operators
        return self

    def __rmul__(self, other):
        """
        Args:
            other(PolynomialOperator/int/float/complex): multiplier

        Returns:
            PolynomialOperator: other * self
        """
        if not isinstance(other, PolynomialOperator):
            return self * other
        return other * self

    def __sub__(self, other):
        """
        Substraction of two operators.

        Args:
            other(PolynomialOperator): Operator to be substracted

        Returns:
            PolynomialOperator: self - other
        """
        return self + other * (-1)

    def __isub__(self, other):
        """
        Implement the '-=' operation.
        """
        self += other * (-1)
        return self

    def __truediv__(self, other):
        """
        Division of an operator with a number.

        Args:
            other(int/float/complex): divisor

        Returns:
            PolynomialOperator: self / other
        """
        return self * (1. / other)

    def __itruediv__(self, other):
        """
        Implement the '/=' operation.
        """
        self *= (1. / other)
        return self

    def __eq__(self, other) -> bool:
        """
        Judge whether two opperator polynomials are the same.
        Error within 10^(-6) can be ignored

        Args:
            other(PolynomialOperator): Operator to be judged

        Returns:
            bool: whether two opperator polynomials are the same
        """
        if not isinstance(other, PolynomialOperator):
            return False
        delta = self - other
        for mono in delta.operators:
            if (abs(mono[1]) > 1e-6):
                return False
        return True

    def parse(self):
        """
        Simply parse the list of the operators to string.
        """
        return f"{self.operators}"

    def __repr__(self) -> str:
        """
        Parse the list format to string format.
        """
        if self.operators == []:
            return '= 0 '
        ans = ''
        for mono in self.operators:
            ans += '+ (' + str(mono[1]) + ') '
            if mono[0] != []:
                ans += '* '
                for var in mono[0]:
                    ans += self.parse_single(var)
        ans = '=' + ans[1:]
        return ans
