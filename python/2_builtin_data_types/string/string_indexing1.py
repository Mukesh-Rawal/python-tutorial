word = "Hello World"

print(word[3])
print(word[-4])

print("Transversing string using forward indexing")

for i in range(len(word)):
    print(word[i], end="")

print("Transversing string using backword indexing")

for i in range(-1, -len(word)-1, -1):
    print(word[i], end="")

print("Transversing string without indexing")

for character in word:
    print(character, end="")
