import pandas as pd

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# First 5 rows
print(df.head())

# Dataset shape
print("\nRows and Columns:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Churn count
print("\nChurn Count:")
print(df["Churn"].value_counts())

# Data types
print("\nData Types:")
print(df.dtypes)