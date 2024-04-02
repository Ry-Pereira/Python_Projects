#Imports of the repsonse pool and magic 8 ball class
from magic_8_ball_class import Magic_8_Ball
from magic_8_ball_responses import responses
from magic_8_ball_program import Magic_8_Ball_Program


magic_8_ball = Magic_8_Ball(responses)
magic_8_ball_program = Magic_8_Ball_Program(magic_8_ball)





#Main function is defined
def main():
    print(magic_8_ball_program.print_menu)
    magic_8_ball_program.menu_selection()



#Main function is callled
main()


