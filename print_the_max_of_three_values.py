while True:
    try:
        x = int(input("Insert the first number:"))
        y = int(input("Insert the second number:"))
        z = int(input("Insert the third number:"))

        j = [x,y,z]
        print("The highest number is {}!".format(max(j)))

    except ValueError:
        print("Not a number!")