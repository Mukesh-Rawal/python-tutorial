from tkinter import *

w = Tk()
w.title("Label1")
w.geometry("300x200")

label1 = Label(w, text="Hello")
label1.grid(row=0, column=0)

label2 = Label(w, text="Hi")
label2.grid(row=0, column=1)

label3 = Label(w, text="Welcome")
label3.grid(row=1, column=0)

label4 = Label(w, text="Bye")
label4.grid(row=1, column=1)

w.mainloop()
