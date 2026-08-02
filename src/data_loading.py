import pandas as pd
from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset Path
DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

# Load Dataset
df = pd.read_csv(DATA_PATH)

print("✅ Dataset Loaded Successfully")
print()

print("Shape:", df.shape)
print()

print("Columns:")
print(df.columns.tolist())
print()

print(df.head())
