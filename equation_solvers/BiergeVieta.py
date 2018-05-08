from sympy import Poly, Symbol

from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root


class BiergeVieta(EquationSolver):

    # Add suitable args
    def __init__(self, equation, x_0):
        super().__init__(equation)
        self.x_0 = x_0
        a = self.get_coeffs()
        n = len(a) - 1
        b = [0] * (n + 1)
        c = [0] * (n + 1)
        d = [0] * (n + 1)

        b[0] = a[0]
        c[0] = a[0]
        for i in range(1, n + 1, 1):
            b[i] = (x_0 * b[i - 1] + a[i])
        for i in range(1, n, 1):
            c[i] = (x_0 * c[i - 1] + b[i])
        r = x_0 - (b[n] / c[n-1])
        ea = abs((r - x_0) / r)
        self.add_root(Root(r, ea))
        x_0 = r
        while not (ea < self.precision):
            for i in range(1, n + 1, 1):
                b[i] = (x_0 * b[i - 1] + a[i])
            for i in range(1, n, 1):
                c[i] = (x_0 * c[i - 1] + b[i])
            r = x_0 - (b[n] / c[n - 1])
            ea = abs((r - x_0) / r)
            self.add_root(Root(r, ea))
            x_0 = r

    def get_coeffs(self):
        x = Symbol("x")
        a = Poly(self.equation, x)
        l = a.coeffs()
        return l



