from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

'''
from tkinter import Tk
from tkinter.ttk import Label,Entry, button
from tkinter.messagebox import showinfo
'''

window = Tk()
window.title("Button")
window.geometry("300x200")

label = Label(window, text="Enter your name")
label.grid(row = 0, column = 0)

entry = Entry(window)
entry.grid(row = 0, column = 1)

def button_click():
    name = entry.get()
    showinfo("Message", "Your Name:"+name)
    
button = Button(window, text="Submit", command=button_click)
button.grid(row=1, column=1)

window.mainloop()
