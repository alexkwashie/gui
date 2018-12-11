import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor() #cursor object allows you to select rows
    cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, Author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def insert(title, Author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title, Author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows


connect()

insert('mong jim', 'jonah hill', 1528, 87582925)

print(view())

