#Name: Ryan Pereira
#Project Name: Quick Email Sender
#Module Name: UI
#Module Purpose: ...
#Description:# A Quick Email Sender
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/18/2026
#Last Modified: 6/24/2026



#From the tkinter module, imporitng all the classes,function, and global variable used in order to make this project program.
from tkinter import *
#From the tkinter module, importing the messagebox class in order to have a messagebox show up in the program for user notification.
from tkinter import messagebox
#Importing the smtplib module, in order to establish email sending functionality
import smtplib

#Defining a UI class in order to provide a Graphical User Interface for the Project program
class UI:
    def __init__(self):

        #The ui's object has window set to a Tkinter class in order to provide a graphical user interface window to work on
        self.window = Tk()
        #The Ui's window has a title with a string title value
        self.window.title("Quick Email Sender")
        #The Ui's window is updated with a padding of 40 for y and x postion, so there is spacing, and background color being set.
        self.window.config(padx=40,pady=40,bg="#F4EBD3")


        #The Ui's title label is set with text, font, foreground and background
        self.title_label = Label(text="Quick Email Sender",font=("Arial",24),bg="#F4EBD3",fg="#DED3C4")
        self.title_label.grid(row=0,column=0,columnspan=4,pady=10)


        #The Ui's from section label is set with text, font, foreground and background
        self.from_section_label = Label(text="From:",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        self.from_section_label.grid(row=1,column=0)

        #The Ui's password section label is set with text, font, foreground and background
        self.password_section_label = Label(text="Password:",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        self.password_section_label.grid(row=2,column=0)


        #The Ui's to section label is set with text, font, foreground and background
        self.to_section_label = Label(text="To",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        self.to_section_label.grid(row=3,column=0)
    

        #The Ui's subject section label is set with text, font, foreground and background
        self.subject_section_label = Label(text="Subject:",font=("Arial",20,),bg="#F4EBD3",fg="#DED3C4")
        self.subject_section_label.grid(row=4,column=0)

        self.message_section_label = Label(text="Message:",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        self.message_section_label.grid(row=5,column=0)

        self.entries = []
        self.from_entry = Text(width=20,height=2,bg="#98A1BC")
        self.from_entry.grid(row=1, column=1, columnspan=3, sticky="ew",pady=(10, 0))

        self.password_entry = Text(width=20,height=2,bg="#98A1BC")
        self.password_entry.grid(row=2, column=1, columnspan=3, sticky="ew",pady=(10, 0))

        self.to_entry = Text(width=20,height=2,bg="#98A1BC")
        self.to_entry.grid(row=3, column=1, columnspan=3, sticky="ew",pady=(10, 0))
    

        self.subject_entry = Text(width=20,height=2,bg="#98A1BC")
        self.subject_entry.grid(row=4, column=1, columnspan=3, sticky="ew",pady=(10, 0))

        self.message_entry = Text(width=40,height=12,bg="#98A1BC")
        self.message_entry.grid(row=6,column=0,columnspan=4,sticky="ew",pady=(20, 0))

        self.entries.append(self.to_entry)
        self.entries.append(self.subject_entry)
        self.entries.append(self.message_entry)


        self.send_button = Button(text="Send",command=self.send_email,font=('Arial',12),bg="#555879",fg="#DED3C4")
        self.send_button.grid(row=7,column=0,sticky="ew",pady=(20, 0))
  


        self.clear_button = Button(text="Clear",command = self.clear_all_sections,font=('Arial',12),bg="#555879",fg="#DED3C4")
        self.clear_button.grid(row=7,column=1,sticky="ew",pady=(20, 0))
       

        self.save_button = Button(text="Save",command=self.save_draft,font=('Arial',12),bg="#555879",fg="#DED3C4")
        self.save_button.grid(row=7,column=2,sticky="ew",pady=(20, 0))
   

        self.exit_button = Button(text="Exit",command = self.exit_program,font=('Arial',12),bg="#555879",fg="#DED3C4")
        self.exit_button.grid(row=7,column=3,sticky="ew",pady=(20, 0))

        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1,uniform="a")

        self.valid_emails = ["gmail.com","office365.com","yahoo.com","me.com","aol.com"]

        self.window.mainloop()

    def exit_program(self):
        self.window.destroy()

    def save_draft(self):
        pass

    def clear_all_sections(self):
        for text_entry in self.entries:
            #Text entry deletes everything at the 0 character and until the end
            text_entry.delete(0,END)

        #Message entry deletes everything, until the end of th text, 1.0
        #Starts at line 1, character 0, and goes until the end of text
        self.message_entry.delete("1.0",END)


    def check_fields(self,email,password,to_text,subject_text,message_text):
        if len(message_text) == 0 and len(to_text) == 0 and len(subject_text) == 0:
            messagebox.showinfo(title="To, Subject, and Message Line Empty",message="Please fill in the to section\nSubject is optional\nMessage is optional")

        elif len(to_text) == 0 and len(subject_text) == 0:
            messagebox.showinfo(title="To and Subject Line Empty",message="Please fill in the to section\nSubject is optional")
        elif len(to_text) == 0 and len(message_text) == 0:
            messagebox.showinfo(title="To and Subject Line Empty",message="Please fill in the to section\nMessage is optional")

        elif len(to_text) == 0:
            messagebox.showinfo(title="To Line",message="To Section Must Be Filled")
        elif len(subject_text) == 0:
            result = messagebox.askokcancel(title="Subject Text Is Empty",message="Do You Wish To Send A Empty Subject")
            if result == True:
                subject_text = "No Subject"
        elif len(message_text) == 0:
            result = messagebox.askokcancel(title="Message Text Is Empty",message="Do You Wish To Send A Empty Message")
            if result == True:
                message_text = "No Message"

        if "@" in email:
            email_list = email.split("@")
            if email_list[1] not in self.valid_emails:
                return False
            
        if "@" in to_text:
            to_text_list = to_text.split("@")
            if to_text_list[1] not in self.valid_emails:
                return False

    def send_email(self):
        print("Went Well")

        email = (self.from_entry.get("1.0",END))
        password = self.password_entry.get("1.0",END)
        to_text = self.to_entry.get("1.0",END)
        subject_text = self.subject_entry.get("1.0",END)
        message_text = self.message_entry.get("1.0", END)
        to_text_list = to_text.split("@")
        print(to_text_list)
        print(to_text_list[1].replace("\n"," "))

        valid_send_form = self.check_fields(email,password,to_text,subject_text,message_text)
        print("well")
        if valid_send_form == True:
            if to_text_list[1].replace("\n"," ") == "gmail.com":
                print("Go into gmail")
                connection = smtplib.SMTP("smtp.gmail.com")
            elif to_text_list[1].replace("\n"," ") == "yahoo.com":
                connection = smtplib.SMTP("smtp.mail.yahoo.com")
            elif to_text_list[1].replace("\n"," ") == "outlook.com":
                connection = smtplib.SMTP("smtp.office365.com")
            else:
                return
            connection.starttls()
            connection.login(user=email,password=password)
            connection.sendmail(from_addr=email,to_addrs=to_text,msg=f"Subject:{subject_text}\n{message_text}")
            connection.close()


        


        
        

        


d = UI()