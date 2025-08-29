import sympy as sp  # SymPy is a Python library for symbolic math (like algebra and calculus)

# ----------------------------------------
# 🧮 STEP 1: Define a Mathematical Function
# ----------------------------------------

# Create a symbolic variable 'x' — like saying "let x be a variable"
x = sp.Symbol('x')

# Define a function f(x) = x³ - 5x + 7
# This is a simple polynomial function
f = x**3 - 5*x + 7

# ----------------------------------------
# 📐 STEP 2: Compute the Derivative of the Function
# ----------------------------------------

# The derivative tells us how the function changes — its slope at any point
# In machine learning, derivatives are used to optimize models (e.g., gradient descent)
derivative = sp.diff(f, x)

# ----------------------------------------
# 📊 STEP 3: Display the Results
# ----------------------------------------

print("Function f(x):", f)
print("Derivative f'(x):", derivative)

"""
### 🧠 Why This Matters in Machine Learning

| Concept     | ML Relevance                                 |
|-------------|----------------------------------------------|
| Function    | Represents a model or cost function          |
| Derivative  | Tells us how to adjust parameters to improve |
| SymPy       | Useful for symbolic math, prototyping logic |

---

### 💡 Example in ML Context

In gradient descent, we often compute the derivative of a **loss function** to figure out:
- Which direction to move
- How fast to update weights

This symbolic derivative is the foundation of how models learn.

"""

