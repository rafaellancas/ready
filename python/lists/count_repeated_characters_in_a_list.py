x = ["a", "a", "b", "c", "a", "b"]
y = {}


for c in x:
    if c not in y:
        y[c] = 1
    else:
        y[c] += 1
   
print(y)