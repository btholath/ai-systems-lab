"""
- fillna() fills missing values with something (like an average).
- interpolate() guesses missing values based on nearby data.
- merge() combines tables using a common column.
- concat() stacks tables either vertically (rows) or horizontally (columns).
- join() is similar to merge, but works with indexes.
"""

import pandas as pd
import numpy as np

# ----------------------------------------
# 🧪 PART 1: Handling Missing Data
# ----------------------------------------

# Create a sample dataset with some missing values (NaN)
data = {
    "Name": ["Alice", "Bob", np.nan, "David"],     # One missing name
    "Age": [25, np.nan, 30, 35],                   # One missing age
    "Score": [85, 90, np.nan, 88],                 # One missing score
}

# Convert the dictionary into a DataFrame (like a table)
df = pd.DataFrame(data)
print("📋 Original Dataset:\n", df)

# Fill missing Age values with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Score values by estimating between known values
df["Score"] = df["Score"].interpolate()

# Rename columns to make them more descriptive
df = df.rename(columns={"Name": "Student_Name", "Score": "Exam:Score"})
print("\n✅ Cleaned & Renamed Dataset:\n", df)

# ----------------------------------------
# 🔗 PART 2: Merging Two Datasets
# ----------------------------------------

# Create first dataset with student details
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
})

# Create second dataset with student scores
df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Score": [85, 90, 88]
})

print("\n📘 Dataset 1 (Student Info):\n", df1)
print("\n📗 Dataset 2 (Scores):\n", df2)

# Merge both datasets using the common 'ID' column
merged = pd.merge(df1, df2, how="inner", on="ID")
print("\n🔀 Merged Dataset:\n", merged)

# Add a new column showing score as a percentage (out of 200)
merged["Score_Percentage"] = (merged["Score"] / 200) * 100
print("\n📈 Transformed Dataset with Score %:\n", merged)

# ----------------------------------------
# 🧱 PART 3: Combining Datasets (Concatenation)
# ----------------------------------------

# Combine vertically (stack rows) — not meaningful here unless IDs differ
combined_vertical = pd.concat([df1, df2], axis=0)
print("\n📎 Combined Vertically (rows stacked):\n", combined_vertical)

# Combine horizontally (side-by-side columns)
combined_horizontal = pd.concat([df1, df2], axis=1)
print("\n📎 Combined Horizontally (columns side-by-side):\n", combined_horizontal)

# ----------------------------------------
# ⚠️ PART 4: Incorrect Merge Examples (Cleaned Up)
# ----------------------------------------

# These lines were incorrect because 'common_column' doesn't exist
# So we remove them to avoid confusion

# If you want to merge on a different column, make sure it exists in both DataFrames
# Example:
# merged = pd.merge(df1, df2, how="left", on="ID")  # Valid if both have 'ID'

# ----------------------------------------
# 🔗 PART 5: Joining Datasets (Alternative to Merge)
# ----------------------------------------

# Join df2 to df1 using index (must align properly)
joined = df1.join(df2.set_index("ID"), on="ID", how="inner")
print("\n🔗 Joined Dataset (using index):\n", joined)