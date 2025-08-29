# Refactored Gradient Descent with Detailed Comments

```python
import numpy as np

def gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    theta: np.ndarray,
    learning_rate: float,
    num_iterations: int
) -> np.ndarray:
    """
    Perform gradient descent to optimize linear model parameters.

    Args:
        X: Feature matrix of shape (m, n),
           where m = number of samples, n = number of features (including bias).
        y: Target vector of shape (m,).
        theta: Initial parameters vector of shape (n,).
        learning_rate: Step size for each parameter update.
        num_iterations: Total number of gradient descent steps.

    Returns:
        theta: Optimized parameters after gradient descent.
    """
    m = X.shape[0]  # number of training examples

    for iteration in range(num_iterations):
        # 1. Compute current predictions: h = X · θ
        predictions = X.dot(theta)

        # 2. Compute errors vector: (h_i - y_i) for each sample
        errors = predictions - y

        # 3. Compute gradient: ∇J(θ) = (1/m) * Xᵀ · errors
        gradients = (1 / m) * X.T.dot(errors)

        # 4. Update parameters: θ := θ − α * ∇J(θ)
        theta = theta - learning_rate * gradients

        # Optional debug: print cost every 100 iterations
        # if iteration % 100 == 0:
        #     cost = (1/(2*m)) * np.sum(errors**2)
        #     print(f"Iter {iteration:4d} | Cost: {cost:.4f}")

    return theta


def main():
    # Sample dataset with a bias (intercept) term in the first column
    X = np.array([
        [1.0, 1.0],   # sample 1: x₀ = 1 (bias), x₁ = 1
        [1.0, 2.0],   # sample 2: x₀ = 1,       x₁ = 2
        [1.0, 3.0],   # sample 3: x₀ = 1,       x₁ = 3
    ])
    y = np.array([2.0, 2.5, 3.5])  # true target values

    # Initialize parameters (θ₀ for bias, θ₁ for feature)
    initial_theta = np.zeros(X.shape[1])

    # Hyperparameters
    learning_rate = 0.1
    num_iterations = 1000

    # Run gradient descent and retrieve optimized θ
    optimized_theta = gradient_descent(
        X,
        y,
        initial_theta,
        learning_rate,
        num_iterations
    )

    print("Optimized Parameters:", optimized_theta)


if __name__ == "__main__":
    main()
```

---

## What We Improved

- Added a clear **docstring** describing inputs, outputs, and the algorithm’s purpose.
- Introduced **type hints** (`np.ndarray`, `float`, `int`) for better editor support and readability.
- Renamed `iterations` → `num_iterations` for clarity.
- Broke out the sample run into a `main()` function and guarded it with `if __name__ == "__main__":`.
- Labeled each step of gradient descent with numbered comments for easy follow-along.
- Provided an **optional debug** block (commented-out) to print the cost function periodically.

---

## Next Steps You Might Explore

- Track the **cost function** over iterations to see convergence visually.
- Implement **feature scaling** (standardization) when features differ in scale.
- Experiment with gradient-descent variants:  
  - **Stochastic GD** (one sample at a time)  
  - **Mini-batch GD** (small groups of samples)  
  - **Momentum** or **Adam** optimizers  
- Wrap this into a reusable class or integrate with scikit-learn’s API style.
- Plot the loss surface in 3D (for two parameters) to build intuition on how gradients guide you downhill.

Which extension should we tackle first?
