a = input("Insira a nota:")
j = ((int(input("Insira o grau desejado entre 1 e 7:")))-1)
do = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
sol = ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
re = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
la = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
escalas = (do, sol, re, la)

if a ==("c") or a == ("C"):
    print ("A escala maior de dó é:", escalas[0])
    print ("O campo harmônico de dó maior é:", escalas[0][0], escalas[0][1],'m')
    print (escalas[0][j])
    
elif a ==("g") or a == ("G"):
    print ("A escala maior de sol é:", escalas[1])
    print ("O campo harmônico de sol maior é:", escalas[1])
    print (escalas[0][j])
    
elif a ==("d") or a == ("D"):
    print (escalas[2][j])
    
elif a ==("a") or a == ("A"):
    print (escalas[3][j])
    
elif a ==("e") or a == ("E"):
    print ("A escala maior de E é E - F# - G# - A - B - C# - D#")
    print ("O campo harmônico maior de E é E - F#m - G#m - A - B - C#m - D#°")

elif a ==("b") or a == ("B"):
    print ("A escala maior de B é B - C# - D# - E - F# - G# - A#")
    print ("O campo harmônico maior de B é B - C#m - D#m - E - F# - G#m - A#°")

elif a ==("f#") or a == ("F#"):
    print ("A escala maior de F# é F# - G# - A# - B - C# - D# - E#")
    print ("O campo harmônico maior de F# é F# - G#m - A#m - B - C# - D#m - E#°")

elif a ==("c#") or a == ("C#"):
    print ("A escala maior de C# é C# - D# - E# - F# - G# - A# - B#")
    print ("O campo harmônico maior de C# é C# - D#m - E#m - F# - G# - A#m - B#°")

elif a ==("f") or a == ("F"):
    print ("A escala maior de F é F - G - A - Bb - C - D - E")
    print ("O campo harmônico maior de F é F - Gm - Am - Bb - C - Dm - E°")

elif a ==("bb") or a == ("Bb"):
    print ("A escala maior de Bb é Bb - C - D - Eb - F - G - A")
    print ("O campo harmônico maior de Bb é Bb - Cm - Dm - Eb - F - Gm - A°")

elif a ==("eb") or a == ("Eb"):
    print ("A escala maior de Eb é Eb - F - G - Ab - Bb - C - D")
    print ("O campo harmônico maior de Eb é Eb - Fm - Gm - Ab - Bb - Cm - D°")

elif a ==("ab") or a == ("Ab"):
    print ("A escala maior de Ab é Ab - Bb - C - Db - Eb - F - G")
    print ("O campo harmônico maior de Ab é Ab - Bbm - Cm - Db - Eb - Fm - G°")

elif a ==("db") or a == ("Db"):
    print ("A escala maior de Db é Db - Eb - F - Gb - Ab - Bb - C")
    print ("O campo harmônico maior de Db é Db - Ebm - Fm - Gb - Ab - Bbm - C°")

elif a ==("gb") or a == ("Gb"):
    print ("A escala maior de Gb é Gb - Ab - Bb - Cb - Db - Eb - F")
    print ("O campo harmônico maior de Gb é Gb - Abm - Bbm - Cb - Db - Ebm - F°")
    
else:
    print ("A nota digitada não é válida!")
