num = int(input("Enter a number: "))


while num != 0:
    r = num % 10

    print(r, end="")

    num = num // 10
