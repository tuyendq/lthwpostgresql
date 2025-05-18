import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define connection parameters
# conn = psycopg2.connect(
#     dbname="your_database",
#     user="your_username",
#     password="your_password",
#     host="your_neon_host",
#     port="5432"
# )
conn = psycopg2.connect(
    dbname=os.getenv("PGDATABASE"),
    user=os.getenv("PGUSER"),
    password=os.getenv("PGPASSWORD"),
    host=os.getenv("PGHOST"),
    port=os.getenv("PGPORT")
)
# Create a cursor object
cur = conn.cursor()

# Execute a test query
sql = """
CREATE TABLE IF NOT EXISTS table_test (column_test text PRIMARY KEY);
"""
cur.execute(sql)
# Commit the changes
conn.commit()
# Print the result
print("Table created successfully.")
# Close the connection
cur.close()
conn.close()