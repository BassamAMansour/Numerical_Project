from equation_solvers.EquationSolver import EquationSolver
from equation_solvers.Root import Root


class Bisection(EquationSolver):
    upper_bound = 0.0
    lower_bound = 0.0

    DEFAULT_INITIAL_LOWER_BOUND = 0
    DEFAULT_INITIAL_UPPER_BOUND = 1000000

    # Add suitable args
    def __init__(self, equation, initial_lower_bound=DEFAULT_INITIAL_LOWER_BOUND,
                 initial_upper_bound=DEFAULT_INITIAL_UPPER_BOUND):
        super().__init__(equation)
        self.lower_bound = initial_lower_bound
        self.upper_bound = initial_upper_bound
        self.get_root()

    def get_root(self):
        root = 0
        first_iteration = True
        ea= 0
        fxl = super().evaluate_equation( self.lower_bound)
        fxu = super().evaluate_equation(self.upper_bound)
        if fxl * fxu > 0 :
            print("no bracket")
            return None
        for i in range (1 , self.max_iterations):
            root = (self.lower_bound +self.upper_bound)/2
            if first_iteration:
                ea = None
            else:
                ea = abs((root - self.roots[-1].root)/ root)
            check = super().evaluate_equation(self.lower_bound) *super().evaluate_equation(root)
            if check < 0 :
                self.upper_bound = root
            elif check > 0 :
                self.lower_bound = root
            else:
                ea = 0
            root1 = Root(0,0)
            root1.root = root
            root1.precision = ea
            self.add_root(root1)
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
