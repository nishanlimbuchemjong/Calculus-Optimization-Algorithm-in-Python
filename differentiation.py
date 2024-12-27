"""
Differentiate the following function with respect to x and y: g(x,y)=5xy^2+3y^3-4x^2y+2
"""
import sympy as sp

"""
sympy is installed to use SymPy library, which is designed for symbolic mathematics
> pip install sympy
"""

# defines the symbols
x, y = sp.symbols('x y')

g_x = 5*x*y**2 + 3*y**3 - 4*x**2*y + 2

# finding the derivative with respect to x and y respectively:
derivative_with_respect_x = sp.diff(g_x, x)
derivative_with_respect_y = sp.diff(g_x, y)

# printing the output of each derivatives:
print(f"Derivative of ({g_x}) with respect to x = {derivative_with_respect_x}")
print(f"Derivative of ({g_x}) with respect to y = {derivative_with_respect_y}")