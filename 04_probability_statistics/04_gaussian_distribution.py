# Import necessary libraries
import numpy as np          # For mathematical operations and arrays
import matplotlib.pyplot as plt  # For creating plots
from scipy.stats import norm  # For Gaussian distribution calculations

# Set up the x-values for the plot (range of growth factors)
x_values = np.linspace(0.5, 1.5, 100)  # Adjusted range to better fit growth factors (0.5 to 1.5)

# Define parameters for the Athene AccuMax 7 growth distribution
mean_growth = 12993 / 10000  # Normalized growth factor from $12,993 (approx. 1.2993)
spread_growth = 0.1          # 10% spread as standard deviation

# Calculate the Gaussian probability density function (PDF)
y_growth = norm.pdf(x_values, loc=mean_growth, scale=spread_growth)

# Create the plot
plt.plot(x_values, y_growth, label="Annuity Growth", color="purple")
plt.title("Athene AccuMax 7 Growth Distribution")
plt.xlabel("Growth Factor")
plt.ylabel("Chance")
plt.legend()  # Show the legend
plt.grid(True)  # Add a grid for better readability

# Save the plot as a PNG file
plt.savefig("/workspaces/ai-systems-lab/04_probability_statistics/04_gaussian_distribution.png")

# Display the plot (optional, for interactive viewing in Jupyter or terminal)
plt.show()

# Optional: Print some stats for understanding
print(f"Mean Growth Factor: {mean_growth:.4f}")
print(f"Standard Deviation: {spread_growth:.4f}")
plt.savefig("/workspaces/ai-systems-lab/04_probability_statistics/04_gaussian_distribution.png")  # Save the graph as a file