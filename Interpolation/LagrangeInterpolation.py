import string

from sympy import simplify





class LagrangeInterpolation :



    def getFunction(self ,points, functions):
        equation = ""
        for i in range(len(points)):
            sub_equation = "1"
            for j in range(len(points)):
                if i != j:
                    x = points[j]
                    y = points[i]
                    sub_equation += " * ((x - " + str(x) + ")/(" + str(y) + " - " + str(x) + "))"
                    sub_equation = str(sub_equation)
            sub_equation += "* " + str(functions[i])
            equation += "+"+ str(sub_equation)
        return equation
