import random
import os


os.system('clear')
print("\n*****WELCOME TO GUESS THE NUMBER*****\n\n")

guess = 0
lifeline = 0
level = input("enter 1 for easy and 2 for hard: \n")

if level == '1':
    lifeline = 10
    guess = int(input("You have 10 chances; enter your first guess (between 1 - 100) here: "))
elif level == '2':
    lifeline = 5
    guess = int(input("You have 5 chances; enter your first guess (between 1 - 100)here: "))
else:
    print("invalid input!!!")

dest = random.randint(1, 100)

while lifeline > 0:
    if guess == dest:
        print(f"\n\nCongratulations, that's correct!! {dest}\n")
        break
    elif guess < dest:
        guess = int(input("too low, try again: "))
        lifeline -= 1
        print(f"\nYou have {lifeline} attempts left")
    else:
        guess = int(input("too high, try again: "))
        lifeline -= 1
        print(f"\nYou have {lifeline} attempts left")

if lifeline == 0 and guess != dest:
    print(f"\nWRONG!!! GAME OVER\nCorrect guess is {dest}\n")
