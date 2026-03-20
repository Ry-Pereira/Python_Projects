from tkinter import *


class KanyeWestGeneratorUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Kanye West Quote Generator")
        self.window.config(padx=20,pady=20)


        self.canvas = Canvas(width = 600,height =600)
        self.canvas.grid(row=1,column=1)


        self.kanye_image = PhotoImage(file="kanye.png")
        self.canvas.create_image(40,40,image = self.kanye_image)

        self.title_label = Label(text="Kanye West Quote Generator",font=("Arial",12))
        self.title_label.grid(row=0,column=0,columnspan=3)


        self.window.mainloop()


d = KanyeWestGeneratorUI()
