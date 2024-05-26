class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    def print_data(self):
        print("Name: ", self.fname, self.lname)

persons = []

for i in range(int(input("How many person's details you want to store: "))):
    print("Input detail of person: ", i+1)
    p = person(input("Enter first name: "), input("Enter last name: "))
    
    persons.append(p)

print("Detail of persons: ")
for per in persons:
    per.print_data()

