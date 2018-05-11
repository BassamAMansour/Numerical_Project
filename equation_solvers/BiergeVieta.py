from sympy import Poly, Symbol

from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root


class BiergeVieta(EquationSolver):
    x_0 = 0

    # Add suitable args
    def __init__(self, equation,x_0, max_iterations = EquationSolver.DEFAULT_MAX_ITERATIONS , precision = EquationSolver.DEFAULT_EPSILON ):
        super().__init__(equation)
        self.x_0 = x_0
        self.max_iterations = max_iterations
        self.precision = precision


    def get_root(self):
        a = self.get_coeffs()
        n = len(a) - 1
        b = [0] * (n + 1)
        c = [0] * (n + 1)
        d = [0] * (n + 1)

        b[0] = a[0]
        c[0] = a[0]
        current_Iteration = 0
        for i in range(1, n + 1, 1):
            b[i] = (self.x_0 * b[i - 1] + a[i])
        for i in range(1, n, 1):
            c[i] = (self.x_0 * c[i - 1] + b[i])
        r = self.x_0 - (b[n] / c[n-1])
        ea = abs((r - self.x_0) / r)
        self.add_root(Root(r, ea))
        self.x_0 = r
        while not (ea < self.precision or current_Iteration >= self.max_iterations ):
            for i in range(1, n + 1, 1):
                b[i] = (self.x_0 * b[i - 1] + a[i])
            for i in range(1, n, 1):
                c[i] = (self.x_0 * c[i - 1] + b[i])
            r = self.x_0 - (b[n] / c[n - 1])
            ea = abs((r - self.x_0) / r)
            self.add_root(Root(r, ea))
            self.x_0 = r
            current_Iteration += 1

    def get_coeffs(self):
        x = Symbol("x")
        a = Poly(self.equation, x)
        l = a.coeffs()
        return l



