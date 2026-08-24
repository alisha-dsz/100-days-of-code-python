import requests
import smtplib

MY_EMAIL = "marina@gmail.com"
MY_PASSWORD = "12345678"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "I3T7EII712902JKA"
stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY
}

NEWS_API_KEY = "80af764d0dff4794866d0f28388633ca"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = stock_response.json()
data_list = [value for (key, value) in data.items()]
yesterday_stock = float(data_list[0]["4. close"])
#Get the day before yesterday's closing stock price
day_before_stock = float(data_list[1]["4. close"])
#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = yesterday_stock - day_before_stock
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percent = round(difference / yesterday_stock * 100)
#If TODO4 percentage is greater than 5 then print("Get News").
if abs(difference_percent) > 5:
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    #Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    new_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=new_parameters)
    articles = news_response.json()["articles"]

#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Brief : {article['description']}" for article in three_articles]
    # STEP 3: Send each news article as a separate
    # email using Gmail's SMTP server.

    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="alisha@gmail.com",
                                msg=f"Subject:{article['title']}\n\n{COMPANY_NAME}:{up_down}{abs(difference_percent)}%\n{formatted_articles}")





