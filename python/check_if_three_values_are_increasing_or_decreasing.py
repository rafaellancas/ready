while True:
    try:
        a = int(input("Insert the first number:"))
        b = int(input("Insert the second number:"))
        c = int(input("Insert the third number:"))

        if a > b > c:
            print("Decreasing order")
        elif c > b > a:
            print("Increasing order")
        else:
            print("None")
    except ValueError:
        print("Invalid number!")