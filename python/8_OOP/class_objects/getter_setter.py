class person:
    def __init__(self, value):
        self.set_age(value)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0:
            self.__age =0

        elif value > 100:
            self.__age = 100

        else:
            self.__age = value


p = person(120)
print("Age: ", p.get_age())

p.set_age = 45
print("Age: ", p.get_age())

p.set_age = 90
print("Age: ", p.get_age())

