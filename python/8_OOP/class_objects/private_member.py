class person:
    def __init__(self, age):
        self.__age = age        # __privatemember

    def print_data(self):
        print("Age: ", self.__age)


p = person(52)
p.print_data()


print("Age: ", p.__age)

p.__Nage = 45

p.print_data()
