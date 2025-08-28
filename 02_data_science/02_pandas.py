import pandas as pd
import os

# Define URL and local filename
url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
local_filename = "insurance.csv"

# Download only if file doesn't exist
if not os.path.exists(local_filename):
    print("Downloading dataset...")
    df = pd.read_csv(url)
    df.to_csv(local_filename, index=False)
else:
    print("File already exists. Loading locally...")
    df = pd.read_csv(local_filename)

# Explore structure
print("First 5 rows:\n", df.head())
print("\nSummary:\n", df.describe())

# Select relevant columns
selected_columns = df[["age", "sex", "charges"]]
print("\nSelected Columns:\n", selected_columns.head())

# Filter: High-cost female customers over 50
filtered_rows = df[
    (df["age"] > 50) &
    (df["sex"] == "female") &
    (df["charges"] > 20000)
]
print("\nFiltered Rows (High-cost female customers over 50):\n", filtered_rows)
print("\nNumber of such customers:", len(filtered_rows))

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("Series s:\n", s)

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print("DataFrame df:\n", df)


# Viewing Data
print("df.head()", df.head())

print(df.tail(3))

print(df.info())
print(df.describe())

print(df[["Name", "Age"]])

print(df[df["Age"] > 25])

print(df.iloc[0])
print(df.iloc[:, 0])

print(df.loc[0])
print(df.loc[:, "Name"])