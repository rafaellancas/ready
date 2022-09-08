class Note:
    def __init__(self,i,ii,iii,iv,v,vi,vii):
        self.i = i
        self.ii = ii
        self.iii = iii
        self.iv = iv
        self.v = v
        self.vi = vi
        self.vii = vii            
        

    #Extract the chord:
    def chord(self):
        c2 =("("+self.i+" "+self.iii+" "+self.v+")")
        return str(c2)

    #Extract the scale:    
    def scale(self):
        s2 = (self.i+" - "+self.ii+" - "+self.iii+" - "+self.iv+" - "+self.v+" - "+self.vi+" - "+self.vii)
        return str(s2)

    #Extract the major field
    def majorfield(self):
        f1 = (self.i+"("+self.i+" "+self.iii+" "+self.v+")")
        f2 = (self.ii+"m"+"("+self.ii+" "+self.iv+" "+self.vi+")")
        f3 = (self.iii+"m"+"("+self.iii+" "+self.v+" "+self.vii+")")
        f4 = (self.iv+"("+self.iv+" "+self.vi+" "+self.i+")")
        f5 = (self.v+"("+self.v+" "+self.vii+" "+self.ii+")")
        f6 = (self.vi+"m"+"("+self.vi+" "+self.i+" "+self.iii+")")
        f7 = (self.vii+"°"+"("+self.vii+" "+self.ii+" "+self.iv+")")
        hf = (f1+"\n "+f2+"\n "+f3+"\n "+f4+"\n "+f5+"\n "+f6+"\n "+f7)
        return str(hf)

    #Extract the major field
    def minorfield(self):
        g1 = (self.i+"m"+"("+self.i+" "+self.iii+" "+self.v+")")
        g2 = (self.ii+"°"+"("+self.ii+" "+self.iv+" "+self.vi+")")
        g3 = (self.iii+"("+self.iii+" "+self.v+" "+self.vii+")")
        g4 = (self.iv+"m"+"("+self.iv+" "+self.vi+" "+self.i+")")
        g5 = (self.v+"m"+"("+self.v+" "+self.vii+" "+self.ii+")")
        g6 = (self.vi+"("+self.vi+" "+self.i+" "+self.iii+")")
        g7 = (self.vii+"("+self.vii+" "+self.ii+" "+self.iv+")")
        gf = (g1+"\n "+g2+"\n "+g3+"\n "+g4+"\n "+g5+"\n "+g6+"\n "+g7)
        return str(gf)

    #Print the majors
    def print_major(self):
        return print(" O acorde de",(x).i,"maior é:","\n",
                     (x).chord(),"\n",
                     "A escala de",(x).i,"maior é :","\n",
                     (x).scale(),"\n",
                     "O campo harmônico de",(x).i,"maior é:","\n",
                     (x).majorfield()
                     )
    
    #Print the minors
    def print_minor(self):
        return print(" O acorde de",(x).i,"menor é:","\n",
                     (x).chord(),"\n",
                     "A escala de",(x).i,"menor natural é :","\n",
                     (x).scale(),"\n",
                     "O campo harmônico de",(x).i,"menor natural é:","\n",
                     (x).minorfield()
                     )
                     


c = Note("C","D","E","F","G","A","B")
g = Note("G","A","B","C","D","E","F#")
d = Note("D","E","F#","G","A","B","C#")
a = Note("A","B","C#","D","E","F#","G#")
e = Note("E","F#","G#","A","B","C#","D#")
b = Note("B","C#","D#","E","F#","G#","A#")
fs = Note("F#","G#","A#","B","C#","D#","E#")
cs = Note("C#","D#","E#","F#","G#","A#","B#")
f = Note("F","G","A","Bb","C","D","E")
bb = Note("Bb","C","D","Eb","F","G","A")
eb = Note("Eb","F","G","Ab","Bb","C","D")
ab = Note("Ab","Bb","C","Db","Eb","F","G")
db = Note("Db","Eb","F","Gb","Ab","Bb","C")
gb = Note("Gb","Ab","Bb","Cb","Db","Eb","F")
cb = Note("Cb","Db","Eb","Fb","Gb","Ab","Bb")

while True:
    inp = input("Insira sua nota:")
    inp = inp.lower()

    if inp == "c":
        x = c
        x.print_major()
    
        #Minor changes for "C":
        (x).iii = "Eb"
        (x).vi = "Ab"
        (x).vii = "Bb"
        x.print_minor()

    elif inp == "g":
        x = g
        x.print_major()

        #Minor changes for "G":
        (x).iii = "Bb"
        (x).vi = "Eb"
        (x).vii = "F"
        x.print_minor()

    elif inp == "d":
        x = d
        x.print_major()

        #Minor changes for "D":
        (x).iii = "F"
        (x).vi = "Bb"
        (x).vii = "C"
        x.print_minor()

    elif inp == "a":
        x = a
        x.print_major()

        #Minor changes for "A":
        (x).iii = "C"
        (x).vi = "F"
        (x).vii = "G"
        x.print_minor()
    
    elif inp == "e":
        x = e
        x.print_major()

        #Minor changes for "E":
        (x).iii = "G"
        (x).vi = "C"
        (x).vii = "D"
        x.print_minor()

    elif inp == "b":
        x = b
        x.print_major()

        #Minor changes for "B":
        (x).iii = "D"
        (x).vi = "G"
        (x).vii = "A"
        x.print_minor()

    elif inp == "f#":
        x = fs
        x.print_major()

        #Minor changes for "F#":
        (x).iii = "A"
        (x).vi = "D"
        (x).vii = "E"
        x.print_minor()

    elif inp == "c#":
        x = cs
        x.print_major()

        #Minor changes for "C#":
        (x).iii = "E"
        (x).vi = "A"
        (x).vii = "B"
        x.print_minor()
    
    elif inp == "f":
        x = f
        x.print_major()

        #Minor changes for "F":
        (x).iii = "Ab"
        (x).vi = "Db"
        (x).vii = "Eb"
        x.print_minor()  
    
    elif inp == "bb":
        x = bb
        x.print_major()

        #Minor changes for "Bb":
        (x).iii = "Db"
        (x).vi = "Gb"
        (x).vii = "Ab"
        x.print_minor()

    elif inp == "eb":
        x = eb
        x.print_major()

        #Minor changes for "Eb":
        (x).iii = "Gb"
        (x).vi = "Cb"
        (x).vii = "Db"
        x.print_minor()

    elif inp == "ab":
        x = ab
        x.print_major()

        #Minor changes for "Ab":
        (x).iii = "Cb"
        (x).vi = "Fb"
        (x).vii = "Gb"
        x.print_minor()

    elif inp == "db":
        x = db
        x.print_major()

        #Minor changes for "Db":
        (x).iii = "Fb"
        (x).vi = "Bbb"
        (x).vii = "Cb"
        x.print_minor()

    elif inp == "gb":
        x = gb
        x.print_major()

        #Minor changes for "Gb":
        (x).iii = "B"
        (x).vi = "E"
        (x).vii = "Fb"
        x.print_minor()

    elif inp == "cb":
        x = cb
        x.print_major()

        #Minor changes for "Cb":
        (x).iii = "Ebb"
        (x).vi = "Abb"
        (x).vii = "Bbb"
        x.print_minor()

    else:
        print("Nota inválida!!!!")



#Testing the saving feature!