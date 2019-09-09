import mysql.connector as conn
from dotenv import load_dotenv
import os
load_dotenv()

def get_connection():

    db = conn.connect(
        host="localhost",
        user="root",
        passwd=os.getenv("DB_PASS"),
        db="emails"
        )
    return db
