from rock_paper_scissors import Game
from player import Player
from move import Move

def main():
    player = Player("Player")
    player.moves = [Move("Rock","Scissors","Paper"),Move("Paper","Rock","Scissors"),Move("Scissors","Paper","Rock")]
    computer = Player("Computer")
    computer.moves = [Move("Rock","Scissors","Paper"),Move("Paper","Rock","Scissors"),Move("Scissors","Paper","Rock")]
    RPS = Game(player,computer)
    RPS.run()


if __name__ == "__main__":
    main()

    
    


