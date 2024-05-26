a = 5               #Global variable
print (a)

def display():
    global a        # Global keyword
    a = 4
    print (a)

display()

print (a)       
