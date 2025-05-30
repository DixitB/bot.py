import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    return psycopg2.connect(os.getenv('DATABASE_URL'))

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tracks (
            id SERIAL PRIMARY KEY,
            chat_id INTEGER,
            origin TEXT,
            destination TEXT,
            depart_date TEXT,
            return_date TEXT,
            last_price REAL
        )
    ''')
    conn.commit()
    conn.close()
