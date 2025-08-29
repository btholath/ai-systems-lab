"""
Explanation
• 	Partial derivatives measure how the function changes as each variable changes independently.
• 	The gradient vector points in the direction of the steepest increase of the function.
• 	This is foundational in optimization, machine learning (e.g., gradient descent), and physics (e.g., force fields).
"""
import sympy as sp

# 🧮 Step 1: Declare symbolic variables
x, y = sp.symbols('x y')  # These represent the independent variables of the function

# 📐 Step 2: Define the multivariable function
f = x**2 + 3*y**2 - 4*x*y  # A quadratic function in terms of x and y

# 🔍 Step 3: Compute partial derivatives (i.e., gradients)
grad_x = sp.diff(f, x)  # Partial derivative with respect to x
grad_y = sp.diff(f, y)  # Partial derivative with respect to y

# 🧭 Step 4: Combine into gradient vector
gradient = [grad_x, grad_y]  # Represents the direction of steepest ascent

# 📤 Step 5: Display results
print("Gradient Vector ∇f(x, y):")
print("∂f/∂x =", grad_x)
print("∂f/∂y =", grad_y)
print("As a vector:", gradient)