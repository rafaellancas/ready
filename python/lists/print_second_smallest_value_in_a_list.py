x = [1,2,3,4]
y = []

if len(x) < 2:
    print("None")
else:
    x.pop(x.index(min(x)))
    y.append(min(x))
    print(y)