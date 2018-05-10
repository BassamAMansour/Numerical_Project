import re
from math import sin

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from sympy import simplify

from equation_solvers.Root import Root

replacements = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

allowed_words = [
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp',
]


class Plotter:
    def __init__(self, equation, roots_list, mode):
        self.equation = equation
        self.mode = mode
        self.roots_list = roots_list
        self.modified_expression = self.compute_modified_expression()

    def compute_modified_expression(self):
        self.modified_expression = self.equation
        for word in re.findall('[a-zA-Z_]+', self.modified_expression):
            if word not in allowed_words:
                raise ValueError(
                    '"{}" is forbidden to use in math expression'.format(word)
                )

        for old, new in replacements.items():
            self.modified_expression = self.modified_expression.replace(old, new)
        x= 'x'
        return eval(self.modified_expression)


    def plot_equation(self):
        max = self.get_max_root()
        min = self.get_min_root()
        x = np.linspace(min, max, 100)

        fig, axis = plt.subplots()
        axis.plot(x, self.modified_expression)
        axis.grid()
        fig.savefig("test.png")
        plt.show()

    def get_max_root(self):
        max = self.roots_list[0].root
        for x in self.roots_list:
            if x.root > max:
                max = x.root

        return max

    def get_min_root(self):
        min = self.roots_list[0].root
        for x in self.roots_list:
            if x.root < min:
                min = x.root

        return min


equation = "sin(x)"
roots = [Root(-10, 0.001), Root(10, 0.0001)]
plot = Plotter(equation, roots, 0)
plot.plot_equation()
