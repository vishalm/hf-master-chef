# Placeholder comment for db.py
import sqlite3
import json
from config.config import DATABASE_PATH

def get_connection():
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def create_table():
    """Create the menus table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menus (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            occasion TEXT NOT NULL,
            menu TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_menu(occasion, menu):
    """Insert a new menu record into the database."""
    # Convert dictionary to JSON string if needed
    if isinstance(menu, dict):
        menu = json.dumps(menu)
        
    # Ensure the table exists
    create_table()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO menus (occasion, menu) VALUES (?, ?)
    ''', (occasion, menu))
    conn.commit()
    conn.close()