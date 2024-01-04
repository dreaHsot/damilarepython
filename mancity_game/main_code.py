import os
import players_DB
import game_art
import random

os.system('clear')

print(game_art.manchester_city)
continue_flag = True
p_point = 0

game_type = input("Select gametype;\n\n enter 1 for nationality version or 2 for jersey number compare")

def nationality():
    global p_point
    global continue_flag
    global player1

    print("Input the country the players represent in the space provided\n(enter a correct spelling)")

    p_answer = input(f"{Aname} ").title()

    '''if Aname not in country_players:
        country_players["Aname"] = 1
    else:
        country_players["Aname"] += 1

    while country_players["Aname"] < 3:'''
    if p_answer == player1["country"]:
        p_point += 1
        print(f"That's correct\n\n")
    else:
        print(f"wrong!!! GAME OVER\n\nFINAL SCORE = {p_point} points\n")
        continue_flag = False

    #player1 = player2


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

country_players = {}

while continue_flag:
    player1 = random.choice(players_DB.player_data)
    player2 = random.choice(players_DB.player_data)

    Aname = player1["name"]
    Bname = player2["name"]

    Aposition = player1["position"]
    Bposition = player2["position"]

    Ajersey = player1["Jersey Number"]
    Bjersey = player2["Jersey Number"]

    if game_type == '2':
        jersey_number_compare()
    elif game_type == '1':
        nationality()
