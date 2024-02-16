print("Welcome To The MORSE CODE TRASNLATOR Program")
print("We can decipher morse code into text and ciypher text into morse code")

morse_code_alphabet_and_numbers = {
    'a' : ".-",
    "b":".---",
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
    1:".----",
    2:"..---",
    3:"...--",
    4:".....-",
    5:".....",
    6:"-....",
    7:"--...",
    8:"---..",
    9:"----.",
    0:"----"
    }

def print_menu():
    print("1. Cypher text to Morse Code")
    print("2. Decpher Morse Code to text")
    print("3.Exit\n\n")
    


def cypher_text(text):
    text_to_morse_code = ""
    for character in text:
        if character == " ":
            text_to_morse_code += "/"
        else:
            for morse_text in morse_code_alphabet_and_numbers.keys():
                if character == morse_text:
                    text_to_morse_code += morse_code_alphabet_and_numbers[morse_text]

    print("Morse Code: ",text_to_morse_code)

def decypher(morse_code):
    text = ''
    morse_code_to_text = []
    morse = ''
    num = -1
 
    for code in morse_code:
      num+=1
      

      if code == "/":
          morse_code_to_text.append(morse)
          morse = ' '
          morse_code_to_text.append(" ")
      
          
      else:
          morse += code
          
          if num == (len(morse_code)-1):
              
              morse_code_to_text.append(morse)
          
    
    print(morse_code_to_text)
    numb = 0
    if numb == len(morse_code_to_text):
        for key in morse_code_alphabet_and_numbers.keys():
            print(morse_code_alphabet_and_numbers[key])
            if morse_code_to_text[numb] == morse_code_alphabet_and_numbers[key]:
                 text += key
                 numb += 1
                 
            else:
                 text += " "
                 numb +=1
             

            

       
      
                    
    print("text:",text)
         
                  
    

menu_input = int(input("Choice: "))

while menu_input != 3:
    if menu_input == 1:
        cypher_text(input("Text to Morse Code: "))
    elif menu_input == 2:
        decypher(input("Morse to Text: "))
    else:
        print("Enter a Valid Choice")
    print_menu()
    menu_input = int(input("Choice: "))

print("Exit")
print("Thankyou for using")
















    

    

    

    

    

    

    
