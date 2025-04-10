import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_expense(self, amount, category, description=""):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
            INSERT INTO expenses (amount, category, description, date)
            VALUES (?, ?, ?, ?)
        ''', (amount, category, description, date))
        self.conn.commit()

    def get_all_expenses(self):
        self.cursor.execute('''
            SELECT * FROM expenses
            ORDER BY date DESC
        ''')
        return self.cursor.fetchall()

    def get_expenses_by_category(self, category):
        self.cursor.execute('''
            SELECT * FROM expenses
            WHERE category = ?
            ORDER BY date DESC
        ''', (category,))
        return self.cursor.fetchall()

    def get_total_expenses(self):
        self.cursor.execute('SELECT SUM(amount) FROM expenses')
        return self.cursor.fetchone()[0] or 0

    def get_category_summary(self):
        self.cursor.execute('''
            SELECT category, SUM(amount) as total
            FROM expenses
            GROUP BY category
            ORDER BY total DESC
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close() 
