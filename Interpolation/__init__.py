import numpy as np
from sympy import simplify, Symbol, Poly

from Interpolation.LagrangeInterpolation import LagrangeInterpolation

# points = [10, 15, 20, 22.5]
# functions = [227.04, 362.78, 517.35, 602.97]
# interpolation = LagrangeInterpolation()
# string = interpolation.getFunction(points, functions)
# print(string)
string = '2*x**2 + 3*x - 2'
a = Poly(string , Symbol("x"))

# reader = Reader()
# reader.read("C:\\Users\\HP\\Desktop\\test_file.txt")
# print(reader.operation)
# print(reader.equation)
# print(reader.initial_1)
# print(reader.initial_2)
# print(reader.tolerance)
# print(reader.max_iterations)
# x = numpy.linspace(0, 2, abs(2 - 0) * 5, True)
# print(x)
