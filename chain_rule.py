"""
Given the following parametric equations:
    x(t) = 2t^3 + 5t^2 -3t + 1
    y(t) = 4t^2 - 7t + 2
    Find dy/dx using the chain rule.
"""

import sympy as sp

t = sp.symbols('t')

x_t = 2*t**3 + 5*t**2 - 3*t + 1
y_t = 4*t**2 - 7*t + 2

derivative_xt_with_respect_t = sp.diff(x_t, t)
derivative_yt_with_respect_t = sp.diff(y_t, t)

"""
chain rule:
    dy/dx = (dy/dt) / (dx/dt)
"""
res = derivative_yt_with_respect_t/derivative_xt_with_respect_t     
print(f"Derivative of dy/dx = {res}")