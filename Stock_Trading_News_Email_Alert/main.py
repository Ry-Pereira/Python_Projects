#Name: Ryan Pereira
#Project Name: Stock Trade News Alert Email Sender
#Module Name: Main
#Module Purpose: The moudle is the main entry into the program.
#Description: ...
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/27/2026
#Last Modified: 6/27/2026 

#Importing the requests module, in order for API retrieval,storing, and accessing to be made possible.
import requests
#Importing the pandas library for data manipulation and analysis, with primarily working on csv info
import pandas
import time
from datetime import datetime, timedelta

key = "KUMA43H9MFPK7SVE"
news_api_key = "ac096e631d564a83bed1ed2951d87969"





def get_stock_data(stock_ticker_name):
    stock_api = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker_name}&apikey={key}'
    response = requests.get(url=stock_api)
    data = response.json()
    for d in data:
        print(d)

    yesterday = datetime.now() - timedelta(days=1).date()
    yesterday_before = datetime.now() - timedelta(days=2).date()
    time_series_data_yesterday = response.json()["Time Series (Daily)"][str(yesterday)]
    time_series_data_yesterday_before = response.json()["Time Series (Daily)"][str(yesterday_before)]
    stock_tracker_list = pandas.read_csv('stock_list.csv')
    stock_tracker_list.loc[stock_tracker_list['Ticker'] == stock_ticker_name,"Open_Price_Yesterday","Close_Price_Yesterday","Open_Price_Yesterday_Before","Close_Price_Yesterday_Before"] = time_series_data_yesterday["1. open"],time_series_data_yesterday["4. close"],time_series_data_yesterday_before["1. open"],time_series_data_yesterday_before["4. close"]
    stock_tracker_list.to_csv("stock_list.csv",header=False,index=False)


def add_stock_data():
    stock_ticker_name = str(input("Stock Ticker Name: "))
    stock_company_name = str(input("Stock Company Name: "))

    new_stock_list_info = pandas.DataFrame({
        "Ticker":[stock_ticker_name],
        "Company":[stock_company_name],
        "Open Price":[0.00],
        "Close Price":[0.00],
        "High Price":[0.00],
        "Low Price":[0.00]
    })
    if check_for_stock_duplicates(stock_ticker_name,stock_company_name) == False:
        new_stock_list_info.to_csv("stock_list.csv",mode="a",header=False,index=False)

def check_stock_list():
    stock_dataframe = pandas.read_csv("stock_list.csv")
    for stock in stock_dataframe.itertuples(index=False):
        print(stock.Ticker,stock.Company,stock.Close_Price)
        time.sleep(2)

        get_stock_data(stock.Ticker)
        get_news_data(stock.Company)


#Defining a function to check the stock track list, to see if the paramater input for Ticker name and company name to check make any duplicates, returns true or false
def check_for_stock_duplicates(ticker_name_to_check: str,stock_company_to_check: str):
    stock_dataframe = pandas.read_csv("stock_list.csv")
    for stock in stock_dataframe.itertuples(index=False):
        if stock.Ticker == ticker_name_to_check or stock.Company == stock_company_to_check:
            return True
    
    return False
        


def get_news_data(company_name):
    yesterday = datetime.now() - timedelta(days=1).date()
    yesterday_before = datetime.now() - timedelta(days=2).date()

    news_api_previous_days = f"https://newsapi.org/v2/top-headlines?q=Apple&from={yesterday_before}&to={yesterday}&sortBy=popularity&apiKey={news_api_key}"
    response = requests.get(url=news_api_previous_days)
    data = response.json()


    for d in data["articles"]:
        print(d)
        print("\n")


#Defining the main function, the main enry point into the project program.
def main() -> None:
    #user_question = input("Do you wish to add a new stock to track(y/n?")
    #if user_question == "y":
    #    add_stock_data()
    day_yesterday = datetime.datetime.now()
    print(day_yesterday)
    check_stock_list()

    


#If the program is being run directly, the main function will be executed
if __name__ == "__main__":
    #The main function is executed
    main()
