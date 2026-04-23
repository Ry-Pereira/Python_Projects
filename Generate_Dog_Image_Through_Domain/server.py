from flask import Flask, render_template
from dog_data import get_dog_image



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html",dog_breed = "Please specify dog breed")


@app.route("/Dog/Random")
def random_dog_picture():
    image_url = get_dog_image("Random")
    return render_template("index.html",dog_breed = " ",dog_image = image_url)


# Run the Flask app only if this file is executed directly
if __name__ == "__main__":
    # Start Flask development server
    app.run()

