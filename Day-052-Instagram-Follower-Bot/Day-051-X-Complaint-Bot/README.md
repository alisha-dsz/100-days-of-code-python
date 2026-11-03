# Day 51 – X Complaint Bot

## 📖 Overview

This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

On Day 51, I developed an automated Internet Speed Twitter Bot using **Python and Selenium WebDriver** to measure internet download and upload speeds and automatically post a complaint when the actual internet speed falls below the promised speed.

The bot uses Speedtest.net to measure internet performance and then logs into a Twitter-inspired web application to publish a message based on the speed test results.

This project focuses on browser automation, web scraping, environment variables, automated login workflows, conditional statements, and interacting with dynamic web elements.

## 🎯 Objectives

- Automate internet speed testing using Selenium WebDriver.
- Retrieve download and upload speed measurements from a website.
- Automate login workflows using Selenium.
- Store login credentials securely using environment variables.
- Use `python-dotenv` to load credentials from a `.env` file.
- Locate web elements using XPath and CSS selectors.
- Use explicit waits to handle dynamically loaded elements.
- Apply conditional statements to compare actual and promised internet speeds.
- Automatically generate and publish messages based on test results.
- Understand practical applications of Python browser automation.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **Selenium WebDriver** – Browser automation.
- **Google Chrome** – Browser controlled by Selenium.
- **python-dotenv** – Loading environment variables from a `.env` file.
- **os Module** – Accessing environment variables.
- **Speedtest.net** – Measuring internet download and upload speeds.

## 📚 Concepts Practiced

| **Concept** | **Description** |
|---|---|
| WebDriver | Launching and controlling the Chrome browser. |
| Element Locators | Finding elements using XPath and CSS selectors. |
| Explicit Waits | Waiting for elements to become visible or clickable. |
| Browser Automation | Automating internet speed testing and login workflows. |
| Environment Variables | Storing sensitive credentials outside the Python source code. |
| python-dotenv | Loading credentials from a `.env` file. |
| Conditional Statements | Comparing actual internet speeds against promised speeds. |
| Type Conversion | Converting speed values into floating-point numbers. |
| String Formatting | Dynamically generating complaint messages. |
| Time Delays | Using `sleep()` to allow web pages and speed tests to load. |
| Classes and Objects | Organizing automation logic using a Python class. |

## ⚙️ How It Works

1. **Load Credentials:** Loads login credentials from the `.env` file using `python-dotenv`.
2. **Launch Browser:** Opens Google Chrome using Selenium WebDriver.
3. **Open Speedtest.net:** Navigates to the Speedtest website.
4. **Handle Privacy Popup:** Accepts the privacy consent popup if displayed.
5. **Start Speed Test:** Clicks the Go button to begin measuring internet speed.
6. **Retrieve Speed Results:** Extracts the download and upload speeds from the results page.
7. **Print Results:** Displays the measured download and upload speeds in the terminal.
8. **Open Login Page:** Navigates to the practice login application.
9. **Authenticate:** Enters the email and password loaded from environment variables.
10. **Compare Speeds:** Compares the measured speeds against the promised download and upload speeds.
11. **Generate Message:** Creates a complaint message if either speed is below the promised speed. Otherwise, generates a positive message.
12. **Publish Message:** Enters the generated message into the application's text area and clicks the Post button.

## 💻 Key Implementation Details

### 1. Secure Credential Management

```python
from dotenv import load_dotenv
import os

load_dotenv()

LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
```

Uses `python-dotenv` to load login credentials from a `.env` file instead of hardcoding sensitive information in the Python script.

### 2. Browser Setup

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

self.driver = webdriver.Chrome(options=chrome_options)
self.wait = WebDriverWait(self.driver, 10)
```

Initializes Chrome WebDriver, configures the browser to remain open after execution, and sets up an explicit wait with a 10-second timeout.

### 3. Internet Speed Measurement

```python
go_button = self.wait.until(
    EC.element_to_be_clickable((By.XPATH, go_button_xpath))
)

go_button.click()
sleep(60)
```

Waits until the Go button becomes clickable, starts the speed test, and allows time for the test to complete before retrieving the results.

The download and upload speeds are extracted using XPath selectors.

### 4. Comparing Internet Speeds

```python
if float(self.down) < float(PROMISED_DOWN) or float(self.up) < float(PROMISED_UP):
```

Converts the measured speed values into floating-point numbers and compares them against the promised download and upload speeds.

If either speed is below the promised speed, the bot prepares a complaint message.

### 5. Automated Message Posting

```python
self.wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="tweet-compose"]')
    )
).send_keys(message)

self.wait.until(
    EC.element_to_be_clickable((By.ID, 'post-btn'))
).click()
```

Locates the message input field, enters the dynamically generated message, and clicks the Post button to publish it.

## 📂 Project Structure

```text
Day-051-X-Complaint-Bot/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

- `main.py` – Contains the Python Selenium automation script.
- `.env` – Stores login credentials securely. Not uploaded to GitHub.
- `.gitignore` – Prevents sensitive files such as `.env` from being tracked by Git.
- `README.md` – Documents the project's functionality and implementation.

## 🔐 Security Implementation

- Stored login credentials in environment variables.
- Used `python-dotenv` to load credentials securely.
- Added `.env` to `.gitignore` to prevent accidental exposure of sensitive information.
- Avoided hardcoding login credentials directly in the Python source code.

## 🧠 What I Learned

- Automating browser-based workflows using Selenium.
- Extracting information from dynamically loaded web pages.
- Measuring and retrieving internet speed results.
- Using explicit waits to synchronize browser interactions.
- Managing sensitive information using environment variables.
- Working with `.env` and `.gitignore` files.
- Applying conditional logic to automate decisions.
- Generating dynamic messages based on retrieved data.
- Organizing automation scripts using classes and methods.

## 🚀 Future Improvements

- Replace fixed `sleep()` delays with dynamic waits wherever possible.
- Use more stable CSS selectors instead of absolute XPath expressions.
- Add exception handling for timeouts and missing elements.
- Improve speed test result detection instead of relying on a fixed 60-second delay.
- Add logging to track speed test results and posting status.
- Implement automated speed testing at scheduled intervals.
- Improve error handling for failed login attempts and message posting.

## 🔑 Key Takeaway

This project strengthened my understanding of **Python browser automation using Selenium WebDriver**. It provided hands-on experience with automated web interactions, extracting dynamic data, environment variable management, conditional logic, and automated message posting.

It also demonstrated how Python can be used to build practical automation tools that monitor website data, evaluate conditions, and perform actions based on the results.
