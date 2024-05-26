class person:
    city = ""
    company = ""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    def print_data(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("City: ", self.city)
        print("Mail: ", self.company)

    def change_age(self, new_age):
        self.age = new_age

    @classmethod
    def set_data(cls, company, city):
        cls.city = city
        cls.company = company

    @classmethod
    def change_company(cls, new_comp):
        cls.company = new_comp



person.set_data("TCS", "Noida")

p1 = person("Rohit", 22)
p1.print_data()

p1.change_age(24)
p1.print_data()


person.change_company("Wipro")
p1.print_data()
