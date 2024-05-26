from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title("Listbox")

label = Label(window, text="Select your known language")
label.grid(row = 0, column = 0)


lang_listbox = Listbox(window, selectmode = EXTENDED, height = 5)       #EXTENDED can select one or more value

for language in ("c", "c++", "python", "java"):
    lang_listbox.insert(END, language)      # END default is 0 and increase by 1 in loop
    
lang_listbox.grid(row=0, column=1)


def submit_button_click():
    selected_languages = []
    
    for i in lang_listbox.curselection():       #curselection() select index of selected value
        selected_languages.append(lang_listbox.get(i))

    known_languages = ",".join(selected_languages)
    messagebox.showinfo("Message", "Language you known: "+known_languages)

button = Button(window, text="Submit", command=submit_button_click)
button.grid(row=1, column=1)

window.mainloop()
