# Day 14 - Higher Lower Game

## 📖 Overview

The **Higher Lower Game** is a command-line game where players compare the social media follower counts of two randomly selected personalities, brands, or organizations. The objective is to correctly guess which one has more followers and continue building a high score until an incorrect guess is made.

This project combines functions, dictionaries, loops, and randomization to create an engaging and interactive game.

---

## 🎯 Objective

Create a game that:

* Randomly selects two accounts from a dataset.
* Displays information about each account without revealing follower counts.
* Prompts the player to guess which account has more followers.
* Awards a point for each correct guess.
* Continues the game until the player makes an incorrect guess.

---

## 🛠️ Concepts Practiced

* Functions
* Dictionaries
* Lists
* `while` Loops
* Conditional Statements (`if`, `else`)
* Random Module (`random`)
* Modules and Imports
* User Input (`input()`)
* Game Logic

---

## 📂 Files

```text
Day-014-Higher-Lower-Game/
├── main.py
├── art.py
├── game_data.py
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
Welcome to the Higher Lower Game!

Compare A: Cristiano Ronaldo, a Footballer, from Portugal.

vs

Compare B: Taylor Swift, a Musician, from United States.

Who has more followers? Type 'A' or 'B': A

You're right! Current score: 1

Compare A: Cristiano Ronaldo, a Footballer, from Portugal.

vs

Compare B: Instagram, a Social Media Platform, from United States.
```

> **Note:** The accounts displayed are selected randomly, so each game offers a different experience.

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Work with lists of dictionaries to manage structured data.
* Build reusable functions for formatting and validation.
* Use loops to control game progression.
* Apply randomization to create dynamic gameplay.
* Develop an interactive command-line game with score tracking.

---

## 🚀 Future Improvements

* Prevent duplicate comparisons more efficiently.
* Add multiple difficulty levels.
* Display the highest score achieved.
* Load account data from an external file or API.
* Add a replay option without restarting the program.
