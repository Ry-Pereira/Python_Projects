
from bs4 import BeautifulSoup
import requests
from movie_class import Movie

url = "https://www.empireonline.com/movies/features/best-movies-of-all-time-us/"


headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,'html.parser')
movie_titles = soup.select("h2 strong")









def write_into_moves_text_file(movie_text_file):
    with open("movies.txt","w") as file:
        for title in movie_titles:
            file.write(title.text + "\n")

def menu():
    print("1) Press 1 to View Movies text file")
    print("2) Press 2 To get movie by position")
    print("3) Press 3 to get movies by name")
    print("4) To get movies by dates")

def print_movies_list(moves_text):
    with open("movies.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)


def main() -> None:
    movies = []
    with open("movies.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace(")","(").split("(")
            print(line)
            movies.append(Movie(line[1],line[0],line[2]))

            
    
    for movie in movies:
        print(movie.name,movie.position,movie.year_made)





if __name__ == "__main__":
    main()