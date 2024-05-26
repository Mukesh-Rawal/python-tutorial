num = 100
div_num = [i for i in range(2, num+1) if all(i%j != 0 for j in range(2, i//2 +1))]
print(div_num)


# need explanation
