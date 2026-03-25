import datetime as dt
import pandas
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
        "First_Name": birthday_first_name,
        "Last_Name": birthday_last_name,
        "Email": birthday_email,
        "Year": birthday_year,
        "Month":birthday_month,
        "Day":birthday_day,
        "Time":birthday_hour
    })

    new_birthday_info.to_csv("birthday.csv",mode="a",header=False,index=False)
   
def check_for_birthdays():
    date_now = dt.datetime.now()
    birthday_dataframe = pandas.read_csv("birthdays.csv")
    birthdays_today = birthday_dataframe[(birthday_dataframe.Year == date_now.year) & (birthday_dataframe.Month == date_now.month) & (birthday_dataframe.Day == date_now.Day)]
    return birthdays_today

    

def send_email(birdthdays):
    for birthday in birthdays:

        random_letter = random.choice(letters_list)



        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.send_mail(
                from_addr = EMAIL,
                to_addr = TO_ADDRESS,
                msg="Subject:Hello There\n\nThis is the body of the mail."
            )

def main():
    with open("letter1.txt", "r") as file:
        r = file.readlines()
  
        print("\n")
        message = ''
        for line in r:
            line = line.replace("[First Name]","Ryan")
            line = line.replace("[Last Name]","Pereira")
            line = line.replace("[Your Name]","L")
            
            message += line
        print(message)
    
           
    
       

        
if __name__ == "__main__":
    main()
