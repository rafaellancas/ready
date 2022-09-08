while True:
    number = input("Guess a number from 1 to 10:")
    if number == "q":
        break
    elif number == "7":
        print("Your guess is right!")   
    elif int(number) <= 0 or int(number) >= 11:
        print("Your number is not between 1 and 10!")
    else:
        print("Your guess is wrong!")
