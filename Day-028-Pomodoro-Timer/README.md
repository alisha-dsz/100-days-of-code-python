# Day 28 - Pomodoro Timer

## 📖 Overview

The Pomodoro Timer is a simple **Tkinter GUI application** designed to help users manage their study or work sessions using the **Pomodoro Technique**. The application alternates between focused work sessions, short breaks, and longer breaks after several sessions.

The timer displays the remaining time, automatically switches between different session types, and adds a **✓ checkmark** for every completed work session.

This project was developed as **Day 28** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on Tkinter GUI development, timers, functions, global variables, and event-driven programming.

---

## 🎯 Objective

Create a Pomodoro Timer that:

* Provides focused work sessions.
* Automatically starts short breaks after work sessions.
* Provides a longer break after multiple sessions.
* Displays the remaining time in minutes and seconds.
* Tracks completed work sessions using checkmarks.
* Allows the user to start and reset the timer.
* Provides a simple and visually appealing graphical interface.

---

## 🛠️ Concepts Practiced

* Tkinter GUI Development
* Canvas Widget
* Labels
* Buttons
* Grid Layout Manager
* `window.after()`
* Timer and Countdown Logic
* Functions
* Global Variables
* Conditional Statements
* Modulo Operator (`%`)
* `math.floor()`
* String Formatting
* Widget Configuration
* Event Handling
* Automatic Function Calls
* Basic State Management

---

## 📂 Files

```text
Day-028-Pomodoro-Timer/
├── main.py          # Main Tkinter application
├── tomato.png       # Tomato image used in the timer
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Ensure Python is installed.
4. Make sure `tomato.png` is in the same folder as `main.py`.
5. Run the program:

```bash
python main.py
```

---

## ⚙️ How It Works

The timer follows a repeating Pomodoro cycle.

### 1. Focus Session

When the user clicks **Start**, the first session begins with a **25-minute focus session**.

```text
Lock In → 25 minutes
```

### 2. Short Break

After completing a focus session, the timer automatically starts a **5-minute short break**.

```text
Reset → 5 minutes
```

### 3. Repeated Sessions

The application continues alternating between focus sessions and short breaks.

### 4. Long Break

After completing four focus sessions, the application starts a **20-minute long break**.

```text
Recharge → 20 minutes
```

The cycle then continues.

---

## ⏱️ Timer Cycle

```text
Lock In   → 25 min
     ↓
Reset     → 5 min
     ↓
Lock In   → 25 min
     ↓
Reset     → 5 min
     ↓
Lock In   → 25 min
     ↓
Reset     → 5 min
     ↓
Lock In   → 25 min
     ↓
Recharge  → 20 min
     ↓
Repeat
```

---

## ✅ Session Tracking

The application keeps track of completed work sessions using the `reps` variable.

Every time a work session is completed, a checkmark is added to the screen.

For example:

```text
✓ ✓ ✓
```

This provides a simple visual representation of how many focused sessions have been completed.

---

## 🔄 Reset Function

The **Reset** button:

* Stops the current countdown.
* Resets the number of sessions.
* Changes the timer display back to `00:00`.
* Resets the session label to `"Timer"`.
* Removes all completed-session checkmarks.

This allows the user to start a fresh Pomodoro cycle.

---

## 🖥️ Example

### Initial Screen

```text
        Timer

       🍅
      00:00

   [ Start ] [ Reset ]
```

### During a Focus Session

```text
       Lock In

       🍅
      24:59

   [ Start ] [ Reset ]
```

### After Completing Sessions

```text
       Lock In

       🍅
      25:00

        ✓ ✓
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Build an interactive desktop application using Tkinter.
* Create a countdown timer using `window.after()`.
* Schedule functions to run after a specific amount of time.
* Use global variables to maintain application state.
* Use the modulo operator to determine different timer stages.
* Automatically switch between work and break sessions.
* Update Tkinter widgets dynamically.
* Use a Canvas to display images and text.
* Track completed sessions using checkmarks.
* Create a reset mechanism for a running timer.
* Combine multiple functions to build a complete GUI application.
* Understand event-driven programming in Python.

---

## 🚀 Future Improvements

* Add customizable work and break durations.
* Add sound notifications when a session ends.
* Add a pause/resume button.
* Allow users to skip a break.
* Add a session counter.
* Save daily productivity statistics.
* Add different themes and color schemes.
* Add keyboard shortcuts for Start, Pause, and Reset.
* Add desktop notifications when a session is completed.
* Allow users to set their own number of focus sessions before a long break.
* Store completed sessions using a database or file.
* Add productivity statistics such as total focus time and completed sessions.

---

## 🧠 Key Takeaway

This project helped me understand how **GUI applications can respond to events and perform actions automatically over time**. It also strengthened my understanding of functions, conditionals, variables, and Tkinter's `after()` method while building a practical productivity application.
