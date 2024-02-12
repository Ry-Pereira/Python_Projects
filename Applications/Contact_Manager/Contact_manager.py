from account_login_class import *
from Contacts_class import *



def create_account(name,username,password):
    name = Account_login(username,password)
    print("We saved you as",name,"\n Your username is:",username,"\n Your password is:",password)
    print("Do not forget this")



def find_account(name,username,password):
    pass

def print_option_menu():
    print("Press 1: To add in a Contact from your contact sheet")
    print("Press 2: To edit a Contacts' information")
    print("Press 2: To removove a contact from your contact sheet")
    print("Press 3: To View your entire contact sheet")
    print("Press 4: To Exit the Program")

    
def contact_sheet_options():
    print_option_menu()

def account_sign_in():
    pass



def main():
    print("Welcome to Contact Manager Program\n")
    user_account_inquiry = input("Do you have an account already (y/n)? ")
    if user_account_inquiry == "y":
        find_account(name = "What is your first name: ",username = "What is your username: ",password = "What is your password: ")
    else:
        
        print("Were going to create a new account for you to login, and access your contacts")
        create_account(name = input("What is your first name: "),username = input("What is a good username for you: "),password = input("What is a good password for you: "))
        contact_sheet_options()


main()
