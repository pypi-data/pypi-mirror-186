from __future__ import annotations

from typing import List, Dict
import warnings
import copy

try:
    from functools import singledispatchmethod
except:
    from singledispatchmethod import singledispatchmethod

from quantagonia.qubo.variable import *
from quantagonia.qubo.expression import *

class QuboTerm(object):

    def __init__(self, coefficient : float, vars : list):
        super().__init__()
        self.coefficient = coefficient

        # by convention, we only store the upper triangular part of the QUBO ->
        # need to sort the variables ascendingly by their IDs
        self.vars = self._unique_vars(vars)

    def _clone(self):
        return QuboTerm(self.coefficient, copy.copy(self.vars))

    def _join_vars(self, set0 : List[QuboVariable], set1 : List[QuboVariable]) -> List[QuboVariable]:
        return self._unique_vars([*set0, *set1])

    def _unique_vars(self, vars : List[QuboVariable]) -> List[QuboVariable]:
        joint = [(i.key(), i) for i in vars]
        joint = dict(joint)

        return sorted(list(joint.values()), key = lambda v : v.id())

    def key(self):
        return "_".join([str(v) for v in self.vars])

    def order(self):
        return len(self.vars)

    def checkIsQUBO(self):
        return (self.order() <= 2)

    def isValid(self):
        is_valid = self.checkIsQUBO()

        if len(self.vars) > 1:
            is_valid &= (self.vars[0].id() < self.vars[1].id())

        return is_valid

    def eval(self):
        # if term represents just the constant shift
        if self.order() == 0:
            return self.coefficient

        E = self.coefficient * self.vars[0].eval()

        for var in self.vars[1:]:
            E *= var.eval()

        return E

    def __add__(self, other : Union[int, float, QuboTerm, QuboExpression]) -> QuboExpression:
        q = QuboExpression()
        q += self
        q += other

        return q

    def __sub__(self, other : Union[int, float, QuboTerm, QuboExpression]) -> QuboExpression:
        q = QuboExpression()
        q += self
        q -= other

        return q

    def __radd__(self, other : Union[int, float]) -> QuboExpression:
        q = QuboExpression()
        q += QuboTerm(other, [])
        q += self
        return q

    def __rsub__(self, other : Union[int, float]) -> QuboExpression:
        q = QuboExpression()
        q += QuboTerm(other, [])
        q -= self
        return q

    @singledispatchmethod
    def __imul__(self, other):
        return NotImplemented

    @singledispatchmethod
    def __mul__(self, other):
        return NotImplemented

    def __rmul__(self, other : Union[int, float]):
        q = self._clone()
        q.coefficient *= other

        return q

    def __str__(self):
        s = ""
        if(self.coefficient >= 0):
            s += "+ "
        else:
            s += "- "

        s += str(abs(self.coefficient))

        if self.order() > 0:
            s += " * " + str(self.vars[0])
            for var in self.vars[1:]:
                s += " * " + str(var)

        return s