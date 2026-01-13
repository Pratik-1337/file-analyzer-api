import sqlite3
from datetime import datetime
import os

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(MAIN_DIR, "report.db")

def db_init():
    conn = sqlite3.connect(DB_PATH)
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
    conn = sqlite3.connect(DB_PATH)
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