import psycopg  # psycopg is the new version of psycopg2 (https://www.psycopg.org/)
from dotenv import load_dotenv
import os

# from config import load_config

def connect():
    """Connect to the PostgreSQL database server."""
    load_dotenv()
    conn = None
    try:
        dbname=os.getenv("PGDATABASE")
        user=os.getenv("PGUSER")
        password=os.getenv("PGPASSWORD") 
        host=os.getenv("PGHOST") 
        port=os.getenv("PGPORT")
        endpointid=os.getenv("ENDPOINTID")
        with psycopg.connect(
            dbname=os.getenv("PGDATABASE"), 
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            host=os.getenv("PGHOST"),
            port=os.getenv("PGPORT"),
            options='endpoint=' + os.getenv("ENDPOINTID")
            ) as conn:
            print(f"Connection successfully {dbname} database on {host} as {user}.")
            return conn
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
        

if __name__ == '__main__':
    conn = connect()
    print(type(conn))
    