import numpy as np

# 1. Generate synthetic (fake) data
np.random.seed(42)                          # Make randomness repeatable
X = 2 * np.random.rand(100, 1)              # 100 random x-values between 0 and 2
y = 4 + 3 * X + np.random.randn(100, 1)     # y = 4 + 3x plus some noise

# 2. Add a “bias” (intercept) column of 1’s so we can learn the constant term
X_b = np.c_[np.ones((100, 1)), X]           # X_b becomes shape (100, 2)

def stochastic_gradient_descent(X, y, theta, learning_rate, n_epochs):
    """
    Runs Stochastic Gradient Descent (SGD) to find optimal parameters theta.

    Args:
      X             – Feature matrix with bias term, shape (m, 2)
      y             – Target values, shape (m, 1)
      theta         – Initial parameters [theta0, theta1], shape (2, 1)
      learning_rate – How big each update step should be
      n_epochs      – Number of full passes through the training set

    Returns:
      theta         – Updated parameters after SGD
    """
    m = len(y)                               # Number of training examples

    for epoch in range(n_epochs):
        for i in range(m):
            # 3. Pick one random data point
            random_index = np.random.randint(m)
            xi = X[random_index:random_index + 1]  # Shape (1, 2)
            yi = y[random_index:random_index + 1]  # Shape (1, 1)

            # 4. Compute prediction error for this single point
            error = xi @ theta - yi             # Shape (1, 1)

            # 5. Compute gradient of the squared error w.r.t. theta
            #    For one example, gradient = 2 * xᵀ · error
            gradients = 2 * xi.T @ error         # Shape (2, 1)

            # 6. Update parameters in the opposite direction of the gradient
            theta = theta - learning_rate * gradients

    return theta

# 7. Initialize parameters randomly
theta_init = np.random.randn(2, 1)       # Two values: one for bias, one for slope
learning_rate = 0.01
n_epochs = 50

# 8. Run SGD to optimize theta
theta_opt = stochastic_gradient_descent(
    X_b, y, theta_init, learning_rate, n_epochs
)

print("Optimized Parameters:", theta_opt)