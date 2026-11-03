# Day 47 – Amazon Price Tracking Bot 🛒💰

## 📖 Overview

This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

On Day 47, I developed an Amazon Price Tracking Bot using **Python, Requests, BeautifulSoup, and SMTP** to monitor the price of a product listed on Amazon.

The bot fetches product information from an Amazon product page, extracts the product title and current price, and compares the price against a predefined target price. If the current price drops below the target, the program can send an email notification to alert the user about the price drop.

This project demonstrates how Python can be used for web scraping, conditional logic, HTTP requests, and email automation.

## 🎯 Objectives

- Retrieve product information from a website using Python.
- Extract product titles and prices using BeautifulSoup.
- Understand how HTTP requests work.
- Compare the current product price with a target price.
- Automate email notifications using SMTP.
- Use environment variables to manage sensitive credentials.
- Explore practical applications of web scraping and automation.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **Requests** – Sending HTTP requests to retrieve webpage content.
- **BeautifulSoup** – Parsing HTML and extracting product information.
- **SMTP** – Sending email notifications.
- **smtplib** – Python's built-in library for email communication.
- **python-dotenv** – Loading sensitive configuration from environment variables.

## 📚 Concepts Practiced

| Concept | Description |
|---|---|
| HTTP Requests | Fetching webpage content using the Requests library. |
| Web Scraping | Extracting product information from HTML. |
| BeautifulSoup | Parsing HTML and locating relevant elements. |
| HTML Parsing | Understanding tags, attributes, and CSS selectors. |
| Conditional Statements | Checking whether the product price meets the target. |
| String Manipulation | Cleaning and converting extracted price text. |
| SMTP | Sending automated email notifications. |
| Environment Variables | Keeping email credentials and configuration out of source code. |
| Exception Handling | Handling request failures and unexpected data. |

## ⚙️ How It Works

1. **Send Request:** Sends an HTTP request to the Amazon product page.
2. **Retrieve HTML:** Receives the webpage content if the request is permitted.
3. **Parse the Page:** Uses BeautifulSoup to parse the HTML.
4. **Extract Product Details:** Retrieves the product title and displayed price.
5. **Convert the Price:** Converts the extracted price into a numeric value.
6. **Check Target Price:** Compares the current price against the predefined target.
7. **Send Notification:** If the price is below the target, sends an email alert.
8. **Monitor the Product:** The script can be extended to check prices periodically.

## 💻 Key Implementation Details

### 1. Sending an HTTP Request

```python
import requests

response = requests.get(
    url,
    headers=headers,
    timeout=15
)

response.raise_for_status()
```

The Requests library sends an HTTP GET request to retrieve the webpage. The headers can provide information such as a user agent, while `raise_for_status()` raises an exception for unsuccessful HTTP responses.

Amazon may block automated requests, require additional verification, or change its page structure. The script must handle these situations appropriately.

### 2. Extracting Product Information

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find(id="productTitle")
```

BeautifulSoup parses the webpage's HTML and helps locate elements containing product information.

The exact selectors used to extract the product title and price may vary depending on the product page and its current HTML structure.

### 3. Checking the Product Price

```python
if current_price < target_price:
    print("The product price is below the target!")
```

The extracted price is converted into a numeric value before comparison.

For example, if the target price is ₹5,000 and the current price drops to ₹4,500, the condition is satisfied and the program can trigger a notification.

### 4. Sending an Email Alert

```python
import smtplib

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
        from_addr=email,
        to_addrs=receiver_email,
        msg="Subject: Amazon Price Drop Alert\n\nThe product is now below your target price!"
    )
```

The `smtplib` library allows Python to connect to an SMTP server and send email notifications.

For Gmail, an app password may be required when using SMTP authentication. Credentials should be stored securely rather than hardcoded in the script.

## 📂 Project Structure

```text
Day-047-Amazon-Price-Tracking-Bot/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

| File | Purpose |
|---|---|
| `main.py` | Contains the product scraping, price comparison, and notification logic. |
| `.env` | Stores sensitive configuration such as email credentials. |
| `.gitignore` | Prevents sensitive and unnecessary files from being committed. |
| `README.md` | Documents the project and its implementation. |

*Note: The file structure may vary depending on the final implementation.*

## 🧠 What I Learned

- How to retrieve webpage content using HTTP requests.
- How to parse HTML and extract information using BeautifulSoup.
- How to work with product titles and price data.
- How to convert extracted strings into numeric values.
- How to implement conditional price comparisons.
- How to send automated email notifications using SMTP.
- How to manage credentials using environment variables.
- How web scraping can be applied to real-world shopping automation.

## 🚀 Future Improvements

- Schedule automatic price checks at regular intervals.
- Track multiple products simultaneously.
- Store historical prices in a database.
- Display product price trends using charts.
- Add support for multiple notification methods.
- Implement logging to record price changes and errors.
- Handle missing price elements and changes in webpage structure.
- Use an authorized product data source or API where available.
- Add configurable target prices for different products.

## 🔑 Key Takeaway

This project strengthened my understanding of **web scraping, HTTP requests, HTML parsing, conditional logic, and email automation using Python**.

It demonstrated how these concepts can be combined to build a practical tool that helps users monitor product prices and receive notifications when their target price is reached.


