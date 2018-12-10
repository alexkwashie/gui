'''
from tkinter import *

window= Tk()

def kmtom():
    txt = int(e1_value.get()) * 10
    t1.insert(END,txt)

b1 = Button(window, text = "Effect", command =kmtom )
b1.grid(row = 0 , column = 0)

e1_value = StringVar()

e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0 , column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row=0, column=2)



window.mainloop()


'''

import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor() #cursor object allows you to select rows
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, Quantity INTEGER, Price REAL)")
    cur.execute("INSERT INTO store VALUES ('Wine Glass',8, 10.5)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

insert('bags', 4, 2.7)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?",[item])
    conn.commit()
    conn.close()

def update(quantity, price,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price =? WHERE item = ?",(quantity, price, item))
    conn.commit()
    conn.close()

update(48,5.3 , 'bags')

print(view())




