
from __future__ import annotations

import os, os.path
import copy

try:
    from functools import singledispatchmethod
except:
    from singledispatchmethod import singledispatchmethod

from quantagonia.qubo.term import *
from quantagonia.qubo.expression import *

class QuboVariable(object):

    def __init__(self, name : str, pos : int, initial=None, fixing=None):
        self.name = name
        self._pos = pos
        if initial and initial not in [0, 1]:
            warnings.warn(f"Initial variable value {initial} not binary. Ignore initial assignment.")
            initial=None
        if fixing and fixing not in [0, 1]:
            warnings.warn(f"Fixing variable value {fixing} not binary. Ignore fixing.")
            initial=None
        if initial and fixing and initial != fixing:
            warnings.warn("Initial != fixing, discard initial and use fixing")
            initial = fixing
        self.fixing = fixing
        self.__assignment = initial

    @property
    def assignment(self):
        return self.__assignment

    @assignment.setter
    def assignment(self, value):
        # check against fixing
        if self.fixing and self.fixing != value:
            raise Exception(f"Assigning {value} to {self.name} contradicts fixing {self.fixing}")
        self.__assignment = value

    def id(self):
        return self._pos

    def eval(self):
        if self.assignment is None:
            raise Exception("Variable " + self.name + " is still unassigned.")
        return self.assignment

    def __str__(self):
        return self.name

    def key(self):
        return str(self)

    @singledispatchmethod
    def __add__(self, other):
        return NotImplemented

    @singledispatchmethod
    def __sub__(self, other):
        return NotImplemented

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
    def __mul__(self, other):
        return NotImplemented

    # other * var -> term
    def __rmul__(self, other : Union[int, float]) -> QuboTerm:
        return QuboTerm(other, [self])