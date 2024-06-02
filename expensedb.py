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

def view_expense():
    with conn:
        command = 'SELECT * FROM expense'
        c.execute(command)
        result = c.fetchall()
    print(result)
    return result

def delete_expense(ID):
    with conn:
        command = 'DELETE FROM expense WHERE ID=(?)'
        c.execute(command,([ID]))
    conn.commit()

def update_expense(ID,field,newvalue):
    with conn:
        command = 'UPDATE expense SET {} = (?) WHERE ID=(?)'.format(field)
        c.execute(command,(newvalue,ID))
    conn.commit()



#insert_expense('A','B','C','D')
#delete_expense(4)
#update_expense(3,'title','น้ำแข็งไสโบราณ')
view_expense()
