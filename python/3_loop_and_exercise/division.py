p = float(input("Enter physics marks: "))

c = float(input("Enter chemistry marks: "))

m = float(input("Enter math marks: "))

h = float(input("Enter hindi marks: "))

e = float(input("Enter english marks: "))

t = p+c+m+h+e

pr = t/5

print("Total", t)


if pr >= 60:
    print("First division with ", pr,"%")

elif pr >= 45 and pr <= 59:
    print("Second division with ", pr,"%")

elif pr >= 33 and pr <45:
    print("Third division with ", pr,"%")

else:
    print("Better luck next time")
