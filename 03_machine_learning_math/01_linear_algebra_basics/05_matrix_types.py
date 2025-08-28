"""
This script shows how to:
• 	Create and manipulate matrices
• 	Perform matrix arithmetic
• 	Understand special matrices like identity, zero, and diagonal matrices
These operations are the building blocks of machine learning models, especially in areas like linear regression, neural networks, and image processing.
"""
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# print("Addition: \n", A + B)
# print("Subtraction: \n", B - A)

C = 2 * A
# print("Scalar Multiplication \n", C)

result = np.dot(A, B)

# print("Matrix Multiplication \n", result)

I = np.eye(5)
# print("Identity Matrix \n", I)

Z = np.zeros((2, 3))
# print("Zero Matrix \n", Z)

D = np.diag([1, 2, 3])
print("Diagonal Matrix\n", D)


