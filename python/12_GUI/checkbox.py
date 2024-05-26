from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title("Checkbox")
#window.geometry("300x200")

label = Label(window, text="Select your known language")
label.grid(row = 0, column = 0)

c, cpp, python, java = IntVar(), IntVar(), IntVar(), IntVar()

c_checkbutton= Checkbutton(window, text="c", variable=c)
c_checkbutton.grid(row=0, column=1)

cpp_checkbutton= Checkbutton(window, text="c++", variable=cpp)
cpp_checkbutton.grid(row=0, column=2)

python_checkbutton= Checkbutton(window, text="python", variable=python)
python_checkbutton.grid(row=0, column=3)

java_checkbutton= Checkbutton(window, text="java", variable=java)
java_checkbutton.grid(row=0, column=4)

def submit_button_click():
    known_language = ""
    
    if c.get() ==1:
        known_language += "c,"

    if cpp.get() ==1:
        known_language += "c++,"

    if python.get() ==1:
        known_language += "python,"

    if java.get() ==1:
        known_language += "java,"

    if known_language != "":
        known_language = known_language[:-1]
        messagebox.showinfo("Message","Languages(s) you know: " + known_language)

    else:
        messagebox.showerror("Message","Please select a language")

button = Button(window, text="Submit", command=submit_button_click)
button.grid(row=1, column=1)

window.mainloop()
