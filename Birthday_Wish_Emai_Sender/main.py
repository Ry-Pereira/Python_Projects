#Importing the datetime module as dt, to get all the information for getting world time functions and variables
import datetime as dt
#Importing the pandas library for data manipulation and analysis, with primarily working on csv info
import pandas
#Importing the random module in order to be able to be randomly choose from the letters list
import random
#Importing smtplib module, in order for Simple Mail Transfer protocol to work, in sending Emails
import smtplib

#EMAIL constant variable set to empty string
EMAIL = ""
#PASSWORD constant variable set to empty string
PASSWORD = ""
#TO ADDRESS constant variable set to empty string
TO_ADDRESS = ""
#YOUR NAME constant variable set to empty string
YOUR_NAME = ""


#Letters list set to a list of letter text documents
letters_list = ["letter1.txt","letter2.txt","letter3.txt","letter4.txt"]


#Defining the store birthday info function
def store_birthday_info():
    #Birthday year is set to the integer casting of asking the user for the year of their birth of the person they want to log in
    birthday_year = int(input("Year of Birth: "))
    #Birthday month is set to the integer casting of asking the user for the month of their birth of the person they want to log in
    birthday_month = int(input("Month of Birth: "))
    #Birthday day is set to the integer casting of asking the user for the day of their birth of the person they want to log in
    birthday_day = int(input("Day of Birth: "))
    #Birthday first name is set to the string casting of asking the user for the first name of the birth of the person they want to log in 
    birthday_first_name = str(input("Birthday First Name: "))
    #Birthday last name is set to the string casting of asking the user for the last name of the birth of the person they want to log in 
    birthday_last_name = str(input("Birthday Last Name: "))
    #Birthday email is set to the string casting of asking the user for the email of the birth of the person they want to log in 
    birthday_email = str(input("Birthday Email To Send: "))

    

    new_birthday_info = pandas.DataFrame({
        "First_Name": [birthday_first_name],
        "Last_Name": [birthday_last_name],
        "Email": [birthday_email],
        "Year": [birthday_year],
        "Month":[birthday_month],
        "Day":[birthday_day]
    })

    new_birthday_info.to_csv("birthdays.csv",mode="a",header=False,index=False)
   
def check_for_birthdays():
    date_now = dt.datetime.now()
    birthday_dataframe = pandas.read_csv("birthdays.csv")
    birthdays_today = birthday_dataframe[(birthday_dataframe.Year == date_now.year) & (birthday_dataframe.Month == date_now.month) & (birthday_dataframe.Day == date_now.day)]
    return birthdays_today

    

def send_email(birthdays):
    for birthday_row in birthdays.itertuples(index=False):
        print(birthday_row)
        print(birthday_row.First_Name,birthday_row.Last_Name,birthday_row.Email,birthday_row.Year,birthday_row.Month,birthday_row.Day)
        print("Tyepe:",type(birthday_row.First_Name))
        random_letter = random.choice(letters_list)

        with open(random_letter, "r") as file:
            file_lines = file.readlines()
    
            print("\n")
            message = ''
            for line in file_lines:
                line = line.replace("[First Name]",birthday_row.First_Name)
                line = line.replace("[Last Name]",birthday_row.Last_Name)
                line = line.replace("[Your Name]",YOUR_NAME)
                line = line.replace("[Date]",str(birthday_row.Year))
                line = line.replace("[Years turning]",str(2026-birthday_row.Year))
                message += line
            print(message)

        full_message = f"Subject:Birthday Wish\n\n{message}"
        full_message_bytes = full_message.encode("utf-8")
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,to_addrs=birthday_row.Email,msg=full_message_bytes)
        connection.close()




#Defining the main function, the entry point into the project program
def main():
    #User_answer stores the input from the question if the user wants to store any birthday information
    user_answer = input("Do you want store any birthday information(y/n?")
    #If user answer is equal to y character string, 
    if user_answer == "y":
        #Exexcutes the store birthday info function to get birthday info to store into the birthdays csv
        store_birthday_info()
    #birthday holds the value of a datframe of the buirthdays that are current today from the check for birthdays function
    birthdays = check_for_birthdays()
    #Executes the send_email function with birthdays as input, to go through each birthday and send a eamil according to each of its own information
    send_email(birthdays)

    
    

    
       

#If the program is being run directly, then the main program will be executed        
if __name__ == "__main__":
    #Main function is executed
    main()
