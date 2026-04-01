#Name: Ryan Pereira
#Project Name: Quick Email Sender
#Module Name: UI
#Module Purpose: The UI module is responsible for providing a graphical user interface for the Quick Email Sender program, allowing users to input their email information and send emails through the program.
#Description:# A Quick Email Sender that allows users to send emails quickly and easily through a graphical user interface.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 3/18/2026
#Last Modified: 3/31/2026



#From the tkinter module, imporitng all the classes,function, and global variable used in order to make this project program.
from tkinter import *
#From the tkinter module, importing the messagebox class in order to have a messagebox show up in the program for user notification.
from tkinter import messagebox
#Importing the smtplib module, in order to establish email sending functionality
import smtplib

#Defining a UI class in order to provide a Graphical User Interface for the Project program
class UI:
    #Defining the init method for the UI class, in order to initialize the UI class and create the graphical user interface for the program.
    def __init__(self) -> None:

        #The ui's object has window set to a Tkinter class in order to provide a graphical user interface window to work on
        self.window = Tk()
        #The Ui's window has a title with a string title value
        self.window.title("Quick Email Sender")
        #The Ui's window is updated with a padding of 40 for y and x postion, so there is spacing, and background color being set.
        self.window.config(padx=40,pady=40,bg="#F4EBD3")


        #The Ui's title label is set with text, font, foreground and background
        self.title_label = Label(text="Quick Email Sender",font=("Arial",24),bg="#F4EBD3",fg="#DED3C4")
        #The Ui's title label is gridded at row,colum location with columnspan and padding for y set
        self.title_label.grid(row=0,column=0,columnspan=4,pady=10)


        #The Ui's from section label is set with text, font, foreground and background
        self.from_section_label = Label(text="From:",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        #The Ui's from section label is gridded at row,colum location
        self.from_section_label.grid(row=1,column=0)

        #The Ui's password section label is set with text, font, foreground and background
        self.password_section_label = Label(text="Password:",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        #The Ui's password section label is gridded at row,colum location
        self.password_section_label.grid(row=2,column=0)


        #The Ui's to section label is set with text, font, foreground and background
        self.to_section_label = Label(text="To",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        #The Ui's to section label is gridded at row,colum location
        self.to_section_label.grid(row=3,column=0)
    

        #The Ui's subject section label is set with text, font, foreground and background
        self.subject_section_label = Label(text="Subject:",font=("Arial",20,),bg="#F4EBD3",fg="#DED3C4")
        #The Ui's subject section label is gridded at row,colum location
        self.subject_section_label.grid(row=4,column=0)

        #The Ui's message section label is set with text, font, foreground and background
        self.message_section_label = Label(text="Message:",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        #The Ui's message section label is gridded at row,colum location
        self.message_section_label.grid(row=5,column=0)


        #The Ui's has entries list to store the entries
        self.entries = []

        #The from entry is set to a Text widget with set width,height, background
        self.from_entry = Text(width=20,height=2,bg="#98A1BC")
        #The from entry is gridded at row,colum location with columnspan and padding for y set
        self.from_entry.grid(row=1, column=1, columnspan=3, sticky="ew",pady=(10, 0))

        #The password entry is set to a Text widget with set width,height, background
        self.password_entry = Text(width=20,height=2,bg="#98A1BC")
        #The password entry is gridded at row,colum location with columnspan and padding for y set
        self.password_entry.grid(row=2, column=1, columnspan=3, sticky="ew",pady=(10, 0))


        #The to entry is set to a Text widget with set width,height, background
        self.to_entry = Text(width=20,height=2,bg="#98A1BC")
        #The to entry is gridded at row,colum location with columnspan and padding for y set
        self.to_entry.grid(row=3, column=1, columnspan=3, sticky="ew",pady=(10, 0))
    
        #The subject entry is set to a Text widget with set width,height, background
        self.subject_entry = Text(width=20,height=2,bg="#98A1BC")
        #The subject entry is gridded at row,colum location with columnspan and padding for y set
        self.subject_entry.grid(row=4, column=1, columnspan=3, sticky="ew",pady=(10, 0))

        #The message entry is set to a Text widget with set width,height, background
        self.message_entry = Text(width=40,height=12,bg="#98A1BC")
        #The message entry is gridded at row,colum location with columnspan and padding for y set
        self.message_entry.grid(row=6,column=0,columnspan=4,sticky="ew",pady=(20, 0))

        #The entries list appends the to entry
        self.entries.append(self.to_entry)
        #The entries list appends the subject entry
        self.entries.append(self.subject_entry)
        #The entries list appends the message entry
        self.entries.append(self.message_entry)

        #The Ui's send button is set to a Button widget with text, command, font, background and foreground
        self.send_button = Button(text="Send",command=self.send_email,font=('Arial',12),bg="#555879",fg="#DED3C4")
        #The Ui's send button is gridded at row,colum location with sticky and padding for y set
        self.send_button.grid(row=7,column=0,sticky="ew",pady=(20, 0))
  

        #The Ui's clear button is set to a Button widget with text, command, font, background and foreground
        self.clear_button = Button(text="Clear",command = self.clear_all_sections,font=('Arial',12),bg="#555879",fg="#DED3C4")
        #The Ui's clear button is gridded at row,colum location with sticky and padding for y set
        self.clear_button.grid(row=7,column=1,sticky="ew",pady=(20, 0))
       

        #The Ui's save button is set to a Button widget with text, command, font, background and foreground
        self.save_button = Button(text="Save",command=self.save_draft,font=('Arial',12),bg="#555879",fg="#DED3C4")
        #The Ui's save button is gridded at row,colum location with sticky and padding for y set
        self.save_button.grid(row=7,column=2,sticky="ew",pady=(20, 0))
   
        #The Ui's exit button is set to a Button widget with text, command, font, background and foreground
        self.exit_button = Button(text="Exit",command = self.exit_program,font=('Arial',12),bg="#555879",fg="#DED3C4")
        #The Ui's exit button is gridded at row,colum location with sticky and padding for y set
        self.exit_button.grid(row=7,column=3,sticky="ew",pady=(20, 0))

        #The Ui's window has grid column configure for 4 columns with weight and uniform set
        for i in range(4):
            #Setting the Ui's window grid column configure for 4 columns with weight and uniform set
            self.window.grid_columnconfigure(i, weight=1,uniform="a")

        #The Ui's valid emails list is set with valid email domains for the program to work with
        self.valid_emails = ["gmail.com","office365.com","yahoo.com","me.com","aol.com"]
        #The Ui's window has the mainloop function called on it in order to keep the program running and the graphical user interface responsive
        self.window.mainloop()

    #Defining a exit program method to exit out of the program
    def exit_program(self) -> None:
        #The Ui's window envokes the destroy functon, destroying the window entirely
        self.window.destroy()

    #Defining the email send form as a draft and to the csv document to save it
    def save_draft(self,email:str,password:str,to_text:str,subject_text:str,message_text:str) -> None:
        #Email is set to the value from getting the text from the from entry field.
        new_emailt_draft = {
            "From":[email],
            "Password":[password],
            "To":[to_text],
            "Subject":[subject_text],
            "Message":[message_text]
        }
        #new email draft is converted to a pandas dataframe, and then the dataframe is appended to the email drafts csv file, with no index and no header, and mode set to append, so it adds to the csv file instead of overwriting it.
        new_emailt_draft.to_csv("email_drafts.csv",mode = "a",index = False,header = False)
        #Executing the Ui's object clear all section method to clear all section in the email sender after saving draft
        self.clear_all_sections()
    
    #Defining clear all sections, that reurns all section in the email send form as empty
    def clear_all_sections(self) -> None:
        for text_entry in self.entries:
            #Text entry deletes everything at the 0 character and until the end
            text_entry.delete(0,END)

        #Message entry deletes everything, until the end of th text, 1.0
        #Starts at line 1, character 0, and goes until the end of text
        self.message_entry.delete("1.0",END)


    #Defining a check fields method to check that section fields are valid in order to send the email
    def check_fields(self,email:str,password:str,to_text:str,subject_text:str,message_text:str) -> bool:
        # If the length of the message,to, and subject text is 0, its empty.
        if len(message_text) == 0 and len(to_text) == 0 and len(subject_text) == 0:
            #Messagebox shows info with title and message to fill in the to section, and that subject and message are optional
            messagebox.showinfo(title="To, Subject, and Message Line Empty",message="Please fill in the to section\nSubject is optional\nMessage is optional")
        #Elif the length of the to and subject is 0, its empty
        elif len(to_text) == 0 and len(subject_text) == 0:
            #Messagebox shows info with title and message to fill in the to section, and that subject is optional
            messagebox.showinfo(title="To and Subject Line Empty",message="Please fill in the to section\nSubject is optional")
        #Elif the length of the to and message is 0, its empty
        elif len(to_text) == 0 and len(message_text) == 0:
            #Messagebox shows info with title and message to fill in the to section, and that message is optional
            messagebox.showinfo(title="To and Subject Line Empty",message="Please fill in the to section\nMessage is optional")
        #Elif the length of the subject and message is 0, its empty
        elif len(to_text) == 0:
            #Messagebox shows info with title and message to fill in the to section, and that subject and message are optional
            messagebox.showinfo(title="To Line",message="To Section Must Be Filled")
        #Elif the length of the subject is 0, its empty
        elif len(subject_text) == 0:
            #Messagebox shows info with title and message to fill in the subject section, and that subject is optional
            result = messagebox.askokcancel(title="Subject Text Is Empty",message="Do You Wish To Send A Empty Subject")
            #If the result is true, then the subject text is set to no subject, in order to send the email with no subject, but not return false and not send the email at all.
            if result == True:
                #Subject text is set to no subject, in order to send the email with no subject, but not return false and not send the email at all.
                subject_text = "No Subject"
        #Elif the length of the message text is 0, its empty
        elif len(message_text) == 0:
            #Messagebox shows info with title and message to fill in the message section, and that message is optional
            result = messagebox.askokcancel(title="Message Text Is Empty",message="Do You Wish To Send A Empty Message")
            #If the result is true, then the message text is set to no message, in order to send the email with no message, but not return false and not send the email at all.
            if result == True:
                #Message text is set to no message, in order to send the email with no message, but not return false and not send the email at all.
                message_text = "No Message"

        #If the email has an @ character in it, then the email list is set to the email split at the @ character, and if the email list at index 1 is not in the valid emails list, then return false, so email is not sent.
        if "@" in email:
            #Email list is set to the email split at the @ character, in order to get the email domain for validation and sending process.
            email_list = email.split("@")
            #If the email list at index 1 is not in the valid emails list, then return false, so email is not sent.
            if email_list[1] not in self.valid_emails:
                #Returns false, to indicate not a valid email
                return False
        #If the to text has an @ character in it, then the to text list is set to the to text split at the @ character, and if the to text list at index 1 is not in the valid emails list, then return false, so email is not sent.
        if "@" in to_text:
            #To text list is set to the to text split at the @ character, in order to get the email domain for validation and sending process.
            to_text_list = to_text.split("@")
            #If the to text list at index 1 is not in the valid emails list, then return false, so email is not sent.
            if to_text_list[1] not in self.valid_emails:
                #Returns false, to indicate not a valid email
                return False

    #Defining a method to verifying and sending the email
    def send_email(self) -> None:
        #Email is set to the value from getting the text from the from entry field.
        email = (self.from_entry.get("1.0",END))
        #Password is set to the value from getting the text from the password entry field.
        password = self.password_entry.get("1.0",END)
        #To text is set to the value from getting the text from the to entry field.
        to_text = self.to_entry.get("1.0",END)
        #Subject text is set to the value from getting the text from the subject entry field.
        subject_text = self.subject_entry.get("1.0",END)
        #Message text is set to the value from getting the text from the message entry field.
        message_text = self.message_entry.get("1.0", END)
        #To text list is set to the to text split at the @ character, in order to get the email domain for validation and sending process.
        to_text_list = to_text.split("@")
        
        #Validating the send form by executing the Ui's object check fields function with email,password,to_text,subject_text,message_text as input
        valid_send_form = self.check_fields(email,password,to_text,subject_text,message_text)
      
        #If the vald send form is true then the mail is in the sending process, but checking to see if the email domain is valud first.
        if valid_send_form == True:
            #If the to text list at index 1, replaces  the new line with space character, if equal to gmail.com string, then the domain is gmail.
            if to_text_list[1].replace("\n"," ") == "gmail.com":
                #Creating a connection variable that is set to the smtplib module's SMTP class with the gmail smtp server as the parameter, in order to establish a connection to the gmail smtp server for sending the email.
                connection = smtplib.SMTP("smtp.gmail.com")
            #ElIf the to text list at index 1, replaces  the new line with space character, if equal to yahoo.com string, then the domain is yahoo.
            elif to_text_list[1].replace("\n"," ") == "yahoo.com":
                #Creating a connection variable that is set to the smtplib module's SMTP class with the yahoo smtp server as the parameter, in order to establish a connection to the yahoo smtp server for sending the email.
                connection = smtplib.SMTP("smtp.mail.yahoo.com")
            #If the to text list at index 1, replaces  the new line with space character, if equal to outlook.com string, then the domain is outlook.
            elif to_text_list[1].replace("\n"," ") == "outlook.com":
                #Creating a connection variable that is set to the smtplib module's SMTP class with the outlook smtp server as the parameter, in order to establish a connection to the outlook smtp server for sending the email.
                connection = smtplib.SMTP("smtp.office365.com")
            #Else the email domain not valid
            else:
                #Showing a message box that show infor of invalid email domain and to enter a valid email domain
                messagebox.showinfo(title="Invalid Email Domain",message="Please enter a valid email domain")
                #Returns out of the function, so email is not sent
                return
            #Connection starts TLS encryption for security
            connection.starttls()
            #Connection logs in with the email and password provided by the user
            connection.login(user=email,password=password)
            #Connection sends the email with the from address, to address, and message formatted with subject and message text
            connection.sendmail(from_addr=email,to_addrs=to_text,msg=f"Subject:{subject_text}\n{message_text}")
            #Connection us closed after sending the email
            connection.close()


        


        
        

        


testing_ui = UI()