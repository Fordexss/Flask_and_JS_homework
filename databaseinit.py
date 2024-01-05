import sqlite3

with sqlite3.connect("app.db") as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS test (question TEXT UNIQUE, answers TEXT, correct TEXT)")
