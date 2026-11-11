# Day 55 – Flask Guess the Number Game

## 📖 Overview

This project is part of the 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu.

On Day 55, I learned the fundamentals of Flask, a lightweight Python web framework used to build web applications.

I developed an interactive Number Guessing Game using Flask, where users have to guess a randomly generated number between 0 and 9 by entering their guesses directly into the website's URL.

The application generates a random number using Python's `random` module. Based on the number entered by the user, the application displays different messages and GIFs indicating whether the guess is too high, too low, or correct.

The project uses Flask's routing functionality, dynamic URL parameters, Python conditional statements, random number generation, and HTML with inline CSS to create a simple web-based game.

It demonstrates how Python functions can be connected to web routes and how user input from a URL can be processed dynamically to generate different web pages.

## 🎯 Objectives

- Understand the fundamentals of Flask and web development using Python.
- Learn how to create a Flask application.
- Understand the purpose of `Flask(__name__)`.
- Learn how Flask routing works using the `@app.route()` decorator.
- Create different URL routes to handle user requests.
- Understand dynamic URL parameters using `<int:number>`.
- Retrieve and process user input from the URL.
- Generate random numbers using Python's `random` module.
- Use conditional statements to compare numbers.
- Generate dynamic HTML responses using Python.
- Apply inline CSS to style HTML elements.
- Understand how Python can generate dynamic web content.
- Learn how to run a Flask application using `app.run()`.

## 🛠️ Technologies Used

- **Python** – Main programming language used to develop the application.
- **Flask** – Lightweight Python web framework used to create the web application and handle URL routing.
- **random Module** – Generates a random integer between 0 and 9.
- **HTML** – Structures the web pages and displays messages and images.
- **CSS** – Styles the background colours, headings, text, and images.
- **Decorators** – Uses Flask's `@app.route()` decorator to associate URLs with Python functions.
- **GIFs** – Displays animated visual feedback based on the user's guess.

## 📚 Concepts Practiced

| **Concept**            | **Description**                                                         |
| ---------------------- | ----------------------------------------------------------------------- |
| Flask                  | A lightweight Python framework used to develop web applications.        |
| `Flask(__name__)`      | Creates a Flask application instance and identifies the current module. |
| `@app.route()`         | Maps a specific URL to a Python function.                               |
| URL Routing            | Directing different URL requests to their corresponding functions.      |
| Dynamic URL Parameters | Passing values through URLs to Python functions.                        |
| `<int:number>`         | Captures an integer from the URL and passes it as a function argument.  |
| `random` Module        | Generates random numbers using Python's built-in library.               |
| `random.randint()`     | Generates a random integer within the specified inclusive range.        |
| Conditional Statements | Uses `if`, `elif`, and `else` to compare the user's guess.              |
| Comparison Operators   | Uses `>`, `<`, and equality comparisons to determine the result.        |
| Functions              | Defines functions to handle different web requests.                     |
| Return Statement       | Returns HTML content as a response to the browser.                      |
| F-Strings              | Inserts dynamic Python values into HTML content.                        |
| HTML                   | Creates headings, images, and the structure of web pages.               |
| Inline CSS             | Applies styling directly through HTML `style` attributes.               |
| `__name__`             | A special Python variable that identifies the current module.           |
| `__main__`             | Checks whether a Python file is being executed directly.                |
| `app.run()`            | Starts the Flask development server.                                    |
| Debug Mode             | Enables debugging features during application development.              |

## ⚙️ How It Works

**Import Required Modules:** Imports `Flask` from the Flask package and Python's built-in `random` module.

**Create Flask Application:** Initializes the Flask application using `Flask(__name__)`.

**Create the Home Route:** Uses `@app.route('/')` to define the homepage of the application.

**Display the Game Instructions:** The `home_page()` function returns HTML content containing a heading, background colour, and an animated GIF asking the user to guess a number between 0 and 9.

**Generate a Random Number:** Uses `random.randint(0, 9)` to generate a random integer between 0 and 9.

**Create a Dynamic Route:** Uses `@app.route('/<int:number>')` to capture an integer entered by the user through the URL.

**Compare the Guess:** The `guess(number)` function compares the number entered by the user with the randomly generated number.

**Handle a High Guess:** If the entered number is greater than the random number, the application displays a "Too high, try again :(" message with a corresponding GIF and background colour.

**Handle a Low Guess:** If the entered number is smaller than the random number, the application displays a "Too low, try again :(" message with another GIF and background colour.

**Handle a Correct Guess:** If the entered number matches the random number, the application displays a congratulatory message with the correct number and a success GIF.

**Run the Flask Application:** Uses `app.run(debug=True)` to start the development server and make the application accessible through a web browser.

## 💻 Key Implementation Details

### 1. Importing Required Modules

```python
from flask import Flask
import random
```

Imports the required modules for developing the application.

- `Flask` – Imported from the Flask package to create the web application.
- `random` – Python's built-in module used to generate random numbers.

The Flask package needs to be installed separately, whereas the random module comes pre-installed with Python.

### 2. Creating the Flask Application

```python
app = Flask(__name__)
```

Creates an instance of the Flask application.

- `Flask` – The class used to create a Flask web application.
- `__name__` – A special Python variable that contains the name of the current module.

Flask uses this information to locate resources associated with the application, such as templates and static files.

The variable `app` represents the Flask application and is used to define routes and run the web server.

### 3. Creating the Homepage Route

```python
@app.route('/')
def home_page():
    return "<body style='background-color:#E5CD82'>"\
    "<h1 style='text-align:center; font-family:Arial'>Guess a number between 0 and 9</h1>"\
    "<img src='YOUR_GIF_URL' style='display:block; margin:auto; width:400px'>"\
    "</body>"
```

Creates the homepage of the game.

- `@app.route('/')` – Defines the root URL of the application.
- `home_page()` – Function executed when the user visits the homepage.
- `return` – Sends the HTML content back to the browser.
- `<body>` – Defines the main body of the webpage.
- `background-color` – Sets the background colour.
- `<h1>` – Displays the game instructions.
- `<img>` – Displays an animated GIF.
- `text-align:center` – Aligns the heading in the centre.
- `margin:auto` – Helps centre the image when used with block display.

The backslash (`\`) at the end of each line allows the HTML strings to continue across multiple lines.

### 4. Generating a Random Number

```python
random_number = random.randint(0, 9)
```

Generates a random integer between 0 and 9.

The `randint()` function accepts two arguments:

- `0` – Starting number (inclusive).
- `9` – Ending number (inclusive).

The generated number is stored in the variable `random_number`.

This number acts as the correct answer that the user needs to guess.

**Important:** The random number is generated when the Python application starts, so it remains the same until the application is restarted.

### 5. Creating a Dynamic URL Route

```python
@app.route('/<int:number>')
def guess(number):
```

Defines a dynamic route that accepts an integer directly from the URL.

For example:

- `http://127.0.0.1:5000/5`
- `http://127.0.0.1:5000/8`
- `http://127.0.0.1:5000/3`

Here, `<int:number>` tells Flask to capture the number from the URL and convert it into an integer.

The captured value is automatically passed to the `guess()` function through its `number` parameter.

For example, when the user visits `/5`, Flask calls:

```python
guess(5)
```

This allows the application to process different guesses without creating separate routes for every number.

### 6. Checking Whether the Guess Is Too High

```python
if number > random_number:
    return "<body style='background-color:#FFA97B'>"\
    "<h2 style='text-align:center; font-family:Arial; color:red'>Too high, try again :(</h2>"\
    "<img src='YOUR_GIF_URL' style='display:block; margin:auto; width:400px'>"\
    "</body>"
```

Checks whether the number entered by the user is greater than the randomly generated number.

- `if` – Executes the code when the specified condition is true.
- `number > random_number` – Checks whether the user's guess is greater than the correct answer.
- `return` – Returns an HTML response displaying the result.

If the guess is too high, the application displays:

- An orange background.
- A red heading.
- A GIF representing an incorrect high guess.

### 7. Checking Whether the Guess Is Too Low

```python
elif number < random_number:
    return "<body style='background-color:#FFA97B'>"\
    "<h2 style='text-align:center; font-family:Arial; color:red'>Too low, try again :(</h2>"\
    "<img src='YOUR_GIF_URL' style='display:block; margin:auto; width:400px; height:420px'>"\
    "</body>"
```

Checks whether the user's guess is smaller than the randomly generated number.

- `elif` – Checks another condition when the previous `if` condition is false.
- `number < random_number` – Checks whether the entered number is smaller than the correct answer.

If the condition is true, the application displays:

- An orange background.
- A red heading.
- A GIF representing an incorrect low guess.

### 8. Checking Whether the Guess Is Correct

```python
else:
    return "<body style='background-color:#9FED72'>"\
    f"<h2 style='text-align:center; font-family:Arial; color:green'>Hurray, {number} is the correct answer!</h2>"\
    "<img src='YOUR_GIF_URL' style='display:block; margin:auto; width:400px; height:420px'>"\
    "</body>"
```

The `else` block executes when both previous conditions are false.

Since the number is neither greater than nor smaller than the random number, it means the user's guess is correct.

The application displays:

- A green background.
- A green congratulatory heading.
- The correct number using an f-string.
- A success GIF.

The f-string allows the value stored in the `number` variable to be inserted directly into the HTML content.

### 9. Running the Flask Application

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Checks whether the Python file is being executed directly.

- `__name__` – Contains the name of the current module.
- `"__main__"` – Indicates that the file is being executed directly rather than imported into another Python file.
- `app.run()` – Starts the Flask development server.
- `debug=True` – Enables debug mode, which provides detailed error messages and automatically reloads the application when code changes are detected.

After running the program, the application becomes accessible through the local development server:

```text
http://127.0.0.1:5000/
```

## 🎮 Game Flow

| **User Action**                         | **Application Response**                                 |
| --------------------------------------- | -------------------------------------------------------- |
| Opens the homepage                      | Displays instructions to guess a number between 0 and 9. |
| Enters a number greater than the answer | Displays "Too high, try again :(".                       |
| Enters a number smaller than the answer | Displays "Too low, try again :(".                        |
| Enters the correct number               | Displays a congratulatory success message.               |

## 📂 Project Structure

```text
Day-055-Flask-Guess-The-Number/
│
├── main.py
└── README.md
```

**main.py** – Contains the Flask application, homepage route, dynamic guessing route, random number generation, conditional statements, and HTML responses.

**README.md** – Documents the project's functionality, technologies, concepts, and implementation details.

## ▶️ How to Run the Project

**Step 1: Install Flask**

Open the terminal and execute:

```bash
pip install flask
```

**Step 2: Navigate to the Project Folder**

Open the project folder in Visual Studio Code.

**Step 3: Run the Python File**

```bash
python main.py
```

**Step 4: Open the Application**

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

**Step 5: Play the Game**

Enter a number between 0 and 9 directly into the URL.

For example:

```text
http://127.0.0.1:5000/5
```

Continue guessing until you find the correct number.

## 🔐 Important Notes

- Flask must be installed before running the application.
- The application runs on Flask's local development server.
- The random number is generated once when the application starts.
- The generated number remains unchanged until the application is restarted.
- The `<int:number>` route converter accepts integer values from the URL.
- The game uses three possible outcomes: too high, too low, and correct.
- HTML content is returned directly from Python functions.
- GIFs are loaded using external Giphy image URLs, so an internet connection is required to display them.
- Debug mode should only be enabled during development and not in a production environment.
- CSS dimensions should include units such as `px`, for example `width:400px`, to ensure the browser applies the styling correctly.
- The project does not use a database or store individual guesses.

## 🧠 What I Learned

- Understanding the fundamentals of Flask and Python web development.
- Creating a Flask application using `Flask(__name__)`.
- Understanding how Flask's routing mechanism works.
- Using the `@app.route()` decorator to connect URLs with Python functions.
- Creating dynamic routes using URL parameters.
- Understanding the `<int:number>` URL converter.
- Passing values from URLs into Python functions.
- Generating random integers using `random.randint()`.
- Applying conditional statements to process user input.
- Returning HTML content directly from Python functions.
- Using f-strings to generate dynamic HTML content.
- Applying inline CSS to style web pages.
- Understanding the purpose of `__name__` and `__main__`.
- Running a local web application using `app.run()`.
- Understanding how Python backend logic interacts with a web browser.

## 🚀 Future Improvements

- Add an HTML input field and submit button instead of requiring users to enter guesses through the URL.
- Generate a new random number for every game session.
- Add a restart or play-again button.
- Track the number of attempts taken to guess the correct answer.
- Add a maximum number of attempts.
- Display hints to help users guess the correct number.
- Use separate HTML templates with Flask's `render_template()`.
- Move CSS into separate static files for better code organization.
- Add a leaderboard to track the best scores.
- Improve the user interface with responsive styling and animations.
- Add session management to maintain individual game progress.

## 🔑 Key Takeaway

This project strengthened my understanding of Flask and the fundamentals of Python web development.

By building an interactive Number Guessing Game, I learned how to create a Flask application, define URL routes, capture dynamic values from URLs, and return HTML responses based on Python logic.

It also helped me understand how backend Python functions interact with a browser to create dynamic web applications.

This project was a practical introduction to Flask and gave me a foundation for developing more advanced Python-based web applications.
