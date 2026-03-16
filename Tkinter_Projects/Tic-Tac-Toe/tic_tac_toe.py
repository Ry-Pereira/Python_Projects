from tkinter import *
from functools import partial



symbol = None

def main():
    #Window Setup

    global symbol
    symbol = "X"


    def symbol_mark(button):
        global symbol
        print(symbol)
        button.config(text=symbol)
        button.config(state=DISABLED)
        if symbol == "X":
            symbol = "O"
        else:
            symbol = "X"


    window = Tk()
    window.title("Tic-Tac-Toe")
    window.config(padx=50,pady=50)

    #Label
    tic_tac_toe_label = Label(text="TIC-TAC-TOE",font=("Arial",15),width=15)
    tic_tac_toe_label.grid(row=0,column=0,columnspan=4,pady = 10)

    #Button Setup
    button_grid = []
    button1 = Button(text="-",height=4,width=7)
    button2 = Button(text="-",height=4,width=7)
    button3 = Button(text="-",height=4,width=7)
    button4 = Button(text="-",height=4,width=7)
    button5 = Button(text="-",height=4,width=7)
    button6 = Button(text="-",height=4,width=7)
    button7 = Button(text="-",height=4,width=7)
    button8 = Button(text="-",height=4,width=7)
    button9 = Button(text="-",height=4,width=7)

    #Button Configuration
    button1.config(command=partial(symbol_mark,button1))
    button2.config(command=partial(symbol_mark,button2))
    button3.config(command=partial(symbol_mark,button3))
    button4.config(command=partial(symbol_mark,button4))
    button5.config(command=partial(symbol_mark,button5))
    button6.config(command=partial(symbol_mark,button6))
    button7.config(command=partial(symbol_mark,button7))
    button8.config(command=partial(symbol_mark,button8))
    button9.config(command=partial(symbol_mark,button9))

    button1.grid(row=1,column=0,padx=0,pady=0)
    button2.grid(row=1,column=1,padx=0,pady=0)
    button3.grid(row=1,column=2,padx=0,pady=0)

    button4.grid(row=2,column=0,padx=0,pady=0)
    button5.grid(row=2,column=1,padx=0,pady=0)
    button6.grid(row=2,column=2,padx=0,pady=0)

    button7.grid(row=3,column=0,padx=0,pady=0)
    button8.grid(row=3,column=1,padx=0,pady=0)
    button9.grid(row=3,column=2,padx=0,pady=0)


    window.mainloop()






if __name__ == "__main__":
    main()
