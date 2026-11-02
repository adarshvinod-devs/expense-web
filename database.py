import sqlite3

def create_connection():
    connection = sqlite3.connect("expenses.db")
    connection.row_factory = sqlite3.Row #To read value by column name
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
    connection, cursor = create_connection()
    create_table(cursor)
    connection.commit()
    connection.close()

def add_expense(amount: float, category: str, date: str, description: str):
    connection , cursor = create_connection()
    cursor.execute("""
        INSERT INTO expenses(amount, category, date, description) VALUES(?,?,?,?)
    """,(amount, category, date, description))
    connection.commit()
    connection.close()

def get_expenses():
    connection, cursor = create_connection()
    cursor.execute("""
        SELECT id, amount, category, date, description FROM expenses ORDER BY date DESC
    """)
    expenses = cursor.fetchall()
    connection.close()
    return expenses