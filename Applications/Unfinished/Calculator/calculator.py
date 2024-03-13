# Imports Here
from art_and_commands import *




#Function that introduces the user ot the program
def intro_to_program():
    print(welcome_text)
    print("Welcome to the Calulcator program")



    

#Theis function prints the menu of the program
def menu():
    print("1. To continue")
    print("2. To exit the program")




#This function is used for menu selection
def menu_selection(choice):
    if choice == 1:
        calculator(first_val = int(input("What is the first value")),operation = input("Operation: "),    second_val = int(input("What is the second value")))
    elif choice == 2:
        print("Thankyou")
    else:
        menu_selection(choice = int(input("Choice: ")))

def calculator(first_val,operation,second_val):
    if operation == 
    


#The main function of the program
def main():
    intro_to_program()
    menu()
    menu_selection(choice = int(input("Choice: ")))


    
    


#The main function is called
main()



                                                                                                                   
                                                                                                                   
                                                                                           
