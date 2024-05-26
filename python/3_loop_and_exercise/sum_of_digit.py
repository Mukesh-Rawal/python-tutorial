num = int(input("Enter a digit: "))

s = 0

while num > 0:
    r = num % 10
    s += r

    num = num // 10

print("Sum", s)
