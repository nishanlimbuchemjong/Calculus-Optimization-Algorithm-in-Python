"""
Implementation of Gradient Descent Optimization Algorithm in python
Q. Minimize the following function using Gradient Descent:f(x)=3x^2−12x+8
    Start with an initial guess of 𝑥=5, a learning rate of 0.1, and 50 iterations.

"""

def cost_function(x):
    return 3*x**2-12*x+8

def gradient(x):
    return 6*x-12

def gradient_descent(learning_rate, iter):
    x = 5

    for i in range(iter):
        grad = gradient(x)
        x = x - learning_rate * grad
        print(f"Iteration-{i+1}: x = {x:.4f}, f(x) = {cost_function(x): .4f}")
    return x

final_result = gradient_descent(0.1, 50)
print(f"Minumum point reached at x = {final_result:.4f}")