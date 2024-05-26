nums = [4, 7, 8, 6, 5, 9, 76, 6, 8, 76, 65, 77]
print(nums)
print(id(nums))

nums.append(43)         # add value in last
print(nums)
print(id(nums))         # Mutable data type

nums.insert(2, 32)      # insert value at index
print(nums)

nums.extend([2,5,7])
print(nums)             # extend list

nums.remove(6)
print(nums)             # remove first accuring value


nums.pop()              # remove last item
print(nums)

nums.pop(5)             # remove index with value
print(nums)

print(nums.index(8))    # index of given value
print(nums.count(8))    # count of value

nums.reverse()          # reverse list
print(nums)

nums.sort()             # sort default accending order
print(nums)

#nums.clear()           # clear values from list
print(nums)

del nums[4]             # delete index
print(nums)
