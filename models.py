import sqlite3
from datetime import datetime

DB_NAME = "budgetwise.db"

def init_db():
    """Crée les tables si elles n'existent pas"""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
                amount REAL NOT NULL,
                category TEXT,
                tags TEXT,
                description TEXT,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_transaction(type, amount, category=None, tags=None, description=None, date=None):
    """Ajoute une transaction dans la base"""
    if type not in ['income', 'expense']:
        raise ValueError("Type must be 'income' or 'expense'")

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transactions (type, amount, category, tags, description, date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (type, amount, category, tags, description, date))
        conn.commit()

def get_transactions():
    """Retourne toutes les transactions"""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM transactions ORDER BY date DESC')
        rows = cursor.fetchall()
        return rows

def get_balance():
    """Retourne le solde actuel"""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'income'")
        income = cursor.fetchone()[0] or 0
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'expense'")
        expense = cursor.fetchone()[0] or 0
        return income - expense
