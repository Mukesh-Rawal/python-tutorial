from tkinter import Tk

class window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, *kwargs)

        self.title("Window using Class")
        self.geometry("300x200")

w = window()
w.mainloop()
