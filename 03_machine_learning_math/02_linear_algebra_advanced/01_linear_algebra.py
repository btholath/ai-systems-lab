"""
# Linear Algebra Advanced Concepts with NumPy
linear algebra—can understand what’s happening and how it connects to machine learning and data science.

---

### ✅ Annotated Code with Layman-Friendly Comments

"""
import numpy as np  # Import NumPy, a library for working with numbers and matrices

# ----------------------------------------
# 🧮 Create a 2x2 Matrix A
# ----------------------------------------
A = np.array([
    [2, 3],
    [1, 4]
])
print

""""
### 📐 Determinant of a Matrix
"""
determinant = np.linalg.det(A)
print("Determinant: ", determinant)
print("Matrix A: \n", A)


# The **determinant** is a single number that tells you how "invertible" or "stretchy" a matrix is.
# If the determinant is **zero**, the matrix can't be inverted.
# In machine learning, determinants help in understanding transformations and solving equations.


"""
### 🔍 Singular Value Decomposition (SVD)

"""
U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular Values: \n", S)
print("V Transpose: \n", Vt)

"""
- **SVD** breaks a matrix into three parts: `U`, `S`, and `Vt`.
- It’s like reverse-engineering the matrix to understand its structure.
- Used in **dimensionality reduction** (like PCA), **image compression**, and **recommendation systems**.
"""

"""
### 🔁 Inverse of a Matrix
"""
inverse = np.linalg.inv(A)
print("Inverse of A: \n", inverse)
"""- The **inverse** of a matrix undoes its transformation.
- Think of it like dividing by a number—but for matrices.
- In ML, inverses are used in solving systems of equations and optimizing models.
"""

### 📊 Eigenvalues and Eigenvectors of A
eigenValues, eigneVectors = np.linalg.eig(A)
print("EigenVal\n", eigenValues)
print("EigenVectors\n", eigneVectors)

"""
- **Eigenvalues** tell you how much a transformation stretches space.
- **Eigenvectors** show the directions that stay the same after transformation.
- In ML, they’re used in **PCA**, **clustering**, and **stability analysis**.
"""


### 📊 Eigenvalues and Eigenvectors of Another Matrix B
B = np.array([
    [4, 2],
    [1, 1]
])
eigval, eigvec = np.linalg.eig(B)
print("EigVal: ", eigval)
print("EigVect: \n", eigvec)

"""
- Same concept as above, but applied to a different matrix.
- Useful for comparing how different systems behave or evolve.
"""

### 🧠 Why This Matters in Machine Learning
"""
| Concept         | ML Use Case Example                          |
|-----------------|-----------------------------------------------|
| Determinant     | Checking invertibility in optimization        |
| Inverse         | Solving linear systems (e.g., regression)     |
| SVD             | Dimensionality reduction (e.g., PCA)          |
| Eigenvalues     | Feature extraction, stability analysis        |
| Eigenvectors    | Finding principal directions in data          |
"""
