import os
from psycopg2 import connect
from dotenv import load_dotenv

load_dotenv()  # charge les variables du .env

def get_connection():
    conn = connect(
        host=os.getenv("HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
    )
    return conn
