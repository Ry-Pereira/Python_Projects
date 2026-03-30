import requests
import datetime as dt

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

#graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#graph_config = {
 #   "id": "graph1",
  #  "name": "Coding Graph",
   # "unit":"hour",
    #"type":"float",
    #"color":"sora"
#}

#Used for authentication
headers ={
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
#print(response)


#update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
#update_graph_config ={
 #   "date": dt.datetime.now().strftime("%Y%m%d"),
 #   "quantity": "1.5"
#}

#response = requests.post(url=update_graph_endpoint,json=update_graph_config,headers=headers)


#print(response)

update_graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20260330"
update_graph_pixel_config = {
    "quantity": "2.0"
}
response = requests.put(url=update_graph_pixel,json=update_graph_pixel_config,headers=headers)
print(response)


delete_graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20260330"
response = requests.delete(url=delete_graph_pixel, headers=headers)
print(response)