import sqlite3

def create_connection():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()
    return connection, cursor

def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
            )
    """)

def setup_database():
    connection , cursor = create_connection()
    create_table(cursor)
    connection.commit()
    connection.close()