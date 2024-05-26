from functools import reduce



nums = [2,3,4,5,6,7,9,9]

e_num = list(filter(lambda n: n%2 ==0, nums))
print(e_num)

sums = reduce(lambda a,b: a+b, e_num)
print(sums)
