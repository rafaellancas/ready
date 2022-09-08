while True:
    try:
        x = int(input("Insert your year: "))
        if x <= 2022:
            if not x % 4 == 0:
                print("{} was a common year!".format(x))
            elif not x % 100 == 0:
                print("{} was a leap year!".format(x))
            elif not x % 400 == 0:
                print("{} was a common year!".format(x))
            else:
                print("{} was a leap year!".format(x))
        else:
            if not x % 4 == 0:
                print("{} is a common year!".format(x))
            elif not x % 100 == 0:
                print("{} is a leap year!".format(x))
            elif not x % 400 == 0:
                print("{} is a common year!".format(x))
            else:
                print("{} is a leap year!".format(x))

    except ValueError:
        print("Invalid year!")