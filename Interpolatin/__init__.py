from sympy import simplify

from Interpolatin.Newton import Newton

pointsX = [2,4.25,5.25,7081,9.2,10.6]
pointsY = [7.2,7.1,6.0,5.0,3.5,5.0]
interpolation = Newton(pointsX, pointsY)
fn = interpolation.get_function()
fn = simplify(str(fn))
