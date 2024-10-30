import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/parag/predictive_maintenance/maintenance_db.db')
cursor = conn.cursor()

# Drop the existing table
cursor.execute('DROP TABLE IF EXISTS machine_data')

# Recreate the table with the correct column name
cursor.execute('''
    CREATE TABLE machine_data (
        id INTEGER PRIMARY KEY,
        machine_id TEXT,
        timestamp DATETIME,
        temperature FLOAT,  -- Corrected column name
        cycle_count INTEGER,
        status TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Table recreated with the correct column name 'temperature'")