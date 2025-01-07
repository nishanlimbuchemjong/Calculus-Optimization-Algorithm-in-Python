# Q) Optimize f(x)=x^4−4x^2+3 and check if it’s convex using the Hessian matrix.

import sympy as sp

# defining symbols
x = sp.symbols('x')

# defining function:
f = x**4 -4*x**2 +3

# calculating first derivative
fst_derivative = sp.diff(f, x)

print(fst_derivative)
# calculating second derivative
snd_derivative = sp.diff(fst_derivative, x)
print(snd_derivative)

# solve the second derivatives
critical_points = sp.solve(snd_derivative, x)
print(critical_points)

values = [snd_derivative.subs(x, point) for point in critical_points]
print(values)

