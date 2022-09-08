while True:
    try:
        x = int(input("Insert your number here: "))
        
        if x <= 0:
            print("Invalid number! Try again!")

        else:
            x = str(x)
            y = []
            for n in (range(len(x))):
                z = x[n]
                y.append(z)

            y.reverse()
            print("".join(y))
    
    except:
        print("Invalid number! Try again!")

