"""
This code introduces basic matrix types used in math and machine learning:
• 	Identity matrix
• 	Diagonal matrix
• 	Zero matrix
These are foundational tools in linear algebra, which powers everything from neural networks to optimization algorithms.

 How These Are Used in Machine Learning

 Matrix Types:              Real-World ML Applications:
 ------------------        ----------------------------------------
 Identity Matrix           Keeps data unchanged during transformations, Initializing weights in neural networks
 Diagonal Matrix           Represnts scaling or feature weighting, Scaling features (e.g., normalizing data)
 Zero Matrix               Used to initialize models or rest gradients, Initializing weights or storing empty data

 

💡 Example in ML Context
Imagine you're building a neural network:
- You might start with a zero matrix to initialize weights.
- Use a diagonal matrix to scale features like age or income.
- Apply an identity matrix when you want to preserve structure during transformations.
Let me know if you'd like to visualize these matrices or simulate how they affect data in a neural network. I can scaffold that next.

"""
import numpy as np  # Import NumPy, a library that helps us work with numbers and matrices

# ----------------------------------------
# 🧮 Identity Matrix
# ----------------------------------------

# Create a 3x3 identity matrix
# An identity matrix has 1s on the diagonal and 0s everywhere else
# It's like the "do nothing" matrix—multiplying by it keeps things the same
I = np.eye(3)

# Create a 3x3 matrix A with numbers from 1 to 9
A = np.array([
    [1, 2, 3],  # Row 1
    [4, 5, 6],  # Row 2
    [7, 8, 9]   # Row 3
])

# Multiply matrix A by the identity matrix I
# This should return A itself, because identity matrix doesn't change the values
# Uncomment the line below to see the result
print("A × I:\n", np.dot(A, I))

# ----------------------------------------
# 📐 Diagonal Matrix
# ----------------------------------------

# Create a diagonal matrix with values 1, 7, and 9 on the diagonal
# All other positions are 0
D = np.diag([1, 7, 9])
print("Diagonal Matrix:\n", D)

# ----------------------------------------
# 🧱 Zero Matrix
# ----------------------------------------

# Create a 3x3 matrix filled entirely with zeros
# This is often used to initialize weights or store empty data
Z = np.zeros((3, 3))
print("Zero Matrix:\n", Z)