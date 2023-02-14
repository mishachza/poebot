import sqlite3 as sl

con = sl.connect('.db')

with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            date INTEGER,
            time TEXT
        );
    """)

sql = 'INSERT INTO USER (id, product, date, time) values(?, ?, ?)'
data = [
    (1, 'Onion', '20.05.2023', '10:00'),

]