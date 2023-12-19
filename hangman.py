'''This code is a task from Jenny's lecture
to create a HANGMAN game.

player 1 gives a word while player 2 has to
guess the letters of the word one after the
other before the 'hangman image' is cleared.'''

real_word = input("PLAYER 1:") #the real word by player 1

l = len(real_word)
display = [] #list of dashes '_'

hangman = ["\n 0\n/|\\\n/ \\\n", "\n 0\n/|\\\n/ \n", "\n 0\n/|\\\n", "\n 0\n/|\n", "\n 0\n |\n", "\n 0\n"]

p = 0

print(hangman[p])

print('Start making your guesses; one letter per try: "', end="")

for i in real_word: # iterating through the realword
    print("_", end=" ")
    display.append('_')

print('"')

while '_' in display and p < 6:
    guess = input("PLAYER 2: ")
    correct_guess = False #to check if there's a tally

    for i, w in enumerate(real_word):
        if guess == w:
            display[i] = w
            correct_guess = True

    if correct_guess == False:
        p += 1 #hangman reduction in life if there's no tally

    for i in display:
        print(i, end=" ")

    if p > 5:
        print(f"\nGAMEOVER!!!, HANGMAN IS DEAD\nThe word is {real_word}")
    else:
        print(hangman[p])

if '_' not in display:
    print("\nCongratulations, your HANGMAN is survived")
