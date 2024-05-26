# 121, 13431, 54345 Are P121alindrome numbers

num = int(input("Enter the number: "))

x = num
i = 0

while num > 0:
    r = num % 10
    i = i*10 + r
    num = num//10


print (i)

if x == i:
    print("Number is palindrome")

else:
    print("Not palindrome")
