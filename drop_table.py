import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/parag/predictive_maintenance/maintenance_db.db')
cursor = conn.cursor()

# Drop the existing machine_data table
cursor.execute('DROP TABLE IF EXISTS machine_data')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Dropped the existing 'machine_data' table.")