#  Day 34 - Quiz App API

## 📖 Overview

The **Quiz App API** is a Python-based interactive quiz application that retrieves quiz questions from an external API and presents them to the user through a graphical user interface.

The application uses the **Open Trivia Database API** to retrieve quiz questions. Each question contains a question statement, a correct answer, and an incorrect answer.

The project uses **Tkinter** to create the graphical user interface, while **Object-Oriented Programming (OOP)** is used to organize the quiz logic and question data.

The application also uses custom **True** and **False** button images to make the quiz interface more interactive and visually appealing.

This project was developed as part of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on **API requests, JSON data, Object-Oriented Programming, Tkinter GUI development, event handling, and application logic**.

---

## 🎯 Objective

Create an interactive quiz application that:

* Retrieves quiz questions from an external API.
* Processes JSON data returned by the API.
* Displays quiz questions using a graphical interface.
* Provides True and False answer buttons.
* Uses custom images for the answer buttons.
* Checks whether the selected answer is correct.
* Updates the user's score.
* Provides visual feedback for correct and incorrect answers.
* Automatically moves to the next question.
* Displays the final score after completing the quiz.

---

## 🛠️ Concepts Practiced

* Python
* Object-Oriented Programming (OOP)
* Classes
* Objects
* Constructors
* Methods
* Functions
* Variables
* Conditional Statements
* `if` / `else`
* Boolean Logic
* Lists
* Dictionaries
* Loops
* API Requests
* REST APIs
* JSON Data
* `requests`
* `response.json()`
* Query Parameters
* Tkinter
* GUI Development
* Canvas
* Buttons
* Labels
* Images in Tkinter
* Event Handling
* Lambda Functions
* String Manipulation
* Score Tracking
* Modular Programming
* Exception Handling

---

## 📂 Files

```text
Day-034-Quiz-App-API/
│
├── main.py                  # Main Python program
├── question_model.py        # Question class
├── quiz_brain.py            # Quiz logic and score management
├── ui.py                    # Tkinter graphical interface
│
├── images/
│   ├── true.png             # True answer button image
│   └── false.png            # False answer button image
│
├── README.md                # Project documentation
└── requirements.txt         # External Python dependencies
```

---

## 📦 Libraries Used

### Requests

The `requests` library is used to communicate with the Open Trivia Database API.

```python
import requests
```

It is used to:

* Send HTTP GET requests.
* Retrieve quiz questions.
* Send API parameters.
* Receive API responses.
* Convert JSON responses into Python data.
* Check HTTP errors using `raise_for_status()`.

---

### Tkinter

Tkinter is Python's built-in GUI library and is used to create the quiz interface.

```python
from tkinter import *
```

It is used to create:

* The application window
* Quiz question display
* Score display
* Canvas
* Answer buttons
* Visual feedback
* Interactive elements

---

## 🖼️ Images

The project includes two image files used for the answer buttons:

```text
images/
├── true.png
└── false.png
```

### `true.png`

Used as the visual button for selecting **True**.

### `false.png`

Used as the visual button for selecting **False**.

These images are loaded into the Tkinter interface and make the answer buttons more visually engaging than standard text buttons.

---

## 🌐 API Used

### Open Trivia Database API

The application retrieves quiz questions from the **Open Trivia Database (OpenTDB)**.

The API returns the questions in JSON format.

The application sends parameters such as:

```python
parameters = {
    "amount": 10,
    "type": "boolean",
}
```

This requests **10 True/False questions**.

The response is retrieved using:

```python
response = requests.get(
    "https://opentdb.com/api.php",
    params=parameters
)

response.raise_for_status()

question_data = response.json()["results"]
```

The returned data contains information such as:

* Question text
* Correct answer
* Incorrect answer
* Category
* Difficulty
* Question type

---

## 🔄 API Data Flow

```text
        Python Application
                ↓
       Send API Request
                ↓
       Open Trivia Database
                ↓
          JSON Response
                ↓
       Extract Questions
                ↓
        Create Question
           Objects
                ↓
          Start Quiz
```

---

## ❓ 1. Creating the Question Model

The project uses a `Question` class to represent individual quiz questions.

For example:

```python
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

Each `Question` object stores:

* The question text
* The correct answer

This keeps the question data organized and makes it easier for the quiz logic to work with individual questions.

---

## 🧠 2. Managing Quiz Logic

The `QuizBrain` class manages the main quiz functionality.

It keeps track of:

* The list of questions
* The current question number
* The user's score
* The correct answer
* Whether more questions remain

For example:

```python
def still_has_questions(self):
    return self.question_number < len(self.question_list)
```

This allows the application to determine when the quiz should continue or finish.

---

## 🔢 3. Tracking the Score

The user's score is updated whenever an answer is submitted.

The program compares the user's answer with the correct answer.

```text
              User Answer
                   ↓
          Compare Answers
             ↙       ↘
         Correct    Incorrect
            ↓           ↓
        Score +1    No Score Change
```

The updated score is displayed in the graphical interface.

---

## 🖥️ 4. Creating the Graphical Interface

The project uses Tkinter to create an interactive quiz interface.

The interface includes:

* Quiz question display
* Score display
* True answer button
* False answer button
* Feedback after answering

The application creates the main window using:

```python
window = Tk()
```

The quiz question is displayed using a Tkinter `Canvas`.

---

## 🖼️ 5. Using True and False Images

Instead of using standard text buttons, the application uses the images stored inside the `images` folder.

```text
images/
├── true.png
└── false.png
```

These images are loaded into Tkinter and displayed as the answer buttons.

Conceptually:

```text
              Quiz Question
                    ↓
          ┌─────────────────┐
          │                 │
          │   Question      │
          │                 │
          └─────────────────┘
                    ↓
           ┌────────┐ ┌─────────┐
           │  TRUE  │ │  FALSE  │
           │  🖼️    │ │   🖼️    │
           └────────┘ └─────────┘
```

When the user clicks one of the images, the selected answer is passed to the quiz logic.

---

## 🖱️ 6. Handling User Answers

The True and False buttons are connected to functions that process the user's answer.

When the user selects an answer:

```text
       User Selects Answer
                ↓
          Check Answer
           ↙       ↘
       Correct    Incorrect
          ↓           ↓
     Score +1     Score Same
           ↘       ↙
          Show Feedback
                ↓
          Next Question
```

The application provides immediate visual feedback.

For example:

```text
Correct Answer
      ↓
Canvas changes color
      ↓
Next question
```

If the answer is incorrect, the application provides corresponding feedback before displaying the next question.

---

## ⏭️ 7. Moving to the Next Question

After the user answers a question, the application moves to the next available question.

The process continues until all questions have been answered.

```text
Question 1
    ↓
Answer
    ↓
Question 2
    ↓
Answer
    ↓
Question 3
    ↓
Answer
    ↓
   ...
    ↓
Last Question
    ↓
Quiz Complete
```

---

## 🏁 8. Completing the Quiz

When all questions have been answered, the quiz ends.

The user's final score is displayed.

For example:

```text
Quiz Complete!

Your final score:
8 / 10
```

This allows the user to see how well they performed.

---

## 🏗️ Project Structure

The application is divided into multiple Python files so that each part of the project has a specific responsibility.

### `main.py`

The main entry point of the application.

It:

* Sends the API request.
* Retrieves the quiz questions.
* Creates `Question` objects.
* Creates the quiz brain.
* Starts the quiz interface.

---

### `question_model.py`

Contains the `Question` class.

The class stores:

* Question text
* Correct answer

It provides a structured way to represent individual quiz questions.

---

### `quiz_brain.py`

Contains the `QuizBrain` class.

It manages:

* Current question
* Question progression
* Answer checking
* Score
* Quiz completion

---

### `ui.py`

Contains the Tkinter user interface.

It manages:

* Application window
* Quiz question display
* Score display
* True button
* False button
* Answer images
* Correct/incorrect feedback
* User interaction

---

### `images/true.png`

Image used for the **True** answer button.

---

### `images/false.png`

Image used for the **False** answer button.

---

## 🧱 Object-Oriented Programming

This project provides practical experience with **Object-Oriented Programming**.

Different classes are responsible for different parts of the application.

```text
Question
   ↓
Stores Question Data

QuizBrain
   ↓
Controls Quiz Logic

QuizInterface
   ↓
Controls Graphical Interface
```

Separating these responsibilities makes the project more organized, readable, and easier to maintain.

---

## 🔐 JSON Data Handling

The project demonstrates how Python can work with structured JSON data returned by an external API.

A simplified API response looks like:

```json
{
    "response_code": 0,
    "results": [
        {
            "type": "boolean",
            "difficulty": "easy",
            "question": "Example question",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        }
    ]
}
```

The program extracts the relevant information and converts the API data into `Question` objects.

---

## 🧪 Example

Suppose the API returns:

```text
Question:
Python was created by Guido van Rossum.

        TRUE        FALSE
```

The user selects an answer using the corresponding image button.

### Correct Answer

```text
Correct! ✓
Score: 1
```

### Incorrect Answer

```text
Wrong! ✗
Score: 0
```

The application then moves to the next question.

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Make HTTP requests using `requests`.
* Work with external REST APIs.
* Use API query parameters.
* Retrieve JSON data.
* Access data inside JSON dictionaries and lists.
* Convert API data into Python objects.
* Create Python classes.
* Create objects using constructors.
* Define and use class methods.
* Apply Object-Oriented Programming principles.
* Separate code into multiple Python modules.
* Build a GUI using Tkinter.
* Create and use Tkinter `Canvas`.
* Create interactive buttons.
* Load images into Tkinter.
* Use images as GUI elements.
* Handle button click events.
* Use lambda functions.
* Compare user answers with correct answers.
* Track a user's score.
* Control the flow of a multi-question application.
* Provide visual feedback.
* Build a complete interactive Python application.

---

## 🚀 Future Improvements

* Add multiple-choice questions.
* Allow users to select quiz categories.
* Add different difficulty levels.
* Allow users to choose the number of questions.
* Add a timer for each question.
* Add a high-score system.
* Store previous scores using JSON or a database.
* Add a restart quiz button.
* Add a question counter.
* Add detailed end-of-quiz statistics.
* Improve the graphical interface.
* Add animations and sound effects.
* Add more Open Trivia Database categories.
* Handle API connection failures more gracefully.
* Add a leaderboard.
* Allow users to enter their name and save their results.

---

## 🧠 Key Takeaway

This project helped me understand how Python can combine **external APIs, JSON data, Object-Oriented Programming, and graphical user interfaces** to create a complete interactive application.

The biggest takeaway was learning how to retrieve quiz questions from an external API, transform the returned JSON data into Python objects, and use those objects to control the quiz logic.

It also strengthened my understanding of **API integration, JSON handling, OOP, Tkinter, event-driven programming, modular Python development, and GUI-based application design**.

