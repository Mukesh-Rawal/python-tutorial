num = {2,4,6,9}
values = {'Mukesh', 34, True}

print(type(num))
print(id(num))
print(num)
print(values)

print(num.add(22))
print(num.remove(4))

#print(num.remove(10))       # Through error if no item in set

print(num.discard(10))      # No error if no item in set
print(num.discard(9))

print(num)

print(2 in num)
print(6 not in num)


num2 = {5,3,6,7,10,44,55,9}

num2.pop()                  # remove random item
print(num2)

#num2.clear()               # clear set

#del num2                   # delete set
print(num2)
