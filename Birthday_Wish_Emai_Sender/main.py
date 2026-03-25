import datetime as dt
import pandas
import smtplib

EMAIL = ""
PASSWORD = ""
TO_ADDRESS = ""

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
   

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.send_mail(
            from_addr = EMAIL,
            to_addr = TO_ADDRESS,
            msg="Subject:Hello There\n\nThis is the body of the mail."
        )

def main():
    get_time()

if __name__ == "__main__":
    main()