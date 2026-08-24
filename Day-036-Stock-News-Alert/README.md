# Day 36 - Stock News Alert

## 📖 Overview

The **Stock News Alert** is a Python-based financial notification application that monitors the daily stock price of a company and sends news updates by email when a significant price change occurs.

The application retrieves daily stock market data for **Tesla Inc. (TSLA)** using the **Alpha Vantage API**. It compares yesterday's closing price with the closing price from the previous day.

If the stock price changes by more than **5%**, the application retrieves the latest news articles related to the company using the **News API**.

The first three news articles are then formatted and sent to the user through **Gmail's SMTP server**.

This project was developed as part of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on API integration, JSON data handling, list comprehensions, conditional logic, percentage calculations, and email automation.

---

## 🎯 Objective

Create a stock monitoring application that:

* Retrieves stock price data from an external API.
* Compares recent stock closing prices.
* Calculates the percentage change in stock price.
* Detects significant stock price movements.
* Retrieves company-related news when the price changes significantly.
* Extracts the first three news articles.
* Formats news information using Python.
* Sends stock alerts through email.
* Uses multiple APIs in a single Python application.
* Automates financial news notifications.

---

## 🛠️ Concepts Practiced

### Python

* Variables
* Dictionaries
* Lists
* List comprehensions
* List slicing
* `if` statements
* `for` loops
* Conditional logic
* `float()` conversion
* `round()`
* `abs()`
* String formatting
* f-strings

### API Integration

* HTTP GET requests
* REST APIs
* Query parameters
* JSON responses
* API authentication
* Multiple API integrations

### APIs Used

* Alpha Vantage API
* News API

### Email Automation

* SMTP
* Gmail SMTP server
* `smtplib`
* TLS encryption
* Email authentication
* Automated email notifications

---

## 📂 Files

```text
Day-036-Stock-News-Alert/
│
├── main.py                  # Main Python program
├── requirements.txt         # External Python dependencies
└── README.md                # Project documentation
```

---

## 📦 Libraries Used

### Requests

The `requests` library is used to communicate with the Alpha Vantage and News APIs.

```python
import requests
```

It is used to:

* Send HTTP GET requests.
* Send API parameters.
* Retrieve stock market data.
* Retrieve news articles.
* Convert API responses into Python data using `.json()`.

---

### smtplib

Python's built-in `smtplib` library is used to send emails through Gmail's SMTP server.

```python
import smtplib
```

It is used to:

* Connect to Gmail's SMTP server.
* Establish a secure TLS connection.
* Authenticate the email account.
* Send stock news alerts.

---

## 🌐 APIs Used

### Alpha Vantage API

The application uses the **Alpha Vantage API** to retrieve daily stock market information.

The stock endpoint is:

```text
https://www.alphavantage.co/query
```

The application sends parameters such as:

```python
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
```

For this project:

```python
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
```

The API returns daily stock information in JSON format.

---

### 📰 News API

The application uses the **News API** to retrieve news articles related to the company.

The news endpoint is:

```text
https://newsapi.org/v2/everything
```

The application sends parameters such as:

```python
new_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}
```

The API returns a collection of news articles in JSON format.

---

## 📊 1. Retrieving Stock Data

The program first requests daily stock data from Alpha Vantage.

```python
stock_response = requests.get(
    url=STOCK_ENDPOINT,
    params=stock_parameters
)

data = stock_response.json()
```

The returned JSON data contains daily stock information.

The program extracts the available daily values using a list comprehension:

```python
data_list = [value for (key, value) in data.items()]
```

The most recent closing price is then retrieved:

```python
yesterday_stock = float(data_list[0]["4. close"])
```

---

## 📅 2. Getting the Previous Closing Price

The program retrieves the closing price from the previous trading day:

```python
day_before_stock = float(data_list[1]["4. close"])
```

The two prices are then used to determine the stock's movement.

---

## 📈 3. Calculating the Price Difference

The difference between the two closing prices is calculated:

```python
difference = yesterday_stock - day_before_stock
```

The program determines whether the stock price increased or decreased.

```python
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
```

The symbols represent:

```text
🔺 Stock price increased
🔻 Stock price decreased
```

---

## 📊 4. Calculating Percentage Change

The percentage change is calculated using:

```python
difference_percent = round(
    difference / yesterday_stock * 100
)
```

The program then checks whether the absolute percentage change is greater than 5%:

```python
if abs(difference_percent) > 5:
```

This means the application only retrieves news when the stock experiences a significant movement.

---

## 🚨 5. Detecting a Significant Stock Movement

The main condition is:

```python
if abs(difference_percent) > 5:
```

If the stock price changes by more than **5%**, the application proceeds to retrieve company-related news.

```text
Stock Price Data
       ↓
Compare Closing Prices
       ↓
Calculate Difference
       ↓
Calculate Percentage Change
       ↓
Is Change Greater Than 5%?
       ↙              ↘
     NO               YES
      ↓                ↓
   Do Nothing       Get News
```

---

## 📰 6. Retrieving Company News

When a significant price movement is detected, the application sends a request to the News API.

```python
new_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}

news_response = requests.get(
    url=NEWS_ENDPOINT,
    params=new_parameters
)
```

The returned JSON data is accessed using:

```python
articles = news_response.json()["articles"]
```

---

## ✂️ 7. Selecting the First Three Articles

The program uses Python list slicing to select the first three articles:

```python
three_articles = articles[:3]
```

This creates a list containing up to three news articles.

For example:

```text
All Articles
     ↓
Article 1
Article 2
Article 3
Article 4
Article 5
     ↓
articles[:3]
     ↓
Article 1
Article 2
Article 3
```

---

## 📝 8. Formatting News Articles

The application uses a list comprehension to format the article descriptions:

```python
formatted_articles = [
    f"Brief : {article['description']}"
    for article in three_articles
]
```

This processes each article and extracts its description.

The formatted information can then be included in the email notification.

---

## 📧 9. Sending Email Notifications

The project uses Gmail's SMTP server to send the stock alert.

```python
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(
        user=MY_EMAIL,
        password=MY_PASSWORD
    )
```

The `starttls()` method establishes a secure connection.

The email account is then authenticated using:

```python
connection.login(
    user=MY_EMAIL,
    password=MY_PASSWORD
)
```

The email is sent using:

```python
connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs="recipient@gmail.com",
    msg=...
)
```

---

## 📩 10. Stock Alert Message

The email contains information about the company's stock movement.

The message includes:

* Company name
* Direction of stock movement
* Percentage change
* News information

The alert format is based on:

```text
Tesla Inc: 🔺5%
```

or:

```text
Tesla Inc: 🔻5%
```

followed by the relevant news information.

---

## 🔄 API Data Flow

```text
             Python Application
                     ↓
             Alpha Vantage API
                     ↓
              Stock JSON Data
                     ↓
           Extract Closing Prices
                     ↓
          Compare Stock Prices
                     ↓
          Calculate % Difference
                     ↓
          Is Change Greater Than 5%?
                ↙           ↘
              NO             YES
               ↓              ↓
          End Program      News API
                               ↓
                        News JSON Data
                               ↓
                       Select 3 Articles
                               ↓
                       Format Articles
                               ↓
                         Gmail SMTP
                               ↓
                        Email Alert
```

---

## 🏗️ Project Structure

### `main.py`

The main Python program.

It:

* Defines the stock and company information.
* Configures the Alpha Vantage API.
* Retrieves stock data.
* Extracts closing prices.
* Calculates the stock price difference.
* Calculates the percentage change.
* Determines whether the stock increased or decreased.
* Checks whether the change is greater than 5%.
* Retrieves company news.
* Selects the first three articles.
* Formats the articles.
* Sends email notifications.

---

### `requirements.txt`

Contains the external Python dependency:

```text
requests
```

`smtplib` does not need to be installed separately because it is included with Python.

---

### `README.md`

Contains the documentation for the project, including:

* Project overview
* Objective
* Concepts practiced
* Libraries used
* APIs used
* Stock price calculation
* News retrieval
* Email automation
* Project structure
* Learning outcomes
* Future improvements

---

## 🔐 Security

API keys, email passwords, and other credentials should **never be hardcoded in a public GitHub repository**.

Instead of:

```python
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_password"
STOCK_API_KEY = "your_api_key"
NEWS_API_KEY = "your_api_key"
```

use environment variables:

```python
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
```

A `.env` file can also be used locally, together with an appropriate environment-variable library.

Make sure `.env` is included in `.gitignore`:

```text
.env
```

**Never commit API keys, passwords, SMTP credentials, or other secrets to GitHub.**

---

## 🧪 Example

Suppose Tesla's stock price changes significantly between two trading days.

```text
Yesterday's Closing Price
          ↓
      $350.00
          ↓
Previous Closing Price
          ↓
      $330.00
          ↓
Calculate Percentage Change
          ↓
 Significant Change
          ↓
      Get News
          ↓
   News API Request
          ↓
    Select 3 Articles
          ↓
     Format Articles
          ↓
    Send Email Alert
```

The user receives an email containing information similar to:

```text
Tesla Inc: 🔺5%

Brief: News article description...

Brief: News article description...

Brief: News article description...
```

---

## 🧠 Program Flow

```text
              Start Program
                    ↓
          Define Stock Information
                    ↓
         Request Stock Market Data
                    ↓
          Receive JSON Response
                    ↓
          Extract Closing Prices
                    ↓
         Calculate Price Difference
                    ↓
       Calculate Percentage Change
                    ↓
          Is Change Greater Than 5?
               ↙           ↘
             NO             YES
              ↓              ↓
         End Program     Request News
                              ↓
                       Receive Articles
                              ↓
                       Select First 3
                              ↓
                       Format Articles
                              ↓
                       Gmail SMTP Server
                              ↓
                         Send Email
                              ↓
                         End Program
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Make HTTP requests using `requests`.
* Work with external REST APIs.
* Use the Alpha Vantage API.
* Use the News API.
* Work with API query parameters.
* Process JSON responses.
* Access nested dictionaries and lists.
* Use list comprehensions.
* Use list slicing.
* Calculate percentage changes.
* Use `abs()` for positive differences.
* Use conditional statements.
* Use loops to process data.
* Detect significant stock price movements.
* Retrieve company-related news.
* Send automated emails using `smtplib`.
* Connect to Gmail's SMTP server.
* Establish secure SMTP connections using TLS.
* Authenticate an email account.
* Combine multiple APIs in one Python application.
* Build a practical financial notification tool.
* Understand the importance of protecting API credentials.

---

## 🚀 Future Improvements

Possible improvements for this project include:

* Add multiple stocks to monitor.
* Allow users to enter their preferred stock symbol.
* Send the article headline and description together.
* Include article URLs in the email.
* Improve the percentage-change calculation.
* Display the exact stock prices in the email.
* Add the current stock price.
* Add company logos to the email.
* Add more detailed news filtering.
* Send HTML-formatted emails.
* Use environment variables for all credentials.
* Add error handling for failed API requests.
* Handle API rate limits.
* Add logging.
* Schedule the application to run automatically.
* Store historical stock prices.
* Create a dashboard for tracking stock movements.
* Support multiple email recipients.

---

## 🔑 Key Takeaway

This project helped me understand how Python can combine **stock market APIs, news APIs, JSON data, mathematical calculations, and email automation** to create a practical financial notification application.

The biggest takeaway was learning how to retrieve stock market data, compare closing prices, calculate percentage changes, detect significant movements, retrieve relevant news, and automatically send the information through email.

It also strengthened my understanding of **API integration, JSON handling, list comprehensions, list slicing, conditional logic, SMTP, TLS, and automation with Python**.


