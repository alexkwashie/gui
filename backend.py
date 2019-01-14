import sqlite3  #to use sqlite commands

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

def search(title="", Author="", year="", isbn=""):
    # set default input as empty strings
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR Author = ? OR  year=? OR  isbn=?", (title, Author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, title, Author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET Author = ?,  year=?,  isbn=? WHERE title = ?", ( Author, year, isbn, title, id))
    #make sure they are in the right order
    conn.commit()
    conn.close()


connect()

#insert('New book', 'Manbook', 2018, 2789429033)
#print(search(Author="ken smith"))
#update('New book', 'Unk jim', 1983, 3789429033)
#delete(2)
print(view())

