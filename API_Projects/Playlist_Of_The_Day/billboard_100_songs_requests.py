#Name: Ryan Pereira
#Project Name: Playlist Of The Day
#Description: A program that scrapes the Hpt 100 songs from Billboard's website and creates a playlist of the top 100 songs for the day.
#Module Name: billboard_100_songs_requests.py
#Module Purpose: This program serves as the user interface for the Billboard Top 100 Songs Scraper application. It defines the BillboardTop100SongsScraperUI class, which sets up the Tkinter window, canvas, and buttons for scraping song titles. The class includes methods for adding song titles to the list and resetting the list.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/12/2026
#Last Modified: 4/13/2026



#Importing requests library to make HTTP requests to the Billboard website and retrieve the HTML content of the page containing the top 100 songs.
import requests



#Defining a function to get the HTML content of the Billboard Top 100 songs page for a given date. The function takes a date as an argument, constructs the URL for the Billboard chart for that date, and makes a GET request to retrieve the HTML content. The function returns the HTML content as a string.
def get_billboard_top_100(date: str) -> str:
    #Url is constructed by concatenating the base URL for the Billboard Hot 100 chart with the date provided as an argument to the function. The date is formatted as "YYYY-MM-DD" to match the expected format in the URL.
    url = "https://www.billboard.com/charts/hot-100/" + date
    #Headers are defined to include a User-Agent string, which is necessary to mimic a browser request and avoid being blocked by the website. The headers are passed as an argument in the GET request to retrieve the HTML content of the page.
    headers = {"User-Agent": "Mozilla/5.0"}
    #Response is obtained by making a GET request to the constructed URL with the specified headers. The response contains the HTML content of the Billboard Hot 100 chart page for the given date.
    response = requests.get(url, headers=headers)
    #Returning the HTML content of the page as a string, which can then be parsed and processed to extract the song titles and artists for the top 100 songs.
    return response.text