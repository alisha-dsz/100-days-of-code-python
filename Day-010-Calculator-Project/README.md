Day 10 - Calculator
📖 Overview

The Calculator is a command-line Python application that performs basic arithmetic operations. Users can repeatedly perform calculations using the previous result or start a new calculation without restarting the program.

This project focuses on applying Python functions, dictionaries, loops, and recursion to build an interactive calculator.

🎯 Objective

Create a calculator that:

Accepts two numbers from the user.
Performs addition, subtraction, multiplication, or division.
Displays the result of the selected operation.
Allows users to continue calculating with the previous result.
Starts a new calculation whenever the user chooses.
🛠️ Concepts Practiced
Functions
Return Statements
Dictionaries
Functions as Dictionary Values
User Input (input())
While Loops
Conditional Statements (if-else)
Recursion
String Formatting (f-strings)
📂 Files
Day-010-Calculator/
├── main.py
├── art.py
└── README.md
▶️ How to Run
Clone this repository.
Navigate to the project folder.
Run the program:
python main.py
💻 Sample Output
 _____________________
|  _________________  |
| | Python Calc    | |
| |_________________| |

What's your first number?
20

+
-
*
/

Pick an operation:
*

What's your second number?
5

20.0 * 5.0 = 100.0

Type 'y' to continue calculation with 100.0, or type 'n' to start a new calculation:
📚 Learning Outcome

By completing this project, I learned how to:

Create reusable functions for arithmetic operations.
Store functions inside a dictionary and call them dynamically.
Build an interactive command-line application.
Use loops to keep a program running until the user exits.
Apply recursion to restart the calculator.
Format output using Python f-strings.
🚀 Future Improvements
Add support for advanced mathematical operations (power, square root, modulus, etc.).
Handle invalid inputs and unsupported operators gracefully.
Prevent division-by-zero errors with proper validation.
Keep a history of previous calculations.
Build a graphical user interface (GUI) version using Tkinter or PyQt.
Add scientific calculator functionality.