from tkinter import *

window = Tk()
window.title("My First Page")
window.geometry("350x200")

label1 = Label(window, text="MY window text")
label1.place(x=10, y=10)

label2 = Label(window, text="MY window details")
label2.place(x=110, y=110)

window.mainloop()
