x = [6,4,5]
y = [1,2,3]
z = []

for c in range(len(x)):
    if x[c] in y:
        z.append(x[c])

print(z)