# Day 52 – Instagram Follower Bot

## 📖 Overview

This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

On Day 52, I developed an automated Instagram-style Follower Bot using Python and Selenium WebDriver. The bot logs into a practice social media application, searches for a specified account, accesses its followers list, and automatically follows users who are not already being followed.

The project focuses on browser automation, interacting with dynamic web elements, handling scrollable containers, automating login workflows, and using explicit waits to manage web page interactions.

## 🎯 Objectives

- Automate login functionality using Selenium WebDriver.
- Search for a specified social media account.
- Navigate to the selected account's profile.
- Retrieve the account's follower count.
- Access and interact with the followers list.
- Automatically identify users who have a Follow button.
- Click Follow buttons to follow users.
- Handle dynamically loaded elements and scrollable containers.
- Store login credentials securely using environment variables.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **Selenium WebDriver** – Browser automation.
- **Google Chrome** – Browser controlled by Selenium.
- **python-dotenv** – Loading credentials from a `.env` file.
- **os Module** – Accessing environment variables.
- **WebDriverWait** – Handling dynamically loaded web elements.
- **Expected Conditions (EC)** – Waiting for elements to become visible or clickable.

## 📚 Concepts Practiced

| Concept | Description |
|---|---|
| WebDriver | Launching and controlling the Chrome browser. |
| Element Locators | Locating elements using XPath and HTML tags. |
| Explicit Waits | Waiting for elements to become visible or clickable. |
| Browser Automation | Automating login, searching, and following workflows. |
| Environment Variables | Storing sensitive credentials outside the Python script. |
| python-dotenv | Loading credentials from a `.env` file. |
| Classes and Objects | Organizing automation logic using a Python class. |
| Lists | Retrieving and iterating through follower elements. |
| Loops | Repeatedly checking and following users. |
| Conditional Statements | Checking whether a user has a Follow button. |
| Scrolling | Scrolling through a dynamically loaded followers list using JavaScript. |
| JavaScript Execution | Controlling the scroll position of a container. |
| Exception Handling Concepts | Understanding challenges with dynamic and interactive web elements. |

## ⚙️ How It Works

1. **Load Credentials:** Loads the username and password from the `.env` file using `python-dotenv`.
2. **Launch Browser:** Opens Google Chrome using Selenium WebDriver.
3. **Open Application:** Navigates to the practice social media application.
4. **Login:** Enters the username and password and submits the login form.
5. **Handle Popups:** Automatically dismisses the save-login and notification popups.
6. **Search Account:** Opens the search panel and searches for the specified account (`chefsteps`).
7. **Open Profile:** Selects the account from the search results.
8. **Access Followers:** Clicks the followers link to open the followers list.
9. **Retrieve Follower Count:** Extracts the displayed follower count.
10. **Identify Users:** Locates follower rows and checks whether their buttons display `Follow`.
11. **Follow Users:** Clicks the Follow button for users who are not already followed.
12. **Scroll Followers List:** Uses JavaScript to scroll through the followers container and load additional users.

## 💻 Key Implementation Details

### 1. Secure Credential Management

```python
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
```

Uses environment variables to load login credentials from a `.env` file instead of hardcoding sensitive information in the Python script.

### 2. Browser Setup

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

self.driver = webdriver.Chrome(options=chrome_options)
self.wait = WebDriverWait(self.driver, 10)
```

Initializes Chrome WebDriver, keeps the browser open after execution, and configures an explicit wait with a 10-second timeout.

### 3. Automated Login

```python
self.wait.until(
    EC.visibility_of_element_located((By.NAME, "username"))
).send_keys(USERNAME)

self.wait.until(
    EC.visibility_of_element_located((By.NAME, "password"))
).send_keys(PASSWORD, Keys.ENTER)
```

Locates the username and password fields, enters the credentials, and submits the login form.

### 4. Searching for an Account

```python
SIMILAR_ACCOUNT = "chefsteps"
```

The bot searches for the specified account using the application's search functionality and selects the first matching result.

### 5. Retrieving the Follower Count

```python
self.follower_count = int(
    self.wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a/b')
        )
    ).text
)
```

Extracts the displayed follower count and converts it into an integer for use in the automation process.

### 6. Automatically Following Users

```python
follower_rows = self.driver.find_elements(
    By.XPATH, '/html/body/div[2]/div/div[3]/div'
)

for row in follower_rows:
    follow_btn = row.find_element(By.TAG_NAME, 'button')

    if follow_btn.text == 'Follow':
        follow_btn.click()
```

Finds follower rows, checks the button text, and clicks only the buttons displaying `Follow`.

### 7. Scrolling Through the Followers List

```python
self.driver.execute_script(
    "arguments[0].scrollTop = arguments[0].scrollHeight",
    scroll
)
```

Uses JavaScript execution to scroll the followers container to its bottom, allowing additional follower entries to load.

## 📂 Project Structure

```text
Day-052-Instagram-Follower-Bot/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

- **main.py** – Contains the Selenium automation script.
- **.env** – Stores login credentials securely. Not uploaded to GitHub.
- **.gitignore** – Prevents sensitive files such as `.env` from being tracked by Git.
- **README.md** – Documents the project's functionality and implementation.

## 🔐 Security Implementation

- Stored login credentials in environment variables.
- Used `python-dotenv` to load credentials securely.
- Added `.env` to `.gitignore`.
- Avoided hardcoding sensitive credentials directly in the Python source code.

## 🧠 What I Learned

- Automating browser interactions using Selenium WebDriver.
- Working with login forms and dynamically loaded web elements.
- Searching for accounts and navigating between pages.
- Extracting information from web pages.
- Iterating through multiple web elements using loops.
- Automating button clicks based on conditional checks.
- Scrolling through dynamically loaded containers using JavaScript.
- Using explicit waits to synchronize browser interactions.
- Managing credentials using environment variables.
- Organizing automation scripts using classes and methods.

## 🚀 Future Improvements

- Replace absolute XPath expressions with more reliable CSS selectors.
- Implement better handling for dynamically loaded follower entries.
- Add exception handling for intercepted clicks and stale elements.
- Avoid processing the same follower multiple times.
- Improve scrolling logic to detect when all followers have been loaded.
- Add configurable limits on the number of users to follow.
- Add logging to track successful and unsuccessful follow actions.
- Replace fixed `sleep()` delays with explicit waits wherever possible.

## 🔑 Key Takeaway

This project strengthened my understanding of Python browser automation using Selenium WebDriver. It provided practical experience in automating login workflows, searching for accounts, retrieving follower information, interacting with dynamic web elements, and automating repetitive actions.

It also helped me understand how JavaScript execution can be used alongside Selenium to interact with scrollable containers and dynamically loaded content.
