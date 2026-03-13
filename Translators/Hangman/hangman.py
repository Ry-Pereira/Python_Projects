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





'''

def lose_screen(letter_buttons):
    global selected_word
    for button in buttons:
            button.config(state=DISABLED)
            canvas.itemconfig(hangman_art,text="YOU LOSE")
            canvas.itemconfig(hangman_word,text=selected_word)
    


def switch_stage(stage):
    canvas.itemconfig(hangman_art,text=hangman_stages[stage])'''



def type_letter(letter,letter_button,hangman_canvas,blank):
    letter_button.config(state=DISABLED)
    print(letter)
    type_in_letter(letter,hangman_canvas,blank)


def type_in_letter(letter,hangman_canvas,blank_word):
        global lives
        global stage_number
        global blankout_word
        global hangman_word
        blank_word = blankout_word
        is_there = False
        for num in range(len(selected_word)):
            if selected_word[num] == letter:
                is_there = True
                print("b",blank_word)
                blank_word[num] = letter
                hangman_canvas.itemconfig(hangman_word,text=blank_word)
        
        if is_there == False:
            stage_number +=1
            lives-=1
            
        if stage_number <= 6:
            switch_stage(stage_number)


        if lives == 0:
            print("You lose")
            kill_game()
            

def select_word():
    selected_word = random.choice(hangman_words)
    selected_word = selected_word.upper()
    return list(selected_word)

def blankout_word(word):
    blankout_word = []
    for letter in word:
        blankout_word.append("_")
    return blankout_word

def window_setup():
    window = Tk()
    window.title("Hangman Game")
    window.config(padx =50,pady=50)
    hangman_title = Label(text="HANGMAN",font=("Arial",20))
    hangman_title.grid(row=0,column=0,columnspan=13)

    return window

    
def canvas_setup(blank_word):
    canvas = Canvas(width=320,height=200,bg="blue")
    hangman_art = canvas.create_text(160,90,text=stage_0,font=("Arial",13),anchor="center")
    hangman_word = canvas.create_text(160,180,text=blank_word,font=("Arial",20),anchor="center")
    canvas.grid(row=1,column=0,columnspan=13)
    return canvas


def button_setup(canvas,blanked_word):
    #Buttons
    buttons = []
    for alphabet_letter in alphabet:
        button = Button(text=alphabet_letter,width=2)
        button.config(command=partial(type_letter,alphabet_letter,button,canvas,blanked_word))
        buttons.append(button)
        if buttons.index(button) < 13:
            buttons[buttons.index(button)].grid(row=2,column=buttons.index(button),padx=0,pady=20)
        else:
            buttons[buttons.index(button)].grid(row=3,column=(buttons.index(button)-13),padx=0,pady=20)
    return buttons

def main():
    hangman_selected_word = select_word()
    hangman_selected_blanked_out_word = blankout_word(hangman_selected_word)
    hangman_window = window_setup()
    hangman_canvas = canvas_setup(hangman_selected_blanked_out_word,)
    hangman_alphabet_buttons = button_setup(hangman_canvas,hangman_selected_blanked_out_word)
    hangman_window.mainloop()
    





main()