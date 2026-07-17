# Day 16 - Coffee Machine (Object-Oriented Programming)

## 📖 Overview

The **Coffee Machine (OOP)** project is an object-oriented implementation of the coffee machine simulator developed in the previous project. Instead of managing the entire program in a single file, the application is divided into multiple classes, each responsible for a specific task such as menu management, resource tracking, and payment processing.

This project introduces the fundamentals of **Object-Oriented Programming (OOP)** in Python by demonstrating how classes and objects can be used to build modular, reusable, and maintainable applications.

---

## 🎯 Objective

Create a coffee machine simulator that:

* Displays available coffee options.
* Checks whether sufficient resources are available.
* Processes coin payments.
* Dispenses the selected drink.
* Displays reports for resources and earnings.
* Uses classes to separate different responsibilities.

---

## 🛠️ Concepts Practiced

* Object-Oriented Programming (OOP)
* Classes and Objects
* Object Instantiation
* Methods
* Modules and Imports
* Encapsulation
* `while` Loops
* Conditional Statements (`if`, `elif`, `else`)

---

## 📂 Files

```text
Day-016-Coffee-Machine-OOP/
├── main.py
├── coffee_maker.py
├── menu.py
├── money_machine.py
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

How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0

Here is $0.00 in change.
Here is your latte ☕️. Enjoy!
```

### Example Report

```text
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.50
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Apply Object-Oriented Programming principles in Python.
* Create and use objects from multiple classes.
* Organize code into reusable modules.
* Improve code readability and maintainability through abstraction.
* Build a modular application with clearly defined responsibilities.

---

## 🚀 Future Improvements

* Add new drink options without modifying the core logic.
* Save inventory and earnings to a file or database.
* Implement an ingredient refill feature.
* Add a graphical user interface (GUI).
* Write unit tests for each class.
