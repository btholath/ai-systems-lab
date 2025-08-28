import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, np.nan, 30, 35],
    "Score": [85, 90, np.nan, 88],
}
df = pd.DataFrame(data)

print("Original Dataset: \n", df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

df = df.rename(columns={"Name":"Student_Name", "Score": "Exam:Score"})
print("Dataset: \n", df)

import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
})

df2 = pd.DataFrame({
    "ID": [1,2,3],
    "Score": [85, 90, 88]
})

print("Dataset 1: \n", df1)
print("Dataset 2: \n", df2)

merged = pd.merge(df1, df2, how="inner", on="ID")
print("Merged Dataset: \n", merged)

merged["Score_Percentage"] = (merged["Score"] / 200) * 100
print("Transformed Dataset \n", merged)



combined = pd.concat([df1, df2], axis=0)
combined = pd.concat([df1, df2], axis=1)

merged = pd.merge(df1, df2, on="common_column")
merged = pd.merge(df1, df2, how="left", on="common_column")
merged = pd.merge(df1, df2, how="inner", on="common_column")


joined = df1.join(df2, how="inner")