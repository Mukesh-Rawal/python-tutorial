from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

window = Tk()
window.title("Button")
window.geometry("300x200")

label = Label(window, text="Enter a Number")
label.grid(row = 0, column = 0)

entry = Entry(window)
entry.grid(row = 0, column = 1)

def button_click():
    while True:
        try:
            num = int(entry.get())
            num+=1
            showinfo("Message", "Your Name:"+str(num))
            break
        except ValueError:
            showinfo("Message","Enter valid number")
            break
    
button = Button(window, text="Number increse by 1", command=button_click)
button.grid(row=1, column=1)

window.mainloop()
