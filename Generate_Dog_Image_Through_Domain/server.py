from flask import Flask, render_template
from dog_data import *



app = Flask(__name__)


app = Flask(__name__)


@app.route("/")
def home():
    instructions = "Use /Dog/Random for a random dog image, /Dog/<breed>/Random for a specific breed, or /Dog/<breed>/<sub_breed>/Random for a sub-breed."
    return render_template("index.html", dog_breed="Please specify dog breed", instructions=instructions,image_description = " ")


@app.route("/Dog/Random")
def random_dog_picture():
    image_url = get_dog_image("Random")
    url_parts = image_url.split("/")
    breed_name = url_parts[url_parts.index("breeds") + 1]
    return render_template("index.html", dog_breed=breed_name, dog_image=image_url,instructions="",image_description = f"Image of a {breed_name} dog")


@app.route("/Dog/<breed>/Random")
def random_breed_dog_picture(breed):
    all_breeds = get_all_dog_breeds()
    if breed in all_breeds:
        image_url = get_dog_breed_image(breed)
        url_parts = image_url.split("/")
        breed_name = url_parts[url_parts.index("breeds") + 1]
        return render_template("index.html", dog_breed=breed_name, dog_image=image_url,image_description = f"Image of a {breed_name} dog")
    else:
        return render_template("index.html", dog_breed="Dog Breed Not found", dog_image=" ",instructions="",image_description = " ")


@app.route("/Dog/<breed>/<sub_breed>/Random")
def random_sub_breed_dog_picture(breed, sub_breed):
    all_breeds = get_all_dog_breeds()
    if breed in all_breeds:
        all_sub_breeds = get_all_dog_sub_breeds(breed)
        if sub_breed in all_sub_breeds:
            image_url = get_dog_sub_breed(breed, sub_breed)
            url_parts = image_url.split("/")
            breed_name = url_parts[url_parts.index("breeds") + 1]
            return render_template("index.html", dog_breed=breed_name, dog_image=image_url,image_description =  f"Image of a {breed_name} dog")
        else:
            return render_template("index.html", dog_breed="Dog Breed but Sub-Breed Not found", dog_image=" ",instructions="",image_description = " ")
    else:
        return render_template("index.html", dog_breed="Dog Breed Not found", dog_image=" ",instructions="",image_description = " ")


# Run the Flask app only if this file is executed directly
if __name__ == "__main__":
    # Start Flask development server
    app.run()