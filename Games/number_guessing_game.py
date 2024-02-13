import random
number_list = []






def main():
    print("Welcome to the Number Guessing Game\n")
    range_indicate = int(input("From 0 to what number shall you guess the secret number"))
    want_lives = input("Do you want to have unlimited lives or limited lives (y/n)")

    
    for number in range(0,range_indicate):
        number_list.append(number)

    selected_number = random.choice(number_list)
    print("Slected number: ", str(selected_number))
    player_won = False

    
    if want_lives == "y":
        lives_amount = int(input("How many lives do you want"))
        guess = int(input("Guess: "))
        while guess != selected_number:
            lives -= 1
            if guess > selected_number:
                print("Guess is too big")
            else:
                print("Guess is too small")
            
            if lives == 0:
                guess == selected_number
            else:
                player_won = True
            
                
        

        
    else:
        player_won = True
        guess = int(input("Guess: "))
        while guess != selected_number:
            if guess > selected_number:
                print("Guess is too big")
            else :
                print("Guess is too small")
                
            guess = int(input("Guess: "))
        

    if player_won == True:
        print("Player has won")
    else:
        print("Player has lost")

      

main()
