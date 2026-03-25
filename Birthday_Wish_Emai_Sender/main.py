import datetime as dt
import smtplib



def get_time():
    now_time = dt.datetime.now()
    now_month = now_time.month
    now_day = now_time.day
    now_hour = now_time.hour
    print(now_time.month)
    print(now_time.day)
    print(now_time.hour-12)

    print(now_time)


def main():
    get_time()

if __name__ == "__main__":
    main()