#Name: Ryan Pereira
#Project Name: Graph Pixel Tracker
#Module Name: Main
#Module Purpose: The moudle is the main entry into the program. It will ask the user for all the necessary information to create a graph and update it. It will also allow the user to edit and delete pixels from the graph.
#Description: A Graph Pixel Tracker is a tool that allows users to track their habits and activities by creating a graph of pixels. Each pixel represents a day and the color of the pixel represents the quantity of the activity. The user can update the graph by adding new pixels, editing existing pixels, and deleting pixels. The graph can be used to visualize the user's progress and motivate them to continue their habits.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/30/2026
#Last Modified: 6/30/2026

#This program uses the Pixela API to create a graph and track habits. The user will be prompted to enter their username, token, and other necessary information to create a graph. The user can then update the graph by adding new pixels, editing existing pixels, and deleting pixels. The program will use the requests library to make API calls to the Pixela API.
import requests
#The datetime module is used to get the current date in the format of YYYYMMDD, which is required by the Pixela API when creating and updating pixels.
import datetime as dt

#The user is prompted to enter their username, token, and whether they are a minor. This information is necessary to create a user account on the Pixela platform and to authenticate API requests. The token is a unique identifier that allows the user to access their account and manage their graphs and pixels.
DATE_TODAY = dt.datetime.now().strftime("%Y%m%d")
USERNAME = input("Enter you username: ")
TOKEN = input("Enter your own custom token: ")
IS_MINOR = input("Are you minor? (yes/no): ")

#Pixela API endpoint for creating a user. The user will be created with the provided username and token. The user must agree to the terms of service and confirm that they are not a minor to create an account.
pixela_endpoint = "https://pixe.la/v1/users"
#The user parameters are stored in a dictionary that will be sent as a JSON payload in the API request to create a user. The parameters include the token, username, agreement to terms of service, and confirmation of not being a minor.
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