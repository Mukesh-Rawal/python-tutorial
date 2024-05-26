
from sqlite3 import *

con = connect('D:/python/python/11_db_programming/Person.db')
#print("Connected")

cur = con.cursor()          # Stores query related information

cur.execute('insert into Student(name, age, city) values("Raaj", 23, "Aligarh")')

con.commit()            # Fire queries that modify data in database

con.close()         # Close connection

print('Data Saved')
