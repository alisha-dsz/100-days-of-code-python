# Day 37 - Habit Tracker with Pixela

## 📖 Overview

The **Habit Tracker** is a Python-based habit tracking application that uses the **Pixela API** to create and maintain a visual graph of daily progress.

The application allows the user to record the amount of time spent on a particular habit each day. The data is sent to the Pixela API and displayed on a graph that visually represents the user's consistency.

The project uses the **Pixela API** to create a user account, create a graph, and add daily pixel values to the graph.

The application uses Python's `requests` library to communicate with the Pixela REST API and send data using HTTP requests.

This project was developed as part of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on API integration, HTTP requests, JSON data, POST requests, headers, parameters, authentication, and date handling.

---

## 🎯 Objective

Create a habit tracking application that:

* Creates a Pixela user account.
* Creates a habit tracking graph.
* Records daily habit progress.
* Sends habit data to the Pixela API.
* Uses HTTP requests to communicate with an external API.
* Uses API authentication through headers.
* Uses query parameters and request bodies.
* Generates a visual habit tracking graph.
* Tracks consistency over multiple days.
* Allows the user to monitor their progress visually.

---

## 🛠️ Concepts Practiced

### Python

* Variables
* Strings
* Dictionaries
* User input
* Functions
* `datetime`
* `strftime()`
* f-strings
* Conditional logic
* HTTP requests
* JSON data
* API integration

### API Integration

* REST APIs
* HTTP POST requests
* HTTP PUT requests
* HTTP GET requests
* Request headers
* Request parameters
* Request body
* JSON payloads
* API authentication
* API endpoints
* Status codes
* Response handling

### API Used

* Pixela API

### Habit Tracking

* Creating a habit graph
* Adding daily values
* Tracking progress
* Visualizing consistency
* Recording data using dates

---

## 📂 Files

```text
Day-037-Habit-Tracker/
│
├── main.py                  # Main Python program
├── requirements.txt         # External Python dependencies
└── README.md                # Project documentation
```

---

## 📦 Libraries Used

### Requests

The `requests` library is used to communicate with the Pixela API.

```python
import requests
```

It is used to:

* Send HTTP requests.
* Send API parameters.
* Send JSON data.
* Send authentication headers.
* Create a Pixela user.
* Create a graph.
* Add daily habit data.
* Receive API responses.

---

## 🌐 API Used

### Pixela API

The application uses the **Pixela API** to create and maintain the habit tracking graph.

The Pixela user endpoint is:

```text
https://pixe.la/v1/users
```

The application sends parameters such as:

```python
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
```

The Pixela API uses the token to authenticate requests associated with the user.

---

## 👤 1. Creating a Pixela User

The program first creates a Pixela user account.

```python
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(
    url=pixela_endpoint,
    json=user_params
)
```

The user information includes:

* Username
* Authentication token
* Terms of service agreement
* Age confirmation

The token acts as the user's authentication credential when communicating with the Pixela API.

---

## 📊 2. Creating the Habit Graph

After creating the user, the application creates a graph to store daily habit data.

The graph endpoint is:

```text
https://pixe.la/v1/users/{username}/graphs
```

The graph parameters contain information such as:

```python
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}
```

The graph configuration defines:

* Graph ID
* Graph name
* Unit of measurement
* Data type
* Graph color

For this project, the graph is used to track the amount of time spent on the habit.

---

## 🔐 3. Authentication Using Headers

Pixela requires authentication when adding and modifying graph data.

The authentication token is sent through the HTTP request headers.

```python
headers = {
    "X-USER-TOKEN": TOKEN
}
```

The header tells Pixela which user is making the request and provides the authentication token required to access the user's graph.

The token should be kept private and should **never be uploaded publicly to GitHub**.

---

## 📚 4. What Are HTTP Headers?

HTTP headers contain additional information about a request or response.

For example:

```python
headers = {
    "X-USER-TOKEN": TOKEN
}
```

The `X-USER-TOKEN` header is used by Pixela for authentication.

Headers can be used to provide information such as:

* Authentication credentials
* Content type
* Authorization information
* Client information

In this project, the header is mainly used to authenticate the request.

---

## 📅 5. Getting the Current Date

The project uses Python's `datetime` module to generate the current date.

```python
from datetime import datetime

date = datetime.now().strftime("%Y%m%d")
```

The date is converted into Pixela's required format:

```text
YYYYMMDD
```

For example:

```text
20261007
```

This date identifies which day the habit value belongs to.

---

## 📝 6. Adding a Habit Value

The application sends the user's daily habit value to the Pixela graph.

The pixel endpoint is:

```text
https://pixe.la/v1/users/{username}/graphs/{graph_id}
```

The request body contains the date and quantity.

```python
pixel_data = {
    "date": date,
    "quantity": "2"
}
```

The request is then sent using:

```python
response = requests.post(
    url=pixel_endpoint,
    json=pixel_data,
    headers=headers
)
```

The value is added to the graph for the selected date.

---

## 📈 7. Recording Daily Progress

The user can enter the amount of time spent on the habit.

For example:

```text
How many hours did you code today?

2
```

The application sends the value to Pixela.

```text
User Input
     ↓
Habit Value
     ↓
Create Date
     ↓
Create JSON Data
     ↓
Add Authentication Header
     ↓
Send POST Request
     ↓
Pixela API
     ↓
Update Graph
```

The graph then displays the recorded value for that date.

---

## 🔄 API Data Flow

```text
                 Python Application
                         ↓
                  Pixela API
                         ↓
                 Create User
                         ↓
                 Create Graph
                         ↓
                  User Input
                         ↓
                  Get Current Date
                         ↓
                  Create JSON Data
                         ↓
              Add Authentication Header
                         ↓
                  Send POST Request
                         ↓
                  Pixela API
                         ↓
                 Store Pixel Value
                         ↓
                  Update Graph
```

---

## 🏗️ Project Structure

### `main.py`

The main Python program.

It:

* Defines the Pixela API endpoints.
* Defines the authentication token.
* Defines the username.
* Creates the Pixela user.
* Creates the habit tracking graph.
* Generates the current date.
* Takes habit information from the user.
* Creates the JSON request body.
* Adds authentication headers.
* Sends the habit data to Pixela.
* Updates the habit tracking graph.

---

### `requirements.txt`

Contains the external Python dependency:

```text
requests
```

The `datetime` module does not need to be installed separately because it is included with Python.

---

### `README.md`

Contains the documentation for the project, including:

* Project overview
* Objective
* Concepts practiced
* API integration
* Authentication
* HTTP headers
* Graph creation
* Habit tracking
* API data flow
* Project structure
* Learning outcomes
* Future improvements

---

## 🔐 Security

The Pixela authentication token should **never be hardcoded in a public GitHub repository**.

Instead of:

```python
TOKEN = "your_token"
```

use environment variables:

```python
import os

TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")
```

A `.env` file can also be used locally with an appropriate environment-variable library.

Make sure `.env` is included in `.gitignore`:

```text
.env
```

**Never commit API tokens, passwords, or other secrets to GitHub.**

---

## 🧪 Example

Suppose the user spends 2 hours coding on a particular day.

```text
User Input
     ↓
     2 hours
     ↓
Current Date
     ↓
20261007
     ↓
Create JSON Request
     ↓
Add Authentication Header
     ↓
Send Request to Pixela
     ↓
Store Habit Value
     ↓
Update Graph
```

The Pixela graph will then display the recorded value for that day.

---

## 🧠 Program Flow

```text
                Start Program
                     ↓
              Define Pixela Data
                     ↓
               Create User
                     ↓
               Create Graph
                     ↓
             Get Current Date
                     ↓
              Get Habit Value
                     ↓
             Create JSON Data
                     ↓
           Add Authentication Header
                     ↓
              Send POST Request
                     ↓
               Pixela API
                     ↓
             Update Graph
                     ↓
                End Program
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Make HTTP requests using `requests`.
* Work with external REST APIs.
* Use the Pixela API.
* Create a Pixela user.
* Create a Pixela graph.
* Send POST requests.
* Send JSON request bodies.
* Use HTTP headers.
* Understand API authentication.
* Work with authentication tokens.
* Generate dates using `datetime`.
* Format dates using `strftime()`.
* Send data to an external API.
* Work with API endpoints.
* Understand API responses.
* Track daily habit progress.
* Visualize data using a graph.
* Understand the difference between request parameters, headers, and request bodies.
* Protect API credentials using environment variables.
* Use `.gitignore` to prevent sensitive information from being uploaded.

---

## 🚀 Future Improvements

Possible improvements for this project include:

* Add multiple habits.
* Allow users to select different habits.
* Create separate graphs for different habits.
* Add an option to update an existing day's value.
* Add an option to delete an incorrect value.
* Store habit data locally.
* Add a graphical user interface.
* Add more detailed progress statistics.
* Calculate weekly and monthly progress.
* Add streak tracking.
* Add reminders for incomplete habits.
* Use environment variables for all credentials.
* Add error handling for failed API requests.
* Handle duplicate entries.
* Handle invalid user input.
* Add logging.
* Create a dashboard for habit progress.

---

## 🔑 Key Takeaway

This project helped me understand how Python can interact with an external **REST API** to create users, configure graphs, authenticate requests, and store daily habit data.

The biggest takeaway was learning how to use the **Pixela API**, send JSON data through HTTP requests, authenticate requests using **HTTP headers**, generate dates dynamically, and visualize daily progress through a habit tracking graph.

It also strengthened my understanding of **API integration, POST requests, JSON data, request headers, authentication tokens, datetime handling, REST APIs, environment variables, and automation with Python**.
