def add(*nums):
    print(nums)
    s = 0
    for num in nums:
        s = s+num

    print ("Sum", s)

add(10, 2, 6)
