from sympy import simplify

from equation_solvers.Bisection import Bisection
from equation_solvers.FalsePosition import FalsePosition
from equation_solvers.FixedPoint import FixedPoint
from equation_solvers.NewtonRaphson import NewtonRaphson

z = FixedPoint("2*x*(1-x) - x",0.1)
