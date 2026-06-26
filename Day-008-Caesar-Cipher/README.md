# Day 8 - Caesar Cipher

## 📖 Overview

The **Caesar Cipher** is a Python program that encrypts and decrypts messages using the classic Caesar Cipher technique. Each letter in the message is shifted by a user-defined number of positions in the alphabet, allowing users to securely encode or decode text.

This project introduces functions with parameters and return values while reinforcing string manipulation and modular programming concepts.

---

## 🎯 Objective

Create a program that:

* Accepts a message from the user.
* Allows the user to choose between **encoding** or **decoding**.
* Accepts a shift value.
* Encrypts or decrypts the message using the Caesar Cipher algorithm.
* Allows the user to continue using the program until they choose to exit.

---

## 🛠️ Concepts Practiced

* Functions
* Function Parameters
* `while` Loops
* Conditional Statements (`if`, `else`)
* Lists
* String Manipulation
* Modular Programming
* User Input (`input()`)

---

## 📂 Files

```text
Day-008-Caesar-Cipher/
├── main.py
└── art.py
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
Type 'encode' to encrypt or 'decode' to decrypt:
encode

Type your message:
hello world

Type the shift number:
5

Here's the encoded result:
mjqqt btwqi

Type 'yes' if you want to go again. Otherwise type 'no':
```

> **Note:** The encrypted output will vary depending on the message and the shift value entered by the user.

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Create reusable functions with parameters.
* Manipulate strings using indexing and loops.
* Implement a simple encryption and decryption algorithm.
* Organize code into logical, reusable components.
* Build an interactive command-line application.

---

## 🚀 Future Improvements

* Support uppercase and lowercase letters.
* Preserve numbers and special characters during encryption.
* Validate user input for invalid shift values.
* Add additional cipher algorithms such as Vigenère or ROT13.
* Build a graphical user interface (GUI) version.
