import random


target = random.randint(1,5)
while True:
    userChoice = input("Guess the target 0r Quit(Q))")
    if(userChoice == "Quit"):
        break


    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess")
        break
    elif(userChoice <target):
        print("your number was too small Take a bigger Guess..")
    else:
        print("your number was too big Take a smaller Guess..")
print("-------GAME OVER----")