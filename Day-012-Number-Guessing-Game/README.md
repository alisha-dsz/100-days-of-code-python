# Day 12 - Number Guessing Game

## 📖 Overview

The **Number Guessing Game** is an interactive command-line application where the computer randomly selects a number between **1 and 100**, and the player attempts to guess it within a limited number of attempts. The game offers multiple difficulty levels, each with a different number of allowed guesses.

This project reinforces Python fundamentals by combining functions, conditional logic, loops, and random number generation to build an engaging game.

---

## 🎯 Objective

Create a game that:

* Randomly generates a number between **1 and 100**.
* Allows the player to choose a difficulty level.
* Provides feedback if the guess is too high or too low.
* Limits the number of attempts based on the selected difficulty.
* Ends the game when the player guesses correctly or runs out of attempts.

---

## 🛠️ Concepts Practiced

* Functions
* Function Parameters and Return Values
* Global Constants
* `while` Loops
* Conditional Statements (`if`, `elif`, `else`)
* Random Module (`random`)
* User Input (`input()`)
* Game Logic

---

## 📂 Files

```text
Day-012-Number-Guessing-Game/
├── main.py
├── art.py
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
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Choose the level of difficulty.
Type 'easy', 'medium' or 'hard': medium

You have 6 attempts remaining to guess the number.
Make a guess: 50

Too low.
Guess again.

You have 5 attempts remaining to guess the number.
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Organize a program into reusable functions.
* Use constants to manage game settings.
* Generate random numbers using Python's `random` module.
* Control program flow using loops and conditional statements.
* Build an interactive command-line game with multiple difficulty levels.

---

## 🚀 Future Improvements

* Validate user input for invalid difficulty levels.
* Handle non-numeric input gracefully.
* Allow players to replay the game without restarting the program.
* Display previous guesses to help the player.
* Add hints based on the proximity of the guess to the correct answer.
