#Imports of the repsonse pool and magic 8 ball class
from magic_8_ball_class import Magic_8_Ball
from magic_8_ball_responses import responses





#Instantiating the Magic 8 Ball
magic_8_ball = Magic_8_Ball(responses)




#Prints the menu of the program
def print_menu():
    print("1. To shake the Magic 8 Ball")
    print("2. To exit the Program")





def menu_selection(user_select):
    if user_select == 1:
        print(magic_8_ball.shake())
        shake_again = input("Shake again(y/n): ")
        if shake_again == "y":
            print(magic_8_ball.shake())
        elif shake_again == "n":
            print("Very well then")
    

    elif user_select == 2:
        print("Exiting...")
    else:
        menu_selection(user_select = int(input("Choice: ")))




#Main function is defined
def main():
    print_menu()
    menu_selection(user_select = int(input("Choice: ")))



#Main function is callled
main()


