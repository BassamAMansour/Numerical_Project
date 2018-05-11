from symtable import Symbol

import numpy
from sympy import Poly, simplify

from equation_solvers import FalsePosition
from equation_solvers.Bisection import Bisection
from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root
from equation_solvers.Secant import Secant


class General_Algorithm(EquationSolver):
    CONSTANT = 3
    equation = ""
    length = 0
    initial_1 = None
    initial_2 = None

    def __init__(self, equation, max_iterations=EquationSolver.DEFAULT_MAX_ITERATIONS,
                 precision=EquationSolver.DEFAULT_EPSILON):
        super().__init__(equation)
        self.max_iterations = max_iterations
        self.precision = precision
        self.equation = equation

    def solve_equation(self, initial_1, initial_2):
        self.initial_1 = initial_1
        self.initial_2 = initial_2
        difference = abs(self.initial_2 - self.initial_1)
        while difference < 1:
            difference *= 10
        interval = numpy.linspace(self.initial_1, self.initial_2, difference * self.CONSTANT, True)
        for i in range(0, len(interval) - 1):
            bisection_method = Bisection(self.equation, interval[i], interval[i + 1])
            root = bisection_method.get_root()
            if root is not None:
                if bisection_method.root_found :
                    root = bisection_method.roots[-1]
                if not self.exist(root):
                    self.add_root(root)



    def exist(self, root: Root):
        for i in range(len(self.roots)):
            if abs(root.root - self.roots[i].root) < EquationSolver.DEFAULT_EPSILON :
                return True
        return False

# false_position = FalsePosition(self.equation, initial_1, initial_2, self.max_iterations,
#                                self.precision)
# last_root = false_position.getRoot()
# if last_root is None:
#     secant = Secant(self.equation, initial_1, initial_2, self.max_iterations, self.precision)
#     secant.start_root_finding()
#     last_root = secant.roots[-1]
# else:
#     last_root = false_position.roots[-1]
# if not self.exist(last_root):
#     self.add_root(last_root)
# if abs(initial_2 - initial_1) > .1:
#     self.solve_polynomial(initial_1, last_root.root - EquationSolver.DEFAULT_EPSILON)
#     self.solve_polynomial(last_root.root + EquationSolver.DEFAULT_EPSILON, initial_2)
