from flask import Flask

random_number = None



app = Flask(__name__)



@app.route("/")
def home():
    return "<p> Change the url to have /number/1 to /number/9"

@app.route("/number/1")
def one_page():
    if random_number == 1:
        return "<h1>CORRECT!!!1!</h1>"
    else:
        return "<h1>INCORRECT!!!1!</h1>"



@app.route("/number/2")
def two_page():
    if random_number == 2:
        return "<h1>CORRECT!!!2!</h1>"
    else:
        return "<h1>INCORRECT!!!2!</h1>"


@app.route("/number/3")
def three_page():
    if random_number == 3:
        return "<h1>CORRECT!!!3!</h1>"
    else:
        return "<h1>INCORRECT!!!3!</h1>"

@app.route("/number/4")
def four_page():
    if random_number == 4:
        return "<h1>CORRECT!!!4!</h1>"
    else:
        return "<h1>INCORRECT!!!4!</h1>"

@app.route("/number/5")
def five_page():
    if random_number == 5:
        return "<h1>CORRECT!!!5!</h1>"
    else:
        return "<h1>INCORRECT!!!5!</h1>"


@app.route("/number/6")
def six_page():
    if random_number == 6:
        return "<h1>CORRECT!!!6!</h1>"
    else:
        return "<h1>INCORRECT!!!6!</h1>"


@app.route("/number/7")
def seven_page():
    if random_number == 7:
        return "<h1>CORRECT!!!7!</h1>"
    else:
        return "<h1>INCORRECT!!!7!</h1>"

@app.route("/number/8")
def eight_page():
    if random_number == 8:
        return "<h1>CORRECT!!!8!</h1>"
    else:
        return "<h1>INCORRECT!!!8!</h1>"

@app.route("/number/9")
def nine_page():
    if random_number == 9:
        return "<h1>CORRECT!!!9!</h1>"
    else:
        return "<h1>INCORRECT!!!9!</h1>"
