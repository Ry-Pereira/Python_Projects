from flask import Flask,render_template
from colordata import get_color_hex



app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/color/<color>")
def color_page(color):
    color_hex = get_color_hex(color)
    if color_hex == "No Color of Description":
        return render_template("index.html",background_color = color)
    else:
        return render_template("index.html",background_color = color)



if __name__ == "__main__":
    app.run()
