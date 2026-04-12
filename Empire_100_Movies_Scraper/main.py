#Name: Ryan Pereira
#Project Name: Color Mixer
#Description:# A Tkinter-based program that allows users to mix colors by clicking on buttons representing different colors. The mixed color is displayed on a canvas, and users can reset the canvas to start over.
#Module Name: Main
#Module Purpose: This program serves as the user interface for the Color Mixer application. It defines the ColorMixerUI class, which sets up the Tkinter window, canvas, and buttons for mixing colors. The class includes methods for adding colors to the mix and resetting the color mix.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/6/2026
#Last Modified: 4/9/2026



from movies_requests import get_movie_titles
from movie_title_scraper import MovieTitleScraper




def main() -> None:
    
    html = get_movie_titles()
    movie_titles = MovieTitleScraper(html).movie_titles
    

    MovieScraper(movie_titles)
    





if __name__ == "__main__":
    main()