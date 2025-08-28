"""
This script shows how to:
• 	Create and manipulate matrices
• 	Perform matrix arithmetic
• 	Understand special matrices like identity, zero, and diagonal matrices
These operations are the building blocks of machine learning models, especially in areas like linear regression, neural networks, and image processing.
"""
import numpy as np  # Load NumPy, a powerful math library for working with arrays and matrices

# ----------------------------------------
# 🧮 Create Two Matrices A and B
# ----------------------------------------

# Matrix A: 2 rows, 2 columns
A = np.array([
    [1, 2],
    [3, 4]
])

# Matrix B: same shape as A
B = np.array([
    [5, 6],
    [7, 8]
])

# ----------------------------------------
# ➕ Matrix Addition
# ----------------------------------------

# Adds corresponding elements from A and B
# Example: (1+5), (2+6), etc.
print("Addition: \n", A + B)

# ----------------------------------------
# ➖ Matrix Subtraction
# ----------------------------------------

# Subtracts elements of A from B
# Example: (5-1), (6-2), etc.
print("Subtraction: \n", B - A)

# ----------------------------------------
# ✖️ Scalar Multiplication
# ----------------------------------------

# Multiply every element in A by 2
# This is like scaling the matrix
C = 2 * A
print("Scalar Multiplication \n", C)

# ----------------------------------------
# 🔁 Matrix Multiplication
# ----------------------------------------

# Multiply A and B using dot product
# This is NOT element-wise—it combines rows and columns
result = np.dot(A, B)
print("Matrix Multiplication \n", result)

# ----------------------------------------
# 🆔 Identity Matrix
# ----------------------------------------

# Create a 5x5 identity matrix
# It has 1s on the diagonal and 0s elsewhere
# Used to preserve values during multiplication
I = np.eye(5)
print("Identity Matrix \n", I)

# ----------------------------------------
# 🧱 Zero Matrix
# ----------------------------------------

# Create a 2x3 matrix filled with zeros
# Often used to initialize weights or placeholders
Z = np.zeros((2, 3))
print("Zero Matrix \n", Z)

# ----------------------------------------
# 📐 Diagonal Matrix
# ----------------------------------------

# Create a 3x3 matrix with values only on the diagonal
# All other elements are 0
D = np.diag([1, 2, 3])
print("Diagonal Matrix\n", D)