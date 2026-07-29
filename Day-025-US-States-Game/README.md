# Day 25 - U.S. States Game

## 📖 Overview

The **U.S. States Game** is an interactive geography quiz built using **Python**, **Turtle Graphics**, and **Pandas**. The player is presented with a blank map of the United States and must correctly guess the names of all 50 states. Every correct guess is displayed at its corresponding location on the map, providing an engaging way to learn U.S. geography.

If the player chooses to exit the game before guessing all the states, the program automatically generates a **`states_to_learn.csv`** file containing all the states that were missed. This allows users to review and practice the remaining states later.

This project was developed as **Day 25** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on data analysis with Pandas, CSV file handling, and integrating datasets with graphical user interfaces using Turtle Graphics.

---

## 🎯 Objective

Create a U.S. States Guessing Game that:

- Display a blank map of the United States.
- Accept state names as user input.
- Check whether the entered state is correct.
- Display correctly guessed states at their respective map locations.
- Keep track of the player's progress.
- Generate a list of unguessed states for future learning.

---

## 🛠️ Concepts Practiced

- Pandas DataFrames
- Reading CSV Files
- Writing CSV Files
- Data Filtering
- Lists and Loops
- Turtle Graphics
- User Input with `textinput()`
- Working with Coordinates
- Data Manipulation
- Interactive GUI Programming

---

## 📂 Files

```text
Day-025-U.S.-States-Game/
├── blank_states_img.gif          # Blank U.S. map
├── 50_states.csv                 # State names and coordinates
├── main.py                       # Main game program
├── states_to_learn.csv           # Generated after exiting (if applicable)
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Install the required library:

```bash
pip install pandas
```

4. Run the program:

```bash
python main.py
```

---

## 🗺️ How It Works

- The program loads a blank map of the United States.
- State names and their coordinates are read from **`50_states.csv`**.
- The player enters the name of a U.S. state.
- If the answer is correct, the state's name appears at its correct location on the map.
- The score updates with every correct guess.
- If the player types **Exit**, the program creates a **`states_to_learn.csv`** file containing all the states that were not guessed.
- The game ends when all 50 states have been correctly identified or the player exits.

---

## 📚 Learning Outcome

By completing this project, I learned how to:

- Read and manipulate CSV files using Pandas.
- Filter DataFrames to retrieve specific information.
- Convert DataFrame columns into Python lists.
- Display data dynamically using Turtle Graphics.
- Collect and validate user input.
- Generate new CSV files programmatically.
- Combine data processing with graphical interfaces.
- Build an interactive educational application using Python.

---

## 🚀 Future Improvements

- Add hints for difficult states.
- Include a countdown timer.
- Track high scores.
- Highlight incorrect guesses.
- Add multiple difficulty levels.
- Support maps of different countries.
- Add animations and sound effects.
- Allow users to resume unfinished games.