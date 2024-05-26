from sqlite3 import *

student_id = int(input("Enter Id: "))
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
city = input("Enter student's city: ")

con = connect('Person.db')

cur = con.cursor()          # Stores query related information

cur.execute('update Student set name = ?, age = ?, city = ? where id = ?', (name, age, city, student_id))

con.commit()            # Fire queries that modify data in database

con.close()         # Close connection

print('Data Updated')
