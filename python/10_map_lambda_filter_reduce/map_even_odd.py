def even_odd(num):
    if num%2 == 0:
        print("The number {} is even".format(num))
    else:
        print( "The number {} is odd".format(num))

#print(even_odd(int(input("Enter the number: "))))

lst = [3,4, 2, 5, 6,7 ,9]
maped_list = list(map(even_odd, lst))

