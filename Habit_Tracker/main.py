import requests
import datetime as dt


DATE_TODAY = dt.datetime.now().strftime("%Y%m%d")
USERNAME = input("Enter you username: ")
TOKEN = input("Enter your own custom token: ")
IS_MINOR = input("Are you minor? (yes/no): ")


pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":IS_MINOR
}


#Running the response again, you will get error, because you already initialized the user with same username and token.
response = requests.post(url=pixela_endpoint, json=user_parameters)

GRAPH_ID = input("Give your graph an id: ")
GRAPH_NAME = input("Give your graph a name: ")
GRAPH_TYPE = input("Give a type for your graph (int/float): ")
GRAPH_DATA_UNIT = input("Give a unit for your graph: ")
GRAPH_COLOR = input("Give a color for your graph: ")

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": GRAPH_DATA_UNIT,
    "type": GRAPH_TYPE,
    "color": GRAPH_COLOR
}

#Used for authentication
headers ={
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(response)


GRAPH_PIXEL_UPDATED_QUANTITY = input("Give a quantity for your graph pixel: ")
update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_graph_config ={
    "date": DATE_TODAY,
    "quantity": GRAPH_PIXEL_UPDATED_QUANTITY
}

response = requests.post(url=update_graph_endpoint,json=update_graph_config,headers=headers)


print(response)

GRAPH_PIXEL_EDIT_PIXEL_QUANTITY = input("Give a quantity for your graph pixel: ")
update_graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_TODAY}"
update_graph_pixel_config = {
    "quantity": GRAPH_PIXEL_EDIT_PIXEL_QUANTITY
}
response = requests.put(url=update_graph_pixel,json=update_graph_pixel_config,headers=headers)
print(response)


GRAPH_DATE_PIXEL_TO_DELETE = input("Give a date for your graph pixel to delete (YYYYMMDD): ")
delete_graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{GRAPH_DATE_PIXEL_TO_DELETE}"
response = requests.delete(url=delete_graph_pixel, headers=headers)
print(response)