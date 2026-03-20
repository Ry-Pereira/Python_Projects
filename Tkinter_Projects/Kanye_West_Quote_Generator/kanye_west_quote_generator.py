from tkinter import *








window = None
canvas = None
kanye_image = None

def window_setup():
    global window
    window = Tk()
    window.title("Kanye West Quote Generator")
    window.config(padx=20,pady=20)
    return window

def canvas_setup():
    global canvas
    canvas = Canvas(width = 600,height =600)
    canvas.grid(row=1,column=1)
    return canvas

def image_setup():
    global kanye_image
    global canvas
    kanye_image = PhotoImage(file="kanye_west_photo.png")
    canvas.create_image(40,40,image = kanye_image)

def label_setup():
    title_label = Label(text="Kanye West Quote Generator",font=("Arial",12))
    title_label.grid(row=0,column=0,columnspan=3)


def main():
    global window
    global canvas
    window = window_setup()
    canvas = canvas_setup()
    label_setup()
    image_setup()
    window.mainloop()




if __name__=="__main__":
    main()