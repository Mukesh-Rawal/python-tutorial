class person:
   
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def print_person_data(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


class student(person):
    def __init__(self, name, age, rollno):
        person.__init__(self, name, age)
        self.rollno= rollno

    def print_student_data(self):
        print("Rollno: : ", self.rollno)


class employee(person):
    def __init__(self, name, age, salary):
        person.__init__(self, name, age)
        self.salary= salary

    def print_student_data(self):
        print("Salary: : ", self.salary)

        
s = student("Neha", 22, 101)
s.print_person_data()
s.print_student_data()


e = employee("Shivi", 33, 25000)
e.print_person_data()
e.print_student_data()
