import random
word_bank = ["red","orange","yello","green","blue","purple","pink","violet","cyan","gray","white","black"]




#This function prints the intro to the program
def intro_to_program():
    print("Welcome to the Guess That Word Program\n")




#This function prints the options menu
def print_options():
    print("Press 1: For Easy mode - 20 lives\nPress 2: For  Moderate - 15 lives\nPress 3: For Hard - 10 lives\nPress 4: For Extreme - 5 lives\nPress 5: Set lives\nPress 6: Exit")
    



#This function is used to select the mode for game and set the lives
def difficulty_selection(selection):
    if selection == 1:
        game_mode(20)
    elif selection == 2:
        game_mode(15)
    elif selection == 3:
        game_mode(10)
    elif selection == 4:
        game_mode(5)
    elif selection == 5:
        game_mode(set_lives = int(input("How many lives: ")))
        
    elif selection == 6:
        print("Thankyou for playing Guess that Word!")
    else:
        print("Choose a valid option")
        difficulty_selection(selection = int(input("CHoice: ")))




#Game mode
def game_mode(lives):
    guessed_letters = ""
    guessed_words = ""
    game_over = False
    game_won = False
    bank = []
    set_lives = lives
    selected_word_for_guess = random.choice(word_bank)
    print(selected_word_for_guess)
    for letter in selected_word_for_guess:
        bank.append("?")
    print(bank)

    while game_over != True:
        print("Press 1: To guess letter\n Press 2: To guess word")
        guess_letter_or_word(choice = int(input("Choice: ")))






#The manin function of the program
def main():
    intro_to_program()
    print_options()
    difficulty_selection(selection = int(input("CHoice: ")))
    #Select opetions for difficulty or amount of lives
    #Pick random words
    #have User guess until correct word
    #Print your donw



# The main function is called
main()