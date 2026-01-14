import sqlite3
from datetime import datetime
from config import Config

def db_init():
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS report (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        count INTEGER,
        average REAL,
        minimum INTEGER,
        maximum INTEGER,
        product INTEGER,
        created_at TEXT
    )
    """)


    conn.commit()
    conn.close()

def save_report(filename, result):
    conn = sqlite3.connect(Config.DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO report
        (filename, count, average, minimum, maximum, product, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        filename,
        result["count"],
        result["average"],
        result["min"],
        result["max"],
        result["product"],
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()