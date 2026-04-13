#Name: Ryan Pereira
#Project Name: Playlist Of The Day
#Description: A program that scrapes the Hpt 100 songs from Billboard's website and creates a playlist of the top 100 songs for the day.
#Module Name: song.py
#Module Purpose: This module defines the Song class, which represents a song with its position, name, and artist. The class includes an initializer method to set these attributes when a Song object is created.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/13/2026
#Last Modified: 4/13/2026



#Defining a class to represent a song object with its position, name, and artist.
class Song:
    #A class constructor that initializes the position, name, and artist of a song when a Song object is created.
    def __init__(self, position, name, artist):
        #The object's position is set to the position value passed as an argument when the Song object is created.
        self.position = position
        #The object's name is set to the name value passed as an argument when the Song object is created.
        self.name = name
        #The object's artist is set to the artist value passed as an argument when the Song object is created.
        self.artist = artist