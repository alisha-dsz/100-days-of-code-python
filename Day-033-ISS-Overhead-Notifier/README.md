# 🛰️ Day 33 - ISS Overhead Notifier

## 📖 Overview

The **ISS Overhead Notifier** is a Python-based automation project that checks whether the **International Space Station (ISS)** is currently close to a specified location and whether it is nighttime.

If both conditions are met, the program automatically sends an email notification telling the user to go outside and look for the ISS.

The project uses the **Open Notify ISS API** to retrieve the current ISS position and the **Sunrise-Sunset API** to determine sunrise and sunset times.

This project was developed as part of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on API requests, JSON data, datetime operations, conditional logic, loops, time delays, and email automation using SMTP.

---

## 🎯 Objective

Create an automated ISS notifier that:

* Retrieves the current ISS location using an API.
* Checks whether the ISS is within ±5 degrees of the user's location.
* Retrieves sunrise and sunset information.
* Determines whether it is currently nighttime.
* Sends an email notification when the ISS is nearby and it is dark.
* Checks the conditions repeatedly every 60 seconds.
* Uses Gmail SMTP to send the notification.

---

## 🛠️ Concepts Practiced

* Python
* Functions
* Variables
* Conditional Statements
* `if` / `else`
* Boolean Logic
* Comparison Operators
* `and` Operator
* `while` Loops
* `time.sleep()`
* API Requests
* REST APIs
* JSON Data
* `requests`
* `response.json()`
* `response.raise_for_status()`
* Query Parameters
* Type Conversion
* String Manipulation
* `datetime`
* Email Automation
* `smtplib`
* SMTP
* `starttls()`
* `login()`
* `sendmail()`

---

## 📂 Files

```text
Day-033-ISS-Overhead-Notifier/
│
├── main.py                  # Main Python program
├── README.md                # Project documentation
└── requirements.txt         # External Python dependencies
```

---

## 📦 Libraries Used

### Requests

The `requests` library is used to communicate with external APIs.

```python
import requests
```

It is used to:

* Send HTTP GET requests.
* Retrieve the current ISS position.
* Retrieve sunrise and sunset information.
* Check HTTP errors using `raise_for_status()`.
* Convert API responses into Python dictionaries using `json()`.

---

### Datetime

Python's `datetime` module is used to work with the current date and time.

```python
from datetime import datetime
```

The program uses the current time when checking whether it is nighttime.

---

### SMTP

Python's built-in `smtplib` module is used to send email notifications through Gmail's SMTP server.

```python
import smtplib
```

The connection uses:

```python
smtplib.SMTP("smtp.gmail.com")
```

The program then:

1. Starts a secure connection.
2. Logs into the email account.
3. Sends the notification email.

---

### Time

The `time` module is used to pause the program between checks.

```python
import time
```

The program waits:

```python
time.sleep(60)
```

This means the ISS position is checked every **60 seconds**.

---

## 🌐 APIs Used

### ISS Current Location API

The program sends a request to:

```text
http://api.open-notify.org/iss-now.json
```

The API provides the current latitude and longitude of the ISS.

The response is converted into JSON:

```python
data = response.json()
```

The ISS coordinates are then extracted:

```python
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
```

---

### Sunrise-Sunset API

The project also uses:

```text
https://api.sunrise-sunset.org/json
```

The user's latitude and longitude are sent as parameters:

```python
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
```

The API returns sunrise and sunset information for the specified location.

---

## 📍 1. Checking the ISS Location

The user's location is stored using latitude and longitude:

```python
MY_LAT = 51.507351
MY_LONG = -0.127758
```

The `is_overhead()` function retrieves the current ISS coordinates.

The program then checks whether the ISS is within **5 degrees** of the user's latitude and longitude.

```python
if float(MY_LAT - 5) <= iss_latitude <= float(MY_LAT + 5) and \
   float(MY_LONG - 5) <= iss_longitude <= float(MY_LONG + 5):
    return True
```

The basic logic is:

```text
Get ISS Position
       ↓
Get ISS Latitude & Longitude
       ↓
Compare with User's Location
       ↓
Within ±5 degrees?
       ↓
     Yes
       ↓
   Return True
```

---

## 🌙 2. Checking if It Is Nighttime

The `is_night()` function retrieves the sunrise and sunset times from the Sunrise-Sunset API.

```python
response = requests.get(
    "https://api.sunrise-sunset.org/json",
    params=parameters
)
```

The response is converted into JSON:

```python
data = response.json()
```

The program extracts the sunrise and sunset hours from the returned data.

The purpose is to determine whether the current time is suitable for spotting the ISS.

---

## 🚨 3. Checking Both Conditions

The program continuously checks:

```python
if is_overhead() and is_night():
```

Both conditions must be satisfied:

```text
ISS is nearby
      +
It is nighttime
      ↓
Send Email
```

If either condition is not satisfied, the program prints:

```text
Sorry, itsn't the day for you spot the ISS.
```

---

## 📧 4. Sending the Email

When the ISS is nearby and it is nighttime, the program connects to Gmail's SMTP server.

```python
with smtplib.SMTP("smtp.gmail.com") as connection:
```

It then starts TLS encryption:

```python
connection.starttls()
```

The program logs into the email account:

```python
connection.login(
    user=MY_EMAIL,
    password=MY_PASSWORD
)
```

Finally, it sends the notification:

```python
connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs="your-email@example.com",
    msg="Subject:ISS Location near you!\n\n"
        "Hurry and go outside to look up for the ISS tracker."
)
```

---

## 🔄 Application Workflow

```text
              Start Program
                   ↓
          Wait for 60 Seconds
                   ↓
        Get Current ISS Position
                   ↓
          Check ISS Location
                   ↓
             Is ISS Nearby?
              ↙          ↘
            No            Yes
            ↓              ↓
          Continue      Check Nighttime
                           ↓
                    Is It Nighttime?
                      ↙          ↘
                    No            Yes
                    ↓              ↓
                 Continue      Send Email 📧
                                   ↓
                              Wait 60 Seconds
                                   ↓
                              Repeat Process
```

---

## 🔁 Continuous Monitoring

The project uses an infinite `while` loop:

```python
while True:
```

The program waits for 60 seconds between checks:

```python
time.sleep(60)
```

This allows the program to continuously monitor the ISS without requiring the user to restart it manually.

---

## 🔐 Email Security

**Important:** Email passwords and Gmail App Passwords should never be hardcoded in a public GitHub repository.

The original code contains an email credential directly in the source code. **Do not upload that credential to GitHub.**

Instead, credentials should be stored using environment variables:

```python
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
```

For a GitHub project, sensitive values can also be stored using **GitHub Secrets**.

> ⚠️ If the App Password shown in the original code is real and still active, revoke it and create a new one before pushing the project to GitHub.

---

## 🧪 Example

Suppose the user's location is:

```text
Latitude: 51.507351
Longitude: -0.127758
```

The program continuously retrieves the ISS location.

If the ISS is within approximately ±5 degrees:

```text
ISS Nearby
    ↓
Check if it is nighttime
    ↓
Nighttime
    ↓
Send Email 📧
```

The user receives:

```text
Subject: ISS Location near you!

Hurry and go outside to look up for the ISS tracker.
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Make HTTP requests using `requests`.
* Work with external APIs.
* Retrieve JSON data from APIs.
* Access nested JSON data.
* Use `response.raise_for_status()` to handle HTTP errors.
* Use API query parameters.
* Convert strings into floating-point numbers.
* Compare latitude and longitude values.
* Create reusable Python functions.
* Use conditional statements.
* Combine multiple conditions using `and`.
* Work with Python's `datetime` module.
* Use `time.sleep()` for timed execution.
* Create an infinite monitoring loop.
* Send emails using Python's `smtplib`.
* Connect to Gmail's SMTP server.
* Use `starttls()` for a secure connection.
* Automate notifications based on real-world API data.

---

## 🚀 Future Improvements

* Store email credentials using environment variables.
* Improve the nighttime calculation using complete datetime values rather than only the hour.
* Add better handling when no ISS position is returned.
* Add logging for successful and failed email notifications.
* Prevent repeated emails while the ISS remains nearby.
* Add a cooldown period after sending an email.
* Use a more reliable ISS tracking API if the current API becomes unavailable.
* Add timezone-aware datetime handling.
* Run the program automatically using GitHub Actions or another scheduler.
* Create a graphical interface showing the ISS's current location.
* Add a map displaying the ISS position.
* Customize the notification message.
* Add error handling for email connection failures.

---

## 🔐 Security Note

This project is created primarily for learning API integration and automation.

Email credentials and App Passwords should **never** be stored directly in the source code or committed to GitHub.

For a real-world application, credentials should be protected using environment variables, GitHub Secrets, or another secure secrets manager.

---

## 🧠 Key Takeaway

This project helped me understand how Python can interact with **real-world APIs** and use the returned data to make automated decisions.

It combined **API requests, JSON data, conditional logic, datetime operations, loops, time delays, and SMTP email automation** into one practical project.

The biggest takeaway was learning how a Python program can continuously monitor real-world data and automatically perform an action when specific conditions are met.
