from equation_solvers.EquationSolver import EquationSolver


class NewtonRaphson(EquationSolver):

    # Add suitable args
    def __init__(self, equation):
        super().__init__(equation)


    def get_root(self,initial):
        last_root=0
        current_root=0
        derivative = self.get_derivative(self.equation)
        if derivative == 0 :
            self.root_found = False
            return None
        last_root = initial
        for i in range (0, self.max_iterations):
            current_root = last_root - (self.evaluate_equation(last_root)/ self.get_first_derivative(last_root))


