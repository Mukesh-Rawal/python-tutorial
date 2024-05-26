fib = [0,1,1,2,3,5,8,13,21,34]

fib2 = [fib[i-1]+fib[i-2] for i in range(2, len(fib))]
print(fib2)
