b = int(input("Enter a base: "))

e = int(input("Enter a power: "))

p = 1

for i in range(e):
    p = p*b
print(f"{b} to the power {e} is: ", p)
