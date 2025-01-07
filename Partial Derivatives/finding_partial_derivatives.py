"""
Q) Partial derivatives for f(x, y): x**2 + y**2 + x*y
Compute ∂f/∂x and ∂f/∂y using sympy
"""

import sympy as sp

# define symbols
x, y = sp.symbols('x y')

# defining the function, f(x, y) = x**2 + y**2 + x*y
fn = x**2 + y**2 + x*y

# finind out partial derivatives
partial_derivated_of_x = sp.diff(fn, x)
partial_derivated_of_y = sp.diff(fn, y)

# printing the result:
print(f"∂f/∂x = {partial_derivated_of_x}")      # output: ∂f/∂x = 2*x + y
print(f"∂f/∂y = {partial_derivated_of_y}")      # output: ∂f/∂y = x + 2*y