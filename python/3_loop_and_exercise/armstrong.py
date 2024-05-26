# 125 = 1**3 + 2**3 + 5**3
# 2235 = 2**4 + 2**4 + 3**4 + 5**4

num = int(input("Enter a number: "))

x = num
s = 0

while num > 0:
    r = num % 10
    s = s + r**3
    num = num // 10
print(s)

if x == s:
    print("Number is Armstrong")

else:
    print("Number is not Armstrong")
