while True:
    try:
        a = int(input("What's yout age?  "))
        b = 18
        c = 60

        if a <= 0:
            print ("Invalid age.")

        elif a < b:
            print ("You are a child.")

        elif a >= b and a < c:
            print ("You are an adult.")

        else:
            print ("You are an elder.")

    except ValueError:
        print("Not a number!")