import random
from rock_paper_scissor_object import RockPaperScissorObject
class Game:

    def __init__(self):
        self.rock = RockPaperScissorObject("Rock","Scissors","Paper")
        self.paper = RockPaperScissorObject("Paper","Rock","Scissors")
        self.scissors = RockPaperScissorObject("Scissors","Paper","Rock")
        self.bank = [self.rock,self.paper,self.scissors]

    def battle(self,other):
        if self.stength == other.value:
            return self.value
        elif self.strength == other.weakness:
            return other.value
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


    def battling(self,choice):
        rounds = 3
        while rounds != 0:
            choice = int(input("Choice: "))
            if user_move == 1:
                 if battle(self.rock,random.choice(self.bank)
            if user_move == 2:
                battle(self.paper,random.choice(self.bank)
            if user_move == 3:
                battle(self.scissor,random.choice(self.bank)
            
                
                
            
        
    def mode_selection(self,choice):
        if choice == 1:
            print("Dueling against.... the computer")
            self.move_list()
        
        elif choice == 2:
            print("Exiting Program...")
        else:
            print("Coming Soon")
   

    def run(self):
        self.intro_to_program
        self.print_menu()
        self.mode_selection(mode = int(input("CHoice: ")))
    


main()


