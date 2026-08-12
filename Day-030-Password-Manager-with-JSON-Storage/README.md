# Day 30 - Password Manager with JSON Storage

## 📖 Overview

The Password Manager with JSON Storage is a **Tkinter GUI application** designed to help users generate, save, and search for passwords and login credentials.

The application allows users to enter a website and email/username, generate a random password, automatically copy the generated password to the clipboard, and securely store login details locally using a **JSON file**.

Users can also search for previously saved credentials by entering the website name.

This project was developed as **Day 30** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on JSON data handling, file operations, exception handling, Tkinter GUI development, password generation, and working with external libraries.

---

## 🎯 Objective

Create a Password Manager that:

* Generates random passwords.
* Includes letters, numbers, and symbols in generated passwords.
* Automatically copies generated passwords to the clipboard.
* Saves website, email/username, and password information.
* Stores data locally using a JSON file.
* Allows users to search for saved credentials.
* Handles missing data files using exception handling.
* Displays appropriate messages using Tkinter message boxes.
* Provides a simple and user-friendly graphical interface.

---

## 🛠️ Concepts Practiced

* Tkinter GUI Development
* Canvas Widget
* Labels
* Entry Widgets
* Buttons
* Grid Layout Manager
* Functions
* Lists
* List Comprehensions
* Dictionaries
* JSON
* `json.load()`
* `json.dump()`
* File Handling
* `open()`
* `try`, `except`, `else`, and `finally`
* `FileNotFoundError`
* Random Password Generation
* `random.choice()`
* `random.shuffle()`
* String Manipulation
* External Libraries
* `pyperclip`
* Message Boxes
* Event Handling
* Data Searching
* Local Data Storage

---

## 📂 Files

```text
Day-030-Password-Manager-with-JSON-Storage/
├── main.py          # Main Tkinter application
├── data.json        # Stores saved login credentials
├── logo.png         # Logo used in the application
└── README.md
```

---

## 📦 Libraries Used

### Tkinter

Used to create the graphical user interface.

```python
from tkinter import *
from tkinter import messagebox
```

### Random

Used to generate random passwords.

```python
import random
```

### Pyperclip

Used to automatically copy generated passwords to the clipboard.

```python
import pyperclip
```

### JSON

Used to store and retrieve login credentials from a JSON file.

```python
import json
```

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Ensure Python is installed.
4. Install the required external library:

```bash
pip install pyperclip
```

5. Make sure `logo.png` is in the same folder as `main.py`.
6. Run the program:

```bash
python main.py
```

---

## ⚙️ How It Works

The application consists of three main functionalities:

```text
Generate Password
       ↓
Save Credentials
       ↓
Search Credentials
```

---

## 🔑 1. Password Generation

When the user clicks **Generate Password**, the application creates a random password.

The password contains:

* Uppercase letters
* Lowercase letters
* Numbers
* Special symbols

The number of characters is randomized to make each generated password different.

The generated password is then:

1. Displayed in the password entry field.
2. Automatically copied to the clipboard.

Example:

```text
Generated Password:

aF7#kLm2$Qx!
```

The password generation process uses:

```python
random.choice()
random.randint()
random.shuffle()
```

---

## 💾 2. Saving Passwords

The user enters:

```text
Website
Email / Username
Password
```

After clicking **Add**, the application stores the information in `data.json`.

Example:

```json
{
    "example.com": {
        "email": "example@gmail.com",
        "password": "aF7#kLm2$Qx!"
    }
}
```

If the `data.json` file already exists, the application loads the existing data, adds the new credentials, and saves the updated dictionary back to the file.

---

## 📄 JSON Data Storage

The project uses JSON for persistent local storage.

The basic structure is:

```text
Website
   ↓
Email / Username
Password
```

For example:

```json
{
    "github.com": {
        "email": "user@gmail.com",
        "password": "X7#kLm91!"
    },
    "example.com": {
        "email": "user@gmail.com",
        "password": "Ab4$kP92!"
    }
}
```

This allows multiple website credentials to be stored in a single JSON file.

---

## 🔍 3. Searching for Passwords

The **Search** button allows the user to retrieve previously saved credentials.

The user enters the website name and clicks **Search**.

The application checks whether the website exists in `data.json`.

### If the website exists:

The saved email and password are displayed using a message box.

Example:

```text
GitHub

Email: user@gmail.com
Password: X7#kLm91!
```

### If the website does not exist:

The application displays:

```text
Sorry, the details do not exist!
```

---

## ⚠️ Error Handling

The project uses exception handling to manage situations where `data.json` does not exist.

When saving credentials, the application attempts to open the file:

```python
try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
```

If the file does not exist:

```python
except FileNotFoundError:
```

A new `data.json` file is created automatically.

The search functionality also handles the situation where no data file exists and displays an appropriate message to the user.

---

## 📋 Required Field Validation

Before saving credentials, the application checks whether the website and password fields are empty.

```text
Website → Required
Password → Required
Email → Optional
```

If a required field is empty, the application displays:

```text
Oops!

Please fill the required fields.
```

This prevents incomplete credentials from being saved.

---

## 🧹 Clearing Input Fields

After successfully saving credentials, the application clears:

* Website field
* Password field

This allows the user to immediately enter another set of credentials.

---

## 📋 Clipboard Functionality

The project uses the **Pyperclip** library to automatically copy generated passwords.

```python
pyperclip.copy(password)
```

This means the user does not need to manually select and copy the generated password.

The workflow becomes:

```text
Generate Password
       ↓
Password appears in Entry
       ↓
Password copied automatically
       ↓
Paste wherever required
```

---

## 🖥️ Example

### Initial Screen

```text
        🔐

Website:       [________________] [ Search ]

Email/Username:[___________________________]

Password:      [________________] [ Generate Password ]

               [        Add        ]
```

### After Generating a Password

```text
Website:       [github.com]

Email/Username:[user@gmail.com]

Password:      [X7#kLm91!] [ Generate Password ]

               [        Add        ]
```

The generated password is also copied to the clipboard.

---

## 🔄 Application Workflow

```text
             Start Application
                    ↓
             Enter Website
                    ↓
          Enter Email / Username
                    ↓
           Generate Password
                    ↓
        Password copied to clipboard
                    ↓
                Click Add
                    ↓
           Check Required Fields
                    ↓
             Load data.json
                    ↓
       ┌────────────┴────────────┐
       ↓                         ↓
 File Exists                 File Missing
       ↓                         ↓
 Load Existing Data       Create data.json
       ↓                         ↓
       └────────────┬────────────┘
                    ↓
             Save Credentials
                    ↓
             Clear Input Fields
```

---

## 🔎 Search Workflow

```text
Enter Website
      ↓
Click Search
      ↓
Open data.json
      ↓
Check Website
      ↓
 ┌────┴─────┐
 ↓          ↓
Found     Not Found
 ↓          ↓
Show      Show Error
Details   Message
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Build a functional desktop application using Tkinter.
* Generate random passwords using Python.
* Work with lists and list comprehensions.
* Use dictionaries to structure application data.
* Read and write JSON files.
* Store data persistently between program executions.
* Use `json.load()` to retrieve stored data.
* Use `json.dump()` to save data.
* Handle missing files using `FileNotFoundError`.
* Use `try`, `except`, `else`, and `finally`.
* Search through stored dictionary data.
* Validate user input.
* Display information using message boxes.
* Use external Python libraries.
* Copy information to the system clipboard using Pyperclip.
* Combine multiple functions into a complete GUI application.
* Build an application that maintains data after it is closed.

---

## 🚀 Future Improvements

* Add encryption for stored passwords.
* Add a master password for accessing the password manager.
* Add a show/hide password button.
* Add password strength indicators.
* Add delete credential functionality.
* Add edit/update credential functionality.
* Add confirmation before overwriting an existing website.
* Add search suggestions.
* Add case-insensitive website searching.
* Replace JSON storage with SQLite or another database.
* Add automatic backup of stored credentials.
* Improve the overall GUI design.
* Add dark/light themes.
* Add password history.
* Add an option to generate passwords of customizable length.

---

## 🔐 Security Note

This project is designed for **learning purposes**.

The passwords are stored as **plain text inside `data.json`** and are therefore not suitable for storing real sensitive credentials.

A production-level password manager should use proper encryption, secure authentication, and protected storage.

---

## 🧠 Key Takeaway

This project helped me understand how **Python applications can store and retrieve persistent data using JSON files**.

It strengthened my understanding of **file handling, dictionaries, JSON, exception handling, randomization, external libraries, and Tkinter GUI development** while combining these concepts into a practical desktop application.
