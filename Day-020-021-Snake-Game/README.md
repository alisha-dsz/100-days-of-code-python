# Day 20 & 21 - Snake Game

## 📖 Overview

The **Snake Game** is a classic arcade game built using Python's **Turtle Graphics** module. The player controls a snake that moves around the screen, eating food to grow longer while avoiding collisions with the walls and its own body.

This project was developed over **Day 20 and Day 21** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on **Object-Oriented Programming (OOP)** concepts by organizing the game into separate classes for the snake, food, and scoreboard.

---

## 🎯 Objective

Create a Snake Game that:

- Controls the snake using keyboard input.
- Randomly generates food on the screen.
- Increases the snake's length after eating food.
- Tracks and displays the player's score.
- Detects collisions with walls.
- Detects collisions with the snake's own body.
- Ends the game when a collision occurs.

---

## 🛠️ Concepts Practiced

- Object-Oriented Programming (OOP)
- Classes and Objects
- Inheritance
- Turtle Graphics
- Keyboard Event Handling
- Collision Detection
- Lists
- `for` Loops
- Functions and Methods
- Screen Animation using `tracer()`
- Random Module (`random`)
- Modular Programming
- Game Development Fundamentals

---

## 📂 Files

```text
Day-020-021-Snake-Game/
├── main.py          # Main game loop
├── snake.py         # Snake creation and movement
├── food.py          # Food generation and repositioning
├── scoreboard.py    # Score tracking and display
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

1. Use the **Arrow Keys** to control the snake.
2. Eat the food to increase your score.
3. Each food item increases your score by **1**.
4. The snake grows longer after every food consumed.
5. Avoid colliding with the walls.
6. Avoid colliding with the snake's own body.
7. The game ends when a collision occurs.

---

## 📚 Learning Outcome

By completing this project, I learned how to:

- Build a complete game using Object-Oriented Programming.
- Create and manage multiple classes in a single project.
- Handle keyboard events using Turtle Graphics.
- Detect collisions between game objects.
- Update the game screen efficiently using `screen.tracer()`.
- Keep track of scores and update the display dynamically.
- Organize code into separate Python modules for better readability and maintainability.

---

## 🚀 Future Improvements

- Save the highest score using a file.
- Add multiple difficulty levels.
- Add a pause and resume feature.
- Include sound effects and background music.
- Improve the snake's appearance with custom sprites.
- Add customizable themes and colors.
- Add a start menu and game-over screen with a restart option.
- Display the high score across multiple game sessions.
```