nums = (1, 2, 3, 4, 5, 6, 5, 6, 9)

print(nums[3])
print(nums[-4])

print("Transversing tuple using forward indexing")

for i in range(len(nums)):
    print(nums[i], end="")

print()
print("Transversing tuple using backword indexing")

for i in range(-1, -len(nums)-1, -1):
    print(nums[i], end="")

print()
print("Transversing tuple without indexing")

for num in nums:
    print(num, end="")
