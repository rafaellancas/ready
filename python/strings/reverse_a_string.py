while True:
    try:
        x = input("Insert your string here: ")
        y = []

        for n in (range(len(x))):
            z = x[n]
            y.append(z)

        y.reverse()
        print("".join(y))
    
    except:
        print("Invalid string! Try again!")