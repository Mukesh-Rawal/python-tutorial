class person:
    gender = ""     # Class variable

    def get_data(self):
        print("Gender of person: ", self.gender)


    @classmethod
    def set_data(cls, gender):
        cls.gender = gender


person.set_data("Female")

p = person()
p.get_data()
