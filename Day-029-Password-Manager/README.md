# Day 29 - Password Manager

## 📖 Overview

The Password Manager is a simple **Tkinter GUI application** that allows users to generate, store, and manage strong passwords for different websites.

The application provides a graphical interface where users can enter a website, email/username, and password. It can also generate a random secure password and automatically copy it to the clipboard.

Before saving the details, the application displays a confirmation message to help prevent accidental entries.

This project was developed as **Day 29** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on Tkinter GUI development, file handling, random password generation, message boxes, and clipboard functionality.

---

## 🎯 Objective

Create a Password Manager that:

* Allows users to enter website details.
* Stores email/username information.
* Generates strong random passwords.
* Automatically copies generated passwords to the clipboard.
* Saves password information to a text file.
* Displays a confirmation message before saving.
* Provides a simple graphical user interface.

---

## 🛠️ Concepts Practiced

* Tkinter GUI Development
* `Entry` widgets
* `Label` widgets
* `Button` widgets
* `Canvas`
* Grid Layout Manager
* Functions
* Global GUI elements
* `random` module
* `random.choice()`
* `random.shuffle()`
* Lists
* String manipulation
* File handling
* `open()`
* Writing to text files
* `messagebox`
* `pyperclip`
* Password generation
* Event-driven programming

---

## 📂 Files

```text
Day-029-Password-Manager/
├── main.py          # Main Tkinter application
├── logo.png         # Lock image used in the interface
├── data.txt         # Stores saved password information
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Make sure Python is installed.
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

## 🖥️ User Interface

The application contains three main input fields:

```text
Website:          [____________________________]

Email/Username:   [____________________________]

Password:         [________________] [Generate Password]

                  [            Add            ]
```

The interface uses **Tkinter's Grid Layout Manager** to organize the labels, entries, and buttons.

---

## 🔐 Password Generator

The **Generate Password** button creates a random password using:

* Uppercase letters
* Lowercase letters
* Numbers
* Symbols

The generated password contains a random number of characters from each category.

### Example

```text
aG7#kP2!xR9$
```

The characters are then shuffled using:

```python
random.shuffle(password_list)
```

This makes the order of the characters unpredictable.

---

## 📋 Automatic Clipboard Copy

After generating a password, the application automatically copies it to the clipboard using:

```python
pyperclip.copy(password)
```

This allows the user to paste the generated password directly into another application.

---

## 💾 Saving Passwords

When the user clicks **Add**, the application first checks whether the required fields have been filled.

```python
if len(website) == 0 or len(password) == 0:
```

If a required field is missing, the application displays:

```text
Oops!

Please fill the required fields.
```

If all required information is available, a confirmation dialog appears.

---

## ⚠️ Confirmation Before Saving

Before saving the password, the application asks the user to confirm the entered details.

Example:

```text
These are the details entered:

Email: example@gmail.com
Password: aG7#kP2!xR9$

Is it OK?
```

The user can choose:

* **OK** → Save the password
* **Cancel** → Do not save the password

This provides an additional safety check before writing information to the file.

---

## 📁 File Handling

The password information is stored in `data.txt`.

The program opens the file in **append mode**:

```python
with open("data.txt", "a") as data:
```

The information is then saved in the following format:

```text
Website | Email/Username | Password
```

Example:

```text
Google | example@gmail.com | aG7#kP2!xR9$
GitHub | example@gmail.com | Xp4!mK8#qL2
```

Using append mode allows new password entries to be added without deleting existing entries.

---

## 🧹 Clearing the Input Fields

After successfully saving the password, the website and password fields are cleared:

```python
website_entry.delete(0, END)
password_entry.delete(0, END)
```

This prepares the application for the next password entry.

---

## 🔄 Application Workflow

The application follows this basic workflow:

```text
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
Check required fields
      ↓
Confirm details
      ↓
Save to data.txt
      ↓
Clear input fields
```

---

## 🧠 How the Password Generator Works

The generator creates three lists:

```python
letters
numbers
symbols
```

It then randomly selects characters from each list.

### Letters

```python
random.choice(letters)
```

### Numbers

```python
random.choice(numbers)
```

### Symbols

```python
random.choice(symbols)
```

The selected characters are combined into one list:

```python
password_list
```

The list is shuffled:

```python
random.shuffle(password_list)
```

Finally, the list is converted into a string:

```python
password = "".join(password_list)
```

The generated password is inserted into the password field:

```python
password_entry.insert(0, password)
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Build a desktop application using Tkinter.
* Create and organize GUI elements using Grid Layout.
* Generate random passwords using Python.
* Work with lists and strings.
* Use `random.choice()` and `random.shuffle()`.
* Handle user input using Entry widgets.
* Display confirmation dialogs using `messagebox`.
* Read and write data using files.
* Use append mode to preserve existing data.
* Copy text to the clipboard using `pyperclip`.
* Clear Entry widgets programmatically.
* Connect buttons to functions using `command`.
* Build an interactive event-driven application.

---

## 🚀 Future Improvements

* Add a **Search Password** feature.
* Add a **Show/Hide Password** button.
* Store passwords in a structured database.
* Encrypt stored passwords.
* Add a master password for accessing the application.
* Add a password strength indicator.
* Prevent duplicate website entries.
* Add a password history feature.
* Add an option to copy saved passwords to the clipboard.
* Add a confirmation before deleting entries.
* Replace the text file with SQLite or MySQL.
* Improve the GUI with custom themes and icons.
* Add an option to edit existing password entries.

---

## 🔒 Security Note

This project is designed as a **learning project** and is not intended for storing real sensitive passwords.

The current version saves passwords as **plain text** inside `data.txt`. For a real-world password manager, passwords should be protected using appropriate encryption and secure authentication mechanisms.

---

## 🧠 Key Takeaway

This project helped me understand how **Python can be used to build practical desktop applications**.

I strengthened my understanding of Tkinter, functions, file handling, randomization, user input, message boxes, and clipboard operations while creating a useful Password Manager application.

The project also introduced an important real-world concept: **handling sensitive information securely**, which can be improved further by using encryption and databases.
