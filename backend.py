import sqlite3 #to use sqlite commands

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor() #cursor object allows you to select rows
        self.cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, Author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self, title, Author, year, isbn):
        self.cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title, Author,year,isbn))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", Author="", year="", isbn=""):
        # set default input as empty strings
        self.cur.execute("SELECT * FROM books WHERE title = ? OR Author = ? OR  year=? OR  isbn=?", (title, Author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id = ?", (id,))
        self.conn.commit()


    def update(self,id, title, Author, year, isbn):
        self.cur.execute("UPDATE books SET title = ?, Author = ? , year = ?,  isbn=? WHERE id =?", ( title, Author, year, isbn, id))
        #make sure they are in the right order
        self.conn.commit()
        self.conn.close()

    def __del__(self):
        self.conn.close()


#insert('New book', 'Manbook', 2018, 2789429033)
#print(search(Author="ken smith"))
#update('New book', 'Unk jim', 1983, 3789429033)
#delete(2)
#print(view())

