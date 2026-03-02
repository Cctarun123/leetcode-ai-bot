import sqlite3
from datetime import datetime

def log_result(problem, status):

    conn = sqlite3.connect("database/results.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            problem TEXT,
            status TEXT,
            timestamp TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO results (problem, status, timestamp)
        VALUES (?, ?, ?)
    """, (problem, status, str(datetime.now())))

    conn.commit()
    conn.close()