# Introduction To The Program
def intro_to_program():
    print("Welcome To The MORSE CODE TRASNLATOR Program")
    print("We can decipher morse code into text and ciypher text into morse code\n\n")

# Morse Code Dictionary

morse_code_alphabet_and_numbers = {
    'a' : ".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":".....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"----"
    }


# Function prints the menu options to the screen
def print_menu():
    ''' Prints The Menu Options to Screen'''
    
    print("1. Cypher text to Morse Code")
    print("2. Decpher Morse Code to text")
    print("3. Print the Morse Code Alphabet and Numbers")
    print("3.Exit\n\n")




#Tutorial Instructions
def print_morse_code_alphabet_and_numbers():
    print("MORSE CODE ALPHABET AND NUMBERS\n")
    for morse_character in morse_code_alphabet_and_numbers.keys():
        print(morse_character,":",morse_code_alphabet_and_numbers[morse_character])
    print("\n")
    

# Function converts Text input into Morse Code
def cypher_text(text):
    text_to_morse_code = ""
    for character in text.lower():
        if character == " ":
            text_to_morse_code += "/"
        else:
            for morse_text in morse_code_alphabet_and_numbers.keys():
                if character == morse_text:
                    text_to_morse_code += morse_code_alphabet_and_numbers[morse_text]

    print("Text to Morse Code:",text_to_morse_code)



    

#Function that converts Morse Code into Text.

def decypher(morse_code):
    morse_code_to_text = " "
    morse_code_list = morse_code.split(" ")
    for code in morse_code_list:
        if code == "/":
            morse_code_to_text += " "
        else:
            for morse_character in morse_code_alphabet_and_numbers.keys():
                if morse_code_alphabet_and_numbers[morse_character] == code:
                    morse_code_to_text += morse_character
                    
    print("Morse Code to Text:",morse_code_to_text)
        
    
         
#Menu Selection Function
def menu_selection(menu_input):
    while menu_input != 4:
        if menu_input == 1:
            cypher_text(input("Text to Morse Code: "))
        elif menu_input == 2:
            decypher(input("Morse to Text: "))
        elif menu_input == 3:
            print_morse_code_alphabet_and_numbers()
        else:
            print("Please put a valid chopice")
            
        print_menu()
        menu_input = int(input("Choice: "))




        

#End of Program Message
def end_message():
    print("Exit")
    print("Thankyou for using")




    
                  
# The Main function of the program
def main():
    intro_to_program()
    print_menu()
    menu_selection(menu_input = int(input("Choice: ")))
    end_message()





#Main Function called
main()
















    

    

    

    

    

    

    
