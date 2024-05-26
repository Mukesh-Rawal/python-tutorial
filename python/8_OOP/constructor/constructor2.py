class person:
    def __init__(self):
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")

    def print_data(self):
        print("Message: ", self.name, "\nAge: ", self.age)


p1 = person()
p1.print_data()
