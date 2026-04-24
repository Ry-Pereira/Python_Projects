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
    

def get_dog_breed_image(dog_breed):
    url = f"https://dog.ceo/api/breed/{dog_breed}/images/random"
    headers = {"User-Agent": "Mozilla/5.0"}
    # Send GET request to API
    response = requests.get(url, headers=headers)
    dog_data = response.json()["message"]
    return dog_data

def get_dog_sub_breed(dog_breed,dog_sub_breed):
    url = f"https://dog.ceo/api/breed/{dog_breed}/{dog_sub_breed}/images/random"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    dog_data = response.json()["message"]
    return dog_data



def get_all_dog_breeds():
    url = "https://dog.ceo/api/breeds/list/all"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    dog_data = response.json()["message"]
    return dog_data
    


breeds = get_all_dog_breeds()
for breed in breeds:
    print("Breed: ",breed)
    for sub_breed in breeds[breed]:
        print("  ",sub_breed)








