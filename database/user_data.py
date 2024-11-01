import sqlite3
from datetime import datetime


def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id BIG INTEGER UNIQUE,
            first_name TEXT NOT NULL,
            last_name TEXT,
            registration_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_db()


def add_user(user_id, first_name, last_name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    registration_date = datetime.now().strftime("%Y-%m-%d")
    
    try:
        cursor.execute('''
            INSERT INTO users (user_id, first_name, last_name, registration_date) 
            VALUES (?, ?, ?, ?)
        ''', (user_id, first_name, last_name, registration_date))
        conn.commit()
    except sqlite3.IntegrityError:
        print('User is already registered.')
    finally:
        conn.close()


def user_exist(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()[0]

    conn.close()

    return result > 0 


def view_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    for user in users:
        print(user)

    conn.close()

# view_users()