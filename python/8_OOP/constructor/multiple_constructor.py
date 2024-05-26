class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def print_data(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\nCity: " + self.city

#'''
p1 = person("Mukesh", 33)
print(p1.print_data())
#'''

p2 = person("Shivi", 21, "Aligarh")
print(p2.print_data())



# When we add two __init__ class latest one will be execute
