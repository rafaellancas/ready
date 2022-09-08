x = ["a",1,"b",2]
y = []

for c in range(len(x)):
    z = str(x[c])
    y.append(z)

y = " ".join(y)

print(y)