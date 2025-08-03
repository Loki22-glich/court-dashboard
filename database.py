# database.py
import sqlite3
from datetime import datetime

def log_query(case_type, case_number, filing_year, raw_html):
    conn = sqlite3.connect("queries.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            timestamp TEXT,
            raw_html TEXT
        )
    """)
    c.execute("INSERT INTO logs VALUES (?, ?, ?, ?, ?, ?)", 
              (None, case_type, case_number, filing_year, datetime.now(), raw_html))
    conn.commit()
    conn.close()
