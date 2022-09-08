while True:
    try:
        x = int(input("Insert your number: "))
        z = int

        if x < 1:
            print("Invalid number! Try again!")

        else:
            print("==== Multiplication Table of {} ====".format(x))
            for i in range(11):
                z = x*i
                print("{} x {} = {}".format(x,i,z))

    except ValueError:
        print("Invalid number! Try again!")