class person:
    def __init__(self, age):
        self.age = age

    def print_data(self):
        print("Age: ", self.age)


p = person(52)
p.print_data()


print("Age: ", p.age)

p.age = 45

p.print_data()
