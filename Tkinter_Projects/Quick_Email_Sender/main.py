#Name: Ryan Pereira
#Project Name: Quick Email Sender
#Module Name: Main
#Module Purpose: The main module is the entry point of the program, and it is responsible for running the program and creating an instance of the UI class to provide a graphical user interface for the program.
#Description: A Quick Email Sender that allows users to send emails quickly and easily through a graphical user interface.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 3/18/2026
#Last Modified: 3/31/2026


#The main module is the entry point of the program, and it is responsible for running the program and creating an instance of the UI class to provide a graphical user interface for the program.
from ui import *




#The main function is defined in order to run the program, and create an instance of the UI class to provide a graphical user interface for the program.
def main() -> None:
    #Creating an instance of the UI class to provide a graphical user interface for the program.
    quick_email_sender_ui = UI()


#The mainloop function is called on the UI's window in order to keep the program running and the graphical user interface responsive.
if __name__ == "__main__":
    #Calling the main function to run the program, and create an instance of the UI class to provide a graphical user interface for the program.
    main()