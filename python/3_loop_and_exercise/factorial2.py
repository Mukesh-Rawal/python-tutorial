# 5! = 5x4x3x2x1

num = int(input("Enter a number: "))

if num >= 0 and num <= 10:

    if num == 0 or num == 1:
        print("Factorial of given number is 1")

    else:
        f = num

        for i in range(1,num):
            f = f*i
        print("Factorial of given number: ", f)


else:
    print("Enter a number between 1 to 10")
