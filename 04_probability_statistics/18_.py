#!/usr/bin/env python3
"""
tips_analysis.py

Load the Seaborn “tips” dataset, run statistical tests, and visualize results.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, ttest_ind
from sklearn.linear_model import LinearRegression


def load_data(url: str) -> pd.DataFrame:
    """
    Download CSV from a URL and return a pandas DataFrame.
    """
    df = pd.read_csv(url)
    return df


def chi_square_test(df: pd.DataFrame, col1: str, col2: str, alpha: float = 0.05):
    """
    Build a contingency table from two categorical columns,
    run chi-square test, and print results.
    """
    table = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = chi2_contingency(table)
    print(f"Chi-Square: {chi2:.3f}, p-value: {p:.3f}")
    if p <= alpha:
        print("→ Reject H0: variables are dependent")
    else:
        print("→ Fail to reject H0: variables are independent")


def compare_tips_by_gender(df: pd.DataFrame, alpha: float = 0.05):
    """
    Separate tips by sex, perform an independent t-test,
    and print whether the difference is significant.
    """
    male = df[df["sex"] == "Male"]["tip"]
    female = df[df["sex"] == "Female"]["tip"]
    t_stat, p_value = ttest_ind(male, female)
    print(f"T-statistic: {t_stat:.3f}, p-value: {p_value:.3f}")
    if p_value <= alpha:
        print("→ Reject H0: significant difference")
    else:
        print("→ Fail to reject H0: no significant difference")


def plot_distribution(df: pd.DataFrame, column: str):
    """
    Plot histogram with KDE for a numeric column.
    """
    sns.histplot(df[column], kde=True, color="skyblue")
    plt.title(f"Distribution of {column.replace('_', ' ').title()}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame):
    """
    Display a heatmap of pairwise correlations among numeric features.
    """
    corr = df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()


def linear_regression_analysis(df: pd.DataFrame, feature: str, target: str):
    """
    Fit a simple linear regression model, print coefficients,
    and overlay the regression line on a scatter plot.
    """
    X = df[[feature]].values
    y = df[target].values
    model = LinearRegression().fit(X, y)

    # Print slope, intercept, and R²
    print(f"Slope: {model.coef_[0]:.3f}")
    print(f"Intercept: {model.intercept_:.3f}")
    print(f"R-Squared: {model.score(X, y):.3f}")

    # Plot scatter + regression line
    sns.scatterplot(x=df[feature], y=df[target], color="navy")
    plt.plot(df[feature], model.predict(X), color="crimson", label="Fit Line")
    plt.title(f"{feature.title()} vs {target.title()}")
    plt.legend()
    plt.show()


def main():
    DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    df = load_data(DATA_URL)

    # Inspect basic structure
    print(df.info())
    print(df.describe(), "\n")

    # Categorical dependence: smoker vs time
    chi_square_test(df, col1="smoker", col2="time")

    # Tip difference by gender
    compare_tips_by_gender(df)

    # Visualizations
    plot_distribution(df, column="total_bill")
    plot_correlation_heatmap(df)

    # Regression: total_bill → tip
    linear_regression_analysis(df, feature="total_bill", target="tip")


if __name__ == "__main__":
    main()