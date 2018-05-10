from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root


class NewtonRaphson(EquationSolver):

    # Add suitable args
    def __init__(self, equation , initial):
        super().__init__(equation)
        self.get_root(initial)


    def get_root(self,initial):
        last_root=0
        current_root=0
        derivative = self.get_first_derivative(self.equation,initial)
        if derivative == 0 :
            self.root_found = False
            return None
        last_root = initial
        root = Root(0,0)
        root.root = last_root
        root.precision = None
        self.add_root(root)
        for i in range (0, self.max_iterations):
            current_root = last_root - (self.evaluate_equation(last_root)/ self.get_first_derivative(self.equation , last_root))
            ea = self.calculate_precision(last_root ,current_root)
            root = Root(0,0)
            root.root = current_root
            root.precision = ea
            self.add_root(root)
            if ea < self.precision:
                break
            last_root = current_root

        if i >= self.max_iterations:
            self.root_found = False
            return None

        self.root_found = True
        return current_root


