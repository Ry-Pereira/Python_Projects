import datetime as dt
import smtplib

EMAIL = ""
PASSWORD = ""
TO_ADDRESS = ""

date_of_birth = dt.datetime(year=2004,month=2,day=17,hour=12)

def get_time():
    now_time = dt.datetime.now()
    now_month = now_time.month
    now_day = now_time.day
    now_hour = now_time.hour
    print(now_time.month)
    print(now_time.day)
    print(now_time.hour-12)

    print(now_time)

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