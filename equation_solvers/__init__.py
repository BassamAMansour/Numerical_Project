from sympy import simplify, Poly, Symbol

from equation_solvers.Bisection import Bisection
from equation_solvers.FalsePosition import FalsePosition
from equation_solvers.FixedPoint import FixedPoint
from equation_solvers.General_Algorithm import General_Algorithm
from equation_solvers.NewtonRaphson import NewtonRaphson

z = FixedPoint("2*x*(1-x) - x",0.1)
equation = "x**3 -4*x"
general = General_Algorithm(equation)
general.solve_polynomial(-1, 3)
print(general.roots)
print("")
