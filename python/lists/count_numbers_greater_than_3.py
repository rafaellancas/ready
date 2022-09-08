list = [2,3,4,0,1,7,2,8,9]
j = 0

for c in range(len(list)):
    if list[c] > 3:
        j += 1

print(j)