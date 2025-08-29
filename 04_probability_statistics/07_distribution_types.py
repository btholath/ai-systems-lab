"""
Probability ideas—Bayes’ Theorem, Gaussian, Bernoulli, Binomial, and Poisson Distributions

What This Does: This script draws four different graphs to show how data behaves:
Gaussian: A bell curve for things like heights or test scores (mean 0, spread 1).
Bernoulli: A bar for one yes/no try (e.g., 60% chance of success).
Binomial: Bars for multiple tries (e.g., 10 coin flips, 50% chance of heads).
Poisson: Bars for rare events (e.g., 3 raindrops on average).


Cool Parts: Each plot saves as a PNG file in your project, and you can see them by running the script!
Purpose and Usefulness in Machine Learning

Gaussian Distribution:
Purpose: Shows where data piles up around an average.
Usefulness: ML predicts normal behaviors, like annuity growth ($12,993 average).


Bernoulli Distribution:
Purpose: Models one yes/no event.
Usefulness: ML uses it for single decisions, like if an annuity beats a benchmark once.


Binomial Distribution:
Purpose: Counts successes in multiple tries.
Usefulness: ML predicts repeated outcomes, like S&P 500 wins over 10 years.


Poisson Distribution:
Purpose: Predicts rare random events.
Usefulness: ML tracks infrequent events, like big annuity payouts.
"""

# Import all the tools we need
import numpy as np          # For math and arrays
import matplotlib.pyplot as plt  # For drawing graphs
from scipy.stats import binom, poisson  # For special distribution calculations

# --------------------------------------------
# Bayes' Theorem Function (Commented for now)
# This calculates the updated chance using prior knowledge and new evidence
# def bayes_theorem(prior, likelihood, evidence):
#     return (likelihood * prior) / evidence

# --------------------------------------------
# Gaussian Distribution
# Set up parameters for a bell-shaped curve
mean = 0      # Average value (center of the bell)
std_dev = 1   # Spread of the data (how wide the bell is)

# Create a range of values to plot
x_values = np.linspace(-4, 4, 100)

# Calculate the Gaussian curve manually (probability density)
y_gaussian = (1 / (np.sqrt(2 * np.pi * std_dev**2))) * np.exp(-0.5 * ((x_values - mean) / std_dev)**2)

# Draw the Gaussian plot
plt.plot(x_values, y_gaussian, label="Gaussian Bell Curve", color="blue")
plt.title("Gaussian Distribution (Bell Shape)")
plt.xlabel("Value (e.g., Height or Score)")
plt.ylabel("Chance")
plt.legend()  # Show the label
plt.grid(True)  # Add a grid for easier reading

# Save and show the plot
plt.savefig("/workspaces/ai-systems-lab/04_probability_statistics/07_gaussian_distribution.png")
plt.show()

# --------------------------------------------
# Bernoulli Distribution
# Set up parameters for a single yes/no event
p_success = 0.6  # Chance of success (e.g., 60% chance of heads)

# Create outcomes (0 for failure, 1 for success)
outcomes = [0, 1]
probabilities = [1 - p_success, p_success]  # Chances of failure and success

# Draw the Bernoulli bar graph
plt.bar(outcomes, probabilities, color="blue")
plt.title("Bernoulli Distribution (One Try)")
plt.xticks(outcomes, labels=["0 (Failure)", "1 (Success)"])
plt.ylabel("Probability")
plt.grid(True)

# Save and show the plot
plt.savefig("/workspaces/ai-systems-lab/04_probability_statistics/07_bernoulli_distribution.png")
plt.show()

# --------------------------------------------
# Binomial Distribution
# Set up parameters for multiple yes/no tries
n_trials = 10    # Number of tries (e.g., 10 coin flips)
p_success_binom = 0.5  # Chance of success each time (50% for heads)

# Create a range of possible successes
x_binom = np.arange(0, n_trials + 1)

# Calculate the probability of each number of successes