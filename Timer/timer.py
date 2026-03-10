#Name: Ryan Pereira
#Project Name: Timer
#Description: A simple timer that lets user enter a time for hours, minutes, and seconds. Let the user start the timer, pause the timer, and reset the timer 
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/10/2026
#Last Modified: 6/10/2026




from tkinter import *
from tkinter import messagebox





def main():
    window = Tk()
    window.title("Timer")
    window.minsize(width = 220, height = 220)
    window.config(padx = 20, pady= 20)
   
    


    #Label
    title_label = Label(text="A Simple Timer",font=("Arial",12))
    title_label.grid(column = 1,row = 0)


    #Entry
    timer_entry = Entry(width = 20)
    timer_entry.grid(column = 1, row = 1)
    timer_entry.focus()




    #Button





    #Main Loop
    window.mainloop()



main()