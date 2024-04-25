import random
from rock_paper_scissor_object import RockPaperScissorObject


class Player:

    def __init__(self,player_name):
        self.player_name = player_name
        self.score = 0
        self.moves = [rock = RockPaperScissorObject("Rock","Scissors","Paper"),paper = RockPaperScissorObject("Paper","Rock","Scissors"),scissors = RockPaperScissorObject("Scissors","Paper","Rock")]
        
class Game:

    def __init__(self,player,computer):
        self.player = player
        self.computer = computer

    def add_point_player(self):
        self.player.score +=1

    def add_point_computer(self):
        self.player.computer +=1
        
        
    def battle(self):
        if self.player.stength == self.computer.value:
            self.add_point_player()
            return (self.value + "wins")
        elif self.strength == other.weakness:
            self.add_point_computer()
            return (computer.value + "wins")
        else:
            return "Tie"
        
    def intro_to_program(self):
        print("Welcome To The Rock Paper Scissors Game Program")


    def print_menu(self):
        print("Press 1: To Duel against the computer")
        print("Press 2: To Exit Program")

    def move_list(self):
        print("Press 1 for Rock: Weakness: Paper ,Strength against: scissors\n ")
        print("Press 2 for Paper: Weakness: Scissors ,Strength against: Rock\n")
        print("Press 3 for Scissors: Weakness: Rock ,Strength against: Paper\n ")


    def battling(self):
        rounds = 3
        while rounds != 0:
            user_move = int(input("Choice: "))
            if user_move == 1:
                self.battle(player.move[1],computer.move[r.choice(self.bank),user_score)
            if user_move == 2:
                self.battle(player.move[2],random.choice(self.bank))
            if user_move == 3:
                self.battle(player.move[3],random.choice(self.bank))
            rounds -= 1

        if user_score > computer_score:
            print("User wins")
        elif user_score < computer_score:
            print("User Loses")
        else:
            print("Its a tie")
            
                
                
            
        
    def mode_selection(self,choice):
        if choice == 1:
            print("Dueling against.... the computer")
            self.move_list()
            self.battling()
        
        elif choice == 2:
            print("Exiting Program...")
        else:
            print("Coming Soon")
   

    def run(self):
        self.intro_to_program
        self.print_menu()
        self.mode_selection(choice = int(input("CHoice: ")))
    


Game = Game(Player(input("Choose Name for User: "),Player("Computer"))
Game.run()


