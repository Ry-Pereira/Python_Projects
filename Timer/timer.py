#Name: Ryan Pereira
#Project Name: Timer
#Description: A simple timer that lets user enter a time for hours, minutes, and seconds. Let the user start the timer, pause the timer, and reset the timer 
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/10/2026
#Last Modified: 6/10/2026



#From the tkinter module, importing everything
from tkinter import *
#From the tkinter module, importing messagebox functionality
from tkinter import messagebox




#Valid Number
VALID_NUMBERS = [0,1,2,3,4,5,6,7,8,9]

set_minutes = None
set_seconds = None
is_paused = False
time_id = None

#Colors
WILLOW_GREEN = "#84B179"
SPRING_GREEN = "#A2CB8B"
SPRING_MIST = "#C7EABB"
SPRING_DEW = "#E8F5BD"

#Main function, the main entry point into the program
def main():
    #Close window function will ask the user with a message box pop up if they wish to leave the program, since they clicked the x button to leave
    def close_window():
        if messagebox.askokcancel(title="Wish to Leave",message="Are you sure you want to leave"):
            window.destroy()

    def countdown(minutes,seconds):
        global time_id
        
        print("In countdown",minutes,seconds)
        
        timer_label.config(text=f"{minutes:02}:{seconds:02}")

        if seconds > 0:
            time_id = window.after(1000,countdown,minutes,seconds-1)
        elif seconds == 0 and minutes > 0:
            time_id = window.after(1000,countdown,minutes-1,seconds + 59)
        elif seconds == 0 and minutes == 0:
    
            timer_label.grid_forget()
            timer_entry.grid(column = 1, row = 1, pady = 10)
            start_button.config(state=NORMAL)
            restart_button.config(state=DISABLED)
            messagebox.showinfo(title="Timer is Done",message="Timer is Done")

        

    def start_timer():
        timer_time = timer_entry.get()

        if len(timer_time) > 5 or len(timer_time) < 5 :
            messagebox.showinfo(title="Error",message="Sorry Please Input a valid time")
            
        elif timer_time == "00:00":
            messagebox.showinfo(title="Error",message="Sorry Please Input a valid time")
        elif int(timer_time[0]) not in VALID_NUMBERS or int(timer_time[1]) not in VALID_NUMBERS or timer_time[2] != ":" or int(timer_time[3]) not in VALID_NUMBERS or int(timer_time[4]) not in VALID_NUMBERS:
            messagebox.showinfo(title="Error",message="Sorry please input in valud format")
        else:
            set_minutes = int(timer_time[0:2])
            set_seconds = int(timer_time[3:5])
            print(set_minutes,set_seconds)
            
            start_button.config(state=DISABLED)
            pause_and_unpause_button.config(state=NORMAL)
            restart_button.config(state=NORMAL)
            

            timer_entry.grid_forget()
            timer_label.grid(column = 1, row = 1, pady = 10)
            timer_label.config(fg = '#6A7E3F' ,bg=SPRING_MIST)
     
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


    window.protocol("WM_DELETE_WINDOW",close_window)


    #Main Loop
    window.mainloop()


#Calling the main function for the whole program to start
main()