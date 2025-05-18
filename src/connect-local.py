import psycopg  # psycopg is the new version of psycopg2 (https://www.psycopg.org/)
from dotenv import load_dotenv
import os

# from config import load_config

def connect():
    """Connect to the PostgreSQL database server."""
    load_dotenv()
    conn = None
    try:
        with psycopg.connect(
            dbname=os.getenv("PGLOCAL_DATABASE"), 
            user=os.getenv("PGLOCAL_USER"),
            password=os.getenv("PGLOCAL_PASSWORD"),
            host=os.getenv("PGLOCAL_HOST"),
            port=os.getenv("PGLOCAL_PORT"),
            # options='endpoint=' + os.getenv("ENDPOINTID")
            ) as conn:
            print(f"Connection successfully.")
            cur = conn.cursor()
            cur.execute("SELECT VERSION();")
            db_version = cur.fetchone()
            print(f"PostgreSQL database version: {db_version}")
            return conn
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
        # print("Connection failed.")



if __name__ == '__main__':
    conn = connect()
    print(type(conn))


