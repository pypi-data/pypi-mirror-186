from quantagonia.qubo.variable import *
from quantagonia.qubo.term import *
from quantagonia.qubo.expression import *

###
## QuboVariable - add
###

@QuboVariable.__add__.register
def _(self, other : int) -> QuboExpression:
    q = QuboExpression()
    q += QuboTerm(1.0, [self])
    q += QuboTerm(float(other), [])

    return q

@QuboVariable.__add__.register
def _(self, other : float) -> QuboExpression:
    q = QuboExpression()
    q += QuboTerm(1.0, [self])
    q += QuboTerm(other, [])

    return q

@QuboVariable.__add__.register
def _(self, other : QuboVariable) -> QuboExpression:
    q = QuboExpression()
    q += QuboTerm(1.0, [self])
    q += QuboTerm(1.0, [other])

    return q

@QuboVariable.__add__.register
def _(self, other : QuboTerm) -> QuboExpression:
    q = QuboExpression()
    q += QuboTerm(1.0, [self])
    q += other

    return q

@QuboVariable.__add__.register
def _(self, other : QuboExpression) -> QuboExpression:
    q = QuboExpression()
    q += QuboTerm(1.0, [self])
    q += other

    return q

###
## QuboVariable - sub
###

@QuboVariable.__sub__.register
def _(self, other : int) -> QuboExpression:
    q = QuboExpression()
    q += QuboTerm(1.0, [self])
    q -= QuboTerm(float(other), [])

    return q

@QuboVariable.__sub__.register
def _(self, other : float) -> QuboExpression:
    q = QuboExpression()
    q += QuboTerm(1.0, [self])
    q -= QuboTerm(other, [])

    return q

@QuboVariable.__sub__.register
def _(self, other : QuboVariable) -> QuboExpression:
    q = QuboExpression()
    q += QuboTerm(1.0, [self])
    q -= QuboTerm(1.0, [other])

    return q

@QuboVariable.__sub__.register
def _(self, other : QuboTerm) -> QuboExpression:
    q = QuboExpression()
    q += QuboTerm(1.0, [self])
    q -= other

    return q

@QuboVariable.__sub__.register
def _(self, other : QuboExpression) -> QuboExpression:
    q = QuboExpression()
    q += QuboTerm(1.0, [self])
    q -= other

    return q

###
## QuboVariable - mul
###

@QuboVariable.__mul__.register
def _(self, other : int) -> QuboTerm:
    return QuboTerm(float(other), [self])

@QuboVariable.__mul__.register
def _(self, other : float) -> QuboTerm:
    return QuboTerm(other, [self])

@QuboVariable.__mul__.register
def _(self, other : QuboVariable) -> QuboTerm:
    return QuboTerm(1.0, [self, other])

@QuboVariable.__mul__.register
def _(self, other : QuboTerm) -> QuboExpression:
    q = other._clone()
    q *= QuboTerm(1.0, [self])

    return q

@QuboVariable.__mul__.register
def _(self, other : QuboExpression) -> QuboExpression:
    q = other._clone()
    q *= QuboTerm(1.0, [self])

    return q

###
## QuboTerm - imul
###

@QuboTerm.__imul__.register
def _(self, other : int) -> QuboTerm:
    self.coefficient *= other
    return self

@QuboTerm.__imul__.register
def _(self, other : float) -> QuboTerm:
    self.coefficient *= other
    return self

@QuboTerm.__imul__.register
def _(self, other : QuboVariable) -> QuboTerm:
    return self.__imul__(QuboTerm(1.0, [other]))

@QuboTerm.__imul__.register
def _(self, other : QuboTerm) -> QuboTerm:
    self.coefficient *= other.coefficient
    self.vars = self._join_vars(self.vars, other.vars)

    if self.order() > 2:
        raise Exception("Only QuboTerms with order <= 2 are supported.")

    return self

###
## QuboTerm - mul
###

@QuboTerm.__mul__.register
def _(self, other : int) -> QuboTerm:
    q = self._clone()
    q *= other
    return q

@QuboTerm.__mul__.register
def _(self, other : float) -> QuboTerm:
    q = self._clone()
    q *= other
    return q

@QuboTerm.__mul__.register
def _(self, other : QuboVariable) -> QuboTerm:
    q = self._clone()
    q *= other
    return q

@QuboTerm.__mul__.register
def _(self, other : QuboTerm) -> QuboTerm:
    q = self._clone()
    q *= other
    return q

@QuboTerm.__mul__.register
def _(self, other : QuboExpression) -> QuboExpression:
    q = other._clone()
    q *= self
    return q


###
## QuboExpression - iadd
###

@QuboExpression.__iadd__.register
def _(self, other : int) -> QuboExpression:
    if "" in self.terms:
        self.terms[""].coefficient += other
    else:
        self.terms[""] = QuboTerm(float(other), [])
    return self

@QuboExpression.__iadd__.register
def _(self, other : float) -> QuboExpression:
    if "" in self.terms:
        self.terms[""].coefficient += other
    else:
        self.terms[""] = QuboTerm(float(other), [])
    return self

@QuboExpression.__iadd__.register
def _(self, other : QuboVariable) -> QuboExpression:
    return self.__iadd__(QuboTerm(1.0, [other]))

@QuboExpression.__iadd__.register
def _(self, other : QuboTerm) -> QuboExpression:
    q = QuboExpression()
    q.terms[other.key()] = other

    return self.__iadd__(q)

@QuboExpression.__iadd__.register
def _(self, other : QuboExpression) -> QuboExpression:
    self.terms = self._iJoinTerms(self.terms, other.terms, 1.0)
    return self

###
## QuboExpression - isub
###

@QuboExpression.__isub__.register
def _(self, other : int) -> QuboExpression:
    return self.__iadd__(-1.0 * other)

@QuboExpression.__isub__.register
def _(self, other : float) -> QuboExpression:
    return self.__iadd__(-1.0 * other)

@QuboExpression.__isub__.register
def _(self, other : QuboVariable) -> QuboExpression:
    return self.__isub__(QuboTerm(1.0, [other]))

@QuboExpression.__isub__.register
def _(self, other : QuboTerm) -> QuboExpression:
    q = QuboExpression()
    q.terms[other.key()] = other._clone()
    q.terms[other.key()].coefficient *= -1.0

    return self.__iadd__(q)

@QuboExpression.__isub__.register
def _(self, other : QuboExpression) -> QuboExpression:
    self.terms = self._iJoinTerms(self.terms, other.terms, -1.0)
    return self

###
## QuboExpression - imul
###

@QuboExpression.__imul__.register
def _(self, other : int) -> QuboExpression:
    for _, term in self.terms.items():
        term *= other
    return self

@QuboExpression.__imul__.register
def _(self, other : float) -> QuboExpression:
    for _, term in self.terms.items():
        term *= other
    return self

@QuboExpression.__imul__.register
def _(self, other : QuboTerm) -> QuboExpression:
    for _, term in self.terms.items():
        term *= other
    return self

@QuboExpression.__imul__.register
def _(self, other : QuboVariable) -> QuboExpression:
    for _, term in self.terms.items():
        term *= other
    return self

@QuboExpression.__imul__.register
def _(self, other : QuboExpression) -> QuboExpression:
    q = QuboExpression()
    for _, s_term in self.terms.items():
        for _, o_term in other.terms.items():
            q += s_term * o_term

    self.terms = q.terms
    return self