class person:
   
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


class student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno= rollno

    def print_data(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Rollno: : ", self.rollno)
        

p = person("Mike", 33)
p.print_data()

s = student("Neha", 22, 101)
s.print_data()



# here we are writing same code again and again
