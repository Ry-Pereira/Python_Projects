#Name: Ryan Pereira
#Project Name: Empire 100 Movies Scraper
#Description:# A python program that scrapes the top 100 movies of all time from the Empire Online website and stores the movie titles in a text file. The program also defines a Movie class to represent each movie with its name, position, and year made. The MovieScraper class is responsible for scraping the data, writing it to a text file, and providing a menu for users to view the movies or search for specific movies by position, name, or year.
#Module Name: Movie Title Scraper
#Module Purpose: This module defines the MovieTitleScraper class, which is responsible for parsing
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/11/2026
#Last Modified: 4/12/2026






import request


def get_amazon_product_page_text(product_page_url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url,headers=headers)
    return response.text