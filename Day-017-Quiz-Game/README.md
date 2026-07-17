# Day 17 - Quiz Game (Object-Oriented Programming)

## 📖 Overview

The **Quiz Game** is a command-line application that presents the user with a series of True/False questions. The questions are loaded from a dataset, converted into objects, and managed by a quiz engine that tracks the player's progress and score.

This project builds upon Object-Oriented Programming (OOP) concepts by separating the application into multiple classes, making the code more organized, reusable, and maintainable.

---

## 🎯 Objective

Create a quiz application that:

* Loads questions from a data source.
* Creates question objects using a custom class.
* Displays questions one at a time.
* Accepts user answers.
* Keeps track of the player's score.
* Displays the final score when the quiz is complete.

---

## 🛠️ Concepts Practiced

* Object-Oriented Programming (OOP)
* Classes and Objects
* Constructors (`__init__`)
* Modules and Imports
* Lists of Objects
* Loops
* User Input (`input()`)
* Data Encapsulation

---

## 📂 Files

```text
Day-017-Quiz-Game/
├── main.py
├── data.py
├── question_model.py
├── quiz_brain.py
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Run the program:

```bash
python main.py
```

---

## 💻 Sample Output

```text
Q.1: A slug's blood is green. (True/False): true
You got it right!
The correct answer was: True.
Your current score is: 1/1

Q.2: The loudest animal is the African Elephant. (True/False): false
You got it right!
The correct answer was: False.
Your current score is: 2/2
```

### Final Output

```text
You've completed the quiz!

Your final score was: 9/10
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Design applications using Object-Oriented Programming.
* Create custom classes to model real-world data.
* Store and manage collections of objects.
* Separate application logic into multiple modules.
* Improve code organization and maintainability through encapsulation.

---

## 🚀 Future Improvements

* Add multiple-choice questions.
* Randomize question order.
* Include different difficulty levels.
* Load questions from an online API.
* Display high scores and save quiz history.
* Build a graphical user interface (GUI) version.
