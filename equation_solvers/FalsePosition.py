from equation_solvers.EquationSolver import EquationSolver


class FalsePosition(EquationSolver):
    upper_bound: float
    lower_bound: float

    DEFAULT_INITIAL_LOWER_BOUND = 0
    DEFAULT_INITIAL_UPPER_BOUND = 1000000

    # Add suitable args
    def __init__(self, equation, initial_lower_bound=DEFAULT_INITIAL_LOWER_BOUND,
                 initial_upper_bound=DEFAULT_INITIAL_UPPER_BOUND):
        super().__init__(equation)
        self.lower_bound = initial_lower_bound
        self.upper_bound = initial_upper_bound

    def getRoot(self):
        root = 0
        fxl = super().evaluate_equation(super().equation, self.lower_bound)
        fxu = super().evaluate_equation(super().equation, self.upper_bound)
        if fxl * fxu > 0 :
            print("no bracket")
            # what to return if no bracket
            return 0

        for i in range(0, self.max_iterations):
            fxl = super().evaluate_equation(super().equation, self.lower_bound)
            fxu = super().evaluate_equation(super().equation, self.upper_bound)
            root = (self.lower_bound *fxu - self.upper_bound * fxl) / (fxu - fxl)
            fxr = super().evaluate_equation(super().equation, root)
            if fxr < 0 :
                self.lower_bound = root
            elif fxr > 0:
                self.upper_bound = root
            else :
                print("root found :" + root)
                return root

