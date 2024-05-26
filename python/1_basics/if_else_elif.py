# WAP to check entered age is minor, adult or senior citison

age = int(input("Enter age: "))

if age > 0 and age < 120:

    if age < 18 and age > 0:
        print("Minor")

    elif age > 18 and age < 60:
        print("Adult")

    else:
        print("Senior citison")

else:
    print("Enter valid age")
