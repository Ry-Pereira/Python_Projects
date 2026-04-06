
from movie_class import Movie


class MovieScraper:
    def __int__(self,movie_titles):
        self.movie_titles = movie_titles
        self.movie_text_file = ""
        self.movies = []

    def add_to_movie_list(self):
        pass

    
    def print_movies_list(self):
        with open(self.movie_text_file,"r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)


    def menu(self):
        print("1) Press 1 to View Movies text file")
        print("2) Press 2 To get movie by position")
        print("3) Press 3 to get movies by name")
        print("4) To get movies by dates")


    with open("movies.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace(")","(").split("(")
            print(line)
            movies.append(Movie(line[1],line[0],line[2]))


    def write_into_moves_text_file(movie_text_file):
        with open("movies.txt","w") as file:
            for title in movie_titles:
                file.write(title.text + "\n")



    def print_movies_list(moves_text):
        with open("movies.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)