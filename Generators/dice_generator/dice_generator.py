# Imports are here
import random

# The function introduces the user to the program
def intro_to_program():
    print("Welcome To The DICE GENERATOR PROGRAM\n\n")



# This function prints the menu to the screen
def print_menu():
    print("1) Generate a random numbered dice ")
    print("2) Choose a numbered dice")
    print("3) Exit Program\n\n")



# This function does the menu selection
def menu_choice(choice):
    if choice == 1:
        roll(generate_random_numbered_dice())
    elif choice == 2:
        roll(choosing_numbered_dice())
    elif choice ==3:
        print("Program Exited")
        print("Thankyou for Using")
    else:
        print("Choose a valid choice")
        menu_choice(choice = int(input("Choice: ")))



# This function generates a random number from the  dice_values
def roll(dice_values):
    pass


        


#This function generates a random genreated numbered sided dice
def generate_random_numbered_dice():
    dice_values = []
    type_of_numbered_dice = random.radint(0,144):
    print(f"You have a {type_of_numbered_dice} sided dice")
    generate_dice_again = input("Generate a new numbered dice(Y/N)")
    if generate_dice_again == "Y":
        generate_random_numbered_dice()
    else:
        for number in range(0,type_of_numbered_dice + 1):
            dice_values.append(number)
        print("Already get ready to roll that dice")
        return dice_values




    
#This function generate a number sided dice on the suer preference
def choosing_numbered_dice():
    dice_values = []
    type_of_numbered_dice = int(input("How many sides should the dice have: "))
    print(f"You have a {type_of_numbered_dice} sided dice")
    for number in range(0,type_of_numbered_dice + 1):
        dice_values.append(number)
    print("Already get ready to roll that dice")
    return dice_values
    






# This the main function of the program.
def main():
    intro_to_program()
    print_menu()
    menu_choice(choice = int(input("Choice: ")))






# Main function is called
main()
