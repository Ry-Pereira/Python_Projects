#Name: Ryan Pereira
#Project Name: Playlist Of The Day
#Description: A program that scrapes the Hpt 100 songs from Billboard's website and creates a playlist of the top 100 songs for the day.
#Module Name: Main
#Module Purpose: This program serves as the user interface for the Billboard Top 100 Songs Scraper application. It defines the BillboardTop100SongsScraperUI class, which sets up the Tkinter window, canvas, and buttons for scraping song titles. The class includes methods for adding song titles to the list and resetting the list.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/12/2026
#Last Modified: 4/13/2026




#Importing datetime library to work with dates and times, which is used to get the current date in the required format for scraping the Billboard Top 100 songs.
import datetime

#Importing the get_billboard_top_100 function from the billboard_100_songs_requests module, which is responsible for making HTTP requests to the Billboard website and retrieving the HTML content of the page containing the top 100 songs.
from billboard_100_songs_requests import get_billboard_top_100
#Importing the BillboardTop100SongsScraper class from the billboard_100_songs_scraper module, which is responsible for parsing the HTML content of the Billboard Top 100 songs page and extracting the song titles and artists.
from billboard_100_songs_scraper import BillboardTop100SongsScraper


#Defining the main function, serves as the entry point of the program. It retrieves the HTML content of the Billboard Top 100 songs page for the current date, creates an instance of the BillboardTop100SongsScraper class to parse the content, and then prints the song titles and artists in a formatted manner.
def main():
    #Getting the HTML content of the Billboard Top 100 songs page for the current date by calling the get_billboard_top_100 function with the current date formatted as "YYYY-MM-DD". The retrieved HTML content is stored in the variable billboard_top_100_songs.
    billboard_top_100_songs = get_billboard_top_100(datetime.date.today().strftime("%Y-%m-%d"))
    #Creating an instance of the BillboardTop100SongsScraper class by passing the retrieved HTML content as an argument to the constructor. This instance is stored in the variable billboard_top_100_song_scraper, which can then be used to access the parsed song titles and artists.
    billboard_top_100_song_scraper = BillboardTop100SongsScraper(billboard_top_100_songs)


    
    print(num + 1, test.artists[num].text.strip(), " - ", test.songs[num].text.strip())
    num+=1





#This block checks if the script is being run directly (as the main program) and if so, it calls the main() function to execute the program. This is a common Python idiom that allows the script to be imported as a module without executing the main() function, while still allowing it to be run as a standalone program.
if __name__ == "__main__":
    #Main function is callled
    main()