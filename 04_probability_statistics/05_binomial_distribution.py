# Import the tools we need
import numpy as np          # For math and arrays
import matplotlib.pyplot as plt  # For drawing graphs
from scipy.stats import binom, norm, poisson  # For distribution calculations

# Set up the Binomial Distribution parameters
n_trials = 10    # Number of tries (e.g., 10 coin flips)
p_success = 0.5  # Chance of success each time (e.g., 50% for heads)

# Create a range of possible outcomes (from 0 to 10 successes)
x_values = np.arange(0, n_trials + 1)

# Calculate the probability of each outcome
y_values = binom.pmf(x_values, n_trials, p_success)

# Draw the bar graph
plt.bar(x_values, y_values, label="Binomial Distribution", color="orange")
plt.title("Chances of Heads in 10 Coin Flips")
plt.xlabel("Number of Heads")
plt.ylabel("Probability")
plt.legend()  # Show the label
plt.grid(True)  # Add a grid for easier reading

# Save the plot as a PNG file
plt.savefig("/workspaces/ai-systems-lab/04_probability_statistics/05_binomial_distribution.png")

# Display the plot (optional, for interactive viewing)
plt.show()

# Optional: Print some fun stats
print(f"Number of tries: {n_trials}")
print(f"Chance of success: {p_success * 100}%")
print(f"Most likely number of heads: {x_values[np.argmax(y_values)]}")
