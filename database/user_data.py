import sqlite3
from datetime import datetime


def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            id BIG INTEGER UNIQUE,
            first_name TEXT NOT NULL,
            last_name TEXT,
            registration_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_db()


def add_user(id, first_name, last_name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    registration_date = datetime.now().strftime("%Y-%m-%d")
    
    try:
        cursor.execute('''
            INSERT INTO users (id, first_name, last_name, registration_date) 
            VALUES (?, ?, ?, ?)
        ''', (id, first_name, last_name, registration_date))
        conn.commit()
    except sqlite3.IntegrityError:
        print('User is already registered.')
    finally:
        conn.close()


