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
#Alphabet literal list of every uppercase letter in the alphabet
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#Setting the stage number to 0, to idnicate the start of the game
stage_number = 0
#Hangmang stages set to a list of the hangman stage art in order
hangman_stages = [stage_0, stage_1, stage_2, stage_3, stage_4, stage_5, stage_6]
#Setting the lives t 6, to indicate the start of the game
lives=6




hangman_selected_word = None
hangman_blanked_out_word = None
            

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
    
    global hangman_selected_word
    global hangman_blanked_out_word

    def disbale_all_buttons():
        for button in buttons:
            button.config(state=DISABLED)
    
    def enable_all_buttons():
        for button in buttons:
            button.grid()
        for button in buttons:
            button.config(state=NORMAL)

    def restart():
        global hangman_selected_word
        global hangman_blanked_out_word
        global lives
        global stage_number

        hangman_selected_word = select_word()
        hangman_blanked_out_word = blankout_word(hangman_selected_word)
        lives = 7
        stage_number = 0
        continue_button.grid_remove()
        quit_button.grid_remove()
        enable_all_buttons()
        canvas.itemconfig(hangman_art,text=hangman_stages[stage_number])
        canvas.itemconfig(hangman_word,text=hangman_blanked_out_word)
        
        



    def quit_game():
        window.destroy()


    def continue_or_leave():
        for button in buttons:
            button.grid_remove()
        continue_button.grid(row=2,column=0,rowspan=2,columnspan=5,pady=5)
        quit_button.grid(row=2,column=10,rowspan=2,columnspan=5,pady=5)




    def lose_screen():
        disbale_all_buttons()
        canvas.itemconfig(hangman_art,text="YOU LOSE")
        canvas.itemconfig(hangman_word,text=hangman_selected_word)
        window.after(4000,continue_or_leave)
    
    def win_screen():
        disbale_all_buttons()
        canvas.itemconfig(hangman_art,text="YOU WIN")
        window.after(4000,continue_or_leave)
       


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
            win_screen()


        if lives == 0:
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
    continue_button = Button(text="RESTART",command=restart,width=21,height=3)
    quit_button = Button(text="QUIT",command=quit_game,width=21,height=3)
    
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