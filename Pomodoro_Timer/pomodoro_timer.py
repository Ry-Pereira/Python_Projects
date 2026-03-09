#Name: Ryan Pereira
#Project Name: Pomdoro Timer
#Description: A simple Pomodoro timer application that helps users manage their time effectively by breaking work into intervals, traditionally 25 minutes in length, separated by short breaks.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/10/2026
#Last Modified: 6/10/2026


#Input: The user can input the desired work interval (in minutes) and break interval (in minutes). The user can also start, pause, and reset the timer.
#Output: The application will display the remaining time for the current interval (work or break)

#From the tkinter module library, I am importing everything fro all helpful functions and classes to create the GUI needed for the Pomodoro Timer application. This will allow me to create windows, buttons, labels, and other GUI elements to interact with the user and display the timer.
from tkinter import *
from random import *


#Colors to be used

RED = "#FF5555"
PEACH = "#FF937E"
LIME = "#C1E59F"
GREEN = "#A3D78A"

#Handful of quotes to give for the usewr for encourgament
quotes = ["The key is not to prioritize what's on your schedule, but to schedule your priorities. - Stephen Covey",
          "The future depends on what you do today. - Mahatma Gandhi",
          "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
          "Time is what we want most, but what we use worst. - William Penn",
          "The bad news is time flies. The good news is you're the pilot. - Michael Altshuler"]


#The main function will serve as main entry into the program itself.
def main():
    #window variable is set to Tk class object, creating application window for the Pomodoro Timer
    window = Tk()
    #The title of the application window is se to "Pomodoro Timer" to indicate purpose of the program for the user.
    window.title("Pomodoro Timer")
    #Setting the minimum size of the window to a good 400 x 400, setting 400 for each the width and the height
    window.minsize(width=400, height=400)
    window.config(padx = 10,pady = 10, bg = PEACH)


    title_label = Label(text="Pomodoro Timer", font=("Times New Roman",16))
    title_label.grid(column=0,row=0)

    name_label = Label(text="By: Ryan Pereira", font=("Times New Roman",16))
    name_label.grid(column=2,row=0)

    timer_label = Label(text="00:00", font=("Times New Roman",24))
    timer_label.grid(column=1,row=1)

    start_button = Button(text = "Start")
    start_button.grid(column = 0, row = 3)


    pause_button = Button(text = "Pause")
    pause_button.grid(column = 1, row = 3)

    reset_button = Button(text = "Reset")
    reset_button.grid(column = 2, row = 3)


    quote_label = Label(text=choice(quotes),font=("Times New Roman",12))
    quote_label.grid(column=1,row=4)



    #The main loop of the window application is started, keeping the window open and repsonsive to user if to be closed later.
    window.mainloop()

    



#If the program is being run directly then main function will be called to start the program.
if __name__ == "__main__":
    #The main function is called
    main()