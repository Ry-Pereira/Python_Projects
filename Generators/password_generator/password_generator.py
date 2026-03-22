import random

number_list = ["1","2","3","4","5","6","7","8","9","0"]

letter_list = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k",
                "L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v",
                "W","w","X","x","Y","y","Z","z"]


special_characters_list = ["!","@","#","$","%","^","&","*","<","(",")","<",">","?"]


def generate_password(number_of_numbers,number_of_letters,number_of_special_characters):
    print("Stage 1")
    password_heap = []
    generated_password = ""
    amount_counter = 0
    print("Stage 2: Varibles are good")
    while amount_counter != number_of_numbers:
        v = random.choice(number_list)
        print(v)
        password_heap.append(v)
        print(password_heap)
        
        amount_counter +=1
    amount_counter = 0
    while amount_counter != number_of_letters:
        password_heap.append(random.choice(letter_list))
        
        amount_counter +=1
    amount_counter = 0
    while amount_counter != number_of_special_characters:
        password_heap.append(random.choice(special_characters_list))
       
        amount_counter +=1

        
    print(password_heap)
    while len(password_heap):
        random_heap_item = random.choice(password_heap)
        generated_password +=  random_heap_item
        password_heap.remove( random_heap_item)

        
    print("Stage3: we got ouf while loops")

    print("Your generated password will be:",generated_password)

    is_password_good = input("Do you want to generate a new password(y/n)")
    if is_password_good == "y":
        print("ALrighty, have a good day with your new password",generated_password)
    elif is_password_good == "n":
        generate_password(number_of_numbers = int(input("How many numbers do you want to put in the password: "))
                      ,number_of_letters = int(input("How many letters do you want to put in the password: ")),
                      number_of_special_characters = int(input("How many special characters do you want to put in the password: ")))
    



def print_menu():
    print("Press 1: To generate a random password\n")
    print("Press 2: Check to see if password if strong- Feature to be coming soon\n")


    
def main():
    print("Welcome to the Password Generator Program")
    print_menu()
    generate_password(number_of_numbers = int(input("How many numbers do you want to put in the password: "))
                      ,number_of_letters = int(input("How many letters do you want to put in the password: ")),
                      number_of_special_characters = int(input("How many special characters do you want to put in the password: ")))


main()
