from sqlite3 import *

conn = connect('D:/python/python/11_db_programming/db_conn/incapp_python.db')
print(type(conn))

cur = conn.cursor()
print(type(cur))

cur.execute("insert into Person(name, age, city) values('Mahi', 17, 'Agra')")
conn.commit()
conn.close()
print("Data saved")
