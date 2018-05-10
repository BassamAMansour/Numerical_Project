from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root


class FixedPoint(EquationSolver):
    UPPER_BOUND = 1000000

    # Add suitable args
    def __init__(self, equation, intial_root):
        super().__init__(equation)
        self.equation = equation + "+ x"
        self.get_root(intial_root)

    def get_root(self, intial_root):
        diverge = False
        converge = abs(self.get_first_derivative(self.equation, intial_root))
        if converge > 1:
            diverge = True
        current_iteration = 0
        self.roots.append(Root(intial_root, self.UPPER_BOUND))
        while (current_iteration < self.max_iterations and
               self.roots[-1].precision > self.precision):
            old_root = self.roots[-1]
            current_root = Root(0, 0)
            current_root.root = self.evaluate_equation(old_root.root)
            current_root.precision = self.calculate_precision(old_root.root, current_root.root)
            self.add_root(current_root)
            current_iteration += 1

        if current_root.precision <= self.precision:
            self.root_found = True




