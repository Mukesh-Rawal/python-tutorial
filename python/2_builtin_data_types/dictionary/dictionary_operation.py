record = {'Name':'Mukesh', 'Age':32, 'rollno':101}
print(id(record))
print(type(record))
print(record)


record['name'] = 'Rahul'    # update, if value not if dict add new
record['Name'] = 'Vikky'    # update value

#or

record.update({'Name':'Shivi'})
print(id(record))
print(record)

for key in record:
    print(key, ':', record[key])


newrecord = record.copy()   # copy dictionary
print("New Record: ",newrecord)


del record['Age']
print(record)

print(record.pop('rollno')) # Remove key value
print(record)

print(record.popitem())     # Remove last added item
print(record)

print('Name' in record)
print('Age' in record)
record.clear()
print(record)
