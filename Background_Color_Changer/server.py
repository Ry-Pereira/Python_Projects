from flask import Flask,render_template
from colordata import get_color_hex



app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html",instruction = "Instruction:In domain put /color/ and after the backlsach put specifc color\nExample:/color/Red")



@app.route("/color/<color>")
def color_page(color):
    color_hex = get_color_hex(color)
    if color_hex == "No Color of Description":
        return render_template("index.html",instruction = " ",color_name = "Color Not Found",background_color = "#ffffff")
    else:
        return render_template("index.html",instruction = " ",color_name = f"{color}",background_color = color)



if __name__ == "__main__":
    app.run()
