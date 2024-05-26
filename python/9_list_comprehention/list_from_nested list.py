nums = [[1,2,3], [4,5,6], [3,4,5]]

new_list = [item for sublist in nums for item in sublist]
print(new_list)
