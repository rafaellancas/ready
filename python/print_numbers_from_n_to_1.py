while True:
    try:
        n = int(input("Insert your number: "))

        if n >= 1:
            for i in range(-n, 0):
                print(abs(i))
        else:
            print("Invalid number! Try again!")        

    except ValueError:
        print("Invalid number! Try again!")