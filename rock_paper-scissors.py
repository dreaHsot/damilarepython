import random

rps = ['r', 'p', 's']
comp = random.choice(rps)

user = input("Enter r for rock; p for paper; or s for scissors:").lower()

if comp == 'r':
    if user == 'r':
        print('Computer - ROCK <<< >>> You - ROCK\n\nThis is a draw!')
    elif user == 'p':
        print('Computer - ROCK <<< >>> You - PAPER\n\nCongratulations, You win!')
    elif user == 's':
        print('Computer - ROCK <<< >>> You - SCISSORS\n\nComputer wins!')
    else:
        print('You Loose!')
elif comp == 'p':
    if user == 'r':
        print('Computer - PAPER <<< >>> You - ROCK\n\nComputer wins!')
    elif user == 'p':
        print('Computer - PAPER <<< >>> You - PAPER\n\nThis is a draw!')
    elif user == 's':
        print('Computer - PAPER <<< >>> You - SCISSORS\n\nCongratulations, you win!')
    else:
        print('Invalid, You Loose!')
elif comp == 's':
    if user == 'r':
        print('Computer - SCISSORS <<< >>> You - ROCK\n\nCongratulations, you win!')
    elif user == 'p':
        print('Computer - SCISSORS <<< >>> You - PAPER\n\ncomputer wins!')
    elif user == 's':
        print('Computer - SCISSORS <<< >>> You - SCISSORS\n\nThis is a draw!')
    else:
        print('You Loose!')