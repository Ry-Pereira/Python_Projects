#Name: Ryan Pereira
#Project Name: Stock Trade News Alert Email Sender
#Module Name: Main
#Module Purpose: The moudle is the main entry into the program.
#Description: ...
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/27/2026
#Last Modified: 6/27/2026 


import requests
import pandas


key = "KUMA43H9MFPK7SVE"
stock_api = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey={key}'
news_api_key = "ac096e631d564a83bed1ed2951d87969"

news_api = f"https://newsapi.org/v2/top-headlines?q=Apple&from=2026-03-20&to=2026-03-27&sortBy=popularity&apiKey={news_api_key}"



def get_stock_data():
    stock_name = ""
    response = requests.get(url=stock_api)
    data = response.json()
    for d in data:
        print(d)

    print("\n")
    time_series_data = response.json()["Time Series (Daily)"]["2026-03-26"]
    print(time_series_data)


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
    new_stock_list_info.to_csv("stock_list.csv",mode="a",header=False,index=False)



def get_news_data():
    response = requests.get(url=news_api)
    data = response.json()


    for d in data["articles"]:
        print(d)
        print("\n")


def main() -> None:
    add_stock_data()

    


if __name__ == "__main__":
    main()