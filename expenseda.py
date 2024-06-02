import sqlite3

conn = sqlite3.connect('expensedb.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS expense (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                dt TEXT,
                title TEXT,
                price REAL,
                ptype TEXT
            )""")


def insert_expense(dt,title,price,ptype):
    with conn:
        command = 'INSERT INTO expense VALUES (?,?,?,?,?)'
        c.execute(command,(None,dt,title,price,ptype))
    conn.commit()

insert_expense('A','B','C','D')