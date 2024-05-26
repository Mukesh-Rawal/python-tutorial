from sqlite3 import *
student_id = int(input("Enter Student Id: "))

con = connect('Person.db')

cur = con.cursor()          # Stores query related information

cur.execute('delete from Student where id =?', (student_id,))

con.commit()            # Fire queries that modify data in database

con.close()         # Close connection

print('Data Deleted')
