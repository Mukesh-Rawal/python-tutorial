from sqlite3 import *


con = connect('Person.db')
cur = con.cursor()          # Stores query related information

cur.execute('select * from Student')
students = cur.fetchmany(2)

print(students)
con.close()         # Close connection

print("Details of two person are: ")

for i in students:
    #print(i)
    print("Student Id: ", i[0])
    print("Student Name: ", i[1])
    print("Student Age: ", i[2])
    print("Student City: ", i[3])
    print()
