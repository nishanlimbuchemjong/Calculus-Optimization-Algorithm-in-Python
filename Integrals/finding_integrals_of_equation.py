# Q) Compute the definite integral of a quadratic function f(x) = ax^2 + bx + c , over a given interval.

# a function to calculate indefine integrals
def indefine_integrals(a, b, c, x):
    return (a/3)*x**3 + (b/2)*x**2 + c*x

# a function to calculate the integrals
def calculate_integrals(a, b, c, x1, x2):
    integral_at_x2 = indefine_integrals(a, b, c, x2)
    integral_at_x1 = indefine_integrals(a, b, c, x1)

    return integral_at_x2 - integral_at_x1


# initializing the values:
a, b, c, x1, x2 = (2, 3, 4, 1, 3)

# calculating the integrals of the given function
result = calculate_integrals(a, b, c, x1, x2)

print(f"Result = {result:.3f}")     # output: Result = 37.333