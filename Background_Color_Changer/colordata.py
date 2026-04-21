import requests

def get_color_hex(color_name):
    url = "https://csscolorsapi.com/api/colors"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    color_data = response.json()["colors"]
    for color in color_data:
        if color["name"] == color_name:
            return color["hex"]

    return "No Color of Description"


