print("Check if a string contains only numbers!")

while True:
    s = input("Insert your word:")
    if s != "quit":
        x = s.isdigit()
        print(x)
    else:
        print("Have a nice day!")
        break

