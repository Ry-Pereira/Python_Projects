from flask import Flask, render_template
from dog_data import *



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html",dog_breed = "Please specify dog breed")


@app.route("/Dog/Random")
def random_dog_picture():
    image_url = get_dog_image("Random")
    image_url_list = image_url.split("/")
    return render_template("index.html",dog_breed = image_url_list[image_url_list.index("breeds") + 1],dog_image = image_url)


@app.route("/Dog/<breed>/Random")
def random_breed_dog_picture(breed):
    if breed in get_all_dog_breeds():
        image_url = get_dog_breed_image(breed)
        image_url_list = image_url.split("/")
        return render_template("index.html",dog_breed = image_url_list[image_url_list.index("breeds") + 1],dog_image = image_url)
    else:
        return render_template("index.html",dog_breed = "Dog Breed Not found",dog_image = " ")



@app.route("/Dog/<breed>/<sub_breed>/Random")
def random_sub_breed_dog_picture(breed,sub_breed):
    image_url = get_dog_sub_breed(breed,sub_breed)
    image_url_list = image_url.split("/")
    return render_template("index.html",dog_breed = image_url_list[image_url_list.index("breeds") + 1],dog_image = image_url)


# Run the Flask app only if this file is executed directly
if __name__ == "__main__":
    # Start Flask development server
    app.run()

