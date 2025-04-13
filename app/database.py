import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '../data/cards.db')

def init_db():
    data_dir = os.path.dirname(DB_PATH)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_name TEXT,
            series TEXT,
            market_price REAL,
            scanned_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
