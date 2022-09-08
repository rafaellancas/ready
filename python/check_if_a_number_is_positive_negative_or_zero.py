while True:
    try:
        x = int(input("Enter a number:"))
        if x == 0:
            print("Zero!")
        elif x >= 0:
            print("Positive!")
        else:
            print("Negative!")
    except ValueError:
        print("Not a number!")
    
