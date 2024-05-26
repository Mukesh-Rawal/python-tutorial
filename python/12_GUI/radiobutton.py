from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title("Radio Button")
window.geometry("300x200")

gender_label = Label(window, text="Select your gender")
gender_label.grid(row = 0, column = 0)

gender = IntVar()
#gender.set(2)

male_radiobutton = Radiobutton(window, text="Male", value=1, variable=gender)
male_radiobutton.grid(row = 0, column = 1)

female_radiobutton = Radiobutton(window, text="Female", value=2, variable=gender)
female_radiobutton.grid(row = 0, column = 2)

def submit_button_click():
    if gender.get() == 1:
        messagebox.showinfo("Output","Your gender: Male")

    elif gender.get() == 2:
        messagebox.showinfo("Output","Your gender: Female")

    else:
        messagebox.showerror("Message","Please select gender")

button = Button(window, text="Submit", command=submit_button_click)
button.grid(row=1, column=1)

window.mainloop()
