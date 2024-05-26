class student:
    def input_details(self):
        self.name = input("Enter Name: ")
        self.collage = input("Enter Collage: ")

    def print_data(self):
        print("Student Name: ", self.name)
        print("Student Collage: ", self.collage)

p1 = student()
p2 = student()

student.input_details(p1)
student.print_data(p1)

student.input_details(p2)
student.print_data(p2)
