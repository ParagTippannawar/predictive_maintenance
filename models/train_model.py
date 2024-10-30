import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sqlalchemy import create_engine

# Connect to the SQLite database
engine = create_engine('sqlite:///C:/Users/parag/predictive_maintenance/maintenance_db.db')

# Load data from the machine_data table
query = 'SELECT * FROM machine_data'
df = pd.read_sql(query, engine)

# Ensure column names are correct
print("Data Columns: ", df.columns)  # Debugging line to check columns

# Check if 'temperature' and 'cycle_count' columns exist
if 'temperature' not in df.columns or 'cycle_count' not in df.columns:
    raise ValueError("Required columns 'temperature' or 'cycle_count' are missing in the database.")

# Prepare the data for training
X = df[['temperature', 'cycle_count']]  # Features
y = df['status'].apply(lambda x: 1 if x == 'error' else 0)  # Target (1 for 'error', 0 otherwise)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to a file
with open('predictive_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as 'predictive_model.pkl'")