from tkinter import Tk
from tkinter.ttk import *
from tkinter import messagebox

class window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, *kwargs)

        self.title("Window using Class")
        self.geometry("300x200")

        b = Button(self, text= "Click Here", command = self.on_click)
        b.pack()

    def on_click(self):
        messagebox.showinfo("Message", "You have clicked")

w = window()
w.mainloop()
