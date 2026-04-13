#Name: Ryan Pereira
#Project Name: Empire 100 Movies Scraper
#Description: A program that scrapes movie titles from Empire Online's list of best movies of all time.
#Module Name: Main
#Module Purpose: This program serves as the user interface for the Empire 100 Movies Scraper application. It defines the EmpireMovieScraperUI class, which sets up the Tkinter window, canvas, and buttons for scraping movie titles. The class includes methods for adding movie titles to the list and resetting the list.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/6/2026
#Last Modified: 4/12/2026

import requests




def get_billboard_top_100(date):
    url = "https://www.billboard.com/charts/hot-100/" + date
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.text