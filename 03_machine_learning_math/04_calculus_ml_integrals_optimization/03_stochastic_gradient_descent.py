import numpy as np
import matplotlib.pyplot as plt

# Simple SGD example: Guessing candies
true_value = 15  # Real number of candies
guess = 10       # Initial guess
learning_rate = 0.1  # How big each step is
losses = []      # Track mistakes

# Simulate SGD with 10 steps, using random samples
for _ in range(10):
    # Random sample (pretend we check 1-3 candies)
    sample = np.random.randint(1, 4)
    error = (guess - true_value) * sample / 3  # Approximate error
    loss = error ** 2  # Loss function
    losses.append(loss)
    # Adjust guess downhill
    guess = guess - learning_rate * error
    print(f"Step {_+1}: Guess = {guess:.1f}, Loss = {loss:.1f}")

# Plot the learning process
plt.plot(losses, '-o')
plt.title("SGD Learning to Guess Candies")
plt.xlabel("Step")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# Annuity example: Adjust rate to match $12,993 growth
target_growth = 12993  # From previous integral (approx.)
initial_rate = 0.02    # Start with 2%
rate = initial_rate

for _ in range(10):
    premium = 10000
    predicted_growth = premium * np.exp(rate * 7)  # Growth model
    error = (predicted_growth - target_growth) / target_growth
    rate = rate - learning_rate * error
    print(f"Step {_+1}: Rate = {rate:.4f}, Predicted Growth = {predicted_growth:.1f}")

print(f"Final rate close to Athene's 3.75%: {rate:.4f}")