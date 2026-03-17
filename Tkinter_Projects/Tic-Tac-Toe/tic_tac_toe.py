from tkinter import *
from functools import partial

import random

symbols=["X","O"]
symbol = None
winner = None
wins = [
    []
]

def main():
    #Window Setup

    global symbol
    symbol = random.choice(symbols)

    def remove_reset_all_buttons():
        for button in buttons:
            button.grid_remove()

    def restart_game():
        global symbol
        symbol = random.choice(symbols)
        quit_button.grid_remove()
        continue_button.grid_remove()
        for button in buttons:
            button.grid()
            button.config(text="-",bg="white",state=NORMAL)
        
        if symbol == "X":
            tic_tac_toe_turn_label.config(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="red",bg='black')
        if symbol == "O":
            tic_tac_toe_turn_label.config(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="blue",bg="black")

    def quit_game():
        window.destroy()


    def restart_or_quit():
        continue_button.grid()
        quit_button.grid()


    def did_win(symbol_to_compare):
        #LEft and right
        
        if buttons[0]["text"] == symbol_to_compare and buttons[1]["text"] == symbol_to_compare and buttons[2]["text"] == symbol_to_compare:
            return "win"
            
        elif buttons[3]["text"] == symbol_to_compare and buttons[4]["text"] == symbol_to_compare and buttons[5]["text"] == symbol_to_compare:
            return "win"
        elif buttons[6]["text"] == symbol_to_compare and buttons[7]["text"] == symbol_to_compare and buttons[8]["text"] == symbol_to_compare:
            return "win"

        #Up and Down
        elif buttons[0]["text"] == symbol_to_compare and buttons[3]["text"] == symbol_to_compare and buttons[6]["text"] == symbol_to_compare:
            return "win"
        elif buttons[1]["text"] == symbol_to_compare and buttons[4]["text"] == symbol_to_compare and buttons[7]["text"] == symbol_to_compare:
            return "win"
        elif buttons[2]["text"] == symbol_to_compare and buttons[5]["text"] == symbol_to_compare and buttons[8]["text"] == symbol_to_compare:
            return "win"


        #Across
        elif buttons[0]["text"] == symbol_to_compare and buttons[4]["text"] == symbol_to_compare and buttons[8]["text"] == symbol_to_compare:
             return "win"
        elif buttons[2]["text"] == symbol_to_compare and buttons[4]["text"] == symbol_to_compare and buttons[6]["text"] == symbol_to_compare:
            return "win"
        else:
            is_tie = True
            for button in buttons:
                if button["text"] == "-":
                    is_tie = False
            if is_tie == True:
                return "tie"

            return "continue"

        

    




    def symbol_mark(button):
        global symbol
        
        
        if symbol == "X":
            button.config(text=symbol,bg="red")
            did_won = did_win(symbol)
            if did_won == "win":
                tic_tac_toe_turn_label.config(text="X WINS!",font=("Arial",15),width=15,fg="red")
                remove_reset_all_buttons()
                restart_or_quit()
            elif did_won == "tie":
                tic_tac_toe_turn_label.config(text="TIE",font=("Arial",15),width=15,fg="GREEN")
                remove_reset_all_buttons()
                restart_or_quit()

            else:
                symbol = "O"
                tic_tac_toe_turn_label.config(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="blue")
         
        else:
            button.config(text=symbol,bg="blue")
            did_won = did_win(symbol)
            if did_won == "win":
                tic_tac_toe_turn_label.config(text="O WINS!",font=("Arial",15),width=15,fg="blue")
                remove_reset_all_buttons()
                restart_or_quit()
            elif did_won == "tie":
                tic_tac_toe_turn_label.config(text="TIE",font=("Arial",15),width=15,fg="GREEN")
                remove_reset_all_buttons()
                restart_or_quit()
            else:
                symbol = "X"
                tic_tac_toe_turn_label.config(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="red")

        button.config(state=DISABLED)


    window = Tk()
    window.title("Tic-Tac-Toe")
    window.config(padx=50,pady=50)

    #Label
    tic_tac_toe_label = Label(text="TIC-TAC-TOE",font=("Arial",15),width=15)
    tic_tac_toe_label.grid(row=0,column=0,columnspan=4,pady = 10)

    if symbol == "X":
        tic_tac_toe_turn_label = Label(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="red",bg='black')
    if symbol == "O":
        tic_tac_toe_turn_label = Label(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="blue",bg="black")

    tic_tac_toe_turn_label.grid(row=1,column=0,columnspan=4,pady = 10)

    #Button Setup
    button_grid = []
    buttons = []

    for num in range(9):
        button = Button(text="-",height=4,width=7)
        button.config(command=partial(symbol_mark,button))
        buttons.append(button)
        


    continue_button = Button(text="Restart",command=restart_game,width=11,height=2)
    continue_button.grid(row=2,column=0,rowspan=3,columnspan=2,padx=0)
    quit_button = Button(text="Quit",command=quit_game, width = 11,height=2)
    quit_button.grid(row=2,column=2,rowspan=3,columnspan=2,padx=0)

    continue_button.grid_remove()
    quit_button.grid_remove()

    buttons[0].grid(row=2,column=0,padx=0,pady=0)
    buttons[1].grid(row=2,column=1,padx=0,pady=0)
    buttons[2].grid(row=2,column=2,padx=0,pady=0)

    buttons[3].grid(row=3,column=0,padx=0,pady=0)
    buttons[4].grid(row=3,column=1,padx=0,pady=0)
    buttons[5].grid(row=3,column=2,padx=0,pady=0)

    buttons[6].grid(row=4,column=0,padx=0,pady=0)
    buttons[7].grid(row=4,column=1,padx=0,pady=0)
    buttons[8].grid(row=4,column=2,padx=0,pady=0)

    

    


    window.mainloop()






if __name__ == "__main__":
    main()
