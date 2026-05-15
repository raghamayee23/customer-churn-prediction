import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Fill missing values with median
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

print("Missing Values:")
print(df.isnull().sum())

label_encoder = LabelEncoder()

# Encode all object columns
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = label_encoder.fit_transform(df[column])

print("\nEncoded Dataset:")
print(df.head())

df.to_csv("cleaned_telco.csv", index=False)

print("\nPreprocessing completed successfully")
