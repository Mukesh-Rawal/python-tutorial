# Normal Way

list1 = []

for i in range(1,21):
    list1.append(i)
print("List without comprehention: ", list1)


nums = []
for i in range(1,6):
    nums.append(i**2)
print(nums)

# List comprehention

list2 = [i for i in range(1,11)]
print("List with comprehention: ",list2)
