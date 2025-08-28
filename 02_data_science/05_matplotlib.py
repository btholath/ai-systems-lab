import matplotlib.pyplot as plt

# ----------------------------------------
# 📈 LINE PLOT: Tracking Sales Over Time
# ----------------------------------------
years = [2010, 2011, 2012, 2013]
sales = [100, 120, 140, 160]

plt.figure(figsize=(6, 4))
plt.plot(years, sales, label="Sales Trend", color="blue", marker="o")
plt.title("Sales Over Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
plt.savefig("sales_over_years.png")
plt.close()

# ----------------------------------------
# 📊 BAR CHART: Comparing Revenue by Category
# ----------------------------------------
categories = ["Electronics", "Clothing", "Groceries"]
revenue = [250, 400, 150]

plt.figure(figsize=(6, 4))
plt.bar(categories, revenue, color="green")
plt.title("Revenue by Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.close()

# ----------------------------------------
# 🔴 SCATTER PLOT: Study Time vs Exam Scores
# ----------------------------------------
hours_studied = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 85]

plt.figure(figsize=(6, 4))
plt.scatter(hours_studied, exam_scores, color="red")
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.tight_layout()
plt.savefig("study_vs_scores.png")
plt.close()