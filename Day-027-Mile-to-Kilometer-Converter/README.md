# Day 27 - Mile to Kilometer Converter

## 📖 Overview

The Mile to Kilometer Converter is a simple **Tkinter GUI application** that allows users to quickly convert distances from miles to kilometers. The user enters a distance in miles, clicks the **Calculate** button, and the application instantly displays the equivalent distance in kilometers.

This project was developed as **Day 27** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on creating graphical user interfaces (GUIs) using Tkinter, working with widgets, handling button events, and updating the interface dynamically.

---

## 🎯 Objective

Create a Mile to Kilometer Converter that:

- Accepts a distance in miles.
- Converts the value into kilometers.
- Displays the converted value instantly.
- Provides a simple and user-friendly graphical interface.
- Demonstrates the basics of event-driven programming with Tkinter.

---

## 🛠️ Concepts Practiced

- Tkinter GUI Development
- Labels
- Entry Widgets
- Buttons
- Grid Layout Manager
- Event Handling
- Widget Configuration
- Functions
- User Input
- Type Conversion
- Basic Arithmetic Operations

---

## 📂 Files

```text
Day-027-Mile-to-Kilometer-Converter/
├── main.py          # Main Tkinter application
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Ensure Python is installed.
4. Run the program:

```bash
python main.py
```

---

## ⚙️ How It Works

1. The application opens a Tkinter window.
2. The user enters a distance in **miles**.
3. Clicking the **Calculate** button triggers the conversion function.
4. The entered value is converted from miles to kilometers using the formula:

```text
Kilometers = Miles × 1.609344
```

5. The converted value is rounded and displayed on the interface.

---

## 🖥️ Example

**Input**

```text
Miles: 10
```

**Output**

```text
10 Miles is equal to 16 Kilometres
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

- Build desktop GUI applications using Tkinter.
- Create and position widgets using the Grid layout manager.
- Accept user input through Entry widgets.
- Respond to button click events using callback functions.
- Update Label widgets dynamically.
- Perform mathematical calculations based on user input.
- Organize GUI components for better readability.
- Develop interactive Python applications.

---

## 🚀 Future Improvements

- Display the result with decimal precision instead of rounding to the nearest whole number.
- Add input validation to prevent invalid or empty inputs.
- Show an error message for non-numeric values.
- Support conversions in both directions (Miles ↔ Kilometers).
- Add keyboard support (press Enter to calculate).
- Improve the interface with custom fonts, colors, and styling.
- Add additional unit conversions such as meters, feet, and centimeters.
- Make the window responsive and visually appealing.