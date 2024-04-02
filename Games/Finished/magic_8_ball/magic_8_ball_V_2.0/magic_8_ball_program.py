class Magic_8_Ball_Program:
    def __init__(self,magic_8_ball):
        self.magic_8_ball = magic_8_ball


    def print_menu():
        print("1. To shake the Magic 8 Ball\n2. To exit the Program")

    def menu_selection(user_select):
        if user_select == 1:
            print(magic_8_ball.shake())
            shake_again = input("Shake again(y/n): ")
            if shake_again == "y":
                print(magic_8_ball.shake())
            elif shake_again == "n":
                print("Very well then")
                menu_selection(user_select = int(input("Choice: ")))
        elif user_select == 2:
            print("Exiting...")
        else:
            menu_selection(user_select = int(input("Choice: ")))

