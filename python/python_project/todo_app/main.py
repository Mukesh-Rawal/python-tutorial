from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox

class todo_window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("ToDo App")
        self.geometry("600x450")
        self.resizable(False, False)

        style = Style()

        style.configure('Header.TFrame', background = 'blue')
        header_frame = Frame(self, style="Header.TFrame")
        header_frame.pack(fill = X)

        style.configure('Header.TLabel', background = 'blue', foreground ='white', font=('Arial', 25))
        header_label = Label(header_frame, text = "ToDo App", style = 'Header.TLabel')
        header_label.pack(pady = 10)

        style.configure('Content.TFrame', background = 'white')
        content_frame = Frame(self, style="content.TFrame")
        content_frame.pack(fill = BOTH, expand = TRUE)

        style.configure('Content.TLabel', background = 'white', foreground ='blue', font=('Arial', 15))
        content_label = Label(content_frame, text = "New Task", style = 'Content.TLabel')
        content_label.grid(row=0, column=0, padx=5, pady=10)

        self.new_task_entry = Entry(content_frame, font = ('Arial', 15), width = 30)
        self.new_task_entry.grid(row=0, column=1, pady=10)

        style.configure('Content.TButton', foreground = 'blue', font = ('Arial', 15))
        add_button = Button(content_frame, text = 'Add', style='Content.TButton', command = self.add_button)
        add_button.grid(row=0, column=2, padx=5, pady=10)

        style.configure('Treeview.Heading', foreground ='blue', font=('Arial', 15))
        style.configure('Treeview', font = ('Arial', 12))

        self.tasks_treeview = Treeview(content_frame, columns = ('title',), show = 'headings', height = 12)
        self.tasks_treeview.grid(row = 1, column = 0, columnspan = 2, pady = 10)
        self.tasks_treeview.heading('title', text = "Title", anchor = W)
        self.tasks_treeview.column('title', width = 440)
        self.tasks_treeview.bind('<<TreeviewSelect>>', self.tasks_treeview_row_selection)

        style.configure('Delete.TButton', foreground = 'red', font = ('Arial', 15))
        delete_button = Button(content_frame, text = 'Delete', style = 'Delete.TButton', command = self.delete_button_click)
        delete_button.grid(row = 1, column = 2, padx = 5, pady = 10, sticky = N)


        self.con = connect('D:/python/python/python_project/todo_app/todo.db')
        self.cur = self.con.cursor()
        self.fill_tasks_treeview()
        self.is_any_task_selected = False


    def fill_tasks_treeview(self):
        for task in self.tasks_treeview.get_children():
            self.tasks_treeview.delete(task)
        
        self.cur.execute("select * from Task")

        tasks = self.cur.fetchall()

        for task in tasks:
            self.tasks_treeview.insert("", END, values = task)
        

    def add_button(self):
        if self.new_task_entry.get() != "":
            self.cur.execute("select * from Task where Title = ?", (self.new_task_entry.get(),))
            if self.cur.fetchone() is None:
                self.cur.execute("insert into Task(Title) values(?)", (self.new_task_entry.get(),))
                self.con.commit()
                messagebox.showinfo("Success Message", 'Task is added successfully')
                self.fill_tasks_treeview()
            else:
                messagebox.showerror("Error Message", 'Task is already added')
        else:
            messagebox.showerror("Error Message", 'Please enter the Task')


    def tasks_treeview_row_selection(self, event):
        self.is_any_task_selected = True
        self.task = self.tasks_treeview.item(self.tasks_treeview.selection())['values']
            
    def delete_button_click(self):
        if self.is_any_task_selected:
            if messagebox.askquestion('Confirmation Message', 'Are you sure to delete?') == 'yes':
                self.cur.execute("delete from Task where Title = ?", (self.task[0],))
                self.con.commit()
                self.fill_tasks_treeview()
                messagebox.showerror("Error Message", 'Task is deleted added')
                self.is_any_task_selected = False
                
        else:
            messagebox.showerror("Error Message", 'Please select the Task')            


tdw = todo_window()
tdw.mainloop()
