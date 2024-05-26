from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Treeview")
window.geometry("500x300")

treeview = Treeview(window, columns = ('name', 'age', 'city'), show='headings')
treeview.heading('name', text='Name')
treeview.heading('age', text='Age')
treeview.heading('city', text='City')

treeview.column('name', width=250)
treeview.column('age', width=150)
treeview.column('city', width=200)

treeview.insert('', END, values=('Mukesh', 23, 'Noida'))
treeview.insert('', END, values=('Manish', 20, 'Delhi'))
treeview.insert('', END, values=('rizwan', 19, 'Gurugram'))

treeview.pack()

window.mainloop()
