from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Button")
window.geometry("300x200")

def button_click():
    label=Label(window, text="You have clicked")
    label.pack()

button = Button(window, text="Click here", command=button_click)
button.pack()

window.mainloop()
