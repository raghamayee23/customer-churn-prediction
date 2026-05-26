import pandas as pd
import shap
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder

# Load Dataset


df = pd.read_csv("featured_telco.csv")

--
# Encode Text Columns


for col in df.columns:
    
    if df[col].dtype == 'O' or str(df[col].dtype) == 'str':
        
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col].astype(str))



df.fillna(0, inplace=True)



if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)



X = df.drop("Churn", axis=1)
y = df["Churn"]



model = XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss'
)

model.fit(X, y)



explainer = shap.Explainer(model)

shap_values = explainer(X)



shap.plots.beeswarm(shap_values)

print("\nSHAP Analysis Completed")
