x = [1,2,3,4]
y = []

if len(x) < 2:
    print("None")
else:
    x.pop(x.index(max(x)))
    y.append(max(x))
    print(y)


