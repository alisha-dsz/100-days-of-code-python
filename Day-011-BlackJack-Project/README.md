# Day 11 - Blackjack (Capstone Project 1)

## 📖 Overview

**Blackjack** is the **first capstone project** of the **100 Days of Code: The Complete Python Pro Bootcamp**. It is a command-line implementation of the classic card game where the player competes against the computer (dealer). The game follows standard Blackjack rules, allowing players to draw cards, calculate scores, and determine the winner based on the closest score to **21** without exceeding it.

This capstone project combines everything learned in the first 11 days of the course, including functions, loops, conditionals, lists, dictionaries, and game logic, to build a complete interactive application.

---

## 🎯 Objective

Create a Blackjack game that:

* Deals two random cards to both the player and the computer.
* Allows the player to draw additional cards or stand.
* Automatically plays the dealer's turn following Blackjack rules.
* Correctly handles Aces as either **11** or **1**.
* Detects a natural Blackjack.
* Determines and displays the winner.

---

## 🛠️ Concepts Practiced

* Functions
* Return Statements
* Lists
* Random Module (`random.choice()`)
* Conditional Statements (`if-elif-else`)
* While Loops
* Boolean Flags
* Score Calculation
* Game Logic
* String Formatting (f-strings)

---

## 📂 Files

```text
Day-011-Blackjack/
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
Do you want to play Blackjack? Type 'y' or 'n': y

Your cards: [10, 7], current score: 17
Computer's first card: 9

Type 'y' to get another card or type 'n' to pass: n

Your final hand: [10, 7], final score: 17
Computer's final cards: [9, 8], final score: 17

DRAW
```

---

## 📚 Learning Outcome

By completing this **first capstone project**, I learned how to:

* Integrate multiple Python concepts into a complete application.
* Simulate a real-world card game using Python.
* Generate random cards using the `random` module.
* Implement Blackjack scoring rules, including Ace value adjustments.
* Organize game logic into reusable functions.
* Manage game flow using loops and conditional statements.
* Compare player and dealer scores to determine the game outcome.
* Build a larger, more structured Python project by combining concepts learned throughout the first 11 days of the bootcamp.

---

## 🚀 Future Improvements

* Implement a full 52-card deck instead of unlimited card selection.
* Prevent duplicate cards from being dealt.
* Add betting and player balance functionality.
* Support multiple players.
* Display cards using ASCII art for a better user experience.
* Keep track of wins, losses, and draws across multiple rounds.
* Build a graphical user interface (GUI) version using Tkinter or Pygame.
