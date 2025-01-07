# Q) Solve the integral of a sine wave sine(pi) over [0, pi]

import math

# defining a function that returns indefine integrals
def indefine_integrals(x):
    return -math.cos(x)

# definding a function that calculate the integrals
def calculate_integrals(x1, x2):
    integral_of_x1 = indefine_integrals(x1)
    integral_of_x2 = indefine_integrals(x2)
    return integral_of_x2 - integral_of_x1

# initializing the upper and lower limit
x1 = 0
x2 = math.pi

# calling the calculate_integrals() function 
result = calculate_integrals(x1, x2)

# printing the result
print(f"Result: {result}")      # output: Result: 2.0