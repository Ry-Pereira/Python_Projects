#Name: Ryan Pereira
#Project Name: Hangman
#Description: A simple hangman game where the user tries to guess a word
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/11/2026
#Last Modified: 6/11/2026

#Stuff to Hash out: Need to work on formatting, becuase only the the left hand of the minute and seconds can sipport number 0-5


#From the tkinter module, importing everything
from tkinter import *
#From the tkinter module, importing messagebox functionality
from tkinter import messagebox
#rom the hagmanart_py module, importing all the ascii art
from hangman_art import stage_0,stage_1, stage_2, stage_3, stage_4, stage_5, stage_6
from functools import partial

import random


#Hangman words set to a list of of hangamn words to choose from.
hangman_words = ["python", "variable", "function", "loop", "string","integer", "boolean", "list", "tuple", "dictionary","computer", "keyboard", "monitor", "program", "debug","compile", "execute", "syntax", "library", "package",
    "network", "server", "client", "database", "algorithm","puzzle", "mystery", "adventure", "galaxy", "treasure",
    "castle", "dragon", "wizard", "knight", "kingdom","forest", "desert", "ocean", "island", "volcano","planet", "asteroid", "comet", "nebula", "universe"
]

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
stage_number = 0
hangman_stages = [stage_0, stage_1, stage_2, stage_3, stage_4, stage_5, stage_6]
lives=7




            

def select_word():
    selected_word = random.choice(hangman_words)
    selected_word = selected_word.upper()
    return list(selected_word)

def blankout_word(word):
    blankout_word = []
    for letter in word:
        blankout_word.append("_")
    return blankout_word




def main():
    def lose_screen():
        for button in buttons:
            button.config(state=DISABLED)
        canvas.itemconfig(hangman_art,text="YOU LOSE")
        canvas.itemconfig(hangman_word,text=hangman_selected_word)
    
    def win_screen():
        for button in buttons:
            button.config(state=DISABLED)
        canvas.itemconfig(hangman_art,text="YOU WIN")
       


    def switch_stage(stage):
        canvas.itemconfig(hangman_art,text=hangman_stages[stage])
    
    def type_letter(letter,letter_button):
        letter_button.config(state=DISABLED)
        type_in_letter(letter)


    def type_in_letter(letter):
        global stage_number
        global lives
        is_there = False
        for num in range(len(hangman_selected_word)):
            if hangman_selected_word[num] == letter:
                is_there = True
                print("b",hangman_blanked_out_word)
                hangman_blanked_out_word[num] = letter
                canvas.itemconfig(hangman_word,text=hangman_blanked_out_word)
        
        


        if is_there == False:
            stage_number +=1
            lives-=1
            
        if stage_number <= 6:
            switch_stage(stage_number)

        if hangman_blanked_out_word == hangman_selected_word:
            print("You win")
            win_screen()


        if lives == 0:
            print("You lose")
            lose_screen()
    

    hangman_selected_word = select_word()
    hangman_blanked_out_word = blankout_word(hangman_selected_word)

    #Window Setup
    window = Tk()
    window.title("Hangman Game")
    window.config(padx =50,pady=50)
    hangman_title = Label(text="HANGMAN",font=("Arial",20))
    hangman_title.grid(row=0,column=0,columnspan=13)


    #Canvas Setup
    canvas = Canvas(width=320,height=200,bg="blue")
    hangman_art = canvas.create_text(160,90,text=stage_0,font=("Arial",13),anchor="center")
    hangman_word = canvas.create_text(160,180,text=hangman_blanked_out_word,font=("Arial",20),anchor="center")
    canvas.grid(row=1,column=0,columnspan=13)
    

    #Button Setup
    buttons = []
    for alphabet_letter in alphabet:
        button = Button(text=alphabet_letter,width=2)
        button.config(command=partial(type_letter,alphabet_letter,button))
        buttons.append(button)
        if buttons.index(button) < 13:
            buttons[buttons.index(button)].grid(row=2,column=buttons.index(button),padx=0,pady=20)
        else:
            buttons[buttons.index(button)].grid(row=3,column=(buttons.index(button)-13),padx=0,pady=20)

    window.mainloop()




main()