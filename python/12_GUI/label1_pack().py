from tkinter import *

w = Tk()
w.title("Label1")
w.geometry("300x200")

label1 = Label(w, text="My labels")
label1.pack() #Pack defines position of label

label2 = Label(w, text="Another Label")
label2.pack(side=BOTTOM)

w.mainloop()
