notas = ["C", "D", "E", "F", "G", "A", "B"]
index = 1

for item in range(len(notas)):
    if index <= 3:
        print("A escala maior de",(notas[(index-1)]),"é",(notas[(index-1)]),(notas[(index+1)]),(notas[(index+3)]))
        index += 1
    elif index == 3:
         print("A escala maior de",(notas[(index-1)]),"é",(notas[3]),(notas[5]),(notas[0]))
         index += 1
    elif index == 4:
         print("A escala maior de",(notas[(index-1)]),"é",(notas[3]),(notas[5]),(notas[0]))
         index += 1
    elif index == 5:
         print("A escala maior de",(notas[(index-1)]),"é",(notas[4]),(notas[6]),(notas[1]))
         index += 1
    elif index == 6:
         print("A escala maior de",(notas[(index-1)]),"é",(notas[5]),(notas[0]),(notas[2]))
         index += 1
    else:
        print("Isso é tudo!")

        
    
