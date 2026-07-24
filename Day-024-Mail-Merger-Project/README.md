# Day 24 - Mail Merge Project

## 📖 Overview

The **Mail Merge Project** is a Python application that automates the process of generating personalized letters for multiple recipients. It reads a list of names from a text file, replaces a placeholder in a letter template with each recipient's name, and creates a separate personalized letter for every individual.

This project was developed as **Day 24** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on Python file handling, reading and writing text files, working with directories, and automating repetitive tasks. It demonstrates how file operations can be used to create practical real-world automation scripts.

---

## 🎯 Objective

Create a Mail Merge program that:

- Read a list of recipient names from a text file.
- Read a letter template containing a placeholder.
- Replace the placeholder with each recipient's name.
- Generate a personalized letter for every recipient.
- Save each generated letter into a separate output file.

---

## 🛠️ Concepts Practiced

- File Handling in Python
- Reading Text Files
- Writing Text Files
- Relative File Paths
- String Manipulation
- `replace()` Method
- Lists and Loops
- Working with Directories
- Automation using Python
- Clean and Modular Code

---

## 📂 Files

```
Day-024-Mail-Merger-Project/
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt      # Letter template
│   └── Names/
│       └── invited_names.txt        # List of recipient names
├── Output/
│   └── ReadyToSend/                 # Generated personalized letters
├── main.py                          # Mail merge program
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

## 📬 How It Works

- The program reads all recipient names from **`invited_names.txt`**.
- It loads the template letter from **`starting_letter.txt`**.
- The placeholder **`[name]`** is replaced with each recipient's name.
- A new personalized letter is created for every recipient.
- All generated letters are saved inside the **`Output/ReadyToSend`** folder.

---

## 📚 Learning Outcome

By completing this project, I learned how to:

- Read data from text files using Python.
- Write new text files programmatically.
- Automate repetitive document creation tasks.
- Manipulate strings using the `replace()` method.
- Work with relative file paths and folder structures.
- Organize input and output files efficiently.
- Apply Python file handling to solve real-world automation problems.

---

## 🚀 Future Improvements

- Generate personalized PDF letters.
- Read recipient information from CSV or Excel files.
- Send personalized emails automatically.
- Add support for multiple placeholders (e.g., address, date, company).
- Create a graphical user interface (GUI).
- Automatically create output folders if they don't exist.
- Add error handling for missing files or invalid paths.