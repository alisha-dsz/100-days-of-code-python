# Day 7 - Hangman

## 📖 Overview

**Hangman** is a classic word-guessing game built in Python. The player attempts to guess a hidden word one letter at a time while avoiding too many incorrect guesses. The game provides visual feedback using ASCII art and tracks the player's remaining lives until they either guess the word or lose the game.

This project combines multiple Python concepts to create a complete command-line game.

---

## 🎯 Objective

Create a game that:

* Randomly selects a word from a predefined list.
* Accepts letter guesses from the player.
* Reveals correctly guessed letters.
* Tracks incorrect guesses and remaining lives.
* Determines whether the player wins or loses.

---

## 🛠️ Concepts Practiced

* Functions
* `while` Loops
* `for` Loops
* Lists
* Strings
* Conditional Statements (`if`, `elif`, `else`)
* Random Module (`random`)
* Modules and Imports
* Game Logic

---

## 📂 Files

```text
Day-007-Hangman/
├── main.py
├── hangman_words.py
└── hangman_art.py
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
Welcome to Hangman!

Word: _ _ _ _ _

Guess a letter: a

Word: _ a _ _ _
Lives Remaining: 5

Guess a letter: e

Word: _ a _ _ e
Lives Remaining: 5
```

> **Note:** The secret word is randomly selected, so the output will differ each time the game is played.

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Organize code across multiple Python modules.
* Use loops and conditional statements to manage game flow.
* Work with lists and strings to update game state.
* Generate random selections using Python's `random` module.
* Build an interactive command-line game with reusable code.

---

## 🚀 Future Improvements

* Add difficulty levels with varying word lengths.
* Prevent duplicate letter guesses.
* Display previously guessed letters.
* Load words from an external file or API.
* Create a graphical user interface (GUI) version using Tkinter or Pygame.
