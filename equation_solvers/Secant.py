from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root


class Secant(EquationSolver):
    DEFAULT_FIRST_INITIAL_POINT = -1
    DEFAULT_SECOND_INITIAL_POINT = 0

    def __init__(self, equation, first_initial_point=DEFAULT_FIRST_INITIAL_POINT,
                 second_initial_point=DEFAULT_SECOND_INITIAL_POINT):
        super().__init__(equation)
        self.first_initial_point = first_initial_point
        self.second_initial_point = second_initial_point
        self.start_root_finding()

    def start_root_finding(self):

        self.add_root(Root(self.calculate_root(self.first_initial_point, self.second_initial_point), None))

        old_root = self.second_initial_point
        current_root = self.roots[-1].root
        new_root = self.calculate_root(old_root, current_root)
        new_precision = self.calculate_precision(current_root, new_root)

        self.add_root(Root(new_root, new_precision))

        if self.roots[-1].precision <= self.precision:
            self.root_found = True

        else:
            counter = 2

            while self.roots[-1].precision > self.precision and counter <= self.max_iterations:
                old_root = self.roots[-2].root
                current_root = self.roots[-1].root
                new_root = self.calculate_root(old_root, current_root)
                new_precision = self.calculate_precision(current_root, new_root)

                self.add_root(Root(new_root, new_precision))

            if self.roots[-1].precision <= self.precision:
                self.root_found = True

    def calculate_root(self, old_root, new_root) -> float:
        old_value = self.evaluate_equation(old_root)
        new_value = self.evaluate_equation(new_root)
        return (new_root - (new_value * ((new_root - old_root) / (
                new_value - old_value))))


secant = Secant("exp(-x) - x", 0, 1)
secant.precision = 0.0000001
print(secant.roots)
