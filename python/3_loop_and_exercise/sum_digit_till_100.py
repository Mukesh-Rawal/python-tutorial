for i in range(1,101):
    s = 0
    j = i

    while j>0:
        d = j % 10
        s = s + d
        j = j//10

    print("Sum of digit",i, "is", s)
