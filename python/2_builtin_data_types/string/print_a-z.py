# WAP to print small a-z:
# Ordinal value for a=97 ... z=122

for i in range(97, 123):
    print(chr(i), end=" ") # chr(): character value

    print(ord(chr(i)), end=" ")
