#Name: Ryan Pereira
#Project Name: Playlist Of The Day
#Description: A program that scrapes movie titles from Empire Online's list of best movies of all time.
#Module Name: song.py
#Module Purpose: This program serves as the user interface for the Empire 100 Movies Scraper application. It defines the EmpireMovieScraperUI class, which sets up the Tkinter window, canvas, and buttons for scraping movie titles. The class includes methods for adding movie titles to the list and resetting the list.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/13/2026
#Last Modified: 4/13/2026




class Song:
    def __init__(self, position, name, artist):
        self.position = position
        self.name = name
        self.artist = artist