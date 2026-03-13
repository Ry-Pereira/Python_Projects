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
selected_word = list(random.choice(hangman_words).upper())
hangman_stages = [stage_0, stage_1, stage_2, stage_3, stage_4, stage_5, stage_6]


lives = 7
stage_number = 0


def type_letter(letter,letter_button):
    letter_button.config(state=DISABLED)
    print(letter)
    #type_in_letter(letter)

'''

def lose_screen(letter_buttons):
    global selected_word
    for button in buttons:
            button.config(state=DISABLED)
            canvas.itemconfig(hangman_art,text="YOU LOSE")
            canvas.itemconfig(hangman_word,text=selected_word)
    
def restart_or_quit():
    pass

def switch_stage(stage):
    canvas.itemconfig(hangman_art,text=hangman_stages[stage])

def game():
    pass


def type_in_letter(letter):
        global lives
        global stage_number
        is_there = False
        for num in range(len(selected_word)):
            if selected_word[num] == letter:
                is_there = True
                blank_word[num] = letter
                canvas.itemconfig(hangman_word,text=blank_word)
        
        if is_there == False:
            stage_number +=1
            lives-=1
            
        if stage_number <= 6:
            switch_stage(stage_number)


        if lives == 0:
            print("You lose")
            kill_game()
            '''


def main():

    #Window Set Up
    window = Tk()

    
    print(selected_word)
    blank_word = []
    buttons = []
    for letter in selected_word:
        blank_word.append("_")
   
    window.title("Hangman Game")
    window.config(padx =50,pady=50)

    hangman_title = Label(text="HANGMAN",font=("Arial",20))
    hangman_title.grid(row=0,column=0,columnspan=13)

    #Labels
    canvas = Canvas(width=320,height=200)
    hangman_art = canvas.create_text(160,90,text=stage_0,font=("Arial",13),anchor="center")
    hangman_word = canvas.create_text(160,180,text=blank_word,font=("Arial",20),anchor="center")
    canvas.config(bg="blue")
    #canvas.create_text(100,20,text="Hangman",font=("Arial",12))
    canvas.grid(row=1,column=0,columnspan=13)
    
    

    #Buttons
    for alphabet_letter in alphabet:
        button = Button(text=alphabet_letter,width=2)
        button.config(command=partial(type_letter,alphabet_letter,button))
        buttons.append(button)




    #Grid Placement

    for num in range(26):
        if num < 13:
            buttons[num].grid(row=2,column=num,padx=0,pady=20)
        
        else:
            buttons[num].grid(row=3,column=(num-13),padx=0,pady=20)


    

    window.mainloop()
    





main()