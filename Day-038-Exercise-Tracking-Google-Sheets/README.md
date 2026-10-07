# Day 38 - Exercise Tracking with Google Sheets

## 📖 Overview

The **Exercise Tracking Google Sheets** is a Python-based fitness tracking application that uses the **Nutritionix API** to calculate the calories burned from physical activities and the **Sheety API** to store the exercise information in a Google Sheet.

The application asks the user which exercise they performed. The exercise description is then sent to the **Nutritionix API**, which uses natural language processing to identify the exercise and calculate information such as duration and calories burned.

The calculated exercise information is then formatted and sent to a Google Sheet using the **Sheety API**.

The project uses Python's `requests` library to communicate with both APIs and uses environment variables to securely store API credentials and authentication tokens.

This project was developed as part of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on API integration, authentication, HTTP headers, JSON data, environment variables, API requests, and Google Sheets integration.

---

## 🎯 Objective

Create an exercise tracking application that:

* Accepts exercise information from the user.
* Sends natural language exercise descriptions to an external API.
* Calculates calories burned from exercise.
* Retrieves exercise duration and other information.
* Adds the current date and time automatically.
* Stores exercise data in a Google Sheet.
* Uses multiple APIs in a single Python application.
* Uses API authentication.
* Uses HTTP headers for authenticated requests.
* Uses environment variables to protect sensitive credentials.
* Automates fitness tracking using Python.

---

## 🛠️ Concepts Practiced

### Python

* Variables
* Dictionaries
* Lists
* User input
* Functions
* `datetime`
* `strftime()`
* `requests`
* JSON data
* Environment variables
* `os`
* f-strings
* Loops
* Conditional logic

### API Integration

* HTTP POST requests
* REST APIs
* API endpoints
* Query parameters
* JSON request bodies
* JSON responses
* HTTP headers
* API authentication
* Bearer tokens
* Multiple API integrations

### APIs Used

* Nutritionix API
* Sheety API

### Data Handling

* Extracting nested JSON data
* Formatting API responses
* Converting API data into dictionaries
* Sending structured data to Google Sheets

---

## 📂 Files

```text
Day-038-Exercise-Tracking-Google-Sheets/
│
├── main.py                  # Main Python program
├── .env                     # Environment variables and API credentials
├── .gitignore               # Prevents sensitive files from being uploaded
├── requirements.txt         # External Python dependencies
└── README.md                # Project documentation
```

---

## 📦 Libraries Used

### Requests

The `requests` library is used to communicate with the Nutritionix and Sheety APIs.

```python
import requests
```

It is used to:

* Send HTTP requests.
* Send API parameters.
* Send JSON data.
* Send authentication headers.
* Receive API responses.
* Send exercise information to Nutritionix.
* Send exercise records to Google Sheets through Sheety.

---

### os

Python's built-in `os` module is used to access environment variables.

```python
import os
```

It is used to retrieve sensitive information such as:

* Nutritionix App ID
* Nutritionix API Key
* Sheety authentication token
* Other configuration values

For example:

```python
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get("TOKEN")
```

---

### datetime

Python's `datetime` module is used to generate the current date and time.

```python
from datetime import datetime
```

It is used to automatically record when the exercise was performed.

---

## 🌐 APIs Used

### Nutritionix API

The application uses the **Nutritionix API** to process natural language exercise descriptions.

The user can enter an exercise in a natural language format such as:

```text
I ran for 20 minutes
```

or:

```text
I walked for 30 minutes
```

Nutritionix processes the input and returns information such as:

* Exercise name
* Duration
* Calories burned

The exercise endpoint is:

```text
https://trackapi.nutritionix.com/v2/natural/exercise
```

The application sends the user's exercise information using a JSON request body.

---

### Sheety API

The application uses the **Sheety API** to connect the Python program with a Google Sheet.

Sheety converts the Google Sheet into an API endpoint that can be accessed using HTTP requests.

The application sends the calculated exercise information to Sheety, which then adds it as a new row in the Google Sheet.

---

## 🔑 1. Getting API Credentials

The Nutritionix API requires authentication credentials.

The application uses:

```python
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
```

These credentials are stored as environment variables instead of being directly written into the Python source code.

The Sheety API also uses an authentication token:

```python
TOKEN = os.environ.get("TOKEN")
```

This keeps sensitive credentials separate from the main program.

---

## 🔐 2. Authentication Using Headers

The Nutritionix API requires authentication information to be included in the HTTP request headers.

The headers contain:

```python
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
```

The headers provide Nutritionix with the credentials required to authenticate the request.

For Sheety, the authentication token is included in the request headers.

```python
headers = {
    "Authorization": f"Bearer {TOKEN}"
}
```

The `Bearer` token tells the API that the request is authenticated using the provided token.

---

## 📚 3. What Are HTTP Headers?

HTTP headers contain additional information about an HTTP request.

For example:

```python
headers = {
    "Authorization": f"Bearer {TOKEN}"
}
```

Headers can contain information such as:

* Authentication credentials
* Authorization tokens
* Content type
* Client information

In this project, headers are important because both Nutritionix and Sheety use authentication information to authorize API requests.

---

## 🏃 4. Getting Exercise Information

The application asks the user what exercise they performed.

```python
exercise_text = input("Tell me which exercise you did: ")
```

For example:

```text
Tell me which exercise you did: I ran for 20 minutes
```

The user's natural language input is then sent to Nutritionix.

---

## 🧮 5. Sending Exercise Data to Nutritionix

The application sends the exercise description to the Nutritionix API.

```python
exercise_params = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER
}
```

The user's physical information is used by Nutritionix to calculate the estimated calories burned.

The request is sent using:

```python
response = requests.post(
    url=EXERCISE_ENDPOINT,
    json=exercise_params,
    headers=headers
)
```

Nutritionix then processes the natural language exercise description.

---

## 📊 6. Processing the Nutritionix Response

Nutritionix returns the exercise information in JSON format.

The response contains an `exercises` list.

For example:

```text
Exercise
Duration
Calories
```

The program accesses the exercise information using:

```python
result = response.json()
```

The exercise information can then be extracted from the returned JSON data.

---

## 🔢 7. Extracting Exercise Information

The application extracts information such as:

* Exercise name
* Duration
* Calories burned

The data returned by Nutritionix is structured inside dictionaries and lists.

The program accesses the information from the `exercises` list.

For example:

```python
for exercise in result["exercises"]:
    exercise_name = exercise["name"]
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
```

This allows the program to process each exercise returned by the API.

---

## 📅 8. Getting the Current Date and Time

The program automatically generates the current date and time.

```python
today = datetime.now()
```

The date can be formatted using:

```python
date = today.strftime("%d/%m/%Y")
```

The time can be formatted using:

```python
time = today.strftime("%H:%M:%S")
```

This information is stored in the Google Sheet along with the exercise details.

---

## 📋 9. Preparing Data for Google Sheets

After receiving the exercise information from Nutritionix, the application prepares the data that needs to be stored in Google Sheets.

The data contains information such as:

```text
Date
Time
Exercise
Duration
Calories
```

The data is structured into a dictionary before being sent to Sheety.

For example:

```python
sheet_inputs = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise_name,
        "duration": duration,
        "calories": calories
    }
}
```

This structure matches the columns configured in the Google Sheet.

---

## 📤 10. Sending Data to Google Sheets

The application sends the prepared exercise data to the Sheety API.

```python
sheet_response = requests.post(
    url=sheet_endpoint,
    json=sheet_inputs,
    headers=sheet_headers
)
```

Sheety receives the request and adds the exercise information as a new row in the Google Sheet.

---

## 📊 11. Google Sheets Output

The Google Sheet stores the exercise records in rows.

For example:

```text
Date       Time      Exercise     Duration    Calories
07/10/2026 10:30:00  Running       20          180
07/10/2026 11:15:00  Walking       30          120
```

Each time the program is executed, a new exercise record can be added to the sheet.

---

## 🔄 API Data Flow

```text
                  Python Application
                          ↓
                    User Input
                          ↓
                Exercise Description
                          ↓
                  Nutritionix API
                          ↓
                 Exercise Information
                          ↓
              Duration + Calories
                          ↓
                 Add Date & Time
                          ↓
                Create JSON Data
                          ↓
              Add Authentication
                          ↓
                    Sheety API
                          ↓
                  Google Sheets
                          ↓
                 New Exercise Row
```

---

## 🏗️ Project Structure

### `main.py`

The main Python program.

It:

* Loads environment variables.
* Defines API credentials.
* Defines the Nutritionix endpoint.
* Defines the Sheety endpoint.
* Gets exercise information from the user.
* Sends the exercise description to Nutritionix.
* Retrieves exercise information.
* Extracts exercise name.
* Extracts exercise duration.
* Extracts calories burned.
* Generates the current date.
* Generates the current time.
* Creates the Google Sheet data.
* Adds authentication headers.
* Sends the data to Sheety.
* Adds the exercise record to Google Sheets.

---

### `.env`

Contains sensitive environment variables such as:

```text
APP_ID=your_app_id
API_KEY=your_api_key
TOKEN=your_token
```

This file should remain private and should not be uploaded to GitHub.

---

### `.gitignore`

The `.gitignore` file prevents sensitive files from being tracked by Git.

For example:

```text
.env
```

This prevents the `.env` file containing API credentials from being uploaded to GitHub.

---

### `requirements.txt`

Contains the external Python dependency:

```text
requests
```

The `os` and `datetime` modules do not need to be installed separately because they are included with Python.

---

### `README.md`

Contains the documentation for the project, including:

* Project overview
* Objective
* Concepts practiced
* Libraries used
* Nutritionix API
* Sheety API
* Authentication
* HTTP headers
* Exercise data processing
* Google Sheets integration
* API data flow
* Project structure
* Learning outcomes
* Future improvements

---

## 🔐 Security

API credentials and authentication tokens should **never be hardcoded in a public GitHub repository**.

Instead of:

```python
APP_ID = "your_app_id"
API_KEY = "your_api_key"
TOKEN = "your_token"
```

use environment variables:

```python
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get("TOKEN")
```

A `.env` file can also be used locally with an appropriate environment-variable library.

Make sure `.env` is included in `.gitignore`:

```text
.env
```

**Never commit API keys, authentication tokens, passwords, or other secrets to GitHub.**

---

## 🧪 Example

Suppose the user enters:

```text
I ran for 20 minutes
```

The program follows this process:

```text
User Input
     ↓
"I ran for 20 minutes"
     ↓
Nutritionix API
     ↓
Exercise Information
     ↓
Running
20 Minutes
Calories Burned
     ↓
Add Current Date & Time
     ↓
Create JSON Data
     ↓
Add Authentication Header
     ↓
Sheety API
     ↓
Google Sheets
     ↓
New Exercise Record
```

The Google Sheet then contains the exercise information.

---

## 🧠 Program Flow

```text
                 Start Program
                      ↓
              Load Environment
                 Variables
                      ↓
               Get User Input
                      ↓
          Send Exercise to Nutritionix
                      ↓
              Receive JSON Data
                      ↓
          Extract Exercise Details
                      ↓
          Extract Duration & Calories
                      ↓
              Get Date & Time
                      ↓
             Create Sheet Data
                      ↓
          Add Authentication Header
                      ↓
              Send Data to Sheety
                      ↓
              Update Google Sheet
                      ↓
                 End Program
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Make HTTP requests using `requests`.
* Work with external REST APIs.
* Use the Nutritionix API.
* Use the Sheety API.
* Send POST requests.
* Work with JSON request bodies.
* Process JSON responses.
* Access nested dictionaries and lists.
* Extract information from API responses.
* Work with natural language API input.
* Calculate and retrieve exercise information.
* Work with API authentication.
* Use HTTP headers.
* Understand Bearer token authentication.
* Use environment variables.
* Use `.env` files to store sensitive credentials.
* Use `.gitignore` to protect sensitive files.
* Generate dates and times using `datetime`.
* Send structured data to Google Sheets.
* Automate exercise tracking using Python.
* Integrate multiple APIs in a single Python application.
* Understand how APIs can connect different services.
* Build a practical fitness tracking application.

---

## 🚀 Future Improvements

Possible improvements for this project include:

* Add more exercise types.
* Allow users to track multiple exercises in one request.
* Add a graphical user interface.
* Add weekly and monthly calorie summaries.
* Calculate total exercise duration.
* Calculate total calories burned.
* Add charts and visualizations to Google Sheets.
* Add a dashboard for fitness progress.
* Add exercise history.
* Add user-specific profiles.
* Add validation for invalid exercise input.
* Add error handling for failed API requests.
* Handle API authentication errors.
* Handle invalid or missing API responses.
* Use environment variables for all credentials.
* Add logging.
* Add automated daily exercise reminders.
* Add additional fitness metrics.
* Store more detailed exercise information.
* Improve Google Sheets formatting.

---

## 🔑 Key Takeaway

This project helped me understand how Python can combine **natural language processing APIs, fitness data, authentication, HTTP requests, and Google Sheets** to create a practical exercise tracking application.

The biggest takeaway was learning how to send natural language exercise descriptions to the **Nutritionix API**, retrieve exercise duration and calorie information, process the JSON response, and send the resulting data to **Google Sheets through the Sheety API**.

It also strengthened my understanding of **API integration, JSON handling, POST requests, HTTP headers, Bearer authentication, environment variables, `.env` files, `.gitignore`, datetime handling, and connecting multiple APIs in a Python application**.
