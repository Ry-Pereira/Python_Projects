import requests





def get_dog_image(dog_breed):
    if dog_breed == "Random":
        # API endpoint that provides CSS color data
        url = "https://dog.ceo/api/breeds/image/random"
        # Header to mimic a browser request
        headers = {"User-Agent": "Mozilla/5.0"}
        # Send GET request to API
        response = requests.get(url, headers=headers)
        dog_data = response.json()["message"]
        return dog_data
    






b = get_dog_image("Random")
print(b)







