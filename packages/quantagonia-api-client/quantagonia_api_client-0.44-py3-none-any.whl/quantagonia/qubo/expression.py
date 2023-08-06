from __future__ import annotations

from typing import List, Dict, Union
try:
    from functools import singledispatchmethod
except:
    from singledispatchmethod import singledispatchmethod

from quantagonia.qubo.variable import *
from quantagonia.qubo.term import *

class QuboExpression(object):

    def __init__(self):
        super().__init__()

        # hash -> (term with coefficient)
        self.terms = {}

    def _clone(self):
        q = QuboExpression()
        for k in self.terms:
            q.terms[k] = self.terms[k]._clone()

        return q

    ###
    # ADDITION + SUBTRACTION
    ###

    # join clones of term dictionaries
    def _joinTerms(self, terms0 : Dict[str, QuboTerm], terms1 : Dict[str, QuboTerm], op_coefficient : float):
        joint_terms = {}
        for key, term in terms0.items():
            joint_terms[key] = term._clone()
        for k in terms1:
            if k in joint_terms:
                joint_terms[k].coefficient += op_coefficient * terms1[k].coefficient
            else:
                joint_terms[k] = terms1[k]._clone()

        return joint_terms

    # join second dictionary into first
    def _iJoinTerms(self, terms0 : Dict[str, QuboTerm], terms1 : Dict[str, QuboTerm], op_coefficient : float):
        for k in terms1:
            if k in terms0:
                terms0[k].coefficient += op_coefficient * terms1[k].coefficient
            else:
                terms0[k] = terms1[k]._clone()

        return terms0

    @singledispatchmethod
    def __iadd__(self, other):
        return NotImplemented

    @singledispatchmethod
    def __isub__(self, other):
        return NotImplemented

    def __add__(self, other : Union[int, float, QuboVariable, QuboTerm, QuboExpression]):
        q = self._clone()
        return q.__iadd__(other)

    def __sub__(self, other : Union[int, float, QuboVariable, QuboTerm, QuboExpression]):
        q = self._clone()
        return q.__isub__(other)

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

    def __mul__(self, other : Union[int, float, QuboVariable, QuboTerm, QuboExpression]):
        q = self._clone()
        q *= other
        return q

    def __rmul__(self, other : Union[int, float]):
        q = self._clone()
        for _, term in q.terms.items():
            term *= other
        return q

    def eval(self, shift = 0):
        E = shift

        for term in self.terms:
            E += self.terms[term].eval()

        return E

    def isValid(self):
        is_valid = True

        for _, term in self.terms.items():
            is_valid &= term.isValid()

        return is_valid

    def __str__(self):
        s = " ".join([str(self.terms[t]) for t in self.terms])

        return s