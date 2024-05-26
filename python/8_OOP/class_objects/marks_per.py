class student:
    def get_details(self):
        self.name = input("Enter Name: ")

        while True:
            self.rollno = int(input("Enter Roll No: "))
            if self.rollno >= 0 and self.rollno <=1000:
                break
            else:
                print("Please enter currect roll number")
        
        while True:
            self.phy = int(input("Enter Physics marks: "))
            if self.phy >= 0 and self.phy <=100:
                break
            else:
                print("Input marks between 1 to 100")

        while True:
            self.che = int(input("Enter chemistry marks: "))
            if self.che >= 0 and self.che <=100:
                break
            else:
                print("Input marks between 1 to 100")

        while True:
            self.math = int(input("Enter math marks: "))
            if self.math >= 0 and self.math <=100:
                break
            else:
                print("Input marks between 1 to 100")
        

    def find_result(self):
        self.total = self.phy+self.che+self.math
        self.per = self.total/300 * 100

    def print_data(self):
        print("Name: ", self.name)
        print("Roll no: ", self.rollno)
        print("Percentage: ", round(self.per, 2))


s1 = student()
s1.get_details()
s1.find_result()
s1.print_data()
