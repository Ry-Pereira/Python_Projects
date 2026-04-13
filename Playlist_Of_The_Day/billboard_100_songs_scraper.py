#Name: Ryan Pereira
#Project Name: Playlist Of The Day
#Description: A program that scrapes the Hpt 100 songs from Billboard's website and creates a playlist of the top 100 songs for the day.
#Module Name: billboard_100_songs_scraper.py
#Module Purpose: This program serves as the user interface for the Billboard Top 100 Songs Scraper application. It defines the BillboardTop100SongsScraperUI class, which sets up the Tkinter window, canvas, and buttons for scraping song titles. The class includes methods for adding song titles to the list and resetting the list.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/12/2026
#Last Modified: 4/13/2026






#Importing BeautifulSoup from the bs4 library to parse the HTML content of the Billboard Top 100 songs page and extract the relevant information such as song titles and artists.
from bs4 import BeautifulSoup



#Defining a class to represent the Billboard Top 100 Songs Scraper, which takes the HTML content of the Billboard Top 100 songs page as input and uses BeautifulSoup to parse the content and extract the song titles and artists. The class initializes
class BillboardTop100SongsScraper:
    #Defined a class constructor that takes the HTML content as an argument, parses it using BeautifulSoup, and extracts the title of the chart, the song titles, and the artists. The extracted information is stored in instance variables for later use.
    def __init__(self, html_content):
        #Soup is created by parsing the HTML content using BeautifulSoup with the "html.parser" parser. The soup object allows for easy navigation and extraction of elements from the HTML structure.
        soup = BeautifulSoup(html_content, "html.parser")
        #The title of the chart is extracted by finding the first <h1> element in the soup and getting its text content. The text is stripped of leading and trailing whitespace, and the last character (which is a colon) is removed to get the clean title of the chart.
        self.title = soup.find("h1").text.strip()[0:-1]
        #The song titles are extracted by finding all <h3> elements with specific class attributes that correspond to the song title elements in the HTML structure of the Billboard Top 100 songs page. The artists are similarly extracted by finding all <span> elements with specific class attributes that correspond to the artist name elements. The extracted song titles and artists are stored in instance variables for later use.
        self.songs = soup.find_all("h3",class_="c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max")
        #The artists are extracted by finding all <span> elements with specific class attributes that correspond to the artist name elements in the HTML structure of the Billboard Top 100 songs page. The extracted artists are stored in an instance variable for later use.
        self.artists = soup.find_all("span",class_="c-label a-no-trucate a-font-secondary u-font-size-15 u-font-size-13@mobile-max u-line-height-18px@mobile-max u-letter-spacing-0010 u-line-height-21px a-children-link-color-black a-children-link-color-brand-secondary:hover lrv-a-children-link-decoration-underline:hover lrv-u-display-block a-truncate-ellipsis-2line u-max-width-397 u-max-width-230@tablet-only u-max-width-300@mobile-max")

