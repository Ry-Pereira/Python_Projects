import requests




def get_response():
    response = requests.get(url="https://api.kanye.rest")
    quote = response.json()["quote"]
    return response,quote
