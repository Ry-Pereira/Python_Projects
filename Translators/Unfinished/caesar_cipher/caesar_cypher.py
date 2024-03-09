
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]





      

def intro_to_program():
    print("Welcome to Casear Cypher Program\n")
    print(alphabet.index("z"))


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
    amount_of_shifts = int(input("Amount of shift")) - 1
    for letter in word_to_cypher:
        index_shift = alphabet.index(letter) + amount_of_shifts
        print(index_shift)
        while index_shift >= 25:
            index_shift -= 25
            
        print(index_shift)
        cyphered_word.append(alphabet[index_shift])
    c = ''
    for letter in cyphered_word:
        c+= letter
    print(c)
        
        



def decypher_code(word_to_decypher):
    decyphered_word = []
    amount_of_shifts = int(input("Amount of shift")) - 1
    for letter in word_to_decypher:
        index_shift = alphabet.index(letter) - amount_of_shifts
        print(index_shift)
        while index_shift <= 25:
            index_shift += 25
            
        print(index_shift)
        decyphered_word.append(alphabet[index_shift])
    c = ''
    for letter in decyphered_word:
        c+= letter
    print(c)
        
    

        
def main():
    intro_to_program()
    print_menu()
    menu_selection(choice = int(input("Choice: ")))


main()
