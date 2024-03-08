
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]





      

def intro_to_program():
    print("Welcome to Casear Cypher Program\n")
    print(alphabet.index("a"))


def print_menu():
    print("1. To Cypher Code")
    print("2. To Decypher Code\n")



    

def menu_selection(choice):
    if choice == 1:
        cypher_code(word_to_cypher = input("Word to Cypher: "))
    elif choice ==2:
        decypher_code(word_to_decypher = input("Word to Decypher: "))
    else:
        print("Goodbye")


def cypher_code(word_to_cypher):
    cyphered_word = []
    amount_of_shifts = int(input("Aount of shift"))
    for letter in word_to_cypher:
        cyphered_word.append(alphabet[(alphabet.index(letter)) + amount_of_shift])
        



def decypher_code(word_to_decypher):
    pass

        
def main():
    intro_to_program()
    print_menu()
    menu_selection(user_choice = int(input("Choice: ")))


main()
