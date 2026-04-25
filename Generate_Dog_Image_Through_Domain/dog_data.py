import requests





def get_dog_image(dog_breed):
    # API endpoint that provides random dog image
    api_url = "https://dog.ceo/api/breeds/image/random"
    # Header to mimic a browser request
    request_headers = {"User-Agent": "Mozilla/5.0"}
    # Send GET request to API
    api_response = requests.get(api_url, headers=request_headers)
    image_url = api_response.json()["message"]
    return image_url
    

def get_dog_breed_image(dog_breed):
    api_url = f"https://dog.ceo/api/breed/{dog_breed}/images/random"
    request_headers = {"User-Agent": "Mozilla/5.0"}
    # Send GET request to API
    api_response = requests.get(api_url, headers=request_headers)
    image_url = api_response.json()["message"]
    return image_url


def get_dog_sub_breed(dog_breed, dog_sub_breed):
    api_url = f"https://dog.ceo/api/breed/{dog_breed}/{dog_sub_breed}/images/random"
    request_headers = {"User-Agent": "Mozilla/5.0"}
    api_response = requests.get(api_url, headers=request_headers)
    image_url = api_response.json()["message"]
    return image_url


def get_all_dog_breeds():
    api_url = "https://dog.ceo/api/breeds/list/all"
    request_headers = {"User-Agent": "Mozilla/5.0"}
    api_response = requests.get(api_url, headers=request_headers)
    breeds_dict = api_response.json()["message"]
    return breeds_dict
    

def get_all_dog_sub_breeds(dog_breed):
    api_url = f"https://dog.ceo/api/breed/{dog_breed}/list"
    request_headers = {"User-Agent": "Mozilla/5.0"}
    api_response = requests.get(api_url, headers=request_headers)
    sub_breeds_dict = api_response.json()["message"]
    return sub_breeds_dict

    





    











