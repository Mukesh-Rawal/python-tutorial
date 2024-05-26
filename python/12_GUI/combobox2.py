from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title("Combobox")
window.geometry("300x200")

city_label = Label(window, text="Select your city")
city_label.grid(row = 0, column = 0)

city_combobox= Combobox(window, state="readonly", value=("Aligarh", "Noida", "Delhi", "Gurugram"))
city_combobox.grid(row=0, column=1)
#city_combobox.current(1)    #Set city by index 1
city_combobox.set("Please select your city")

def submit_button_click():
    if city_combobox.get() != "Please select your city":
        messagebox.showinfo("Message", "Your city: "+city_combobox.get())

    else:
        messagebox.showerror("Message","Please select city first")

button = Button(window, text="Submit", command=submit_button_click)
button.grid(row=1, column=1)

window.mainloop()
