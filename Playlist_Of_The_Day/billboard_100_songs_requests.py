

import requests




def get_billboard_top_100(date):
    url = "https://www.billboard.com/charts/hot-100/" + date
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.text