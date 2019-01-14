from tkinter import *
import backend

#backend :- this allows us to use functions from the backend.py file
def get_selected_row(event):
    global select_tuple
    index=list1.curselection()[0] # this the to grab the first index
    select_tuple = list1.get(index) #list1.get() is to select the data of the selected index
    #Allow selected row to shoe in fields
    e1.delete(0, END) #Empty the field
    e1.insert(END, select_tuple[1])
    e2.delete(0, END) #Empty the field
    e2.insert(END, select_tuple[2])
    e3.delete(0, END) #Empty the field
    e3.insert(END, select_tuple[3])
    e4.delete(0, END) #Empty the field
    e4.insert(END, select_tuple[4])

def veiw_command():
    list1.delete(0,END)#this is to delete everthing from index of 0 to the end: stops repitition
    for row in backend.view():
        list1.insert(END,row)#END is used to put the others at the end of the first one

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),Auth_text.get(),year_text.get(), isb_text.get()): #.get() allows you to get the exact string
        list1.insert(END,row)

def insert_command():
    backend.insert(title_text.get(),Auth_text.get(),year_text.get(), isb_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),Auth_text.get(),year_text.get(), isb_text.get())) # this will show the values entered
    #Clear fields after adding input
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def delete_command():
    backend.delete(select_tuple[0])
    list1.delete(0,END)
    for row in backend.view(): #this is to display all other enteries after a delete
        list1.insert(END,row)

def delete_command():
    backend.update(select_tuple[1],select_tuple[2],select_tuple[3],select_tuple[4])

#backend


#tkinter
window = Tk()

l1 = Label(window, text = "Title")
l1.grid(row=0, column=0)

l2 = Label(window, text = "Author")
l2.grid(row=0, column=2)

l3 = Label(window, text = "Year")
l3.grid(row=1, column=0)

l4 = Label(window, text = "ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row=0,column= 1)

year_text = StringVar()
e2 = Entry(window, textvariable = year_text)
e2.grid(row=1,column= 1)

Auth_text = StringVar()
e3 = Entry(window, textvariable = Auth_text)
e3.grid(row=0,column= 3)

isb_text = StringVar()
e4 = Entry(window, textvariable = isb_text)
e4.grid(row=1,column= 3)

list1 = Listbox(window, height = 6, width = 30)
list1.grid(row = 3, column = 0, rowspan = 4, columnspan = 2)

#creat scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=3, column=2, rowspan = 4, columnspan = 1)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command=list1.yview)
#creat scrollbar

#list bind allow u to select a row
list1.bind('<<ListboxSelect>>', get_selected_row)


b1=Button(window,text="View all", width=12, command = veiw_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12, command = search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12, command = insert_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12, command = delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12)
b6.grid(row=7,column=3)


window.mainloop()

#tkinter