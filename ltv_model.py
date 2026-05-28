import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# Load Dataset


df = pd.read_csv("featured_telco.csv")
# Encode Text Columns


for col in df.columns:

    if df[col].dtype == 'O' or str(df[col].dtype) == 'str':

        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(df[col].astype(str))


# Fill Missing Values


df.fillna(0, inplace=True)

# Remove customerID

if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)

# Create LTV Target


df["LTV"] = df["MonthlyCharges"] * df["tenure"]
# Features and Target


X = df.drop("LTV", axis=1)

y = df["LTV"]

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Regression Model

model = RandomForestRegressor(random_state=42)

model.fit(X_train, y_train)

# Prediction

predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", mae)

print("\nLTV Prediction Completed")
