s = input("Insert your word or sentence:")
y = len(s)
z = []

for i in range(len(s)): 
    y -= 1
    x = (s[y])
    if x.islower() == True:
        x = x.upper()
        z.append(x)
    else:
        x = x.lower()
        z.append(x)
    
print("".join(z))

        
    
    