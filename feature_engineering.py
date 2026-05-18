import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load cleaned dataset
df = pd.read_csv("cleaned_telco.csv")
# Feature Engineering

df['AvgMonthlyValue'] = df['TotalCharges'] / (df['tenure'] + 1)

df['ChargePerTenure'] = df['MonthlyCharges'] / (df['tenure'] + 1)

df['LongTermCustomer'] = df['tenure'].apply(lambda x: 1 if x > 24 else 0)

df['HighMonthlyCharges'] = df['MonthlyCharges'].apply(lambda x: 1 if x > 70 else 0)
# Encode ALL text columns

for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column].astype(str)
# Save dataset

df.to_csv("featured_telco.csv", index=False)

print(df.head())

print("\nFeature Engineering Completed Successfully")
