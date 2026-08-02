import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# -----------------------------
# Project Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(DATA_PATH)

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

# Shape
print("\nShape:")
print(df.shape)

# Columns
print("\nColumns:")
print(df.columns.tolist())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Data Types
print("\nData Types:")
print(df.dtypes)

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe(include="all"))

# -----------------------------
# Graph Style
# -----------------------------
sns.set_style("whitegrid")

# -----------------------------
# Graph 1: Churn Distribution
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()

# Save Graph
plt.savefig(BASE_DIR / "reports" / "figures" / "churn_distribution.png")

# Show Graph
plt.show()

# -----------------------------
# Graph 2: Contract vs Churn
# -----------------------------
plt.figure(figsize=(7,5))
sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Contract Type vs Churn")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.tight_layout()

plt.savefig(BASE_DIR / "reports" / "figures" / "contract_vs_churn.png")
plt.show()

# -----------------------------
# Graph 3: Monthly Charges vs Churn
# -----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)

plt.title("Monthly Charges vs Churn")
plt.tight_layout()

plt.savefig(BASE_DIR / "reports" / "figures" / "monthly_charges_vs_churn.png")
plt.show()

# -----------------------------
# Graph 4: Tenure vs Churn
# -----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x="Churn", y="tenure", data=df)

plt.title("Tenure vs Churn")
plt.xlabel("Churn")
plt.ylabel("Tenure (Months)")
plt.tight_layout()

plt.savefig(BASE_DIR / "reports" / "figures" / "tenure_vs_churn.png")
plt.show()

# -----------------------------
# Graph 5: Correlation Heatmap
# -----------------------------
import numpy as np

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig(BASE_DIR / "reports" / "figures" / "correlation_heatmap.png")
plt.show()
