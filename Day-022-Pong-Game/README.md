# Day 22 - Pong Game

## 📖 Overview

The **Pong Game** is a classic two-player arcade game built using Python's **Turtle Graphics** module. Two players control paddles on opposite sides of the screen, attempting to bounce the ball past their opponent to score points. The game includes real-time paddle movement, collision detection, score tracking, and dynamic ball movement.

This project was developed as part of **Day 22** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on **Object-Oriented Programming (OOP)** by organizing the game into separate classes for the paddles, ball, and scoreboard.

---

## 🎯 Objective

Create a Pong Game that:

* Controls two paddles using keyboard input.
* Moves the ball continuously across the screen.
* Detects collisions between the ball and paddles.
* Detects collisions with the top and bottom walls.
* Tracks and displays each player's score.
* Resets the ball after a player scores.
* Increases the game's pace after successful paddle hits.

---

## 🛠️ Concepts Practiced

* Object-Oriented Programming (OOP)
* Classes and Objects
* Turtle Graphics
* Keyboard Event Handling
* Collision Detection
* Screen Animation using `tracer()`
* Timers and Game Loop
* Functions and Methods
* Conditional Statements
* Modular Programming
* Game Development Fundamentals

---

## 📂 Files

```text
Day-022-Pong-Game/
├── main.py          # Main game loop
├── paddle.py        # Paddle creation and movement
├── ball.py          # Ball movement and collision logic
├── score.py    # Score tracking and display
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

## 🎮 Gameplay

1. Player 1 controls the left paddle using the **W** and **S** keys.
2. Player 2 controls the right paddle using the **Up (↑)** and **Down (↓)** arrow keys.
3. Bounce the ball back using your paddle.
4. Score a point when your opponent misses the ball.
5. The ball resets to the center after each point.
6. The game continues while keeping track of both players' scores.

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Build a complete two-player game using Object-Oriented Programming.
* Create and manage multiple interacting classes.
* Handle keyboard events for multiple players.
* Implement collision detection between moving objects.
* Develop a continuous game loop with smooth screen updates.
* Track and display scores dynamically.
* Organize game logic into separate Python modules for better readability and maintainability.

---

## 🚀 Future Improvements

* Add a start menu and game-over screen.
* Introduce single-player mode with an AI-controlled paddle.
* Add multiple difficulty levels.
* Include sound effects and background music.
* Display the winning player after reaching a target score.
* Add customizable paddle and ball themes.
* Implement a pause and resume feature.
* Improve game visuals with custom sprites and animations.
