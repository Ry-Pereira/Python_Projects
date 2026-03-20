from tkinter import *

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


        self.kanye_image = PhotoImage(file="kanye.png")
        self.canvas.create_image(150,500,image = self.kanye_image)

        self.bubble = PhotoImage(file="speech_bubble.png")
        self.canvas.create_image(150,500,image = self.bubble)

        

        self.window.mainloop()


d = KanyeWestGeneratorUI()
