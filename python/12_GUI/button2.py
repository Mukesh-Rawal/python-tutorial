from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

window = Tk()
window.title("Button")
window.geometry("300x200")

def button_click():
    showerror("Message","You have clicked me")
button = Button(window, text="Click here", command=button_click)
button.pack()

window.mainloop()
