list = [1,2,1,2,1,3,5,6,4]
y = []

for c in range(len(list)):
    if list[c] not in y:
        y.append(list[c])
        
        
print(sorted(y))
