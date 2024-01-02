import os
import players_DB
import game_art
import random

os.system('clear')

continue_flag = True
p_point = 0

#print("Choose level")
while continue_flag:
    player1 = random.choice(players_DB.player_data)
    player2 = random.choice(players_DB.player_data)
    A = player1["name"]
    B = player2["name"]

    Aposition = player1["position"]
    Bposition = player2["bposition"]

    print(f"whose jersey number is greater?\n\nA:{A} ({Aposition})\nOR\nB:{B} ({Bposition})\n")
    
    if player1["Jersey Number"] > player2["Jersey Number"]:
        answer = 'A'
    else:
        answer = 'B'

    p_answer = input("Your answer: ").title()

    if p_answer == answer:
        p_point += 1
        print(f"That's correct; you have {p_point} points\n\n")
    else:
        print(f"wrong!!! GAME OVER\n\nYou have {p_point} points\n")
        continue_flag = False



