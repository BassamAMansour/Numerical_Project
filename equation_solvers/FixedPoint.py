from equation_solvers.EquationSolver import EquationSolver


class FixedPoint(EquationSolver):
    current_iteration = 0
    current_precision = 0

    # Add suitable args
    def __init__(self, equation):
        super().__init__(equation)
        self.equation = equation + "x"

    def next_iteration(self):
        self.add_root(self, self.current_root)
        old_root = self.current_root
        self.current_root = self.evaluate_equation(self.equation, self.current_root)
        self.current_precision = (self.current_root - old_root) / self.current_root

    def get_root(self):
        while (self.current_iteration < self.max_iterations &
               self.current_precision > self.precision):
            self.next_iteration()
