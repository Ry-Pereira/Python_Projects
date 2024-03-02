# Imports 
import random




# Magic 8 Ball Repsonse Pool
magic_8_ball_responses = ["It is certain","It is decidely so","Without a doubt","Yes", "definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]



# This function prints the menu
def print_menu():
    print("1. Ask the Magic 8 Ball, a question")
    print("2. Exit the Program\n")





# This function shakes the magic 8 ball for a random answer after the user, has given input
def shake_ball():
    user_question = input("Ask any question: ")
    magic_8_ball_answer = random.choice(magic_8_ball_responses)
    print("Magic 8 Ball Response: ",magic_8_ball_answer)
    shake_again = input("Would you like to shake again(y/n)")
    if shake_again == "y":
        shake_ball()
    else:
        print("Thankyou and come again")




# This is the main function of the program
def main():
    print("Welcome to the Magic 8 Ball Program\n")
    print_menu()
    shake_ball()



# The main function is called
main()
