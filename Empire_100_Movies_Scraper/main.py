
from bs4 import BeautifulSoup
import requests

from movie_scraper import MovieScraper




def main() -> None:
    url = "https://www.empireonline.com/movies/features/best-movies-of-all-time-us/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    movie_titles = soup.select("h2 strong")
    MovieScraper(movie_titles)
    





if __name__ == "__main__":
    main()