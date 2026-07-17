# Day 15 - Coffee Machine

## 📖 Overview

The **Coffee Machine** is a command-line application that simulates the functionality of a real coffee vending machine. Users can order different types of coffee, insert coins for payment, receive change when applicable, and view the machine's available resources and total earnings.

This project combines multiple Python concepts to build a complete application with resource management, payment processing, and user interaction.

---

## 🎯 Objective

Create a coffee machine simulator that:

* Offers multiple coffee options.
* Checks whether sufficient resources are available.
* Accepts coin input and processes payments.
* Returns change when necessary.
* Updates ingredient inventory after each successful order.
* Displays a report of available resources and money collected.
* Allows the machine to be turned off.

---

## 🛠️ Concepts Practiced

* Dictionaries
* Functions
* Nested Dictionaries
* `while` Loops
* Conditional Statements (`if`, `elif`, `else`)
* User Input (`input()`)
* Arithmetic Operations
* Resource Management
* Program Flow Control

---

## 📂 Files

```text
Day-015-Coffee-Machine/
├── main.py
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

## 💻 Sample Output

```text
What would you like? (espresso/latte/cappuccino): latte

Please insert coins.
How many quarters? 10
How many dimes? 0
How many nickels? 0
How many pennies? 0

Here's $0.00 in change.
Here's your latte. Enjoy!
```

### Example Report

```text
Water : 100ml
Milk : 50ml
Coffee : 76g
Money : $2.50
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Store and manipulate structured data using nested dictionaries.
* Build reusable functions for resource management and payment processing.
* Simulate a real-world system using Python.
* Manage program state across multiple user interactions.
* Apply logical decision-making to validate resources and transactions.

---

## 🚀 Future Improvements

* Validate invalid drink selections and coin inputs.
* Improve monetary calculations using Python's `decimal` module.
* Refactor the project using Object-Oriented Programming (OOP).
* Add the ability to refill ingredients without restarting the machine.
* Store sales and inventory data in a file for persistence.
