from symtable import Symbol

import numpy
from sympy import Poly

from equation_solvers import FalsePosition
from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root
from equation_solvers.Secant import Secant


class General_Algorithm(EquationSolver):
    CONSTANT = 5
    equation = ""

    def __init__(self, max_iterations=EquationSolver.max_iterations,
                 precision=EquationSolver.precision):
        self.max_iterations = max_iterations
        self.precision = precision

    def solve_polynomial(self, equation, initial_1, initial_2):
        a = Poly(self.equation, Symbol("x"))
        length = len(a.coeffs()) - 1
        false_position = FalsePosition(equation, initial_1, initial_2, self.max_iterations,
                                       self.precision)
        self.add_root(Root(false_position.roots[-1], 0))
        if len(self.roots) < length:
            self.solve_polynomial()

        # interval = numpy.linspace(self.initial_1, self.initial_2, abs(self.initial_2 - self.initial_1) * self.CONSTANT,
        #                           True)
        # for i in range(len(interval) - 1):
        #     false_position = FalsePosition(equation, interval[i], interval[i + 1])
        #     if false_position.getRoot() is not None:
        #         self.roots.extend(false_position.roots)
        #     elif len(self.roots) < length:
        #         secant = Secant(equation, interval[i], interval[i + 1])
        #         secant.start_root_finding()
        #         self.roots.extend(secant.roots)roots
