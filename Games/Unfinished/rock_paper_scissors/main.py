
import random

game_moves = ["rock","paper","scissors"]

print("Welcome To The Rock Paper Scissors Game Program")


def print_menu():
    print("Press 1: To Duel against the computer")
    print("Press 2: To Duel agaisnt other player next you")

def move_list():
    print("Press 1 for Rock: Weakness: Paper ,Strength against: scissors\n ")
    print("Press 2 for Paper: Weakness: Scissors ,Strength against: Rock\n")
    print("Press 3 for Scissors: Weakness: Rock ,Strength against: Paper\n ")

def mode_selection(mode):
    if mode == 1:
        print("Dueling against.... the computer")
        mode_1()
    if mode == 3:
        print("Dueling against.... the other person")

        


def mode_1():
    rounds = int(input("Best of how many rounds"))
    round_counter = 0
    player_win_count = 0
    computer_win_count = 0
    while round_counter != rounds:
        move_list()
        player_select = game_moves[int(input("Select move: ")) - 1]
        computer_select = random.choice(game_moves)
        print("Player:",player_select,"Computer:",computer_select)
        if player_select == "scissors" and computer_select == "paper":
            player_win_count +=1
            print("Player won round",str(round_counter))
            
        elif player_select == "scissors" and computer_select == "rock":
            computer_win_count += 1
            print("Computer won round",str(round_counter))
        elif player_select == "paper" and computer_select == "rock":
            player_win_count += 1
            print("Player won round",str(round_counter))
        elif player_select == "paper" and computer_select == "scissors":
           computer_win_count += 1
           print("Computer won round",str(round_counter))
        elif player_select == "rock" and computer_select == "paper":
            computer_win_count += 1
            print("Computer won round",str(round_counter))
        elif player_select == "rock" and computer_select == "scissors":
            player_win_count += 1
            print("Player won round",str(round_counter))
        elif player_select == "scissors" and computer_select == "scissors":
            print("tie")
            
        elif player_select == "paper" and computer_select == "paper":
            print("tie")
            
        elif player_select == "rock" and computer_select == "rock":
            print("tie")
        print(player_win_count)
        print(computer_win_count)
        round_counter = +1
        print(round_counter)
        
        
    if player_win_count > computer_win_count:
        print("Player has won")
    else:
        print("Computer has won")

        

def main():
    print_menu()
    mode_selection(mode = int(input("What mofr will you select: ")))
    


main()


