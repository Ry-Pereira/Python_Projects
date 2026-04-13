#Name: Ryan Pereira
#Project Name: Empire 100 Movies Scraper
#Description: A program that scrapes movie titles from Empire Online's list of best movies of all time.
#Module Name: Main
#Module Purpose: This program serves as the user interface for the Empire 100 Movies Scraper application. It defines the EmpireMovieScraperUI class, which sets up the Tkinter window, canvas, and buttons for scraping movie titles. The class includes methods for adding movie titles to the list and resetting the list.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/12/2026
#Last Modified: 4/12/2026





import datetime

from billboard_100_songs_requests import get_billboard_top_100
from billboard_100_songs_scraper import BillboardTop100SongsScraper



def main():
    billboard_top_100_songs = get_billboard_top_100(datetime.date.today().strftime("%Y-%m-%d"))
    billboard_top_100_song_scraper = BillboardTop100SongsScraper(billboard_top_100_songs)


    
    print(num + 1, test.artists[num].text.strip(), " - ", test.songs[num].text.strip())
    num+=1






if __name__ == "__main__":
    main()