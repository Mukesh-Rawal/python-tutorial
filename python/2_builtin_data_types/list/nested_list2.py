s = []

n1 = int(input("Enter number of student: "))
n2 = int(input("Enter number of subject: "))

for i in range(n1):
    m = []
    print("Input details of student: ", i+1)

    for j in range(n2):
        m.append(int(input("Enter the marks of subject: ")))

    s.append(m)

print(s)
