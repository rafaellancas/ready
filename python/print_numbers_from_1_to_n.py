while True:
    try:
        n = int(input("Insert your number: "))

        if n <= 0:
            print("Invalid number!")
        else:
            for i in range(n):
                print(i+1)

    except ValueError:
        print("Invalid number!")