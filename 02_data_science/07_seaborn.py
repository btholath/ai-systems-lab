"""

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# 📥 Load Titanic Dataset
# ----------------------------------------
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ----------------------------------------
# 🧪 Inspect Data Structure and Summary
# ----------------------------------------
print("🔍 Data Info:")
print(df.info())
print("\n📊 Statistical Summary:")
print(df.describe())

# ----------------------------------------
# 🧼 Data Cleaning: Handle Missing Values
# ----------------------------------------
df["Age"] = df["Age"].fillna(df["Age"].median())  # Fill missing ages with median
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])  # Fill missing embarkation with mode

# ----------------------------------------
# 🧹 Remove Duplicate Records
# ----------------------------------------
df = df.drop_duplicates()

# ----------------------------------------
# 🎩 Filter: First-Class Passengers
# ----------------------------------------
first_class = df[df["Pclass"] == 1]
print("\n🎩 First Class Passengers Sample:")
print(first_class.head())

# ----------------------------------------
# 📊 Bar Chart: Survival Rate by Class
# ----------------------------------------
survival_by_class = df.groupby("Pclass")["Survived"].mean()

plt.figure(figsize=(6, 4))
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.tight_layout()
plt.savefig("survival_rate_by_class.png")
plt.close()

# ----------------------------------------
# 📈 Histogram: Age Distribution
# ----------------------------------------
plt.figure(figsize=(6, 4))
sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("age_distribution_histogram.png")
plt.close()

# ----------------------------------------
# 🔍 Scatter Plot: Age vs Fare
# ----------------------------------------
plt.figure(figsize=(6, 4))
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
plt.title("Age vs Fare Paid")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("age_vs_fare_scatter.png")
plt.close()