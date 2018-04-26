class EquationSolver:
    precision: float
    max_iterations: int
    equation: str
    current_root: float

    DEFAULT_MAX_ITERATIONS = 50
    DEFAULT_EPSILON = 0.0001

    @staticmethod
    def get_derivative(equation: str) -> str:
        """TODO: Get derivative"""
        pass

    @staticmethod
    def evaluate_equation(equation, value_to_substitute) -> float:
        """TODO: Evaluate the function"""
        pass

    def __init__(self, equation, max_iterations=DEFAULT_MAX_ITERATIONS, precision=DEFAULT_EPSILON):
        self.equation = equation
        self.max_iterations = max_iterations
        self.precision = precision
        self.roots = []

    def next_iteration(self) -> bool:
        """TODO: Get the next step in the iteration"""
        pass

    def add_root(self, new_root):
        self.roots.append(new_root)

    def delete_root(self, root_to_delete):
        self.roots.remove(root_to_delete)

    @property
    def max_iterations(self):
        return self._max_iterations

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        if max_iterations > 0:
            self._max_iterations = max_iterations
        else:
            self._max_iterations = self.DEFAULT_MAX_ITERATIONS

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, precision):
        if precision > 0:
            self._precision = precision
        else:
            self._precision = self.DEFAULT_EPSILON
