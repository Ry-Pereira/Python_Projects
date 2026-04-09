from tkinter import *
from functools import partial
from colors import *



class ColorMixerUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Color Changer And Mixer")
        self.canvas_background_color = "#FFFFFF"
        self.window.config(padx=20,pady=20,bg="white")

        self.color_mix = []

        self.title_label = Label(text="COLOR CHANGER AND MIXER", font=("Arial",18),bg="white")
        self.title_label.grid(row=0,column=0,columnspan=5,pady=10)

        self.title_label = Label(text="By: Ryan Pereira", font=("Arial",16),bg="white")
        self.title_label.grid(row=1,column=0,columnspan=5,pady=10)

        self.canvas = Canvas(width=850,height=300,bg=self.canvas_background_color,highlightthickness=0,bd=3,relief="solid")
        self.canvas.grid(row=2,column=0,columnspan=5,padx=15,pady=15)
                            
        self.red_button = Button(text="RED",width=17,pady=15,padx=15,bg="red",command=partial(self.add_color_to_background_color,RED))
        self.red_button.grid(row=3,column=0,pady=10,padx=15)

        self.orange_button = Button(text="ORANGE",width=17,pady=15,padx=15,bg="orange",command=partial(self.add_color_to_background_color,ORANGE))
        self.orange_button.grid(row=3,column=1,pady=10,padx=15)

        self.yellow_button = Button(text="YELLOW",width=17,pady=15,padx=15,bg="yellow",command=partial(self.add_color_to_background_color,YELLOW))
        self.yellow_button.grid(row=3,column=2,pady=10,padx=15)

        self.lime_button = Button(text="LIME",width=17,pady=15,padx=15,bg="lime",command=partial(self.add_color_to_background_color,LIME))
        self.lime_button.grid(row=3,column=3,pady=10,padx=15)

        self.green_button = Button(text="GREEN",width=17,pady=15,padx=15,bg="green",command=partial(self.add_color_to_background_color,GREEN))
        self.green_button.grid(row=3,column=4,pady=10,padx=15)


        self.teal_button = Button(text="TEAL",width=17,pady=15,padx=15,bg="teal",command=partial(self.add_color_to_background_color,TEAL))
        self.teal_button.grid(row=4,column=0,pady=10,padx=15)


        self.light_blue_button = Button(text="LIGHT-BLUE",width=17,pady=15,padx=15,bg="light blue",command=partial(self.add_color_to_background_color,LIGHT_BLUE))
        self.light_blue_button.grid(row=4,column=1,pady=10,padx=15)


        self.indigo_button = Button(text="INDIGO",width=17,pady=15,padx=15,bg="indigo",command=partial(self.add_color_to_background_color,INDIGO))
        self.indigo_button.grid(row=4,column=2,pady=10,padx=15)


        self.blue_button = Button(text="BLUE",width=17,pady=15,padx=15,bg="blue",command=partial(self.add_color_to_background_color,BLUE))
        self.blue_button.grid(row=4,column=3,pady=10,padx=15)

        self.purple_button = Button(text="PURPLE",width=17,pady=15,padx=15,bg="purple",command=partial(self.add_color_to_background_color,PURPLE))
        self.purple_button.grid(row=4,column=4,pady=10,padx=15)

        self.violet_button = Button(text="VIOLET",width=17,pady=15,padx=15,bg="violet",command=partial(self.add_color_to_background_color,VIOLET))
        self.violet_button.grid(row=5,column=0,pady=10,padx=15)


        self.pink_button = Button(text="PINK",width=17,pady=15,padx=15,bg="pink",command=partial(self.add_color_to_background_color,PINK))
        self.pink_button.grid(row=5,column=1,pady=10,padx=15)

        self.white_button = Button(text="WHITE",width=17,pady=15,padx=15,bg="white",command=partial(self.add_color_to_background_color,WHITE))
        self.white_button.grid(row=5,column=2,pady=10,padx=15)

        self.black_button = Button(text="BLACK",width=17,pady=15,padx=15,bg="black",command=partial(self.add_color_to_background_color,BLACK))
        self.black_button.grid(row=5,column=3,pady=10,padx=15)

        self.gray_button = Button(text="GRAY",width=17,pady=15,padx=15 ,bg="gray",command=partial(self.add_color_to_background_color,GRAY))
        self.gray_button.grid(row=5,column=4,pady=10,padx=15)

        self.reset_button = Button(text="RESET COLOR MIX",width=17,pady=15,padx=15,bg="white",command=self.reset_color_mix)
        self.reset_button.grid(row=6,column=0,columnspan=5,pady=15)

        

    
        
        self.window.mainloop()

    def add_color_to_background_color(self,rgb_color):
        self.color_mix.append(rgb_color)
        r_value = 0
        g_value = 0
        b_value = 0
        for color in self.color_mix:
            r_value += color[0]
            g_value += color[1]
            b_value += color[2]
        self.canvas_background_color = (r_value//len(self.color_mix),g_value//len(self.color_mix),b_value//len(self.color_mix))
        hex_number_of_color = self.convert_rgb_to_hex_color(self.canvas_background_color)
        self.canvas.config(bg=hex_number_of_color)

    def reset_color_mix(self):
        self.color_mix = []
        self.canvas_background_color = "#FFFFFF"
        self.canvas.config(bg=self.canvas_background_color)

    def convert_rgb_to_hex_color(self,rgb_color_value: tuple) -> str:
        return f"#{rgb_color_value[0]:02X}{rgb_color_value[1]:02X}{rgb_color_value[2]:02X}"


    
    
    










testui = ColorChangerAndMixerUI()