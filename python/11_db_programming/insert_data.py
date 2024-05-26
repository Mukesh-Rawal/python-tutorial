from sqlite3 import *

name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
city = input("Enter student's city: ")

con = connect('Person.db')

cur = con.cursor()          # Stores query related information

cur.execute('insert into Student(name, age, city) values(?, ?, ?)', (name, age, city))

con.commit()            # Fire queries that modify data in database

con.close()         # Close connection

print('Data Saved')
