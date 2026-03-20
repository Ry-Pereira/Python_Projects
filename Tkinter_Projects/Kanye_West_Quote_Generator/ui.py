from tkinter import *
import requests
import random

BACKGROUND_COLOR = "#8CC7C4"
WINDOW_COLOR = "#2C687B"
TITLE_COLOR = "white"
class KanyeWestGeneratorUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Kanye West Quote Generator")
        self.window.config(padx=20,pady=20,bg=WINDOW_COLOR)


        self.title_label = Label(text="Kanye West Quote Generator",font=("Arial",24,"bold italic"),bg=WINDOW_COLOR,fg=TITLE_COLOR)
        self.title_label.grid(row=0,column=0,columnspan=2)

        self.canvas = Canvas(width = 600,height=600,bg=BACKGROUND_COLOR,highlightthickness=0)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=10)


        self.kanye_image = PhotoImage(file="images/kanye.png")
        self.canvas.create_image(230,500,image = self.kanye_image)

        self.red_bubble = PhotoImage(file="images/speech_bubbles/red_speech.png")
        self.orange_bubble = PhotoImage(file="images/speech_bubbles/orange_speech.png")
        self.yellow_bubble = PhotoImage(file="images/speech_bubbles/yellow_speech.png")
        self.green_bubble = PhotoImage(file="images/speech_bubbles/green_speech.png")
        self.blue_bubble = PhotoImage(file="images/speech_bubbles/blue_speech.png")
        self.purple_bubble = PhotoImage(file="images/speech_bubbles/purple_speech.png")
        self.pink_bubble = PhotoImage(file="images/speech_bubbles/pink_speech.png")
        
        self.speech_bubbles = [self.red_bubble,self.orange_bubble,self.yellow_bubble,self.green_bubble,self.blue_bubble,self.purple_bubble, self.pink_bubble]

        self.generate_random_quote()

        

        

        self.window.mainloop()

    def generate_random_quote(self):
        response = requests.get(url="https://api.kanye.rest")
        quote = response.json()["quote"]
        

        self.canvas.create_image(300,250,image = random.choice(self.speech_bubbles))
        self.canvas.create_text(300,240,text=quote,font=("Arial",22,"bold italic"),width=120)





d = KanyeWestGeneratorUI()
