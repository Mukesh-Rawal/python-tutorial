nums = set()
print(type(nums))

while True:
    nums.add(int(input("Enter number: ")))
    print(nums)

    ch = input("Enter y to continue adding numbers: ")
    if ch.lower() != "y":
        break
    

while True:
    num = int(input("Enter number to remove: "))
    if num in nums:
        nums.remove(num)
        print(nums)

    else:
        print(num, "is not present")

    ch = input("Enter y to continue remove numbers: ")
    if ch.lower() != "y":
        break
