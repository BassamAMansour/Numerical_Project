from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root


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
        self.getRoot()
    def getRoot(self):
        root = 0
        eq = 0
        first_iteration = True
        fxl = super().evaluate_equation(self.lower_bound)
        fxu = super().evaluate_equation(self.upper_bound)
        if fxl * fxu > 0 :
            print("no bracket")
            return 0

        for i in range(0, self.max_iterations):
            fxl = super().evaluate_equation(self.lower_bound)
            fxu = super().evaluate_equation(self.upper_bound)
            root = (self.lower_bound *fxu - self.upper_bound * fxl) / (fxu - fxl)
            if first_iteration:
                ea = None
            else:
                ea = abs((root - self.roots[-1].root)/ root)
            fxr = super().evaluate_equation(root)
            root1 = Root(0,0)
            root1.root = root
            root1.precision = ea
            self.add_root(root1)
            if fxr < 0 :
                self.lower_bound = root
            elif fxr > 0:
                self.upper_bound = root
            else :
                break
            if not first_iteration and ea <self.precision:
                break
            if first_iteration:
                first_iteration = False



        if i>= self.max_iterations:
            print("root not found to desired tolerance")
            self.root_found = False
            return root
        self.root_found = True
        return root

