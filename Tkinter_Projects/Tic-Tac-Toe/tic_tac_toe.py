from tkinter import *







def main():
    #Window Setup
    window = Tk()
    window.title("Tic-Tac-Toe")
    window.config(padx=50,pady=50)

    #Label
    tic_tac_toe_label = Label(text="TIC-TAC-TOE",font=("Arial",15),width=15)
    tic_tac_toe_label.grid(row=0,column=0,columnspan=4,pady = 10)

    #Button Setup
    button_grid = []
    button1 = Button(text="X",height=4,width=7)
    button2 = Button(text="X",height=4,width=7)
    button3 = Button(text="X",height=4,width=7)
    button4 = Button(text="X",height=4,width=7)
    button5 = Button(text="X",height=4,width=7)
    button6 = Button(text="X",height=4,width=7)
    button7 = Button(text="X",height=4,width=7)
    button8 = Button(text="X",height=4,width=7)
    button9 = Button(text="X",height=4,width=7)


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
