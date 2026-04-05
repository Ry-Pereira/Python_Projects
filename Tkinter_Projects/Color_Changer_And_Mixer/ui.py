from tkinter import *


RED = (214, 33, 33)
ORANGE = (214, 103, 33)
YELLOW = (214, 211, 33)
LIME = (151, 214, 33)
GREEN = (63, 214, 33)
TEAL = (33, 214, 178)
LIGHT_BLUE = (33, 208, 214)
INDIGO = (33, 118, 214)
BLUE = (33, 54, 214)
PURPLE = (118, 33, 214)
VIOLET = (175, 33, 214)
PINK = (214, 33, 193)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (107, 107, 107)
BROWN = (165, 42, 42)


class ColorChangerAndMixerUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Color Changer And Mixer")
        self.window.config(bg=f"{self.convert_rgb_to_hex_color(WHITE)}")

        self.title_label = Label(text="COLOR CHANGER AND MIXER", font=("Arial",24))
        self.title_label.grid(row=0,column=0,columnspan=2)

        self.title_label = Label(text="By: Ryan Pereira", font=("Arial",20))
        self.title_label.grid(row=1,column=0,columnspan=2)


        self.red_button = Button(text="RED")


        
        self.window.mainloop()

    def convert_rgb_to_hex_color(rgb_color_value):
        return f"#{rgb_color_value[0]:02X}{rgb_color_value[1]:02X}{rgb_color_value[2]:02X}"


    
    
    










testui = ColorChangerAndMixerUI()