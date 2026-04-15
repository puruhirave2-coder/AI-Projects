import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "database" / "regression.db"

conn = sqlite3.connect(db_path)

# Create a cursor object
cursor = conn.cursor()

# Query to retrieve table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all table names
tables = cursor.fetchall()

# Print the table names
for table in tables:
    print(table[0])

# Fetch rows from predicting_sales table
cursor.execute("SELECT * FROM predicting_sales LIMIT 10;")
rows = cursor.fetchall()

print("\nSample rows from predicting_sales table:")
for row in rows:
    print(row)

# Close connection
conn.close()
