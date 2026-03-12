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
from hangman_art import stage_0

import random


#Hangman words set to a list of of hangamn words to choose from.
hangman_words = ["python", "variable", "function", "loop", "string","integer", "boolean", "list", "tuple", "dictionary","computer", "keyboard", "monitor", "program", "debug","compile", "execute", "syntax", "library", "package",
    "network", "server", "client", "database", "algorithm","puzzle", "mystery", "adventure", "galaxy", "treasure",
    "castle", "dragon", "wizard", "knight", "kingdom","forest", "desert", "ocean", "island", "volcano","planet", "asteroid", "comet", "nebula", "universe"
]













def main():

    


    def type_a():
        a_button.config(state=DISABLED)
        type_in_letter("a")

    def type_b():
        b_button.config(state=DISABLED)
        type_in_letter("b")

    def type_c():
        c_button.config(state=DISABLED)
        type_in_letter("c")

    def type_d():
        d_button.config(state=DISABLED)
        type_in_letter("d")

    def type_e():
        e_button.config(state=DISABLED)
        type_in_letter("e")

    def type_f():
        f_button.config(state=DISABLED)
        type_in_letter("f")


    def type_g():
        g_button.config(state=DISABLED)
        type_in_letter("g")

    def type_h():
        h_button.config(state=DISABLED)
        type_in_letter("h")

    def type_i():
        i_button.config(state=DISABLED)
        type_in_letter("i")


    def type_j():
        j_button.config(state=DISABLED)
        type_in_letter("j")

    def type_k():
        k_button.config(state=DISABLED)
        type_in_letter("k")

    def type_l():
        l_button.config(state=DISABLED)
        type_in_letter("l")

    def type_m():
        m_button.config(state=DISABLED)
        type_in_letter("m")

    def type_n():
        n_button.config(state=DISABLED)
        type_in_letter("n")

    def type_o():
        o_button.config(state=DISABLED)
        type_in_letter("o")

    def type_p():
        p_button.config(state=DISABLED)
        type_in_letter("p")

    def type_q():
        q_button.config(state=DISABLED)
        type_in_letter("q")

    def type_r():
        r_button.config(state=DISABLED)
        type_in_letter("r")

    def type_s():
        s_button.config(state=DISABLED)
        type_in_letter("s")

    def type_t():
        t_button.config(state=DISABLED)
        type_in_letter("t")

    def type_u():
        u_button.config(state=DISABLED)
        type_in_letter("u")

    def type_v():
        v_button.config(state=DISABLED)
        type_in_letter("v")
    
    def type_w():
        w_button.config(state=DISABLED)
        type_in_letter("w")
    def type_x():
        x_button.config(state=DISABLED)   
        type_in_letter("x")  
    def type_y():
        y_button.config(state=DISABLED) 
        type_in_letter("y")
    def type_z():
        z_button.config(state=DISABLED)
        type_in_letter("z")

    
    def type_in_letter(letter):
        for num in range(len(letter)):
            if selected_word[num] == letter:
                blank_word[num] = letter
        canvas.itemconfig(hangman_word,text=blank_word)



    

    #Window Set Up
    window = Tk()

    selected_word = list(random.choice(hangman_words))
    blank_word = []
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
    a_button = Button(text="A", command = type_a,width = 2)
    b_button = Button(text="B", command = type_b,width = 2)
    c_button = Button(text="C", command = type_c,width = 2)
    d_button = Button(text="D", command = type_d,width = 2)
    e_button = Button(text="E", command = type_e,width = 2)
    f_button = Button(text="F", command = type_f,width = 2)
    g_button = Button(text="G", command = type_g,width = 2)
    h_button = Button(text="H", command = type_h,width = 2)
    i_button = Button(text="I", command = type_i,width = 2)
    j_button = Button(text="J", command = type_j,width = 2)
    k_button = Button(text="K", command = type_k,width = 2)
    l_button = Button(text="L", command = type_l,width = 2)
    m_button = Button(text="M", command = type_m,width = 2)
    n_button = Button(text="N", command = type_n,width = 2)
    o_button = Button(text="O", command = type_o,width = 2)
    p_button = Button(text="P", command = type_p,width = 2)
    q_button = Button(text="Q", command = type_q,width = 2)
    r_button = Button(text="R", command = type_r,width = 2)
    s_button = Button(text="S", command = type_s,width = 2)
    t_button = Button(text="T", command = type_t,width = 2)
    u_button = Button(text="U", command = type_u,width = 2)
    v_button = Button(text="V", command = type_v,width = 2)
    w_button = Button(text="W", command = type_w,width = 2)
    x_button = Button(text="X", command = type_x,width = 2)
    y_button = Button(text="Y", command = type_y,width = 2)
    z_button = Button(text="Z", command = type_z,width = 2)



    #Grid Placement


    

    a_button.grid(row=2,column=0,padx=0,pady=20)
    b_button.grid(row=2,column=1,padx=0,pady=20)
    c_button.grid(row=2,column=2,padx=0,pady=20)
    d_button.grid(row=2,column=3,padx=0,pady=20)
    e_button.grid(row=2,column=4,padx=0,pady=20)   
    f_button.grid(row=2,column=5,padx=0,pady=20)
    g_button.grid(row=2,column=6,padx=0,pady=20)
    h_button.grid(row=2,column=7,padx=0,pady=20)
    i_button.grid(row=2,column=8,padx=0,pady=20)
    j_button.grid(row=2,column=9,padx=0,pady=20)
    k_button.grid(row=2,column=10,padx=0,pady=20)
    l_button.grid(row=2,column=11,padx=0,pady=20)
    m_button.grid(row=2,column=12,padx=0,pady=20)
    n_button.grid(row=3,column=0,padx=0,pady=10)
    o_button.grid(row=3,column=1,padx=0,pady=10)
    p_button.grid(row=3,column=2,padx=0,pady=10)
    q_button.grid(row=3,column=3,padx=0,pady=10)
    r_button.grid(row=3,column=4,padx=0,pady=10)
    s_button.grid(row=3,column=5,padx=0,pady=10)
    t_button.grid(row=3,column=6,padx=0,pady=10)
    u_button.grid(row=3,column=7,padx=0,pady=10)
    v_button.grid(row=3,column=8,padx=0,pady=10)
    w_button.grid(row=3,column=9,padx=0,pady=10)
    x_button.grid(row=3,column=10,padx=0,pady=10)
    y_button.grid(row=3,column=11,padx=0,pady=10)
    z_button.grid(row=3,column=12,padx=0,pady=10)


    

    window.mainloop()
    





main()