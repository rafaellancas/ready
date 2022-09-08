while True:
    try:
        x = int(input("Insert your number here: "))

        if x == 0:
            print(1)
        elif x < 0:
            print("Invalid number! Try again!")
        else:
            for n in range(1,x):
                x *= n
            print("{:,}".format(x))
    except:
        print("Invalid number! Try again!")