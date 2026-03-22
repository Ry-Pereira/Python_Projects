#Name: Ryan Pereira
#Project Name: Quick Email Sender
#Module Name: UI
#Module Purpose: ...
#Description:# A Quick Email Sender
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/18/2026
#Last Modified: 6/22/2026




from tkinter import *
from tkinter import messagebox
import smtplib

class UI:
    def __init__(self):

        self.entries = []
        self.window = Tk()
        self.window.title("Quick Email Sender")
        self.window.config(padx=40,pady=40,bg="#F4EBD3")

        self.title_label = Label(text="Quick Email Sender",font=("Arial",24),bg="#F4EBD3",fg="#DED3C4")
        self.title_label.grid(row=0,column=0,columnspan=4,pady=10)

        self.from_section_label = Label(text="From:",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        self.from_section_label.grid(row=1,column=0)


        self.to_section_label = Label(text="To:",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        self.to_section_label.grid(row=2,column=0)
    


        self.subject_section_label = Label(text="Subject:",font=("Arial",20,),bg="#F4EBD3",fg="#DED3C4")
        self.subject_section_label.grid(row=3,column=0)

        self.message_section_label = Label(text="Message:",font=("Arial",20),bg="#F4EBD3",fg="#DED3C4")
        self.message_section_label.grid(row=4,column=0)

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

        #self.entries.append(self.to_entry)
        #self.entries.append(self.subject_entry)


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


    def send_email(self):
        print("Went Well")

        email = self.from_entry.get()
        password = self.password_entry.get()
        to_text = self.to_entry.get()
        subject_text = self.subject_entry.get()
        message_text = self.message_entry.get("1.0", END)

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

        

        


d = UI()