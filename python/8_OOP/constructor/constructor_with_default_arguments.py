class person:
    def __init__(self, name, age, city= None, mail=None, ):
        self.name = name
        self.age = age
        self.city = city
        self.mail = mail

    def print_data(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("City: ", self.city)
        print("Mail: ", self.mail)
       
p2 = person("Shivi", 21, "Aligarh")
p2.print_data()

p1 = person("Mike", 27, "Bmb", "mike221@gmail.com")
p1.print_data()

