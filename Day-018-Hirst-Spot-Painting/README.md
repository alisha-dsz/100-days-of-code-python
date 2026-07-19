# Day 18 - Hirst Spot Painting (Turtle Graphics)

## 📖 Overview

The Hirst Spot Painting project recreates the famous dot paintings inspired by artist Damien Hirst using Python's Turtle Graphics. The program extracts the dominant colors from an image and uses them to generate a colorful grid of randomly colored dots.

This project focuses on working with RGB colors, external Python libraries, loops, functions, and Turtle graphics to create generative artwork.

---

## 🎯 Objective

Create a Python program that:

- Extracts dominant colors from an image using the `colorgram` library.
- Stores the extracted RGB values in a list.
- Randomly selects colors from the palette.
- Draws a 10 × 10 grid of evenly spaced colored dots using Turtle Graphics.
- Produces artwork inspired by Damien Hirst's spot paintings.

---

## 🛠️ Concepts Practiced

- Python Turtle Graphics
- Functions
- RGB Color Values
- Python Modules
- External Libraries (`colorgram.py`)
- Lists & Tuples
- Loops
- Random Module
- Coordinate Movement
- Pen Control (`penup()`)

---

## 📂 Files

```
Day-018-Hirst-Spot-Painting/
├── main.py
├── spot-painting.jpg
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Install the required package:

```bash
pip install colorgram.py
```

4. Run the program:

```bash
python main.py
```

---

## 💻 How It Works

1. Extracts the dominant colors from the reference image using `colorgram.py`.
2. Stores the RGB values as tuples in a list.
3. Randomly selects a color for each dot.
4. Uses Turtle Graphics to draw a 10 × 10 grid with evenly spaced colored dots.
5. Produces a vibrant Hirst-inspired spot painting.

---

## 📸 Sample Output

The program generates artwork consisting of **100 colorful dots** arranged in a neat 10 × 10 grid, with each dot randomly colored from the extracted palette.

---

## 📚 Learning Outcome

By completing this project, I learned how to:

- Use external Python libraries to process images.
- Work with RGB color values in Turtle Graphics.
- Create reusable functions.
- Draw graphics using loops and coordinate movement.
- Generate artwork through procedural programming.
- Organize code for readability and maintainability.

---

## 🚀 Future Improvements

- Allow users to choose the grid size.
- Let users upload their own reference image.
- Generate larger or smaller dot paintings.
- Save the artwork as an image.
- Add animation while drawing the painting.
- Create different artistic patterns using the extracted color palette.