import os

# file = open("index.txt", "r")

# data = file.read()
# print(data)
# print(type(data))

# file.close()

with open("D:/python/python/file_i_o.py/demo.txt", "r") as f:
    data = f.read()
    print(data)

os.remove('D:/python/python/file_i_o.py/index.txt')