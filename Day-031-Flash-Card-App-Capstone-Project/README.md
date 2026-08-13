# Day 31 - Flash Card App (Capstone Project 3)

## 📖 Overview

The **Flash Card Language Learning App** is a **Tkinter GUI application** designed to help users learn and memorize French vocabulary using digital flash cards.

The application displays a French word on the front of a flash card and automatically flips the card after **3 seconds** to reveal its English translation.

Users can indicate whether they know the displayed word by clicking the **✓ button**. Words that are correctly identified are removed from the learning list, while remaining words are stored in a separate CSV file so that the user can continue learning them later.

This project was developed as **Day 31** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on Tkinter GUI development, Pandas, CSV data handling, dictionaries, file handling, random selection, and timed events.

---

## 🎯 Objective

Create a Flash Card application that:

* Displays French vocabulary words.
* Automatically flips cards after 3 seconds.
* Shows the English translation on the back of the card.
* Allows users to mark words they know.
* Removes known words from the learning list.
* Saves remaining words to a CSV file.
* Loads previously saved learning data when the application starts.
* Uses a graphical interface built with Tkinter.
* Provides an interactive and simple language-learning experience.

---

## 🛠️ Concepts Practiced

* Tkinter GUI Development
* Canvas Widget
* Buttons
* Grid Layout Manager
* `PhotoImage`
* Functions
* Global Variables
* Lists
* Dictionaries
* Dictionary Methods
* `random.choice()`
* Pandas
* DataFrames
* CSV Files
* `pd.read_csv()`
* `pd.DataFrame()`
* `to_dict()`
* `to_csv()`
* File Handling
* `try`, `except`, and `else`
* `FileNotFoundError`
* Event Handling
* `window.after()`
* `window.after_cancel()`
* Timed Events
* Data Filtering
* Persistent Data Storage

---

## 📂 Files

```text
Day-031-FlashCard-Language-Learning-App/
├── main.py                     # Main Tkinter application
├── data/
│   ├── french_words.csv        # Original French-English vocabulary
│   └── words_to_learn.csv      # Remaining words to learn
├── images/
│   ├── card_front.png          # Front of the flash card
│   ├── card_back.png           # Back of the flash card
│   ├── wrong.png               # Cross button image
│   └── right.png               # Check button image
└── README.md
```

---

## 📦 Libraries Used

### Tkinter

Used to create the graphical user interface and display the flash cards.

```python
from tkinter import *
```

### Pandas

Used to read vocabulary data from CSV files, convert the data into dictionaries, and save the remaining words.

```python
import pandas as pd
```

### Random

Used to randomly select a French word from the vocabulary list.

```python
import random
```

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Ensure Python is installed.
4. Install Pandas if it is not already installed:

```bash
pip install pandas
```

5. Make sure the `data` and `images` folders are present.
6. Run the program:

```bash
python main.py
```

---

## ⚙️ How It Works

The application follows a simple learning cycle:

```text
Load Vocabulary
       ↓
Display French Word
       ↓
Wait 3 Seconds
       ↓
Flip Card
       ↓
Show English Translation
       ↓
User Decides
   ↙         ↘
Know      Don't Know
  ↓            ↓
Remove      Keep Word
  ↓            ↓
Save CSV    Generate New Card
       ↘      ↙
        New Card
```

---

## 📚 1. Loading Vocabulary Data

When the application starts, it first tries to open:

```text
data/words_to_learn.csv
```

This file contains the words that the user still needs to learn.

The application uses:

```python
try:
    data = pd.read_csv("data/words_to_learn.csv")
```

If the file does not exist, the application loads the original vocabulary:

```text
data/french_words.csv
```

This is handled using:

```python
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
```

This allows the application to continue working even when the user launches it for the first time.

---

## 🎴 2. Creating the Vocabulary Dictionary

The Pandas DataFrame is converted into a list of dictionaries using:

```python
data_dict = data.to_dict(orient="records")
```

The resulting structure looks like:

```python
[
    {"French": "partie", "English": "part"},
    {"French": "histoire", "English": "story"},
    {"French": "chercher", "English": "search"}
]
```

Each dictionary represents one flash card.

---

## 🎲 3. Generating a Random Card

The application randomly selects a word from the vocabulary list using:

```python
random_dict_data = random.choice(data_dict)
```

For example:

```text
French

chercher
```

The selected word is displayed on the front of the flash card.

The card image is also changed to the front-card image:

```python
canvas.itemconfig(card_canvas, image=front_card)
```

---

## ⏱️ 4. Automatic Card Flip

After displaying the French word, the application starts a **3-second timer**:

```python
flip_timer = window.after(3000, func=flip)
```

After 3 seconds, the `flip()` function is called automatically.

The card changes from the front image to the back image:

```python
canvas.itemconfig(card_canvas, image=back_card)
```

The English translation is then displayed.

Example:

```text
French:

chercher


After 3 seconds...


English:

search
```

This creates an interactive flash-card experience.

---

## 🔄 5. Cancelling the Previous Timer

Before generating a new card, the previous timer is cancelled:

```python
window.after_cancel(flip_timer)
```

This prevents multiple timers from running at the same time.

A new timer is then created for the newly generated card.

```text
Generate New Card
       ↓
Cancel Previous Timer
       ↓
Display New French Word
       ↓
Start New 3-Second Timer
       ↓
Flip Card
```

---

## ✅ 6. Marking a Word as Known

When the user knows the displayed word, they click the **✓ button**.

This calls:

```python
is_known()
```

The currently displayed word is removed from the learning list:

```python
data_dict.remove(random_dict_data)
```

This means the word will no longer appear in future flash cards.

---

## 💾 7. Saving Remaining Words

After removing a known word, the remaining vocabulary is converted back into a Pandas DataFrame:

```python
df = pd.DataFrame(data_dict)
```

The remaining words are then saved to:

```text
data/words_to_learn.csv
```

using:

```python
df.to_csv("data/words_to_learn.csv", index=False)
```

This allows the application to remember the user's progress.

---

## ❌ 8. Unknown Words

If the user does not know the word, they can click the **✕ button**.

The application simply generates another card:

```python
cross_btn = Button(image=cross_mark, command=generate_card)
```

The word remains inside the learning list and can appear again in the future.

```text
Don't Know
    ↓
Keep Word
    ↓
Generate New Card
```

---

## 📄 CSV Data Storage

The project uses CSV files to store vocabulary.

### Original Vocabulary

```text
data/french_words.csv
```

This contains the complete list of French-English words.

Example:

```csv
French,English
partie,part
histoire,story
chercher,search
```

### Remaining Vocabulary

```text
data/words_to_learn.csv
```

This contains only the words that the user still needs to learn.

Example:

```csv
French,English
chercher,search
comprendre,understand
possible,possible
```

---

## 🧠 Learning Progress System

The application automatically maintains the user's learning progress.

For example:

```text
Initial Vocabulary
       ↓
100 Words
       ↓
User knows 20 words
       ↓
20 Words Removed
       ↓
80 Words Remaining
       ↓
Saved to words_to_learn.csv
```

When the application is opened again, it loads the remaining 80 words instead of starting from the beginning.

---

## 🖥️ User Interface

The application contains:

```text
        ┌─────────────────────────────┐
        │                             │
        │          French             │
        │                             │
        │          chercher           │
        │                             │
        └─────────────────────────────┘

             ❌             ✅
```

### Front of Card

The front displays:

```text
French

chercher
```

### Back of Card

After 3 seconds:

```text
English

search
```

---

## 🔄 Application Workflow

```text
Start Application
       ↓
Check words_to_learn.csv
       ↓
 ┌─────┴────────┐
 ↓              ↓
Exists        Doesn't Exist
 ↓              ↓
Load File     Load Original
 ↓              ↓
 └──────┬───────┘
        ↓
Convert Data to Dictionary
        ↓
Generate Random Card
        ↓
Display French Word
        ↓
Wait 3 Seconds
        ↓
Flip Card
        ↓
Display English Translation
        ↓
     User Choice
      ↙       ↘
    ❌         ✅
  Unknown     Known
    ↓           ↓
Keep Word    Remove Word
    ↓           ↓
Generate     Save Remaining
New Card       Words
      ↘       ↙
       New Card
```

---

## ⚠️ Error Handling

The project handles situations where the learning file does not exist.

```python
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
```

If `words_to_learn.csv` is unavailable, the application automatically falls back to the original vocabulary file.

This makes the application easier to use for first-time users.

---

## 🧹 Persistent Learning Progress

One of the most useful features of the application is that learning progress is saved between sessions.

For example:

```text
Session 1
   ↓
Learn 10 words
   ↓
Known words removed
   ↓
words_to_learn.csv updated
   ↓
Close Application


Session 2
   ↓
Open Application
   ↓
Load words_to_learn.csv
   ↓
Continue learning remaining words
```

The user therefore does not lose progress when the application is closed.

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Build an interactive GUI using Tkinter.
* Work with the Canvas widget.
* Display and change images dynamically.
* Create buttons using images.
* Use Pandas to work with CSV data.
* Convert DataFrames into dictionaries.
* Work with lists of dictionaries.
* Select random items using `random.choice()`.
* Read CSV files using `pd.read_csv()`.
* Write CSV files using `DataFrame.to_csv()`.
* Handle missing files using `FileNotFoundError`.
* Use `try`, `except`, and `else`.
* Schedule functions using `window.after()`.
* Cancel scheduled events using `window.after_cancel()`.
* Build an automatic card-flipping system.
* Remove learned words from a dataset.
* Maintain persistent learning progress.
* Combine data processing with GUI development.
* Build a practical language-learning application.

---

## 🚀 Future Improvements

Possible improvements include:

* Add more languages besides French and English.
* Allow users to import their own vocabulary.
* Add a difficulty level for words.
* Track learning statistics.
* Display the number of remaining words.
* Add a progress bar.
* Add pronunciation audio.
* Add text-to-speech functionality.
* Add spaced-repetition learning.
* Add a configurable card-flip timer.
* Add a "Restart Learning" option.
* Add categories such as Food, Travel, Animals, and Daily Life.
* Add a search feature for vocabulary.
* Add a database such as SQLite for storing vocabulary.
* Add user profiles and individual learning progress.
* Improve the visual design and animations.
* Add dark/light themes.

---

## 🎯 Key Takeaway

This project helped me understand how **Python can combine GUI development with data processing and persistent storage** to create a practical application.

It strengthened my understanding of **Tkinter, Pandas, CSV files, dictionaries, lists, randomization, file handling, exception handling, and timed events**.

Most importantly, I learned how to build an application that **tracks user progress and remembers that progress between sessions**, making the project more than just a basic flash-card interface.
