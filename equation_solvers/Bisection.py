from equation_solvers.EquationSolver import EquationSolver


class Bisection(EquationSolver):
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


    def get_root(self):
        root = 0
        fxl = super().evaluate_equation(super().equation , self.lower_bound)
        fxu = super().evaluate_equation(super().equation , self.upper_bound)
        if fxl * fxu > 0 :
            print("no bracket")
            # what to return if no bracket
            return None
        for i in range (1 , self.max_iterations):

            root = (self.lower_bound +self.upper_bound)/2
            ea = abs((self.upper_bound - self.lower_bound)/ self.lower_bound)
            check = super().evaluate_equation(super().evaluate_equation(), self.lower_bound) *super().evaluate_equation(super().evaluate_equation(), root)

            if check < 0 :
                self.upper_bound = root
            elif check > 0 :
                self.lower_bound = root
            else:
                ea = 0

            if ea < self.precision :
                break
        if i>= self.max_iterations:
            print("root not found to desired tolerance")
            #return what if it exceded the desired tolerance
            return None
        return root
