from magic_8_ball_program import Magic8BallProgram

#Main function is defined
def main():
    responses_file_name = input("Type in the name of the responses file: ")
    
    Magic8BallProgram(responses_file_name)
    
    Magic8BallProgram.run()

    if __name__ == "__main__":
        main()




