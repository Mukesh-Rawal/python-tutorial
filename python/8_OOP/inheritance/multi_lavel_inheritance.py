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
        self.rollno = rollno

    def print_student_data(self):
        print("Rollno: : ", self.rollno)


class result(student):
    def __init__(self, name, age, rollno, marks1, marks2, marks3):
        student.__init__(self, name, age, rollno)
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def print_student_data(self):
        self.per = (self.marks1 + self.marks2 + self.marks3) / 3
        
        print("Name: : ", self.name)
        print("Age: : ", self.age)
        print("Roll no.  ", self.rollno)
        print("Percentage: ", round(self.per, 2))

        
s = result("Neha", 22, 101, 55, 60, 84)
s.print_student_data()
