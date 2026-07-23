# Day 23 - Turtle Crossing Game (Capstone Project)

## 📖 Overview

The **Turtle Crossing Game** is a Frogger-inspired arcade game built using Python's **Turtle Graphics** module. The player controls a turtle that must safely cross a busy road while avoiding moving cars. Each successful crossing increases the level, making the cars move faster and the game progressively more challenging.

This project was developed as the **Day 23 Capstone Project** of the **100 Days of Code: The Complete Python Pro Bootcamp**, bringing together the concepts learned throughout the previous lessons. It emphasizes **Object-Oriented Programming (OOP)** by organizing the game into separate classes for the player, car manager, and scoreboard while applying collision detection, event-driven programming, and game loop mechanics.

---

## 🎯 Objective

Create a Turtle Crossing Game that:

* Controls the turtle using keyboard input.
* Randomly generates moving cars across the screen.
* Detects collisions between the turtle and cars.
* Increases the game level after each successful crossing.
* Gradually increases the speed of the cars.
* Ends the game when the turtle collides with a car.

---

## 🛠️ Concepts Practiced

* Object-Oriented Programming (OOP)
* Classes and Objects
* Turtle Graphics
* Keyboard Event Handling
* Collision Detection
* Screen Animation using `tracer()`
* Timers and Game Loop
* Random Module (`random`)
* Functions and Methods
* Modular Programming
* Game Development Fundamentals

---

## 📂 Files

```text
Day-023-Turtle-Crossing-Game/
├── main.py          # Main game loop
├── player.py        # Player movement and reset logic
├── car_manager.py   # Car creation, movement, and speed management
├── scoreboard.py    # Level tracking and game over display
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

1. Press the **Up Arrow (↑)** key to move the turtle forward.
2. Avoid colliding with the moving cars.
3. Successfully reach the top of the screen to advance to the next level.
4. Each new level increases the speed of the cars.
5. Continue progressing through increasingly difficult levels.
6. The game ends if the turtle collides with a car.

---

## 📚 Learning Outcome

By completing this capstone project, I learned how to:

* Build a complete arcade-style game using Object-Oriented Programming.
* Design and manage multiple interacting classes.
* Implement collision detection between moving game objects.
* Create progressively increasing game difficulty.
* Handle keyboard events for player movement.
* Develop a smooth game loop with continuous screen updates.
* Organize code into modular Python files for better readability and maintainability.
* Apply multiple Python concepts learned throughout the previous course modules into a single project.

---

## 🚀 Future Improvements

* Add multiple lives before the game ends.
* Introduce different car types with varying speeds.
* Add a start menu and restart option.
* Include sound effects and background music.
* Display the highest level achieved.
* Add collectible power-ups or bonus points.
* Implement multiple lanes with unique traffic patterns.
* Enhance the game with custom graphics and animations.
