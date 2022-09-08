list_a = [2,4,5]
list_b = [1,2,3,4]
y = []

for c in range(len(list_a)):
    if list_a[c] not in list_b:
        y.append(list_a[c])

print(y)