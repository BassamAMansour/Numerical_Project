from equation_solvers.EquationSolver import EquationSolver


class NewtonRaphson(EquationSolver):

    # Add suitable args
    def __init__(self, equation):
        super().__init__(equation)


    def get_root(self,initial):
        derivative = self.get_derivative(self.equation)
        if derivative == 0 :

            return None
        root = initial - (se)

