from magic_8_ball import Magic8Ball

class Magic8BallProgram:
    def __init__(self,response_file):
        self.magic_8_ball = Magic8Ball(response_file)


    def print_menu(self):
        print("1. Shake the Magic 8 Ball\n2. To exit the Program")

    def print_shaking(self):
        print("\nSHAKE...\nSHAKE...\nSHAKE...\n")

    def get_answer(self):
        question = input("Question: ")
        self.print_shaking()
        response = self.magic_8_ball.shake()
        print(f"Question:{question}- Answer:{response}")

    def menu_selection(self,user_select):
        if user_select == 1:
            self.get_answer()
            shake_again = input("Shake again(y/n): ")
            while shake_again != "n":
                self.get_answer()
                shake_again = input("Shake again(y/n): ")  
            print("Very well then")
            self.menu_selection(user_select = int(input("Choice: ")))
            
                    

                
        elif user_select == 2:
            print("Exiting Program...")
        else:
            print("Please select a valid choice")
            self.print_menu()
            self.menu_selection(user_select = int(input("Choice: ")))



    def run(self):
        self.print_menu()
        self.menu_selection(user_select = int(input("Choice: ")))




