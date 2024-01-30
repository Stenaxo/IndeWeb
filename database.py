import sqlite3
from datetime import datetime

def create_database():
    conn = sqlite3.connect('crawler.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS crawled_pages (url TEXT PRIMARY KEY, age TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_to_database(url):
    conn = sqlite3.connect('crawler.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO crawled_pages (url, age) VALUES (?, ?)', (url, datetime.now()))
    conn.commit()
    conn.close()
