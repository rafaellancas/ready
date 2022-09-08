import random

while True:
    print("====== Welcome to the game ======")
    x = input("Please enter Rock, Paper, or Scissors: ")
    x = x.lower()
    y = random.randint(1,3)
    if y == 1:
        y = "Rock"            
    elif y == 2:
        y = "Paper"
    elif y == 3:
        y = "Scissors"
    
    if x == "rock":
        if y == "Rock":
            print("The computer chose {}!".format(y))
            print("It's a tie!")
        elif y == "Paper":
            print("The computer chose {}!".format(y))
            print("Paper beats Rock!")
            print("You lose!")
        elif y == "Scissors":
            print("The computer chose {}!".format(y))
            print("Rock beats Scissors!")
            print("You win!")

    elif x == "paper":
        if y == "Rock":
            print("The computer chose {}!".format(y))
            print("Paper beats Rock!")
            print("You win!")
        elif y == "Paper":
            print("The computer chose {}!".format(y))
            print("It's a tie!")
        elif y == "Scissors":
            print("The computer chose {}!".format(y))
            print("Scissors beats Paper!")
            print("You lose!")
    
    elif x == "scissors":
        if y == "Rock":
            print("The computer chose {}!".format(y))
            print("Rock beats Scissors!")
            print("You lose!")            
        elif y == "Paper":
            print("The computer chose {}!".format(y))
            print("Scissors beats Paper!")
            print("You win!")            
        elif y == "Scissors":
            print("The computer chose {}!".format(y))
            print("It's a tie!")
    else:
        print("Invalid option!")


        
    
    
        



        
        