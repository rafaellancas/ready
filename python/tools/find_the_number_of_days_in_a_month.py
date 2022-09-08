while True:
    a = input("Insert month:")

    months_31_days = ("january", "march", "may", "july", "august", "october", "december")
    months_30_days = ("april", "june", "september", "november")
    
    y = [28,30,31]
    x = a.lower()
    z = x.isalpha()

    if z == True:
        if x in months_31_days:
            print("{} has {} days!".format(x.capitalize(),y[2]))
        elif x in months_30_days:
            print("{} has {} days!".format(x.capitalize(),y[1]))
        elif x == "february":
            print("{} has {} days!".format(x.capitalize(),y[0]))
        else:
            print("Insert a valid month!")

    else:
        print("Insert a valid month!")



