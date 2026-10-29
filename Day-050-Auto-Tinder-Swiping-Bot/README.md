# Day 50 – Auto Tinder Swiping Bot

## 📖 Overview

This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

On Day 50, I developed an automated swiping bot using **Python and Selenium WebDriver** to interact with a Tinder-inspired web application called TinDog.

The bot automates the login workflow, manages multiple browser windows, navigates through the application, and repeatedly clicks the Like button. It also handles situations where a match popup interferes with the swiping process.

This project focuses on browser automation, web element interaction, explicit waits, window management, and exception handling.

## 🎯 Objectives

- Automate browser interactions using Selenium WebDriver.
- Locate web elements using different selection strategies.
- Automate login and navigation workflows.
- Handle multiple browser windows and window handles.
- Use explicit waits to improve automation reliability.
- Handle exceptions during automated clicking.
- Perform repetitive actions using loops.
- Understand practical applications of Python browser automation.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **Selenium WebDriver** – Browser automation.
- **Google Chrome** – Browser controlled by Selenium.

## 📚 Concepts Practiced

| Concept            | Description                                                        |
| ------------------ | ------------------------------------------------------------------ |
| WebDriver          | Launching and controlling the Chrome browser.                      |
| Element Locators   | Finding elements using class names, IDs, CSS selectors, and XPath. |
| Explicit Waits     | Waiting for elements or browser conditions before proceeding.      |
| Window Handling    | Switching between the main application and authentication window.  |
| Keyboard Actions   | Simulating Enter using `Keys.ENTER`.                               |
| Exception Handling | Managing intercepted clicks and missing elements.                  |
| Loops              | Repeating swiping actions using a `for` loop.                      |
| Chrome Options     | Configuring browser behavior using `ChromeOptions`.                |
| Time Delays        | Using `sleep()` to pause execution.                                |

## ⚙️ How It Works

1. **Launch Browser:** Opens Chrome using Selenium WebDriver.
2. **Open TinDog:** Navigates to the web application.
3. **Login:** Clicks the login button and opens the authentication window.
4. **Enter Credentials:** Fills in the email and password fields.
5. **Switch Windows:** Returns to the main application after the authentication window closes.
6. **Navigate:** Clicks the necessary buttons to reach the swiping interface.
7. **Automate Swiping:** Attempts to click the Like button up to 20 times.
8. **Handle Popups:** Attempts to interact with a match popup if it blocks the Like button.
9. **Close Session:** Ends the WebDriver session.

## 💻 Key Implementation Details

### 1. Browser Setup

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
```

Initializes Chrome WebDriver, configures browser behavior, and sets up an explicit wait with a 10-second timeout.

### 2. Handling Multiple Windows

```python
wait.until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[-1])
```

Waits for the authentication window to open and switches Selenium's focus to the newly opened window.

### 3. Automated Swiping

```python
for n in range(20):
    sleep(1)

    try:
        driver.find_element(By.CLASS_NAME, "btn-like").click()

    except ElementClickInterceptedException:
        try:
            driver.find_element(
                By.CSS_SELECTOR,
                ".match-popup a"
            ).click()

        except NoSuchElementException:
            sleep(2)

    except NoSuchElementException:
        sleep(2)
```

Repeats the Like-button click attempt 20 times and includes basic exception handling for intercepted clicks and missing elements.

**Note:** The loop makes 20 attempts; it does not guarantee 20 successful swipes.

## 📂 Project Structure

```text
Auto Tinder Swiping Bot/
│
├── main.py
└── README.md
```

- `main.py` – Contains the Python Selenium automation script.
- `README.md` – Documents the project's functionality and implementation.

## 🧠 What I Learned

- Automating browser-based workflows with Selenium.
- Locating and interacting with web elements.
- Using explicit waits for dynamic web pages.
- Managing multiple browser windows.
- Simulating keyboard actions.
- Handling common Selenium exceptions.
- Automating repetitive actions using loops.
- Understanding the importance of reliable selectors and synchronization.

## 🚀 Future Improvements

- Replace fixed delays with explicit waits wherever possible.
- Store credentials securely using environment variables.
- Add logging to track successful actions and errors.
- Use stable CSS selectors instead of absolute XPath expressions.
- Add robust handling for timeouts and stale elements.
- Organize the code into reusable functions.
- Improve popup detection and recovery logic.

## 🔑 Key Takeaway

This project strengthened my understanding of **Python browser automation using Selenium WebDriver**. It provided hands-on practice with login automation, window switching, element selection, explicit waits, loops, and exception handling.

These skills are useful for developing browser automation scripts, website testing tools, and other web-based automation solutions.


