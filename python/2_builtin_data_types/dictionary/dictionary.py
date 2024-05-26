record = {'Name':'Mukesh', 'Age':32, 'rollno':101}
print(record)

print(type(record))
print(id(record))

print("Name: ", record['Name'])
print("Age: ", record['Age'])
print("Rollno: ", record['rollno'])

print(record.keys())
print(record.values())
print(record.items())       # Print all item in tuple pair
print(record.get('Name'))   # Get value of key
