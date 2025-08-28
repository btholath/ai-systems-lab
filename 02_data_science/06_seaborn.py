"""

"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# ----------------------------------------
# 🔥 HEATMAP: Visualizing Random Matrix
# ----------------------------------------
data = np.random.rand(5, 5)

plt.figure(figsize=(6, 4))
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("Heatmap of Random Values")
plt.tight_layout()
plt.savefig("heatmap_random_matrix.png")
plt.close()

# ----------------------------------------
# 🔗 PAIRPLOT: Exploring Relationships in Sample DataFrame
# ----------------------------------------
# Create a sample DataFrame for pairplot
df = pd.DataFrame({
    "Height": np.random.normal(170, 10, 100),
    "Weight": np.random.normal(65, 15, 100),
    "Age": np.random.randint(18, 60, 100)
})

sns.pairplot(df)
plt.savefig("pairplot_height_weight_age.png")
plt.close()

# ----------------------------------------
# 🔴 SCATTER PLOT: Simple Relationship Visualization
# ----------------------------------------
x = [1, 2, 3, 4, 5]
y = [10, 12, 25, 30, 45]

plt.figure(figsize=(6, 4))
plt.scatter(x, y, color="red")
plt.title("Scatter Plot: X vs Y")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.legend(["Dataset 1"])
plt.tight_layout()
plt.savefig("scatter_x_vs_y.png")
plt.close()

# ----------------------------------------
# 📊 HISTOGRAM: Frequency Distribution
# ----------------------------------------
hist_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.figure(figsize=(6, 4))
plt.hist(hist_data, bins=4, color="green", edgecolor="black")
plt.title("Histogram of Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_distribution.png")
plt.close()

# ----------------------------------------
# 🧱 BAR CHART: Category Comparison
# ----------------------------------------
categories = ["A", "B", "C"]
values = [10, 15, 7]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color="blue")
plt.title("Bar Chart: Category Values")
plt.xlabel("Category")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig("bar_chart_categories.png")
plt.close()

# ----------------------------------------
# 📈 BASIC LINE PLOT: Simple Trend
# ----------------------------------------
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure(figsize=(6, 4))
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.tight_layout()
plt.savefig("basic_line_plot.png")
plt.close()

# ----------------------------------------
# 🟠 STYLED LINE PLOT: Trend Visualization
# ----------------------------------------
plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [10, 20, 30], label="Trend", color="orange", linestyle="--", marker="x")
plt.title("Styled Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.tight_layout()
plt.savefig("styled_line_plot.png")
plt.close()