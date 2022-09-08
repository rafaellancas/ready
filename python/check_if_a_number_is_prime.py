while True:
    try:
        x = int(input("Insert your number here: "))
        
        
        if x == 0 or x == 1:
            print("Not Prime")
            
        elif x < 0:
            print("Invalid number! Try again!")

        else:
            for i in range(2, x):
                if x % i == 0:
                    print("Not Prime")
                    break
            else:
                print("Prime")
                    
    except:
        print("Invalid number! Try again!")
