nums = [2,3,6,4,5,8,9]

def even(a):
    if a%2 == 0:
        return True

e = list(filter(even, nums))
print(e)
