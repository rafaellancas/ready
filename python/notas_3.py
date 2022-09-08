escalasmaiores = {"C":["C","D","E","F","G","A","B"],
                  "D":["D","E","F#","G","A","B","C#"],
                  "E":["E","F#","G#","A","B","C#","D#"],
                  "F":["F","G","A","Bb","C","D","E"],
                  "G":["G","A","B","C","D","E","F#"],
                  "A":["A","B","C#","D","E","F#","G#"],
                  "B":["B","C#","D#","E","F#","G#","A#"],
                  "C#":["C#","D#","E#","F#","G#","A#","B#"],
                  "F#":["F#","G#","A#","B","C#","D#","E#"],
                  "Bb":["Bb","C","D","Eb","F","G","A"],
                  "Eb":["Eb","F","G","Ab","Bb","C","D"],
                  "Ab":["Ab","Bb","C","Db","Eb","F","G"],
                  "Db":["Db","Eb","F","Gb","Ab","Bb","C"],
                  "Gb":["Gb","Ab","Bb","Cb","Db","Eb","F"],
                  "Cb":["Cb","Db","Eb","Fb","Gb","Ab","Bb"]
                  }
escalasmenores = {"C":["C","D","Eb","F","G","Ab","Bb"],
                  "D":["D","E","F","G","A","Bb","C"],
                  "E":["E","F#","G","A","B","C","D"],
                  "F":["F","G","Ab","Bb","C","Db","Eb"],
                  "G":["G","A","Bb","C","D","Eb","F"],
                  "A":["A","B","C","D","E","F","G"],
                  "B":["B","C#","D","E","F#","G","A"],
                  "C#":["C#","D#","E","F#","G#","A","B"],
                  "F#":["F#","G#","A","B","C#","D","E"],
                  "Bb":["Bb","C","Db","Eb","F","Gb","Ab"],
                  "Eb":["Eb","F","Gb","Ab","Bb","Cb","Db"],
                  "Ab":["Ab","Bb","Cb","Db","Eb","Fb","Gb"],
                  "Db":["Db","Eb","Fb","Gb","Ab","Bbb","Cb"],
                  "Gb":["Gb","Ab","B","Cb","Db","E","Fb"],
                  "Cb":["Cb","Db","E","Fb","Gb","A","B"]
                  }
k = input("Insira sua nota aqui:")
a = 0
b = 0
a1 = 0
b1 = 0

if (k) in escalasmaiores:    
    notas = (escalasmaiores[(k)])
    r = notas[(a+5)]
    print("A escala maior de",(k),"é:",escalasmaiores[k])
    print("O campo harmônico de",(k),"maior é:")
    for i in range(len(notas)):
        if a == 0:        
            print(notas[(a)],"-",notas[(a)],notas[(a+2)],notas[(a+4)])
            a = (a+1)
        elif a == 1:
            print((notas[(a)]+"m"),"-",notas[(a)],notas[(a+2)],notas[(a+4)])
            a = (a+1)
        elif a == 2:
            print((notas[(a)]+"m"),"-",notas[(a)],notas[(a+2)],notas[(a+4)])
            a = (a+1)
          
        else:
            if a == 3:
                (s1) = notas[:3]
                (s2) = notas[3:]
                notas = (s2+s1)
                print(notas[(b)],"-",notas[(b)],notas[(b+2)],notas[(b+4)])
                b = (b+1)
                a = (a+1)
                
            elif b == 2:
                print((notas[(b)]+"m"),"-", notas[(b)],notas[(b+2)],notas[(b+4)])
                b = (b+1)
                a = (a+1)
            elif a == 6:
                print((notas[(b)]+"°"),"-", notas[(b)],notas[(b+2)],notas[(0)])
            
            
            else:
                print(notas[(b)],"-", notas[(b)],notas[(b+2)],notas[(b+4)])
                b = (b+1)
                a = (a+1)
                
        

 
    notasx = (escalasmenores[(k)])
    print("A relativa menor de",(k),"é:",r)
    print("A escala menor natural de",(k),"é:",escalasmenores[k])
    print("O campo harmônico de",(k),"menor natural é:")
    for i in range(len(notasx)):
        if a1 == 0:        
            print((notasx[(a1)]+"m"),"-",notasx[(a1)],notasx[(a1+2)],notasx[(a1+4)])
            a1 = (a1+1)
        elif a1 == 1:
            print((notasx[(a1)]+"°"),"-",notasx[(a1)],notasx[(a1+2)],notasx[(a1+4)])
            a1 = (a1+1)
        elif a1 == 2:
            print((notasx[(a1)]),"-",notasx[(a1)],notasx[(a1+2)],notasx[(a1+4)])
            a1 = (a1+1)
          
        else:
            if a1 == 3:
                s3 = notasx[:3]
                s4 = notasx[3:]
                notasx = s4+s3
                print((notasx[(b1)]+"m"),"-",notasx[(b1)],notasx[(b1+2)],notasx[(b1+4)])
                b1 = (b1+1)
                a1 = (a1+1)
                
                
            elif a1 == 4:
                print((notasx[(b1)]+"m"),"-", notasx[(b1)],notasx[(b1+2)],notasx[(b1+4)])
                b1 = (b1+1)
                a1 = (a1+1)
                
            elif a1 == 5:
                print((notasx[(b1)]),"-", notasx[(b1)],notasx[(b1+2)],notasx[(6)])
                b1 = (b1+1)
                a1 = (a1+1)
                    
            
            else:
                print(notasx[(b1)],"-", notasx[(b1)],notasx[(b1+2)],notasx[(b1-3)])
                b1 = (b1+1)
                a1 = (a1+1)
                        
    
else:
    print("Nota não encontrada!")

    
    
        
        

    
        

    
        
        
