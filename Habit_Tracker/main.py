import requests


USERNAME = "tatertots"
TOKEN = "hashrbowns:)"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


#Running the response again, you will get error, because you already initialized the user with same username and token.
#response = requests.post(url=pixela_endpoint, json=user_parameters)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit":"hour",
    "type":"float",
    "color":"sora"
}

headers ={
    "X-USER-TOKEN": TOKEN
}

requests.post(url=graph_endpoint,json=graph_config,headers=headers)