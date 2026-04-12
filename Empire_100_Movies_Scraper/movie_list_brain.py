#Name: Ryan Pereira
#Project Name: Color Mixer
#Description:# A Tkinter-based program that allows users to mix colors by clicking on buttons representing different colors. The mixed color is displayed on a canvas, and users can reset the canvas to start over.
#Module Name: Movie Scraper
#Module Purpose: This program serves as the user interface for the Color Mixer application. It defines the ColorMixerUI class, which sets up the Tkinter window, canvas, and buttons for mixing colors. The class includes methods for adding colors to the mix and resetting the color mix.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/4/2026
#Last Modified: 4/6/2026

from movie_class import Movie


class EmpireMovieBrain:
    def __init__(self,movie_titles):
        self.movie_titles = movie_titles
        self.movie_text_file = ""
        self.movies = []

    
    def menu(self) -> None:
        print("1) Press 1 to View Movies text file")
        print("2) Press 2 To get movie by position")
        print("3) Press 3 To get movies by position range")
        print("4) Press 4 To get movie by name")
        print("5) Press 5 To get movies by letter")
        print("6) Press 6 To get movies by year")
        print("7) Press 7 To get movies by year range")
        print("8) Press 8 To Exit")
     

    def write_into_moves_text_file(self, movie_text_file: str) -> None:
        with open("movies.txt","w") as file:
            for title in self.movie_titles:
                file.write(title.text + "\n")

    def read_movies_from_text_file(self) -> None:
        with open("movies.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace(")","(").split("(")
                print(line)
                self.movies.append(Movie(line[1],line[0],line[2]))
    
    def print_movies_list(self) -> None:
        with open(self.movie_text_file,"r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)


    def get_movie_by_position(self,position) -> None:
        for movie in self.movies:
            if movie.position == position:
                print(f"{movie.position}) {movie.name} ({movie.year_made})")
            



    def get_move_by_position_range(self,position1,position2) -> None:
        for movie in self.movies:
            if movie.position >= position1 and movie.position <= position2:
                print(f"{movie.position}) {movie.name} ({movie.year_made})")
    



    def get_movie_by_name(self,name) -> None:
        for movie in self.movies:
            if movie.name == name:
                print(f"{movie.position}) {movie.name} ({movie.year_made})")
            
            


    def get_movie_by_letter(self,letter) -> None:
        for movie in self.movies:
            if movie.name.startswith(letter):
                print(f"{movie.position}) {movie.name} ({movie.year_made})")
    

    def get_movie_by_year(self,year) -> None:
        for movie in self.movies:
            if movie.year_made == year:
                print(f"{movie.position}) {movie.name} ({movie.year_made})")
                

    
    def get_movie_by_year_range(self,year1,year2) -> None:
        for move in self.movies:
            if move.year_made >= year1 and move.year_made <= year2:
                print(f"{move.position}) {move.name} ({move.year_made})")

    


    

    




    

    def run(self) -> None:
        self.write_into_moves_text_file(self.movie_text_file)
        self.menu()
        user_input = input("Enter your choice: ")
        while user_input != "8":
            if user_input == "1":
                self.print_movies_list()
            elif user_input == "2":
                position = input("Enter the position of the movie: ")
                self.get_movie_by_position(position)
            elif user_input == "3":
                position1 = input("Enter the first position: ")
                position2 = input("Enter the second position: ")
                self.get_move_by_position_range(position1,position2)
            elif user_input == "4":
                name = input("Enter the name of the movie: ")
                self.get_movie_by_name(name)
            elif user_input == "5":
                letter = input("Enter the letter: ")
                self.get_movie_by_letter(letter)
            elif user_input == "6":
                year = input("Enter the year: ")
                self.get_movie_by_year(year)
            elif user_input == "7":
                year1 = input("Enter the first year: ")
                year2 = input("Enter the second year: ")
                self.get_movie_by_year_range(year1,year2)
            
            self.menu()
            user_input = input("Enter your choice: ")
        