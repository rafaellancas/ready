while True:
    try:
        print("=== Welcome to your Interactive Python Calculator ===")
        a = int(input("Please enter the first value: "))
        b = int(input("Please enter the second value: "))

        print("Great! Now enter the operation.")
        print("These are the available options:")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Integer Division")
        print("6 - Modulo")
        c = int(input("--> Enter the corresponding integer: "))

        if c == 1:
            x = a + b
            print("The result of {} + {} is {}!".format(a,b,x))
        elif c == 2:
            x = a - b
            print("The result of {} - {} is {}!".format(a,b,x))
        elif c == 3:
            x = a * b
            print("The result of {} * {} is {}!".format(a,b,x))
        elif c == 4:
            x = a / b
            print("The result of {} / {} is {}!".format(a,b,x))
        elif c == 5:
            x = a // b
            print("The result of {} // {} is {}!".format(a,b,x))
        elif c == 6:
            x = a % b   
            print("The result of {} % {} is {}!".format(a,b,x)) 
        else:
            print("Invalid operation number!")

        

    except ValueError:
        print("Invalid number!")