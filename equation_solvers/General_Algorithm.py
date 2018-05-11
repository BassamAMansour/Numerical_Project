from symtable import Symbol

import numpy
from sympy import Poly, simplify

from equation_solvers import FalsePosition
from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root
from equation_solvers.Secant import Secant


class General_Algorithm(EquationSolver):
    CONSTANT = 5
    equation = ""
    length = 0

    def __init__(self, equation, max_iterations=EquationSolver.DEFAULT_MAX_ITERATIONS,
                 precision=EquationSolver.DEFAULT_EPSILON):
        super().__init__(equation)
        self.max_iterations = max_iterations
        self.precision = precision
        self.equation = equation

    def solve_polynomial(self, initial_1, initial_2):

        false_position = FalsePosition(self.equation, initial_1, initial_2, self.max_iterations,
                                       self.precision)
        last_root = false_position.getRoot()
        if last_root is None:
            secant = Secant(self.equation, initial_1, initial_2, self.max_iterations, self.precision)
            secant.start_root_finding()
            last_root = secant.roots[-1]
        if not self.exist(last_root):
            self.add_root(last_root)
        if abs(initial_2 - initial_1) > EquationSolver.DEFAULT_EPSILON:
            self.solve_polynomial(initial_1, last_root.root - EquationSolver.DEFAULT_EPSILON)
            self.solve_polynomial(last_root.root + EquationSolver.DEFAULT_EPSILON, initial_2)

    # interval = numpy.linspace(self.initial_1, self.initial_2, abs(self.initial_2 - self.initial_1) * self.CONSTANT,
    #                           True)
    # for i in range(len(interval) - 1):
    #     false_position = FalsePosition(equation, interval[i], interval[i + 1])
    #     if false_position.getRoot() is not None:
    #         self.roots.extend(false_position.roots)
    #     elif len(self.roots) < length:
    #         secant.start_root_finding()
    #         self.roots.extend(secant.roots)roots
    def exist(self, root: Root):
        for i in range(len(self.roots)):
            if abs(root.root - self.roots[i].root) < EquationSolver.DEFAULT_EPSILON:
                return True
        return False
