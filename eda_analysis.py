import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Churn count
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Count")
plt.show()

# Contract vs Churn
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Contract Type vs Churn")
plt.xticks(rotation=15)
plt.show()

# Tenure distribution
sns.histplot(df['tenure'], bins=30)
plt.title("Tenure Distribution")
plt.show()
