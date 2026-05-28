from sqlalchemy import create_engine
import pandas as pd

# PostgreSQL connection details
username = "postgres"
password = "minihani"
host = "localhost"
port = "5432"
database = "customer_churn_db"

# Create connection
engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)

# Load dataset
df = pd.read_csv("featured_telco.csv")

# Store data into PostgreSQL
df.to_sql("customer_data", engine, if_exists="replace", index=False)

print("Database Connected Successfully")
print("Data Uploaded to PostgreSQL")
