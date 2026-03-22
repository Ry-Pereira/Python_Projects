from magic_8_ball_program import Magic8BallProgram

#Main function is defined
def main():
    responses_file_name = input("Type in the name of the responses file: ")
    
    my_magic_8_ball = Magic8BallProgram(responses_file_name)
    
    my_magic_8_ball.run()

if __name__ == "__main__":
    main()




