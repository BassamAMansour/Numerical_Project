from equation_solvers.EquationSolver import EquationSolver


class BiergeVieta(EquationSolver):


    def getCoeffecients(equation):
        coeff = []
        return coeff

    # Add suitable args
    def __init__(self, initialValue, equation):
        super().__init__(equation)
        coef = self.getCoeffecients(equation)

