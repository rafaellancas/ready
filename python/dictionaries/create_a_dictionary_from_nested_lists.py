list = [['a', 1], ['b', 2], ['c', 3], ['d', 4]]
dict = {}

for i in range(len(list)):
    a = list[i]
    dict[a[0]] = a[1]

print(dict)