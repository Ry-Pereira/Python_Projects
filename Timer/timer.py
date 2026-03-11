#Name: Ryan Pereira
#Project Name: Timer
#Description: A simple timer that lets user enter a time for hours, minutes, and seconds. Let the user start the timer, pause the timer, and reset the timer 
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/10/2026
#Last Modified: 6/11/2026



#From the tkinter module, importing everything
from tkinter import *
#From the tkinter module, importing messagebox functionality
from tkinter import messagebox




#Valid numbers for the timer, since the user will input the time in string format, there needs to be checking to see if they are putting numbers, not letters or any specual characters.
VALID_NUMBERS = [0,1,2,3,4,5,6,7,8,9]




#Global variables to keep track of time, since user can pause and unpause the timer, and even reset the timer, to keep track of time, and if the timer is paused or not.
#Set minutes is set to None at the start, since user has not inputed a time for minutes yet.
set_minutes = None
#Set seconds is set to None at the start, since user has not input a tiime for seconds yet.
set_seconds = None
#Is paused is set to False at the start, since the timer is not paused at the start of the program.
is_paused = False
#time_id is set to None at the start, since there is no timer running at the start of the progam, so there is no time_id to keep track of yet.
time_id = None




#Colors to use for the program, to make it look nice and appealing to the user, and to make it more enjoyable to use the program.
#WILLOW GREEN is a light green color, to use for the background of the program, and for the timer label when the timer is running.
WILLOW_GREEN = "#84B179"
#SPRING GREEN is a light green color, to use for the background of the entry and buttons, and for the timer label when the timer is paused.
SPRING_GREEN = "#A2CB8B"
#SPRING MIST is a light green color, to use for the background of the timer label when the timer is running.
SPRING_MIST = "#C7EABB"
#SPRING DEW is a light green color, to use for the background of the timer label when the timer is paused.
SPRING_DEW = "#E8F5BD"




#Main function, the main entry point into the program
def main():


    #Close window function will ask the user with a message box pop up if they wish to leave the program, since they clicked the x button to leave
    def close_window():
        #A messagebox aks ok cancel will pop up, asking the user if they wish to leave, if they click ok, then window will be destroyed, if they click cancel, then the program will continue to run and the window will not be destroyed.
        if messagebox.askokcancel(title="Wish to Leave",message="Are you sure you want to leave"):
            #If the user clicks ok, then the window will be destroyed, and the program will end.
            window.destroy()
    
    
    
    #Cuntdown function will take in the minutes and seconds argument from the user, and will update the timer label every second, and will check if the timer is done, if the timer is done, then it will show a messagebox to the user saying that the timer is done, and will reset the timer back to the entry for the user to input a new time.
    def countdown(minutes,seconds):
        #Since the user can pause the timer, and unpause the timer, and even reset the timer, there needs to be a global variable to keep track of the time_id, so that when the user pauses the timer, the program can cancel the after function using the time_id, and when the user unpauses the timer, the program can start a new after function using the time_id.
        global time_id
        
        #This will print the minutes and seconds to the console for testing purposes, to make sure the program is counting down correctly, and to make sure if the pause,unpause, and reset function are working correctly, since the user can pause the timer, and unpause the timer, and even reset the timer, there needs to be a way to keep track of the time, and to make sure the time is counting down correctly, and to make sure the time is updating correctly when the user pauses, unpauses, and resets the timer.
        #print("In countdown",minutes,seconds)
        
        #timer_label will be updated to show the current minutes and seconds, and will be formatted to show two digits for minutes and seconds, like any clock format is, so if the minutes is less than 10, it will show a 0 before the minutes, and if the seconds is less than 10, it will show a 0 before the seconds, to make it look like a clock format.
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        #If seconds is greate than 0, then the program will call the after function to call the countdown function again after 1000 milliseconds or a second, and will pass in the same minutes and seconds -1, since the seconds will be counting down by 1 every second, and the minutes will stay the same until the seconds reaches 0, and then the minutes will start counting down by 1, and the seconds will reset to 59.
        if seconds > 0:
            time_id = window.after(1000,countdown,minutes,seconds-1)
        #If seconds is 0 and minutes is greater than 0, then the program will call the after function to call the countdonwn function after 1000 milliseconds or a second, and will pass in the minutes - 1, since the minutes will be counting down by 1 every time the seconds reaches 0, and the seconds will reset to 59, since the seconds will be counting down by 1 every second, and when the seconds reaches 0, it will reset to 59, and the minutes will start counting down by 1.
        elif seconds == 0 and minutes > 0:
            time_id = window.after(1000,countdown,minutes-1,seconds + 59)
        #If the seocnds is 0 and minutes is also 0, the timer is done, so the program will show a messagebox to the user saying that the timer is done, and will reset the timer back to the entry for the user to input a new time, and will also disable the pause and unpause button, since there is no timer running, and will also disable the restart button, since there is no timer running, and will also hide the timer label, since there is no timer running, and will show the entry for the user to input a new time.
        elif seconds == 0 and minutes == 0:
            #Timer label will be hidden, since the timer is no longer running
            timer_label.grid_forget()
            #Timer entry will be shown again, in the same place as the timer label, with same configuration
            timer_entry.grid(column = 1, row = 1, pady = 10)
            #Start button will be updated to be normal, since the timer is no longer running
            start_button.config(state=NORMAL)
            #Restart button will be updated to be disabled, ince the timer is no longer running, ther is no time to restart, so the restart button will be disabled
            restart_button.config(state=DISABLED)
            #Message bow will show info with the title and message to indicate that the timer is done, to let user know the timer is finished, and to let user know they can input a new time if they wish to start a new timer.
            messagebox.showinfo(title="Timer is Done",message="Timer is Done")

        



    #The function start timer will be called when the user clicks the start button, and will get the time from the entry, and will check if the time is in the correct format, and if it is in the correct format, it will start the timer by calling the countdown function with the minutes and seconds that the user inputed, and will also update the buttons and labels to reflect that the timer is running, and will also disable the start button, since there is a timer running, and will enable the pause and unpause button, since there is a timer running, and will enable the restart button, since there is a timer running, and will also hide the entry for the user to input a new time, since there is already a timer running, and will show the timer label to show the time counting down.
    def start_timer():
        #Timter time is set to the value of the timer entry, which is the time that the user inputed, and will be in string format, since the entry is in string format, so the time will be in string format, and will need to be checked to make sure it is in the correct format, and will need to be converted to integers for minutes and seconds to be used in the countdown function.
        timer_time = timer_entry.get()
        #if the length of timer time is greater than 5 or lesser than 5, then the program will show a messagebox to the user saying to input a a valid time, since the correct format only supports minutes and seconds occupied by 5 characters, with a colon in the middle, so if the length is greater than 5 or lesser than 5, then it is not in the correct format, and the program will show a messagebox to the user saying to input a valid time.
        if len(timer_time) > 5 or len(timer_time) < 5 :
            messagebox.showinfo(title="Error",message="Sorry Please Input a valid time")
        #If the timer time is 00:00, then the program will show a messagebox to the user saying to input a valid time, since 00:00 is not a valid time to start a timer, since it is already at 0, so the program will show a messagebox to the user saying to input a valid time.
        elif timer_time == "00:00":
            #Message box will show info with the title and message to indicate that the user needs to input a valid time, since 00:00 is not a valid time to start a timer, since it is already at 0, so the program will show a messagebox to the user saying to input a valid time.
            messagebox.showinfo(title="Error",message="Sorry Please Input a valid time")
        #If the timer time is not in the correct format, which means that the first two characters are not numbers, or the third character is not a colon, or the last two characters are not numbers, then the program will show a messagebox to the user saying to input a valid time, since the correct format only supports minutes and seconds occupied by 5 characters, with a colon in the middle, so if the first two characters are not numbers, or the third character is not a colon, or the last two characters are not numbers, then it is not in the correct format, and the program will show a messagebox to the user saying to input a valid time.
        elif int(timer_time[0]) not in VALID_NUMBERS or int(timer_time[1]) not in VALID_NUMBERS or timer_time[2] != ":" or int(timer_time[3]) not in VALID_NUMBERS or int(timer_time[4]) not in VALID_NUMBERS:
            #Message box will show info with the title and message to indicate that the user needs to input a valid time, since the correct format only supports minutes and seconds occupied by 5 characters, with a colon in the middle, so if the first two characters are not numbers, or the third character is not a colon, or the last two characters are not numbers, then it is not in the correct format, and the program will show a messagebox to the user saying to input a valid time.
            messagebox.showinfo(title="Error",message="Sorry please input in valud format")
        #Else if all conditions are passed, which means the timer is in correct format and characters used, then the program will start the timer by calling the countdown function with the minutes and seconds that the user inputed, and will also update the buttons and labels to reflect that the timer is running, and will also disable the start button, since there is a timer running, and will enable the pause and unpause button, since there is a timer running, and will enable the restart button, since there is a timer running, and will also hide the entry for the user to input a new time, since there is already a timer running, and will show the timer label to show the time counting down.
        else:
            #Set minutes is set to the first two characters of the timer time, which is the minutes that the user inputed, and will be converted to an integer, since the entry is in string format, so the time will be in string format, and will need to be converted to integers for minutes and seconds to be used in the countdown function.
            set_minutes = int(timer_time[0:2])
            #Set seconds is set to the last two characters of the timer time, which is the seconds that the user inputed, and will be converted to an integer, since the entry is in string format, so the time will be in string format, and will need to be converted to integers for minutes and seconds to be used in the countdown function.
            set_seconds = int(timer_time[3:5])
            #Start button will be updated to be disabled, since there is a timer running, so the user should not be able to start another timer while there is already a timer running.
            start_button.config(state=DISABLED)
            #Pause and unpause button will be updated to be normal, since there is a timer running, so the user should be able to pause and unpause the timer while there is a timer running.
            pause_and_unpause_button.config(state=NORMAL)
            #Restart button will be updated to be normal, since there is a timer running, so the user should be able to restart the timer while there is a timer running.
            restart_button.config(state=NORMAL)
            #Timer entry will be hidden, since there is already a timer running, so the user should not be able to input a new time while there is already a timer running.
            timer_entry.grid_forget()
            #Timer label will be shown, in the same place as the timer entry, with same configuration, to show the time counting down, since there is a timer running, so the user should be able to see the time counting down while there is a timer running.
            timer_label.grid(column = 1, row = 1, pady = 10)
            #Timer label will be configured to have the foreground color of WILLOW GREEN, and the background color of SPRING MIST, to indicate that the timer is running, since there is a timer running, so the timer label should be configured to indicate that the timer is running.
            timer_label.config(fg = '#6A7E3F' ,bg=SPRING_MIST)
            #Countdown function will be called with the set minutes and set seconds that the user inputed, to start the timer counting down, since there is a timer running, so the countdown function should be called to start the timer counting down.
            countdown(set_minutes,set_seconds)

            
    
    def pause_timer():
        global is_paused, time_id
        if is_paused == False:
            window.after_cancel(time_id)
            pause_and_unpause_button.config(text="Unpause")
            start_button.config(state=DISABLED)
            restart_button.config(state=DISABLED)
            is_paused = True
            
            timer_label.config(fg = SPRING_MIST ,bg='#6A7E3F')
         
        else:
            pause_and_unpause_button.config(text="Pause")
            start_button.config(state=DISABLED)
            restart_button.config(state=NORMAL)
            is_paused = False
            set_minutes = int(timer_label['text'][0:2])
            set_seconds = int(timer_label['text'][3:5])
            timer_label.config(fg = '#6A7E3F' ,bg=SPRING_MIST)
            countdown(set_minutes,set_seconds-1)




    def restart_timer():
        window.after_cancel(time_id)
        timer_label.grid_forget()
        timer_entry.grid(column = 1, row = 1, pady = 10)
        start_button.config(state=NORMAL)
        pause_and_unpause_button.confug(state=DISABLED)
        restart_button.config(state=DISABLED)
        
        


    window = Tk()
    window.title("Timer")
    window.minsize(width = 220, height = 220)
    window.config(padx = 25, pady= 25, bg = "#84B179")
   



    #Label
    title_label = Label(text="A Simple Timer",font=("Arial",12))
    title_label.config(bg = "#A2CB8B")
    title_label.grid(column = 1,row = 0)

    timer_label = Label(text = "00:00",font=("Arial",12),width = 10)


    #Entry
    timer_entry = Entry(width = 10,font=("Arial",12))
    timer_entry.grid(column = 1, row = 1, pady = 10)
    timer_entry.insert(0,"00:00")
    timer_entry.config(bg = "#A2CB8B")
    timer_entry.focus()




    #Button
    start_button = Button(text = "Start", command = start_timer,font=("Arial",12))
    start_button.config(bg = "#A2CB8B")
    start_button.grid(column=0,row=2, pady = 10)
    pause_and_unpause_button = Button(text="Pause", command = pause_timer,font=("Arial",12))
    pause_and_unpause_button.config(bg = "#A2CB8B")
    pause_and_unpause_button.grid(column=1,row=2, pady = 10)
    restart_button = Button(text="Restart", command = restart_timer,font=("Arial",12))
    restart_button.config(bg = "#A2CB8B")
    restart_button.grid(column=2,row=2, pady = 10)
    restart_button.config(state=DISABLED)
    pause_and_unpause_button.config(state=DISABLED)

    #If the user clicks the x buttons on the window, which meaning they want to leave, the function close window will be called, to ask if the user really want to leave the program.
    window.protocol("WM_DELETE_WINDOW",close_window)


    #Window will kepp on looping until the user themselves exit the program.
    window.mainloop()


#Calling the main function for the whole program to start
main()