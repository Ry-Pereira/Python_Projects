from memory_card import MemoryCard


class ColorMemoryMadness:

    def __init__(self,card_file):
        self.card_deck = []
        with open(card_file,"r") as file:
             for line in file:
                self.card_deck.append(MemoryCard("Memory Madness",line))




    def print_stuff(self):
        for f in self.card_values:
            print(f)

    def create_board(self,number):
        board = []
        for num in range(0,number):
            row = []
            for num in range(0,number):
                row.append("Blank")
            board.append(row)

        return board
        
    def print_board(self,board):
        for row in board:
            for space in row:
                print(space, end = " ")
            
            print(" ")



    def print_menu(self):
        print("1: Easy 4X4 Board\n2: Medium 5X% Board\n3: Hard 6X6 Board\n4: Quit")

    def menu_selection(self,choice):
        if choice == 1:
            self.print_board(self.create_board(int(4)))
        elif choice == 2:
            self.print_board(self.create_board(int(4)))
        elif choice == 3:
            self.print_board(self.create_board(int(4)))
        elif choice == 4:
            print("Exiting a Program")
        else:
            print(" Please Choose a Valid Choice")
            self.print_menu()
            self.menu_selection(choice = int(input("Choice: ")))
            
        

    def run(self):
        self.print_menu()
        self.menu_selection(choice = int(input("Choice: ")))




nod = ColorMemoryMadness("cards.txt")



nod.run()
