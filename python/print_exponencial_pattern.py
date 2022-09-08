while True:
    try:
        x = int(input("Insert your number here: "))
        
        if x < 0:
            print("Invalid number! Try again!")

        else:
            for i in range(1, x+1):
                print("* "*i)
                    
    except:
        print("Invalid number! Try again!")