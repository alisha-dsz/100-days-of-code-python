# Day 9 - Secret Auction Program

## 📖 Overview

The **Secret Auction Program** is a command-line application that simulates a silent auction. Multiple participants can place bids without seeing each other's amounts, and once all bids have been collected, the program determines and announces the highest bidder.

This project introduces dictionaries in Python and demonstrates how they can be used to store and process key-value data efficiently.

---

## 🎯 Objective

Create a program that:

* Collects bidder names and bid amounts.
* Stores bid information using a dictionary.
* Allows multiple participants to enter bids.
* Determines the highest bidder.
* Displays the winner and the winning bid.

---

## 🛠️ Concepts Practiced

* Dictionaries
* Functions
* `while` Loops
* Conditional Statements (`if`, `else`)
* User Input (`input()`)
* Key-Value Data Storage
* Iteration over Dictionaries

---

## 📂 Files

```text
Day-009-Secret-Auction/
├── main.py
└── art.py
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
Welcome to the Secret Auction Program!

What is your name? Alice
What's your bid? $250
Are there any other bidders? yes

What is your name? Bob
What's your bid? $320
Are there any other bidders? no

The winner is Bob with a bid of $320.
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Store and manage data using dictionaries.
* Iterate through key-value pairs to find the highest value.
* Create reusable functions to organize program logic.
* Build an interactive command-line application that handles multiple users.

---

## 🚀 Future Improvements

* Validate user input for bid amounts.
* Handle duplicate bidder names.
* Save auction results to a file for future reference.
* Support multiple auction rounds in a single session.
* Display a summary of all bids after the auction ends.
