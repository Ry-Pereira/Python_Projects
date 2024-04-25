import random
class Game:
    def __init__(self,player,computer):
        self.player = player
        self.computer = computer

    def add_point_player(self):
        self.player.score +=1

    def add_point_computer(self):
        self.computer.score +=1
        
        
    def battle(self,player_move,computer_move):
        if player_move.strength == computer_move.move_name:
            self.add_point_player()
            print("Player wins")
        elif  player_move.strength == computer_move.weakness:
            self.add_point_computer()
            print("Computer wins")
        else:
            print("Its a tie")
        
    def intro_to_program(self):
        print("Welcome To The Rock Paper Scissors Game Program")


    def print_menu(self):
        print("Press 1: To Duel against the computer")
        print("Press 2: To Exit Program")

    def move_list(self):
        print("Press 1 for Rock: Weakness: Paper ,Strength against: scissors\n ")
        print("Press 2 for Paper: Weakness: Scissors ,Strength against: Rock\n")
        print("Press 3 for Scissors: Weakness: Rock ,Strength against: Paper\n ")

    def determine_winner(self):
        if self.player.score > self.computer.score:
            print("User wins")
        elif self.player.score < self.computer.score:
            print("User Loses")
        else:
            print("Its a tie")


    def battling(self):
        rounds = 3
        while rounds != 0:
            user_move = int(input("Choice: "))
            if user_move == 1:
                self.battle(self.player.moves[0],self.computer.moves[random.randint(0,2)])
            if user_move == 2:
                self.battle(self.player.moves[1],self.computer.moves[random.randint(0,2)])
            if user_move == 3:
                self.battle(self.player.moves[2],self.computer.moves[random.randint(0,2)])
            rounds -= 1

        self.determine_winner()
            
        
    def mode_selection(self,choice):
        if choice == 1:
            print("Dueling against.... the computer")
            self.move_list()
            self.battling()
            self.mode_selection(choice = int(input("CHoice: ")))
        
        elif choice == 2:
            print("Exiting Program...")
        else:
            print("Please Choose a Valid Option")
            self.print_menu()
            self.mode_selection(choice = int(input("CHoice: ")))

    def run(self):
        self.intro_to_program
        self.print_menu()
        self.mode_selection(choice = int(input("CHoice: ")))
    




