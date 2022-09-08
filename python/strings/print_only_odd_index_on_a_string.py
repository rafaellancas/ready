word = input("Insert your word:")
new = ""

for i in range(len(word)):
    if i % 2 != 0:
        new += word[i]

print(new)
