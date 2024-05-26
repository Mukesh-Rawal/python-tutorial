# 0,1,1,2,3,5,8,13,21,34....

first = 0
second = 1
num = int(input("Upto which element: "))
print(first)
print(second)



for i in range(1, num):
    third = first+second
    print(third)
    first, second = second, third
