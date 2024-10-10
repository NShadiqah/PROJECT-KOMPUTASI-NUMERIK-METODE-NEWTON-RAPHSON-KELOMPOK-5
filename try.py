import matplotlib.pyplot as plt
import numpy as np

def function(x):
    """
    Calculates the value of the function f(x) = x^2 - 2.

    Args:
        x (float): Input value.

    Returns:
        float: The calculated value of f(x).
    """
    return x**2 - 2

def derivative(x):
    """
    Calculates the derivative of the function f(x) = x^2 - 2, which is 2x.

    Args:
        x (float): Input value.

    Returns:
        float: The derivative of f(x) at x.
    """
    return 2*x

def newton_raphson(function, derivative, x0, tol=1e-6, max_iter=100):
    """
    Implements the Newton-Raphson method to find the root of a function.

    Args:
        function (callable): The function for which to find the root.
        derivative (callable): The derivative of the function.
        x0 (float): The initial guess for the root.
        tol (float, optional): The tolerance for convergence. Defaults to 1e-6.
        max_iter (int, optional): The maximum number of iterations allowed. Defaults to 100.

    Returns:
        float or None: The approximate root of the function, or None if convergence fails.
    """

    x1 = x0
    print("Iteration\tx0\t\tfunction(x0)")

    for k in range(1, max_iter + 1):
        try:
            # Calculate the next approximation using the Newton-Raphson formula
            x1 = x0 - function(x0) / derivative(x0)

            # Check for convergence using both absolute and relative error
            if abs(x1 - x0) <= tol and abs((x1 - x0) / x0) <= tol:
                # Print the final iteration if convergence is achieved
                print(f"x{k}\t{x1:.6e}\t{function(x1):.6e}")
                plt.plot(x0, function(x0), 'or')
                return x1

            # Update x0 for the next iteration
            x0 = x1

            # Print the current iteration details
            print(f"x{k}\t{x1:.6e}\t{function(x1):.6e}")
            plt.plot(x0, function(x0), 'or')

        except ZeroDivisionError:
            print(f"Iteration {k}: Division by zero encountered. Aborting.")
            return None

    # If the loop completes without convergence, print an error message
    print("ERROR: Maximum iterations reached without convergence.")
    return None

# Find the approximate root of the function f(x) = x^2 - 2
x_root = newton_raphson(function, derivative, 1.7)

if x_root is not None:
    print(f"The approximate root of the equation f(x) = 0 is: {x_root:.6e}")
else:
    print("Root not found using Newton-Raphson method.")

# Plotting configuration
u = np.arange(1.0, 2.0, 0.0001)  # Setting up values for x in the plot
w = u**2 - 2  # Define the main function again

plt.plot(u, w, label='f(x) = x^2 - 2')  # Label the plotted function
plt.axhline(y=0.0, color='black', linestyle='-', label='y = 0')  # Add label for x-axis
plt.title('Newton-Raphson Graphics for y = x^2 - 2')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()  # Include legend for all plotted lines
plt.show()