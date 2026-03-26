import datetime as dt
import pandas
import random
import smtplib

EMAIL = ""
PASSWORD = ""
TO_ADDRESS = ""

letters_list = ["letter1.txt","letter2.txt","letter3.txt","letter4.txt"]

date_of_birth = dt.datetime(year=2004,month=2,day=17,hour=12)

def store_birthday_info():
    birthday_year = int(input("Year of Birth: "))
    birthday_month = int(input("Year of Month: "))
    birthday_day = int(input("Year of Day: "))
    birthday_hour = int(input("Hour to send Birthday"))
    post_or_past_meridian  = input("Past or Post Meridian:")
    birthday_first_name = input("Birthday First Name: ")
    birthday_last_name = input("Birthday Last Name: ")
    birthday_email = input("Birthday Email To Send: ")

    if post_or_past_meridian == "PM":
        birthday_hour +=12


    new_birthday_info = pandas.DataFrame({
        "First_Name": [birthday_first_name],
        "Last_Name": [birthday_last_name],
        "Email": [birthday_email],
        "Year": [birthday_year],
        "Month":[birthday_month],
        "Day":[birthday_day],
        "Time":[birthday_hour],
        "Time_Period":[post_or_past_meridian]
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
                line = line.replace("[Your Name]","Li")
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





def main():
    user_answer = input("Do you want store any birthday information(y/n?")
    if user_answer == "y":
        store_birthday_info()
    birthdays = check_for_birthdays()
    send_email(birthdays)

    
    

    
       

        
if __name__ == "__main__":
    main()
