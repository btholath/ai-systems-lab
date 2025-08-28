""" lets you split data into categories (like Class A, B, C).
• 	 lets you apply multiple functions (mean, max, min) at once.
• 	 is a cleaner way to summarize data.
"""
import pandas as pd

# ----------------------------------------
# 🧪 STEP 1: Create a Sample Dataset
# ----------------------------------------

# Define a dictionary with student class, score, and age
data = {
    "Class": ["A", "B", "A", "B", "C", "C"],
    "Score": [85, 90, 88, 72, 95, 80],
    "Age": [15, 16, 15, 17, 16, 15],
}

# Convert the dictionary into a DataFrame (like a spreadsheet)
df = pd.DataFrame(data)
print("📋 Original Dataset:\n", df)

# ----------------------------------------
# 📊 STEP 2: Grouping and Aggregating Data
# ----------------------------------------

# Group the data by 'Class' and calculate the average Score and Age
grouped_mean = df.groupby("Class").mean()
print("\n📈 Average Score and Age by Class:\n", grouped_mean)

# Group by 'Class' and calculate multiple statistics for Score and Age
stats = df.groupby("Class").agg({
    "Score": ["mean", "max", "min"],
    "Age": ["mean", "max", "min"]
})
print("\n📊 Detailed Stats by Class:\n", stats)

# ----------------------------------------
# 🔍 STEP 3: Iterating Through Groups
# ----------------------------------------

# Loop through each group to see individual records per Class
grouped = df.groupby("Class")
print("\n🔍 Records by Class:")
for name, group in grouped:
    print(f"\nClass {name}:\n", group)

# ----------------------------------------
# 📈 STEP 4: More Aggregation Examples
# ----------------------------------------

# Calculate mean and sum for each Class
print("\n📉 Mean values by Class:\n", grouped.mean())
print("\n📊 Sum of values by Class:\n", grouped.sum())

# ----------------------------------------
# 🧮 STEP 5: Aggregation on Specific Columns
# ----------------------------------------

# Get average Score per Class
print("\n🎯 Average Score per Class:\n", df.groupby("Class")["Score"].mean())

# Get multiple stats for Score per Class
print("\n📌 Score Stats per Class:\n", df.groupby("Class").agg({"Score": ["mean", "max", "min"]}))

# ----------------------------------------
# 🔄 STEP 6: Pivot Table (Alternative to GroupBy)
# ----------------------------------------

# Create a pivot table showing average Score per Class
pivot = df.pivot_table(
    values="Score",
    index="Class",
    aggfunc="mean"
)
print("\n📊 Pivot Table (Average Score per Class):\n", pivot)

# ----------------------------------------
# 📏 STEP 7: Custom Aggregation Function
# ----------------------------------------

# Define a function to calculate range (max - min)
def range_func(x):
    return x.max() - x.min()

# Apply custom function to Score per Class
score_range = df.groupby("Class")["Score"].agg(range_func)
print("\n📐 Score Range per Class:\n", score_range)

# ----------------------------------------
# 🧮 STEP 8: Individual Aggregations
# ----------------------------------------

# Mean, Max, Min of Score per Class
print("\n📈 Mean Score per Class:\n", df.groupby("Class")["Score"].mean())
print("\n📈 Max Score per Class:\n", df.groupby("Class")["Score"].max())
print("\n📈 Min Score per Class:\n", df.groupby("Class")["Score"].min())

# Combined aggregation using .agg()
combined_stats = df.groupby("Class").agg({
    "Score": ["mean", "max", "min"]
})
print("\n📊 Combined Score Stats per Class:\n", combined_stats)