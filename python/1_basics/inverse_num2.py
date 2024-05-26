num = int(input("Enter a number: "))

i = 0

while num > 0:
    r = num % 10
    
    i = i*10 + r

    num = num // 10


print("Inverse of given number is: ", i)
