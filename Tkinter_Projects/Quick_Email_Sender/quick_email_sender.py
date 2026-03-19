#Name: Ryan Pereira
#Project Name: Quick Email Sender
#Description:# A Quick Email Sender
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/18/2026
#Last Modified: 6/18/2026




import smtplib
from tkinter import *

window = None
buttons = []




def window_setup():
    window = Tk()
    window.title("Quick Email Sender")
    window.config(padx=20,pady=20)
    return window



def label_setup():
    title_label = Label(text="Quick Email Sender",font=("Arial",24))
    title_label.grid(row=1,column=0,columnspan=5)

    to_section_label = Label(text="To:",font=("Arial",24))
    to_section_label.grid(row=2,column=1)


    subject_section_label = Label(text="Subject:",font=("Arial",24))
    subject_section_label.grid(row=3,column=1)

    message_section_label = Label(text="Message:",font=("Arial",24))
    message_section_label.grid(row=4,column=1)


def entry_setup():
    to_entry = Entry(width=20)
    to_entry.grid(row=2,column=2)

    subject_entry = Entry(width=20)
    subject_entry.grid(row =3,column=2)

    message_entry = Text(width=40,height=20)
    message_entry.grid(row=5,column=1,columnspan=3)


def send_email():
    pass

def clear_all_sections():
    pass

def save_draft():
    pass

def exit_program():
    global window
    window.destroy()



def button_setup():
    send_button = Button(text="Send",command=send_email)
    clear_button = Button(text="Clear",command = clear_all_sections)
    save_button = Button(text="Save",command=save_draft)
    exit_button = Button(text="Exit",command = exit_program)

    send_button.grid(row=6,column=0)
    clear_button.grid(row=6,column=1)
    save_button.grid(row=6,column=2)
    exit_button.grid(row=6,column=3)


def main():
    global window 
    window = window_setup()
    label_setup()
    entry_setup()
    button_setup()
    window.mainloop()




if __name__ == "__main__":
    main()