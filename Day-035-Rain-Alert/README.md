# Day 35 - Rain Alert

## 📖 Overview

The **Rain Alert** is a Python-based weather notification application that checks the weather forecast using the **OpenWeatherMap API** and sends a WhatsApp notification through **Twilio** if rain is expected.

The application retrieves weather forecast data for a specified location using its latitude and longitude. It then processes the JSON response and checks the weather condition codes.

If rain is detected in the upcoming forecast, the program automatically sends a WhatsApp message reminding the user to carry an umbrella.

The project uses the **Requests** library to communicate with the OpenWeatherMap API and the **Twilio Python SDK** to send WhatsApp messages.

This project was developed as part of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on **API requests, JSON data handling, environment variables, API authentication, conditional logic, and Twilio messaging**.

---

## 🎯 Objective

Create a weather alert application that:

* Retrieves weather forecast data from an external API.
* Uses latitude and longitude to identify a location.
* Processes JSON data returned by the API.
* Checks weather condition codes.
* Determines whether rain is expected.
* Sends a WhatsApp notification when rain is detected.
* Uses Twilio to send WhatsApp messages.
* Keeps API keys and authentication credentials outside the source code.
* Uses environment variables for sensitive information.
* Handles HTTP errors from the API.
* Provides a simple weather-based notification system.

---

## 🛠️ Concepts Practiced

* Python
* Variables
* Functions
* Conditional Statements
* `if` Statements
* Boolean Logic
* `for` Loops
* Lists
* Dictionaries
* JSON Data
* API Requests
* REST APIs
* Query Parameters
* HTTP Requests
* `requests`
* `response.json()`
* `raise_for_status()`
* OpenWeatherMap API
* Twilio API
* Twilio WhatsApp Messaging
* Environment Variables
* `os.environ.get()`
* API Authentication
* Error Handling
* External API Integration

---

## 📂 Files

```text
Day-035-Rain-Alert/
│
├── main.py                  # Main Python program
├── requirements.txt         # External Python dependencies
└── README.md                # Project documentation
```

---

## 📦 Libraries Used

### Requests

The `requests` library is used to communicate with the OpenWeatherMap API.

```python
import requests
```

It is used to:

* Send HTTP GET requests.
* Send weather API parameters.
* Retrieve weather forecast data.
* Receive API responses.
* Convert JSON responses into Python data.
* Check HTTP errors using `raise_for_status()`.

---

### Twilio

The `twilio` library is used to communicate with the Twilio API and send WhatsApp messages.

```python
from twilio.rest import Client
```

It is used to:

* Authenticate with the Twilio account.
* Create a Twilio client.
* Send WhatsApp messages.
* Retrieve the message SID.
* Check the message status.

---

### OS

Python's built-in `os` module is used to retrieve sensitive information from environment variables.

```python
import os
```

The application retrieves:

```python
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")
```

This prevents API keys and authentication credentials from being directly written into the source code.

---

## 🌐 API Used

### OpenWeatherMap API

The application uses the **OpenWeatherMap API** to retrieve weather forecast information.

The forecast request uses latitude and longitude to identify the location.

The application sends parameters such as:

```python
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}
```

The API request is made using:

```python
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)
```

The application then checks for HTTP errors:

```python
response.raise_for_status()
```

The JSON response is converted into Python data using:

```python
weather_data = response.json()
```

---

## 🔄 API Data Flow

```text
          Python Application
                  ↓
        Send API Request
                  ↓
       OpenWeatherMap API
                  ↓
           JSON Response
                  ↓
        Extract Forecast Data
                  ↓
       Check Weather Conditions
                  ↓
          Is Rain Expected?
             ↙         ↘
           NO           YES
           ↓             ↓
       Do Nothing       Twilio
                          ↓
                  WhatsApp Message
```

---

## ☔ 1. Retrieving the Weather Forecast

The application retrieves weather forecast information from OpenWeatherMap.

```python
response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)

response.raise_for_status()
weather_data = response.json()
```

The API returns forecast information in JSON format.

The program accesses the forecast list using:

```python
weather_data["list"]
```

The application then examines each forecast entry.

---

## 🌧️ 2. Detecting Rain

The application checks the weather condition code returned by OpenWeatherMap.

```python
will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True
```

The program starts with:

```python
will_rain = False
```

If a weather condition matching the specified condition is found, it changes to:

```python
will_rain = True
```

This tells the program that a notification should be sent.

---

## 📲 3. Sending the WhatsApp Alert

If rain is expected, a Twilio client is created:

```python
if will_rain:
    client = Client(account_sid, auth_token)
```

The application then sends a WhatsApp message:

```python
message = client.messages.create(
    from_="whatsapp:+17372508034",
    body="It's going to rain today. Remember to bring an umbrella",
    to="whatsapp:+918291434538",
    content_sid="HX25161c213d71bb75e073ead06f38fbbd",
)
```

The message SID and status are displayed:

```python
print(message.sid)
print(message.status)
```

---

## 🔐 4. Using Environment Variables

Sensitive information such as API keys and authentication credentials should not be hardcoded into the Python program.

Instead, the application uses environment variables:

```python
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")
```

This keeps sensitive credentials separate from the main application code.

The required environment variables are:

```text
OWM_API_KEY
ACCOUNT_SID
AUTH_TOKEN
```

---

## 📱 5. Twilio WhatsApp Messaging

The project uses Twilio to send a WhatsApp notification when rain is detected.

The Twilio client is created using:

```python
client = Client(account_sid, auth_token)
```

The application then sends the message through Twilio's WhatsApp service.

The notification reminds the user:

```text
It's going to rain today.
Remember to bring an umbrella
```

This demonstrates how Python can interact with an external messaging service.

---

## 🧪 Example

Suppose the weather API returns forecast information containing a condition that indicates rain.

The application processes the data:

```text
Weather Forecast
      ↓
Condition Code
      ↓
Rain Detected
      ↓
will_rain = True
      ↓
Create Twilio Client
      ↓
Send WhatsApp Message
```

The user receives:

```text
It's going to rain today.
Remember to bring an umbrella
```

If rain is not detected:

```text
Weather Forecast
      ↓
No Rain Detected
      ↓
will_rain = False
      ↓
No Message Sent
```

---

## 🏗️ Project Structure

### `main.py`

The main Python program.

It:

* Retrieves API credentials from environment variables.
* Defines the user's location.
* Creates the weather API parameters.
* Sends a request to OpenWeatherMap.
* Retrieves weather forecast data.
* Processes the JSON response.
* Checks weather condition codes.
* Determines whether rain is expected.
* Creates a Twilio client.
* Sends a WhatsApp notification.
* Displays the message SID and status.

---

### `requirements.txt`

Contains the external Python dependencies:

```text
requests
twilio
```

These libraries are required for communicating with OpenWeatherMap and Twilio.

---

### `README.md`

Contains the documentation for the project, including:

* Project overview
* Objective
* Concepts practiced
* Libraries used
* API information
* Project structure
* Learning outcomes
* Future improvements

---

## 🔒 Security

This project demonstrates the importance of keeping sensitive credentials outside the source code.

The following information should **not be hardcoded**:

```text
OpenWeatherMap API Key
Twilio Account SID
Twilio Auth Token
```

Instead, the project uses:

```python
os.environ.get()
```

to retrieve these values from environment variables.

This makes it safer to publish the project on GitHub without exposing private API credentials.

---

## 🧠 Program Flow

```text
             Start Program
                   ↓
        Load Environment Variables
                   ↓
        Define Location Coordinates
                   ↓
        Create Weather Parameters
                   ↓
       Request Weather Forecast
                   ↓
          Receive JSON Data
                   ↓
       Check Weather Conditions
                   ↓
          Is Rain Expected?
             ↙         ↘
           NO           YES
           ↓             ↓
       End Program     Twilio
                         ↓
                 Send WhatsApp Alert
                         ↓
                    End Program
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Make HTTP requests using `requests`.
* Work with external REST APIs.
* Use the OpenWeatherMap API.
* Use API query parameters.
* Retrieve weather forecast data.
* Process JSON responses.
* Access nested dictionaries and lists.
* Work with weather condition codes.
* Use conditional statements.
* Use loops to process API data.
* Integrate Twilio with Python.
* Send WhatsApp messages using Twilio.
* Create a Twilio client.
* Work with environment variables.
* Use `os.environ.get()`.
* Keep sensitive credentials outside source code.
* Handle HTTP errors using `raise_for_status()`.
* Combine multiple external services in a Python application.
* Build a practical API-based automation tool.

---

## 🚀 Future Improvements

* Add temperature information to the WhatsApp message.
* Include the expected rainfall time.
* Include the current weather condition.
* Add humidity information.
* Add wind speed information.
* Send different messages depending on the weather condition.
* Add support for multiple locations.
* Allow users to configure their own coordinates.
* Add a weather forecast summary.
* Improve error handling for API failures.
* Add retry functionality when an API request fails.
* Add more detailed Twilio message status handling.
* Support multiple notification recipients.
* Store weather history using JSON or a database.
* Create a graphical or web interface for configuring the alert.

---

## 🧠 Key Takeaway

This project helped me understand how Python can combine **external APIs, JSON data, environment variables, and Twilio messaging** to create a practical weather notification application.

The biggest takeaway was learning how to retrieve weather forecast data from an external API, process the returned JSON data, determine whether rain is expected, and send a WhatsApp notification using Twilio.

It also strengthened my understanding of **API integration, JSON handling, environment variables, API authentication, HTTP requests, error handling, and external service integration in Python**.
