import re
from math import sin

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from sympy import simplify

from equation_solvers.Root import Root
from equation_solvers.Secant import Secant

replacements = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'tan': 'np.tan',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
    'log': 'np.log'
}

allowed_words = [
    'x',
    'sin',
    'cos',
    'tan',
    'sqrt',
    'exp',
    'log'
]

MODE_SLOW = 1
MODE_FAST = 0
DEFAULT_MODE = MODE_FAST
HORIZONTAL_PADDING = 1.1


class Plotter:
    def __init__(self, equation: str, roots_list: list, mode):
        print(mode)
        self.mode = DEFAULT_MODE
        print(self.mode)
        self.equation = equation
        self.mode = mode
        print(self.mode)
        self.roots_list = roots_list
        self.modified_expression = self.compute_modified_expression()

    def compute_modified_expression(self):
        modified_expression = self.equation
        for word in re.findall('[a-zA-Z_]+', modified_expression):
            if word not in allowed_words:
                raise ValueError(
                    '"{}" is forbidden to use in math expression'.format(word)
                )

        for old, new in replacements.items():
            modified_expression = modified_expression.replace(old, new)

        return modified_expression

    def plot_equation(self):
        max = self.get_max_root()
        min = self.get_min_root()
        max = max +((min+max)/2)

        x = np.linspace(int(min * HORIZONTAL_PADDING), int(max * HORIZONTAL_PADDING), 500)
        y = eval(self.modified_expression)

        if self.mode == MODE_SLOW:
            self.plot_graph_in_slow_mode(x, y)
        else:
            self.plot_graph_in_fast_mode(x, y)

    def plot_graph_in_fast_mode(self, x, y):
        equation_line, = plt.plot(x, y)

        precision = self.roots_list[-1].precision

        plt.title(
            "Equation: " + self.equation.__str__() + "\n" +
            "Root = " + self.roots_list[-1].root.__str__() + "\n" +
            "Ea = " + precision.__str__() + "%" + " | " +
            "Iteration = " + self.roots_list.__len__().__str__())

        plt.axvline(x=self.roots_list[-1].root)
        plt.axhline(y=0)
        plt.grid()
        plt.legend()
        plt.show()

    def plot_graph_in_slow_mode(self, x, y):
        self.current_root_index = 0
        for root in self.roots_list:
            figure = plt.figure()
            figure.canvas.mpl_connect('button_press_event', self.on_click)
            self.x = x
            self.y = y
            plt.plot()
            equation_line, = plt.plot(x, y)
            precision = root.precision
            if not (precision is None):
                precision = precision * 100
            plt.title(
                "Equation: " + self.equation.__str__() + "\n" +
                "Root = " + root.root.__str__() + "\n" +
                "Ea = " + precision.__str__() + "%" + " | " +
                "Iteration = " + str(self.current_root_index + 1))
            plt.axvline(x=root.root)
            plt.axhline(y=0)
            plt.grid()
            plt.show()
            figure.savefig("root" +str(self.current_root_index)+ ".png")
            self.current_root_index +=1

    def on_click(self, event):
        event.canvas.figure.clear()
        current_canvas = event.canvas.figure.gca()

        self.current_root_index += 1
        if self.current_root_index >= self.roots_list.__len__():
            self.current_root_index = 0

        equation_line, = plt.plot(self.x, self.y)

        precision = self.roots_list[self.current_root_index].precision
        if not (precision is None):
            precision = precision * 100

        plt.title(
            "Equation: " + self.equation.__str__() + "\n" +
            "Root = " + self.roots_list[self.current_root_index].root.__str__() + "\n" +
            "Ea = " + precision.__str__() + "%" + " | " +
            "Iteration = " + str(self.current_root_index + 1))

        current_canvas.axvline(x=self.roots_list[self.current_root_index].root)
        current_canvas.axhline(y=0)
        current_canvas.grid()

        event.canvas.draw()

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


# equation = "exp(x)-x"
# secant = Secant(equation, 0, 1)
# roots = secant.roots
# plot = Plotter(equation, roots, 0)
# plot.plot_equation()
