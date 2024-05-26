from sqlite3 import *

student_id = input("Enter student Id: ")

con = connect('Person.db')
cur = con.cursor()          # Stores query related information

cur.execute('select * from Student where id = ?', (student_id,))
student = cur.fetchone()

print(student)
con.close()         # Close connection

print("Details student is: ")

if student is not None:
    #print(i)
    print("Student Id: ", student[0])
    print("Student Name: ", student[1])
    print("Student Age: ", student[2])
    print("Student City: ", student[3])
    print()

else:
    print("Person of Id" + student_id + "does not exist")
