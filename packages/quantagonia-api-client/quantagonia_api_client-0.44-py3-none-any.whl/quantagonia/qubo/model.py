from __future__ import annotations

import os, os.path
import readline
from operator import itemgetter

from typing import List, Dict
import warnings
import re
import tempfile
import gzip

try:
    from functools import singledispatchmethod
except:
    from singledispatchmethod import singledispatchmethod

from quantagonia.enums import HybridSolverOptSenses

from quantagonia.runner import Runner
from quantagonia.runner_factory import RunnerFactory
from quantagonia.spec_builder import QUBOSpecBuilder

from quantagonia.qubo.variable import *
from quantagonia.qubo.term import *
from quantagonia.qubo.expression import *

class QuboModel(object):

    def __init__(self, sense : HybridSolverOptSenses = HybridSolverOptSenses.MAXIMIZE):

        self.vars = {}
        self.objective = QuboExpression()
        self.__sense = sense

        # for future use
        self.sos1 = []
        self.sos2 = []

        self._pos_ctr = 0

    @property
    def sense(self):
        return self.__sense

    @sense.setter
    def sense(self, sense : HybridSolverOptSenses):
        if isinstance(sense, HybridSolverOptSenses):
            self.__sense = sense
        else:
            raise RuntimeError(f"Try to set invalid optimization sense: {sense}")

    def addSOS1(self, vars : list):
        warnings.warn("SOS1 constraints are currently not supported in QUBOs")
        self.sos1.append(vars)

    def addSOS2(self, vars : list):
        warnings.warn("SOS2 constraints are currently not supported in QUBOs")
        self.sos2.append(vars)

    def addVariable(self, name : str, initial=None, fixing=None, disable_warnings=False):
        if(name in self.vars):
            if(not disable_warnings):
                warnings.warn("Variable " + name + " already in QUBO...")

            return self.vars[name]

        self.vars[name] = QuboVariable(name, self._pos_ctr, initial, fixing)
        self._pos_ctr += 1

        return self.vars[name]

    def variable(self, name : str):
        return self.vars[name]

    def eval(self):
        return self.objective.eval()

    def isValid(self):

        # check that all terms are in the upper triangle and that they
        # have been reduced in the right way

        return self.objective.isValid()

    def writeQUBO(self, path : str):

        shift = 0.0
        num_shift = 0
        if "" in self.objective.terms:
            num_shift = 1
            shift = self.objective.terms[""].coefficient

        # check that all terms are in the upper triangular part
        if not self.isValid():
            raise Exception("QUBO invalid - check that all terms are in the upper triangular part of Q.")

        # prepare sorted (by row) COO triplets
        triplets = []
        for key in self.objective.terms:
            if key == "":
                continue

            term = self.objective.terms[key]

            if(term.order() == 1):
                triplets.append((term.vars[0].id(), term.vars[0].id(), term.coefficient))

            # By convention, we only store the upper triangular part of the matrix, but it
            # is mirrored into the lower triangular part inside the QUBO solver - hence in
            # order to maintain the optimum, we have to divide the coefficients of
            # off-diagonal entries by 2
            if(term.order() == 2):
                triplets.append((term.vars[0].id(), term.vars[1].id(), 0.5 * term.coefficient))

        triplets.sort(key=itemgetter(0,1))

        with open(path, 'w') as f:

            sense_str = "MAXIMIZE" if self.sense == HybridSolverOptSenses.MAXIMIZE else "MINIMIZE"
            f.write(sense_str + "\n")
            f.write("1\n")
            f.write("1.0\n")

            f.write(f"{shift}\n")

            # create sparse matrix from terms in objective
            f.write(f"{len(self.vars)} {len(self.objective.terms) - num_shift}\n")
            for t in triplets:
                f.write(f"{t[0]} {t[1]} {t[2]}\n")

            # add fixings
            for var in self.vars.values():
                if var.fixing:
                    f.write(f"f {var.id()} {var.fixing}\n")

    def getNNZUpperTriangle(self):
        """
        Get the number of nonzeros for the upper triangle matrix.
        This corresponds to the number of terms in the objective function, excluding the shift.
        """

        # do we have a shift?
        if "" in self.objective.terms:
            return len(self.objective.terms) - 1
        else:
            return len(self.objective.terms)

    def getNnzFullMatrix(self):
        """
        Compute number of nonzeros of the full matrix.
        Instead of using an attribute for the nonzeros, we simply compute them on demand.
        """
        # first, get nnz of the upper triangle matrix, this is only the number of terms in the objective
        upper_triangle_nnz = self.getNNZUpperTriangle()
        # count linear terms to compute nnz of full matrix
        linear_terms = 0
        for term in self.objective.terms.values():
            if term.order() == 1:
                linear_terms += 1
        full_matrix_nnz = 2*upper_triangle_nnz - linear_terms

        return full_matrix_nnz

    @classmethod
    def readQUBO(cls, path : str):

        if path.endswith(".gz"):
            with gzip.open(path, 'rt') as f:
                qubo = cls._readQuboFile(f)
        else:
            with open(path, 'r') as f:
                qubo = cls._readQuboFile(f)

        return qubo


    @classmethod
    def _readQuboFile(cls, f):

        # check if sense is specified in first line
        first_line = f.readline().strip()
        if first_line in [sense.value for sense in HybridSolverOptSenses]:
            sense = HybridSolverOptSenses(first_line)
            num_terms = int(f.readline().strip())
        else:
            sense = HybridSolverOptSenses.MAXIMIZE # default
            num_terms = int(first_line)
        if num_terms != 1:
            raise Exception("Aggregated QUBOs are not supported...")
        weight = float(f.readline().strip())
        if weight != 1.0:
            raise Exception("Weighted QUBOs are not supported...")
        shift = float(f.readline().strip())

        nnz_string = f.readline().strip().split(" ")
        num_vars = int(nnz_string[0])
        num_nnz = int(nnz_string[1])

        # create variables
        qubo = QuboModel(sense)

        if shift != 0:
            qubo.objective += shift

        vars = []
        for ix in range(0, num_vars):
            vars.append(qubo.addVariable(f"x_{ix}"))

        # create terms
        term_ctr = 0
        check_symmetry = False
        lower_terms = []
        for line in f:
            split = line.split(" ")
            ix_i = int(split[0])
            ix_j = int(split[1])
            entry = float(split[2])

            if ix_i == ix_j:
                qubo.objective += entry * vars[ix_i]
            elif ix_i > ix_j:
                raise Exception("Invalid .qubo file, only upper triangular matrix can be stored")
            else:
                # since we only store the upper triangular matrix, we need to
                # make the entries in the lower triangular matrix explicit
                # through doubling the coefficient
                qubo.objective += 2.0 * entry * vars[ix_i] * vars[ix_j]

            term_ctr += 1


        if term_ctr != num_nnz:
            raise Exception("Invalid .qubo files, float of NNZ specified does not match NZ entries!")

        return qubo

    def __str__(self):
        return str(self.objective)

    def _solvePrep(self):

        # temporary folder for the QUBO problem
        tmp_path = tempfile.mkdtemp()
        tmp_problem = os.path.join(tmp_path, "pyclient.qubo")

        # convert problem into QUBO format (i.e. a matrix)
        self.writeQUBO(tmp_problem)

        return tmp_problem

    def _solveParse(self, solution):

        # parse solution, store assignments in variables
        sol_string_splitted = solution.split("\n")

        for var in self.vars:
            self.vars[var].assignment = int(sol_string_splitted[self.vars[var].id()])

    async def solveAsync(self, specs : dict, runner : Runner):

        tmp_problem = self._solvePrep()
        res = await runner.solveAsync(tmp_problem, specs)

        self._solveParse(res['solution_file'])

        # return (optimal) objective
        return self.eval()

    def solve(self, specs : dict, runner : Runner):

        tmp_problem = self._solvePrep()
        res = runner.solve(tmp_problem, specs)

        self._solveParse(res['solution_file'])

        # return (optimal) objective
        return self.eval()

    def __str__(self):
        return str(self.objective)