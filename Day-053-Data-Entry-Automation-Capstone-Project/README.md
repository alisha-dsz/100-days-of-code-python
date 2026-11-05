# Day 53 – Data Entry Automation Capstone Project

## 📖 Overview

This project is part of the 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu.

On Day 53, I developed a Data Entry Automation project using Python, BeautifulSoup, Requests, and Selenium WebDriver. The program scrapes rental property information from a Zillow clone website, including property prices, addresses, and listing URLs. It then automatically enters the extracted information into a Google Form and submits a separate response for each property.

The project focuses on web scraping, HTML parsing, data extraction, browser automation, form submission, and combining multiple Python libraries to automate a real-world data entry task.

## 🎯 Objectives

- Send HTTP requests to retrieve website content.
- Scrape rental property listings using BeautifulSoup.
- Extract property prices from the website.
- Retrieve and clean property addresses.
- Extract direct URLs for individual property listings.
- Store scraped information in Python lists.
- Automate Google Chrome using Selenium WebDriver.
- Automatically fill out Google Form fields with scraped data.
- Submit multiple form responses without manual intervention.
- Use explicit waits to handle dynamic browser interactions.

## 🛠️ Technologies Used

- **Python** – Programming language.
- **Requests** – Sending HTTP requests to retrieve webpage content.
- **BeautifulSoup** – Parsing HTML and extracting property information.
- **Selenium WebDriver** – Automating browser interactions and form submissions.
- **Google Chrome** – Browser controlled by Selenium.
- **WebDriverWait** – Waiting for web elements to become available.
- **Expected Conditions (EC)** – Waiting for elements to become clickable or visible.
- **time Module** – Introducing short delays between browser interactions.

## 📚 Concepts Practiced

| Concept             | Description                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| HTTP Requests       | Retrieving webpage content using the Requests library.                    |
| BeautifulSoup       | Parsing HTML content to extract property information.                     |
| HTML Parsing        | Identifying relevant HTML tags and CSS classes.                           |
| Web Scraping        | Extracting property prices, addresses, and URLs from a website.           |
| List Comprehensions | Creating lists from extracted property information.                       |
| String Manipulation | Cleaning prices and formatting property addresses.                        |
| find_all()          | Finding multiple HTML elements matching specific tags and classes.        |
| getText()           | Extracting readable text from HTML elements.                              |
| get()               | Retrieving HTML attributes such as href.                                  |
| Selenium WebDriver  | Launching and controlling the Chrome browser.                             |
| Element Locators    | Locating Google Form input fields and buttons using XPath.                |
| send_keys()         | Automatically entering property information into form fields.             |
| Explicit Waits      | Waiting for browser elements before interacting with them.                |
| Expected Conditions | Checking whether elements are clickable or visible.                       |
| Loops               | Iterating through property listings and submitting multiple responses.    |
| Indexing            | Accessing corresponding prices, addresses, and links from separate lists. |
| Browser Automation  | Automating repetitive form-filling and submission tasks.                  |

## ⚙️ How It Works

**Send HTTP Request:** Sends a GET request to the Zillow clone website using the Requests library to retrieve its HTML content.

**Parse HTML:** Uses BeautifulSoup to parse the retrieved webpage content.

**Extract Property Prices:** Finds all property price elements using their CSS class and extracts the price information.

**Clean Prices:** Removes unnecessary rental duration information and separates the actual price from the remaining text.

**Extract Addresses:** Finds all address elements and removes unwanted commas, separators, and extra whitespace.

**Extract Property Links:** Locates property listing anchor tags and retrieves their href attributes.

**Launch Browser:** Opens Google Chrome using Selenium WebDriver and initializes WebDriverWait with a 10-second timeout.

**Open Google Form:** Navigates to the Google Form where the property information needs to be submitted.

**Fill Form Fields:** Iterates through the extracted property information and automatically enters the corresponding address, price, and property URL into their respective input fields.

**Submit Responses:** Clicks the Submit button after filling in the details.

**Open New Response:** Waits for the submission confirmation and clicks the Submit another response link to open a fresh form.

**Repeat Process:** Continues filling and submitting responses until all scraped property listings have been processed.

**Close Browser:** Closes the Chrome browser after all form submissions are completed.

## 💻 Key Implementation Details

### 1. Sending HTTP Requests

```python
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_URL)
print(response.status_code)

content = response.text
```

Uses the Requests library to send an HTTP GET request to the Zillow clone website. The response status code is printed, and the webpage's HTML content is stored for further processing.

### 2. Parsing HTML Using BeautifulSoup

```python
soup = BeautifulSoup(content, "html.parser")
```

Creates a BeautifulSoup object to parse the HTML content using Python's built-in HTML parser. This allows the program to search for specific HTML elements and extract the required property information.

### 3. Extracting Property Prices

```python
prices = soup.find_all(
    name="span",
    class_="PropertyCardWrapper__StyledPriceLine"
)

price_list = [
    price.getText().replace("/", "+").split("+")
    for price in prices
]

price = [amount[0] for amount in price_list]
```

Finds all property price elements using their CSS class.

The extracted text is cleaned by replacing the rental duration separator and splitting the text to retain only the actual property price.

### 4. Extracting Property Addresses

```python
addresses = soup.find_all(name="address")

address_list = [
    address.getText()
    .replace(",", "")
    .replace(" |", "")
    .strip()
    for address in addresses
]
```

Locates all address elements and extracts their text.

String manipulation methods are used to remove commas, unwanted separators, and extra whitespace to obtain clean property addresses.

### 5. Extracting Property Links

```python
links = soup.find_all(
    name="a",
    class_="StyledPropertyCardDataArea-anchor"
)

link_list = [link.get("href") for link in links]
```

Finds the anchor elements associated with individual property listings and retrieves their href attributes.

These URLs provide direct links to the corresponding property listings.

### 6. Browser Setup

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get(FORM_URL)
```

Initializes Chrome WebDriver and configures the browser to remain open after the script finishes.

WebDriverWait is initialized with a 10-second timeout to handle browser interactions more reliably.

### 7. Automatically Filling Google Form Fields

```python
for index in range(len(price)):

    address_input = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )

    address_input.click()
    address_input.send_keys(address_list[index])

    price_input = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )

    price_input.click()
    price_input.send_keys(price[index])

    link_input = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )

    link_input.click()
    link_input.send_keys(link_list[index])
```

Uses a for loop to iterate through all the extracted property listings.

For each iteration, Selenium locates the three Google Form input fields and automatically enters the corresponding property address, price, and listing URL.

### 8. Submitting the Google Form

```python
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    )
).click()
```

Uses WebDriverWait and Expected Conditions to wait until the Submit button becomes clickable before clicking it.

This helps ensure that the form is ready for submission before Selenium interacts with it.

### 9. Submitting Another Response

```python
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    )
).click()
```

After submitting a response, the program waits for the confirmation page and locates the Submit another response link.

Clicking this link opens a fresh form so that the next property's information can be entered.

### 10. Closing the Browser

```python
driver.quit()
```

Closes all browser windows and terminates the Selenium WebDriver session after all property listings have been submitted.

## 📂 Project Structure

```text
Day-053-Data-Entry-Automation-Capstone-Project/
│
├── main.py
└── README.md
```

**main.py** – Contains the complete web scraping and Selenium automation script.

**README.md** – Documents the project's functionality, technologies, and implementation details.

## 🔐 Important Notes

- The project uses a practice Zillow clone website provided by App Brewery.
- The Google Form URL is configured directly in the Python script.
- The Google Form must contain fields corresponding to property address, price, and listing URL.
- XPath expressions must match the structure of the Google Form.
- An active internet connection is required.
- Selenium requires Google Chrome and a compatible WebDriver setup.

## 🧠 What I Learned

- Scraping website content using Requests and BeautifulSoup.
- Parsing HTML and identifying elements using tags and CSS classes.
- Extracting text and attributes from HTML elements.
- Cleaning scraped data using Python string methods.
- Working with multiple lists containing related information.
- Automating Google Forms using Selenium WebDriver.
- Locating input fields and buttons using XPath.
- Automatically entering data using send_keys().
- Handling browser interactions using explicit waits.
- Using Expected Conditions to synchronize automation.
- Automating repetitive data entry tasks.
- Combining web scraping and browser automation into a single workflow.

## 🚀 Future Improvements

- Replace absolute XPath expressions with more reliable CSS selectors or relative XPath expressions.
- Add exception handling for missing or unavailable elements.
- Validate extracted data before submitting form responses.
- Check that prices, addresses, and property links have matching list lengths.
- Replace fixed sleep() delays with explicit waits wherever possible.
- Add logging to track successful and unsuccessful submissions.
- Store scraped property information in a CSV or Excel file.
- Implement duplicate detection to prevent submitting the same property multiple times.
- Add support for scraping additional property details.

## 🔑 Key Takeaway

This project strengthened my understanding of web scraping and browser automation using Python. It provided practical experience in extracting structured data from websites using BeautifulSoup and Requests and transferring that information into online forms using Selenium WebDriver.

It also demonstrated how multiple Python libraries can work together to automate repetitive tasks, reduce manual data entry, and build practical end-to-end automation solutions.
