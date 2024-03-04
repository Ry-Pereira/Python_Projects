
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]




def intro_to_program():
    print("Welcome to Casear Cypher Program\n")


def print_menu():
    print("1. To Cypher Code")
    print("2. To Decypher Code\n")

def menu_selection(choice):
    if choice == 1:
        cypher_code()
    elif choice ==2:
        decypher_code()
    else:
        print("Goodbye")
def main():
    intro_to_program()
    print_menu()
    menu_selection(user_choice = int(input("Choice: ")))


main()
