
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


print('''

  .oooooo.                                                          .oooooo.    o8o             oooo                           
 d8P'  `Y8b                                                        d8P'  `Y8b   `"'             `888                           
888           .oooo.    .ooooo.   .oooo.o  .oooo.   oooo d8b      888          oooo  oo.ooooo.   888 .oo.    .ooooo.  oooo d8b 
888          `P  )88b  d88' `88b d88(  "8 `P  )88b  `888""8P      888          `888   888' `88b  888P"Y88b  d88' `88b `888""8P 
888           .oP"888  888ooo888 `"Y88b.   .oP"888   888          888           888   888   888  888   888  888ooo888  888     
`88b    ooo  d8(  888  888    .o o.  )88b d8(  888   888          `88b    ooo   888   888   888  888   888  888    .o  888     
 `Y8bood8P'  `Y888""8o `Y8bod8P' 8""888P' `Y888""8o d888b          `Y8bood8P'  o888o  888bod8P' o888o o888o `Y8bod8P' d888b    
                                                                                      888                                      
                                                                                     o888o                                     
                                                                                                                               
''')


      

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
    amount_of_shifts = int(input("Amount of shift")) 
    for letter in word_to_cypher:
        index_shift = alphabet.index(letter) + amount_of_shifts
        print(index_shift)
        while index_shift >= 25:
            index_shift -= 1
            index_shift -= 25
            
        print(index_shift)
        cyphered_word.append(alphabet[index_shift])
    c = ''
    for letter in cyphered_word:
        c+= letter
    print(c)
        
        



def decypher_code(word_to_decypher):
    decyphered_word = []
    amount_of_shifts = int(input("Amount of shift"))
    for letter in word_to_decypher:
        index_shift = alphabet.index(letter) - amount_of_shifts
        print(index_shift)
        while index_shift <= 0:
            index_shift += 1
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
