my_dict = {"a": [4, 3, 2], "b": [5, 3, 7], "c": [13, 9, 10], "d": [3, 4, 1]}

x = []
j = []
y = {}

for i in my_dict:
    x.append(sorted(my_dict[i]))
    j.append(i)

for c in range(len(my_dict)):
    y[j[c]] = x[c]
 
print(y)
