import os
import players_DB
import game_art
import random

print(game_art.manchester_city)
continue_flag = True
p_point = 0

def jersey_number_compare():
    global p_point
    global continue_flag
       
    print(f"whose jersey number is greater?\n\nA:{Aname} ({Aposition})\n{game_art.vs}\nB:{Bname} ({Bposition})\n")
    
    if Ajersey > Bjersey:
        answer = 'A'
    else:
        answer = 'B'

    p_answer = input("Your answer: ").title()

    if p_answer == answer:
        p_point += 1
        print(f"That's correct\n\n")
    else:
        print(f"wrong!!! GAME OVER\n\nFINAL SCORE = {p_point} points\n")
        continue_flag = False

os.system('clear')

while continue_flag:
    player1 = random.choice(players_DB.player_data)
    player2 = random.choice(players_DB.player_data)

    Aname = player1["name"]
    Bname = player2["name"]

    Aposition = player1["position"]
    Bposition = player2["position"]

    #Acountry = player1["country"]
    #Bcountry = player2["country"]

    Ajersey = player1["Jersey Number"]
    Bjersey = player2["Jersey Number"]

    jersey_number_compare()