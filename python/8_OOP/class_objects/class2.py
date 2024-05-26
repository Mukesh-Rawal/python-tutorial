class student:
    def input_details(self):
        self.name = input("Enter Name: ")
        self.collage = input("Enter Collage: ")

    def print_data(self):
        print("Student Name: ", self.name)
        print("Student Collage: ", self.collage)

s1 = student()
s2 = student()

s1.input_details()
s1.print_data()

s2.input_details()
s2.print_data()
