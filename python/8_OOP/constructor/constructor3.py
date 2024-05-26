class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        return "Name: " + self.name + "\nAge: " + str(self.age)


p1 = person(input("Enter Name: "), int(input("Enter Age: ")))
print(p1.print_data())

p2 = person(input("Enter Name: "), int(input("Enter Age: ")))
print(p2.print_data())
