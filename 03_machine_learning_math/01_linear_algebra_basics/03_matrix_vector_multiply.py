import numpy as np

# Create matrix and vector
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([1, 0, -1])

# Matrix-vector multiplication 
result = np.dot(M, v)
print("Matrix-Vector Multiplication: \n", result)


# Predicting Surrender Risk
# This dot product gives a risk score—a scalar that can be thresholded to flag high-risk contracts.
# Weights that determine how much each input feature (like age, premium, duration, etc.) influences the final risk score. 
import numpy as np
customer = np.array([65, 75000, 5000, 20, 0.3])  # Age, income, premium, duration, risk
weights = np.array([0.01, 0.0005, 0.002, 0.005, 1.2])  # Model coefficients

risk_score = np.dot(customer, weights)
print("Surrender Risk Score: \n", risk_score)

