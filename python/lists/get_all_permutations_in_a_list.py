from itertools import permutations

x = [1, 2, 3]
y = permutations(x)
 
for i in list(y):
    print(list(i))