word = "Hello World!"
print(word)

word = word.lower()
print(word)

print(word.islower())

word = word.upper()
print(word)

print(word.isupper())

print(word.isalpha())
print(word.isdigit())
print(word.isspace())

print(word.startswith("HELLO"))
print(word.endswith("GOOD"))

print(word.find("WORLD"))
print(word.find("WORLD", 8, 11))
print(word.find("RLD", 8, 11))

print(word.count("L"))
print(word.count("D", 6))
print(word.count("D", 6, 11))

print(word.isalnum())
print(word.isdecimal())

word = word.replace('WORLD', 'INCAPP')
word = word.replace(' ', '')
print(word)

print("-".join(['hello', 'hi', 'bye']))

print("I am fine thank you".split())
print("I am fine thank you".split('a'))
