class person:
    def __init__(self, value):
        self.age = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            self.__age =0

        elif value > 100:
            self.__age = 100

        else:
            self.__age = value


p = person(20)
print("Age: ", p.age)

p.set_age = 45
print("Age: ", p.age)

p.set_age = 90
print("Age: ", p.age)

