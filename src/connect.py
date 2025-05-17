import psycopg2
from config import load_config

def connect(config):
    """Connect to the PostgreSQL database server."""
    conn = None
    try:
        with psycopg2.connect(**config) as conn:
            print("Connection successful")
            return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    config = load_config()
    connect(config)