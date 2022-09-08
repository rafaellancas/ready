s = input("Insert your string:")
s = s.lower()
x = []
y = {}

for i in range(len(s)):
    x.append(s[i])

for c in x:
    if c not in y:
        y[c] = 1
    else:
        y[c] += 1


print(y)