import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("featured_telco.csv"
# Convert ALL text columns

for col in df.columns:
    
    # Check if column is NOT numeric
    if df[col].dtype == 'O' or df[col].dtype == object or str(df[col].dtype) == 'str':
        
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col].astype(str))
# Fill missing values

df.fillna(0, inplace=True)
# Remove customerID

if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)

# Features and Target

X = df.drop("Churn", axis=1)
y = df["Churn"
# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# Logistic Regression

lr_model = LogisticRegression(max_iter=2000)

lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

print("\n===== Logistic Regression =====")
print(classification_report(y_test, lr_predictions))

# Random Forest

rf_model = RandomForestClassifier(random_state=42)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

print("\n===== Random Forest =====")
print(classification_report(y_test, rf_predictions))

# XGBoost

xgb_model = XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss'
)

xgb_model.fit(X_train, y_train)

xgb_predictions = xgb_model.predict(X_test)

print("\n===== XGBoost =====")
print(classification_report(y_test, xgb_predictions))

print("\nModel Training Completed Successfully")
