while True:
    try:
        x = int(input("Insert the first number:"))
        y = int(input("Insert the second number:"))
        z = int(input("Insert the third number:"))

        if x == y and y == z:
            print("Equal")
        else:
            print("Not equal")
    except ValueError:
        print("Insert a valid number!")