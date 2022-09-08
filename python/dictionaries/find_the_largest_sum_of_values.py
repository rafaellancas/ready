my_dict = {"a": [1, 2, 3], "b": [1, 2, -1], "c": [3, 5, 9], "d": [4, 0, -4]}

j = []
y = []

for i in range(len(my_dict)):    
    y = list(my_dict.values())
    j.append(sum(y[i]))

print(max(j))

