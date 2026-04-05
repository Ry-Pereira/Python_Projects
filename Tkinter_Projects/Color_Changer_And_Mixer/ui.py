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



class ColorChangerAndMixerUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Color Changer And Mixer")
        self.window.config(padx=50,pady=50,bg="white")

        self.title_label = Label(text="COLOR CHANGER AND MIXER", font=("Arial",24),bg="white")
        self.title_label.grid(row=0,column=0,columnspan=5,pady=10)

        self.title_label = Label(text="By: Ryan Pereira", font=("Arial",20),bg="white")
        self.title_label.grid(row=1,column=0,columnspan=5,pady=10)


        self.red_button = Button(text="RED",width=25,pady=15,padx=15,bg="red")
        self.red_button.grid(row=2,column=0,pady=15,padx=15)

        self.orange_button = Button(text="ORANGE",width=25,pady=15,padx=15,bg="orange")
        self.orange_button.grid(row=2,column=1,pady=15,padx=15)

        self.yellow_button = Button(text="YELLOW",width=25,pady=15,padx=15,bg="yellow")
        self.yellow_button.grid(row=2,column=2,pady=15,padx=15)

        self.lime_button = Button(text="LIME",width=25,pady=15,padx=15,bg="lime")
        self.lime_button.grid(row=2,column=3,pady=15,padx=15)

        self.green_button = Button(text="GREEN",width=25,pady=15,padx=15,bg="green")
        self.green_button.grid(row=2,column=4,pady=15,padx=15)


        self.teal_button = Button(text="TEAL",width=25,pady=15,padx=15,bg="teal")
        self.teal_button.grid(row=3,column=0,pady=15,padx=15)


        self.light_blue_button = Button(text="LIGHT-BLUE",width=25,pady=15,padx=15,bg="light blue")
        self.light_blue_button.grid(row=3,column=1,pady=15,padx=15)


        self.indigo_button = Button(text="INDIGO",width=25,pady=15,padx=15,bg="indigo")
        self.indigo_button.grid(row=3,column=2,pady=15,padx=15)


        self.blue_button = Button(text="BLUE",width=25,pady=15,padx=15,bg="blue")
        self.blue_button.grid(row=3,column=3,pady=15,padx=15)

        self.purple_button = Button(text="PURPLE",width=25,pady=15,padx=15,bg="purple")
        self.purple_button.grid(row=3,column=4,pady=15,padx=15)

        self.violet_button = Button(text="VIOLET",width=25,pady=15,padx=15,bg="violet")
        self.violet_button.grid(row=4,column=0,pady=15,padx=15)


        self.pink_button = Button(text="PINK",width=25,pady=15,padx=15,bg="pink")
        self.pink_button.grid(row=4,column=1,pady=15,padx=15)

        self.white_button = Button(text="WHITE",width=25,pady=15,padx=15,bg="white")
        self.white_button.grid(row=4,column=2,pady=15,padx=15)

        self.black_button = Button(text="BLACK",width=25,pady=15,padx=15,bg="black")
        self.black_button.grid(row=4,column=3,pady=15,padx=15)

        self.gray_button = Button(text="GRAY",width=25,pady=15,padx=15 ,bg="gray")
        self.gray_button.grid(row=4,column=4,pady=15,padx=15)

        

    def change_background_color(self,color):
        
        self.window.mainloop()

    def convert_rgb_to_hex_color(rgb_color_value):
        return f"#{rgb_color_value[0]:02X}{rgb_color_value[1]:02X}{rgb_color_value[2]:02X}"


    
    
    










testui = ColorChangerAndMixerUI()