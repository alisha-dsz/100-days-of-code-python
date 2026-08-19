Day 35 - Rain Alert
📖 Overview

The Rain Alert is a Python-based weather notification application that checks the weather forecast using the OpenWeatherMap API and sends a WhatsApp notification through Twilio if rain is expected.

The application retrieves weather forecast data for a specified location and checks the weather condition codes returned by the API.

If any of the upcoming forecast periods indicate rain, the program automatically sends a WhatsApp message reminding the user to carry an umbrella.

The project uses the Requests library to communicate with the OpenWeatherMap API and the Twilio Python SDK to send WhatsApp messages.

The project also uses GitHub Actions to automate the execution of the Python script on a daily schedule.

This project was developed as part of the 100 Days of Code: The Complete Python Pro Bootcamp, focusing on API integration, JSON data handling, environment variables, automation, GitHub Actions, scheduled tasks, and Twilio messaging.

🎯 Objective

Create an automated rain alert application that:

Retrieves weather forecast data from OpenWeatherMap.
Uses latitude and longitude to identify the required location.
Processes JSON data returned by the weather API.
Checks weather condition codes.
Determines whether rain is expected.
Sends a WhatsApp notification when rain is detected.
Uses Twilio to send WhatsApp messages.
Keeps API keys and authentication credentials secure using environment variables.
Uses GitHub Secrets to securely store sensitive credentials.
Uses GitHub Actions to run the script automatically.
Schedules the script to run every day.
Provides a simple automated weather notification system.
🛠️ Concepts Practiced
Python
Variables
Functions
Conditional Statements
if Statements
Boolean Logic
for Loops
Lists
Dictionaries
JSON Data
API Requests
REST APIs
Query Parameters
HTTP Requests
requests
response.json()
raise_for_status()
OpenWeatherMap API
Twilio API
Twilio WhatsApp Messaging
Environment Variables
os.environ.get()
Git
GitHub
GitHub Actions
YAML
Cron Scheduling
GitHub Secrets
Automation
Error Handling
External API Integration
📂 Files
Day-035-Rain-Alert/
│
├── main.py                         # Main Python program
├── requirements.txt                # External Python dependencies
│
└── .github/
    └── workflows/
        └── scheduled.yml           # GitHub Actions workflow
│
└── README.md                       # Project documentation
📦 Libraries Used
Requests

The requests library is used to communicate with the OpenWeatherMap API.

import requests

It is used to:

Send HTTP GET requests.
Send weather API parameters.
Retrieve weather forecast data.
Receive API responses.
Convert JSON responses into Python data.
Check HTTP errors using raise_for_status().
Twilio

The twilio library is used to communicate with the Twilio API and send WhatsApp messages.

from twilio.rest import Client

It is used to:

Authenticate with the Twilio account.
Create a Twilio client.
Send WhatsApp messages.
Retrieve the message SID.
Check the message status.
OS

Python's built-in os module is used to retrieve sensitive information from environment variables.

import os

The application retrieves:

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")

This prevents API keys and authentication credentials from being directly written into the source code.

🌐 API Used
OpenWeatherMap API

The application uses the OpenWeatherMap API to retrieve weather forecast information.

The forecast request uses latitude and longitude to identify the location.

The application sends parameters such as:

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

The API request is made using:

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)

The application then checks for HTTP errors:

response.raise_for_status()

The JSON response is converted into Python data using:

weather_data = response.json()
📱 Twilio WhatsApp API

The application uses Twilio to send a WhatsApp notification when rain is expected.

A Twilio client is created using the Account SID and Authentication Token:

client = Client(account_sid, auth_token)

The WhatsApp message is sent using:

message = client.messages.create(
    from_="whatsapp:+17372508034",
    body="It's going to rain today. Remember to bring an umbrella",
    to="whatsapp:+918291434538",
    content_sid="HX25161c213d71bb75e073ead06f38fbbd",
)

The application prints the message SID and status:

print(message.sid)
print(message.status)
🔄 Weather Data Flow
             Python Application
                    ↓
          Send Weather Request
                    ↓
           OpenWeatherMap API
                    ↓
              JSON Response
                    ↓
          Extract Forecast Data
                    ↓
        Check Weather Condition
                    ↓
             Is Rain Expected?
                ↙       ↘
              NO         YES
              ↓           ↓
          Do Nothing     Twilio
                           ↓
                    WhatsApp Message
                           ↓
                    ☔ Bring Umbrella
☔ 1. Checking the Weather Forecast

The application retrieves the forecast data from OpenWeatherMap.

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)

response.raise_for_status()
weather_data = response.json()

The returned JSON data contains a list of forecast information.

The program loops through the forecast:

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

The weather condition code is extracted from the API response.

🌧️ 2. Detecting Rain

The application uses the OpenWeatherMap weather condition code to determine whether rain is expected.

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

If the condition code meets the specified condition, the variable:

will_rain

is changed to:

True

This tells the program that a rain alert should be sent.

📲 3. Sending the WhatsApp Alert

The Twilio client is created only when rain is expected.

if will_rain:
    client = Client(account_sid, auth_token)

The application then sends the WhatsApp notification.

message = client.messages.create(
    from_="whatsapp:+17372508034",
    body="It's going to rain today. Remember to bring an umbrella",
    to="whatsapp:+918291434538",
    content_sid="HX25161c213d71bb75e073ead06f38fbbd",
)

The user receives a message reminding them to carry an umbrella.

🔐 4. Using Environment Variables

Sensitive information such as API keys and authentication credentials should not be hardcoded into the Python program.

Instead, the application uses environment variables:

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")

This allows the same Python program to run locally and through GitHub Actions without exposing sensitive credentials.

🔒 5. GitHub Secrets

GitHub Secrets are used to securely store sensitive information required by the application.

The project uses the following secrets:

OWM_API_KEY
ACCOUNT_SID
AUTH_TOKEN

These values are stored inside the GitHub repository's:

Settings
    ↓
Secrets and variables
    ↓
Actions

The secrets are then provided to the Python program through environment variables when the GitHub Action runs.

⚙️ 6. GitHub Actions Automation

GitHub Actions is used to automatically execute the Rain Alert script.

The workflow file is located at:

.github/workflows/scheduled.yml

The workflow performs several steps:

GitHub Actions
      ↓
Checkout Repository
      ↓
Set Up Python
      ↓
Install Dependencies
      ↓
Load GitHub Secrets
      ↓
Run main.py
      ↓
Check Weather
      ↓
Send WhatsApp Alert if Rain is Expected
🕐 7. Scheduling the Script

GitHub Actions uses a cron expression to determine when the script should run.

Example:

schedule:
  - cron: "30 3 * * *"

GitHub Actions schedules use UTC time.

For India:

3:30 AM UTC
      ↓
9:00 AM IST

Therefore, the workflow can be configured to run the Rain Alert automatically every morning.

📝 8. GitHub Actions Workflow

The workflow uses the following structure:

name: Daily Rain Alert

on:
  workflow_dispatch:
  schedule:
    - cron: "30 3 * * *"

jobs:
  rain-alert:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run Rain Alert
        env:
          OWM_API_KEY: ${{ secrets.OWM_API_KEY }}
          ACCOUNT_SID: ${{ secrets.ACCOUNT_SID }}
          AUTH_TOKEN: ${{ secrets.AUTH_TOKEN }}
        run: python main.py

The workflow allows the Python script to run automatically without manually starting the program.

📦 9. Project Dependencies

The project uses a requirements.txt file to specify its external Python libraries.

requests
twilio

When GitHub Actions runs, these dependencies are installed using:

pip install -r requirements.txt

This ensures that the required libraries are available before main.py is executed.

🧪 Example

Suppose the OpenWeatherMap API returns forecast data containing a weather condition indicating rain.

The program processes the data:

Weather Forecast
      ↓
Condition Code
      ↓
Rain Detected
      ↓
will_rain = True
      ↓
Twilio Client
      ↓
WhatsApp Message

The user receives:

It's going to rain today.
Remember to bring an umbrella

If rain is not detected:

Weather Forecast
      ↓
No Rain Detected
      ↓
will_rain = False
      ↓
No Message Sent
🏗️ Project Structure

The application consists of a Python script, dependency file, and GitHub Actions workflow.

main.py

The main Python program.

It:

Retrieves API credentials from environment variables.
Defines the user's location.
Sends a request to OpenWeatherMap.
Retrieves weather forecast data.
Processes the JSON response.
Checks weather condition codes.
Determines whether rain is expected.
Creates a Twilio client.
Sends a WhatsApp notification.
Displays the message SID and status.
requirements.txt

Contains the external Python dependencies:

requests
twilio

This file allows the required libraries to be installed easily both locally and through GitHub Actions.

.github/workflows/scheduled.yml

Contains the GitHub Actions automation workflow.

It manages:

Repository checkout.
Python setup.
Dependency installation.
Secret configuration.
Python script execution.
Daily scheduling.
🔐 Security

This project demonstrates the importance of keeping sensitive credentials outside the source code.

The following information should never be hardcoded:

OpenWeatherMap API Key
Twilio Account SID
Twilio Auth Token

Instead, the project uses:

os.environ.get()

and GitHub Secrets.

This makes the application safer to publish on GitHub.

🚀 Automation Flow
             GitHub Actions
                    ↓
             Scheduled Run
                    ↓
              Start Python
                    ↓
          Install Dependencies
                    ↓
           Load GitHub Secrets
                    ↓
        OpenWeatherMap API Request
                    ↓
             Receive JSON
                    ↓
          Check Weather Codes
                    ↓
             Is it raining?
              ↙          ↘
            NO            YES
            ↓              ↓
        End Script       Twilio
                           ↓
                    WhatsApp Alert
                           ↓
                    ☔ Take Umbrella
📚 Learning Outcome

By completing this project, I learned how to:

Make HTTP requests using requests.
Work with external REST APIs.
Use OpenWeatherMap API.
Use API query parameters.
Retrieve weather forecast data.
Process JSON responses.
Access nested dictionaries and lists.
Work with weather condition codes.
Use conditional statements.
Use loops to process API data.
Integrate Twilio with Python.
Send WhatsApp messages using Twilio.
Create a Twilio client.
Work with environment variables.
Use os.environ.get().
Keep sensitive credentials outside source code.
Use GitHub Secrets.
Create GitHub Actions workflows.
Write YAML configuration files.
Use cron expressions.
Schedule automated Python programs.
Install dependencies using requirements.txt.
Automate Python scripts using GitHub Actions.
Monitor workflow execution.
Read GitHub Actions logs.
Combine multiple APIs and services into one application.
🚀 Future Improvements
Add temperature information to the WhatsApp message.
Include the expected rainfall time.
Include the current weather condition.
Add humidity information.
Add wind speed information.
Send different messages depending on the weather condition.
Add support for multiple locations.
Allow users to configure their own coordinates.
Add a weather forecast summary.
Improve error handling for API failures.
Add logging for failed requests.
Add retry functionality when an API request fails.
Add more detailed Twilio message status handling.
Add a configurable notification time.
Support multiple notification recipients.
Create a web interface for configuring the alert.
Store weather history using a database.
Add temperature and precipitation data to notifications.
🧠 Key Takeaway

This project helped me understand how Python can combine external APIs, JSON data, environment variables, Twilio messaging, and GitHub Actions to create a fully automated application.

The biggest takeaway was learning how to retrieve weather forecast data from an external API, process the returned JSON data, determine whether rain is expected, and automatically send a WhatsApp notification using Twilio.

It also strengthened my understanding of API integration, JSON handling, environment variables, API authentication, GitHub Secrets, YAML workflows, cron scheduling, automation, and cloud-based execution with GitHub Actions.