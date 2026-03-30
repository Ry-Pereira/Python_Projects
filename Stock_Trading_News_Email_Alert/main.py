#Name: Ryan Pereira
#Project Name: Stock Trade News Alert Email Sender
#Module Name: Main
#Module Purpose: The moudle is the main entry into the program.
#Description: ...
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/28/2026
#Last Modified: 6/28/2026 

#Importing the requests module, in order for API retrieval,storing, and accessing to be made possible.
import requests
#Importing the pandas library for data manipulation and analysis, with primarily working on csv info
import pandas
import time
from datetime import datetime, timedelta

#Importing smtplib module, in order for Simple Mail Transfer protocol to work, in sending Emails
import smtplib

EMAIL = ""
PASSWORD = ""

key = "KUMA43H9MFPK7SVE"
news_api_key = "ac096e631d564a83bed1ed2951d87969"




#Defining a function to get stock data, with the parameter of stock ticker name, which is the stock ticker symbol for the stock that is being tracked, such as AAPL for Apple, MSFT for Microsoft, etc.
def get_stock_data(stock_ticker_name):
    #Stock API is set to a string with the url for the stock API, with the function of TIME_SERIES_DAILY, and the symbol set to the stock ticker name parameter, and the apikey set to the key variable
    stock_api = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker_name}&apikey={key}'
    #Response is set to the result of the requests get function with the url parameter set to the stock API variable
    response = requests.get(url=stock_api)
    #Data is set to the result of the response json function, which converts the response to a json format
    data = response.json()
    
    #Yesterday is set to the result of the datetime now function minus the result of the timedelta function with days set to 1, and then the date function is called on that result, which gives the date for yesterday
    yesterday = datetime.now() - timedelta(days=1).date()
    #Yesterday before is set to the result of the datetime now function minus the result of the timedelta function with days set to 2, and then the date function is called on that result, which gives the date for the day before yesterday
    yesterday_before = datetime.now() - timedelta(days=2).date()
    #Time series data yesterday is set to the result of the response json function with the key of "Time Series (Daily)" and then the key of yesterday, which gives the stock data for yesterday
    time_series_data_yesterday = response.json()["Time Series (Daily)"][str(yesterday)]
    #Time series data yesterday before is set to the result of the response json function with the key of "Time Series (Daily)" and then the key of yesterday before, which gives the stock data for the day before yesterday
    time_series_data_yesterday_before = response.json()["Time Series (Daily)"][str(yesterday_before)]
    #Stock tracker list is set to the result of the pandas read csv function with the parameter of the stock list csv file, which gives a dataframe of the stock list csv file
    stock_tracker_list = pandas.read_csv('stock_list.csv')
    #The stock tracker list dataframe is updated with the new stock data for yesterday and the day before yesterday, with the loc function to locate the row with the stock ticker name, and then the columns for open price yesterday, close price yesterday, open price yesterday before, and close price yesterday before are set to the corresponding values from the time series data for yesterday and the day before yesterday
    stock_tracker_list.loc[stock_tracker_list['Ticker'] == stock_ticker_name,"Open_Price_Yesterday","Close_Price_Yesterday","Open_Price_Yesterday_Before","Close_Price_Yesterday_Before"] = time_series_data_yesterday["1. open"],time_series_data_yesterday["4. close"],time_series_data_yesterday_before["1. open"],time_series_data_yesterday_before["4. close"]
    #The stock tracker list dataframe is then saved back to the stock list csv file with the to csv function, with the header set to false and the index set to false to avoid adding an index column and a header row to the csv file
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
    #Stock datafram is set to a dtarame from pandas executing the read csv function on the csv file
    stock_dataframe = pandas.read_csv("stock_list.csv")
    #For loop in iterating through the stcok tuple rows with no regard of index inclusion
    for stock in stock_dataframe.itertuples(index=False):
        #If the stocker Ticker or Company value is equal to either the ticker or stock company to check, there is a duplicate
        if stock.Ticker == ticker_name_to_check or stock.Company == stock_company_to_check:
            #Returns True to indicate there is a duplicate
            return True
    #Returns False to indicate there is no duplicate
    return False
        


def get_news_data(company_name):
    yesterday = (datetime.now() - timedelta(days=1)).date()
    yesterday_before = (datetime.now() - timedelta(days=2)).date()

    news_api_previous_days = f"https://newsapi.org/v2/top-headlines?q={company_name}&from={yesterday_before}&to={yesterday}&sortBy=popularity&apiKey={news_api_key}"
    response = requests.get(url=news_api_previous_days)
    data = response.json()

    news_message = ""

    for d in data["articles"]:

        message+= "SOruce",d["source"]["name"]
        message += "Author",d["author"]
        message += "Title",d["title"]
        message += "Description",d["description"]
        message += "URL",d["url"]
        message += "\n\n"

    return news_message
    
def send_email(company_name,news_message):
    stock_and_company_dataframe = pandas.read_csv("stocks_list.csv")
    stock_and_company = stock_and_company_dataframe[(stock_and_company_dataframe.Date == "company_name")]

    for s in stock_and_company.ittrtuples(index=False):
        #TLS starts for transport layer security
        full_message = f"Subject:{company_name} has a {s.Close_Price_Yesterday}-{s.Close_Price_Yesterday_Before}\n\n{news_message}"
        #Full message bytes is set to full message is encoded
        full_message_bytes = full_message.encode("utf-8")
        connection.starttls()
        #Connection requring a login with user set to email address and password to app password
        connection.login(user=EMAIL,password=PASSWORD)
        #Conneection to send email from address to my email addres and to addres to my addres with mesg set to hello, have SUbject: to have subject in there
        connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=full_message_bytes)
        #Closes the connection
        connection.close()
    

    
    
#Defining the main function, the main enry point into the project program.
def main() -> None:
    #user_question = input("Do you wish to add a new stock to track(y/n?")
    #if user_question == "y":
    #    add_stock_data()
    
    get_news_data("Apple")

    


#If the program is being run directly, the main function will be executed
if __name__ == "__main__":
    #The main function is executed
    main()
