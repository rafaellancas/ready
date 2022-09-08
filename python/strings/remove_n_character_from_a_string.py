print("Remove the \"n\" character from a string")

while True:
    s=input("Insert your word:")
    

    if s == "": #Check if s is empty!
        print("Empty word!")

    elif s == "quit": #Check if the user hit "quit".
        print("Have a nice day!")
    
    else:
        i=input("Insert the number of the character:")
        x=i.isdigit()
        
        
        if x == False: #Check if the word is a word without numbers.
        
        
            print("Please insert a positive integer number!")
    
        elif i == "0": #Check if the number is 0
            print("Invalid number!")

        else:
            i=int(i)
            if i <= len(s): #Check if the number is equal or smaller then the amount of characters on the string.
                n1 = (s[:(i-1)])
                n2 = (s[(i):(len(s))])
                n3 = [n1,n2]
                r="".join(n3)
                print(r)

            else:
                print("Invalid number for this word!")
           
                
