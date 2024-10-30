import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite database
engine = create_engine('sqlite:///C:/Users/parag/predictive_maintenance/maintenance_db.db')

# Query to check the columns in the machine_data table
query = 'SELECT * FROM machine_data LIMIT 5'
df = pd.read_sql(query, engine)

#Print the first few rows and column names
print(df.head())
print(df.columns)