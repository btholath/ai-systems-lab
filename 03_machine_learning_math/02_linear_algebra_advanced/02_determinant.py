"""
working with a 3×3 matrix A, and this snippet is trying to compute both its determinant and inverse.
This matrix is not invertible because its determinant is zero.

"""
import numpy as np
A = np.array([[2, 3, 4], [4, 5, 6], [7, 8, 9]])

determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)

print("Determinant: ", determinant)
print("Inverse: ", inverse)

"""
Why np.linalg.inv(A) Fails
- The determinant of A is:
np.linalg.det(A)  # Output: 0.0
- 
- A matrix with a zero determinant is called singular, meaning it doesn't have an inverse.
- Trying to compute np.linalg.inv(A) will raise:

"""

"""
Handle This Gracefully
If you're building a robust system (e.g., for annuity matrix ops or supplier scoring), wrap it like this:
"""
try:
    determinant = np.linalg.det(A)
    print("Determinant:", determinant)

    if np.isclose(determinant, 0):
        print("Matrix is singular; inverse does not exist.")
    else:
        inverse = np.linalg.inv(A)
        print("Inverse:\n", inverse)

except np.linalg.LinAlgError as e:
    print("Error computing inverse:", e)


# Bonus Tip: Use np.linalg.pinv(A) for Pseudo-Inverse
#If you still need something like an inverse (e.g., for least squares or regression), try:
# This works even for singular matrices and is widely used in ML and data fitting.
# Want to explore how this ties into solving linear systems or optimizing backend workflows? I can scaffold that next.
pseudo_inverse = np.linalg.pinv(A)
print("Pseudo-Inverse:\n", pseudo_inverse)