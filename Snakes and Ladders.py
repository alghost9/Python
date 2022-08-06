import random
import numpy as np
import os

Dice = int(input("How many sides on the dice? "))
number_of_players = int(input("How many players in each game? "))
games = int(input("How many games do you want to simulate? "))
player = {"name": " ", "position": 0}
winner = {"name": " ", "turns": 0}
turn ={"turn":0, "name":" ", "position":0}
ladders = {4:14,9:31,20:38,21:42,28:84,36:44,51:67,71:91}
snakes={16:6,47:26,49:30,62:19,63:60,87:24,93:73,95:75,98:78}

player_list = []


player_has_won = False
turn_number = 0
turns_list = []
winner_list = []
list_by_turns = []


def set_up_players(quantity):
    global player_has_won, turn_number
    if len(player_list) > 0:
        player_list.clear()
        player_has_won = False
        turn_number = 0
        print("Reset!!!!!!!!!!!!!")

    for i in range(quantity):
        player_list.append({"name": "Player " + str(i+1), "position": 0})

def set_position(player_num, position):
    player_list[player_num]["position"] = position

def roll_dice():
    return random.randint(1,Dice)

def player_turn(player_num):
    print(player_list[player_num]["name"] + "'s turn")
    print_position(player_num)
    roll = roll_dice()
    print(player_list[player_num]["name"] + " rolled a " + str(roll))
    add_to_position(player_num,roll)
    print_position(player_num)
    check_for_ladders(player_num)
    check_for_snakes(player_num)
    


def add_to_position(player_num, position):
    print(str(position) + " has been added to " + player_list[player_num]["name"] + "'s position")
    player_list[player_num]["position"] += position
    check_equals_100(player_num)

    if check_over_100(player_num):
        rebound_on_100(player_num)

def sub_from_position(player_num, position):
    player_list[player_num]["position"] -= position
    check_equals_100(player_num)
    
    

def get_position(player_num):
    return player_list[player_num]["position"]

def check_equals_100(player_num):
    global player_has_won
    if get_position(player_num) == 100:
        player_has_won = True

def check_over_100(player_num):
    if get_position(player_num) > 100:
        print(player_list[player_num]["name"] + " is over 100 with a score of  " + str(get_position(player_num)))
        return True
    else:
        return False

def rebound_on_100(player_num):
    if get_position(player_num) > 100:
        old_position = get_position(player_num)
        remainder = old_position % 100
        set_position(player_num,100)
        sub_from_position(player_num,remainder)
        print(player_list[player_num]["name"] + " has been rebound by " + str(remainder))

def check_for_ladders(player_num):
    for key in ladders:
        if get_position(player_num) == key:
            print(player_list[player_num]["name"] + " has hit a ladder! ")
            set_position(player_num, ladders[key])
            print(player_list[player_num]["name"] + " has climbed a ladder to " + str(ladders[key]))
            print_position(player_num)


def check_for_snakes(player_num):
    for key in snakes:
        if get_position(player_num) == key:
            print(player_list[player_num]["name"] + " has hit a snake!")
            set_position(player_num, snakes[key])
            print(player_list[player_num]["name"] + " has dropped to " + str(snakes[key]))
            print_position(player_num)


def print_position(player_num):
    pos = get_position(player_num)
    print(player_list[player_num]["name"] + " is at position " + str(pos))
    if pos == 100:
        print(player_list[player_num]["name"] + " has won!!!")
        #print("game took " + str(turn_number) + " turns")
        winner_list.append({"name":player_list[player_num]["name"], "turns":turn_number})


def run_game():
    global turn_number
    set_up_players(number_of_players)
    while not player_has_won:
        print("Turn " + str(turn_number) + "-------------------------------------")
        turn_number += 1
        for i in range(number_of_players):
            if not player_has_won:
                player_turn(i)
                print("\n")
            list_by_turns.append({"turn":turn_number, "name":player_list[i]["name"], "position":player_list[i]["position"]})
            
    turns_list.append(turn_number)
    

    print("game took " + str(turn_number) + " turns")


def play_x_games(games):
    for i in range(games):
        run_game()
        print("\n\n")

def main():

    play_x_games(games)

    print("Total Games played: " + str(games))
    print("Average number of turns: ~" + str(np.ceil((sum(turns_list) / len(turns_list)))))
    print("Shortest amount of turns: " + str(min(turns_list)))
    print("Longest amount of turns: " + str(max(turns_list)))
    


if __name__ == "__main__":
    main()
    os.system("pause")


