# Import tools we need
import numpy as np          # For math and arrays
import matplotlib.pyplot as plt  # For drawing graphs
from scipy.stats import norm  # For Gaussian distribution calculations

# Create a range of values to plot (from -4 to 4, 100 points)
x_values = np.linspace(-4, 4, 100)

# Calculate the Gaussian curve (mean = 0, spread = 1)
y_values = norm.pdf(x_values, loc=0, scale=1)

# Draw the graph
plt.plot(x_values, y_values, label="Gaussian Bell Curve", color="blue")
plt.title("What a Gaussian Distribution Looks Like!")
plt.xlabel("Value (e.g., Candies Eaten)")
plt.ylabel("Chance of Happening")
plt.legend()  # Show the label
plt.grid(True)  # Add a grid for easier reading
plt.show()

# Add a fun example: Candies eaten by friends
mean_candies = 5    # Average candies eaten
spread_candies = 1  # How much it varies
y_candies = norm.pdf(x_values, loc=mean_candies, scale=spread_candies)
plt.plot(x_values, y_candies, label="Candies Eaten", color="green")
plt.title("How Many Candies Friends Eat")
plt.xlabel("Candies")
plt.ylabel("Chance")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("/workspaces/ai-systems-lab/04_probability_statistics/gaussian_distribution.png")  # Save the graph as a file