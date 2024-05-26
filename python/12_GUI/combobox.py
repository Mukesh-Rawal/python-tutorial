from tkinter import *
from tkinter.ttk import *
#from tkinter.messagebox import *
from tkinter import messagebox

window = Tk()
window.title("Combobox")
window.geometry("300x200")

city_label = Label(window, text="Select your city")
city_label.grid(row = 0, column = 0)

city_combobox= Combobox(window, value=("Aligarh", "Noida", "Delhi", "Gurugram"))
city_combobox.grid(row=0, column=1)
#city_combobox.current(1)    #Set city by index 1
city_combobox.set("Delhi")

def submit_button_click():
    #showinfo("Message", "Your city: "+city_combobox.get())
    messagebox.showinfo("Message", "Your city: "+city_combobox.get())

button = Button(window, text="Submit", command=submit_button_click)
button.grid(row=1, column=1)

window.mainloop()
