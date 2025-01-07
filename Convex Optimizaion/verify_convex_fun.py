# Q) Verify if a function f(x)=4x^2+2x+3 is convex using the second derivative test.

import sympy as sp

# defining the symbols using sp.symbols()
x, a, b, c = sp.symbols('x a b c')

# defining the function
fun = 4*x**2 + 2*x + 3

# finding out the second derivative of given function
second_derivatives = sp.diff(fun, x, 2)

# checking whether the value of second derivative is greater or less than 0 to determine convex function
if second_derivatives > 0:
    print(f"The function is convex because f''(x) > 0")
else:
    print(f"The function is convex because f''(x) < 0")