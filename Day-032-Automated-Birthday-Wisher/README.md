# Day 32 - Automated Birthday Wisher

## 📖 Overview

The **Automated Birthday Wisher** is a Python-based email automation project that checks a list of birthdays and automatically sends a personalized birthday email when someone's birthday matches the current date.

The application reads birthday information from a **CSV file**, identifies the person whose birthday is today, randomly selects a birthday letter template, replaces the `[NAME]` placeholder with the person's actual name, and sends the personalized message using **Gmail SMTP**.

The project can also be automated using **GitHub Actions**, allowing the Python script to run automatically every day without manually running the program.

This project was developed as **Day 32** of the **100 Days of Code: The Complete Python Pro Bootcamp**, focusing on CSV data handling, Pandas, datetime operations, file handling, email automation, SMTP, environment variables, and GitHub Actions.

---

## 🎯 Objective

Create an automated Birthday Wisher that:

* Checks the current date.
* Reads birthday information from a CSV file.
* Finds people whose birthday matches today's date.
* Selects a random birthday letter template.
* Replaces `[NAME]` with the birthday person's name.
* Sends a personalized birthday email.
* Uses Gmail SMTP for sending emails.
* Keeps email credentials secure using environment variables.
* Can be scheduled to run automatically using GitHub Actions.

---

## 🛠️ Concepts Practiced

* Python
* Pandas
* DataFrames
* CSV File Handling
* `pandas.read_csv()`
* `DataFrame.to_csv()`
* Data Filtering
* Boolean Conditions
* `&` Operator
* `.iloc[0]`
* Lists
* Dictionaries
* String Manipulation
* `str.replace()`
* File Handling
* `open()`
* `datetime`
* `datetime.now()`
* Random Selection
* `random.choice()`
* SMTP
* `smtplib`
* `starttls()`
* `login()`
* `sendmail()`
* Email Automation
* Environment Variables
* `os.environ.get()`
* GitHub Actions
* GitHub Secrets
* Cron Scheduling
* Automation

---

## 📂 Files

```text
Day-032-Birthday-Wisher/
├── main.py                  # Main Python program
├── birthdays.csv            # Stores birthday information
├── requirements.txt         # External Python dependencies
├── README.md                # Project documentation
└── letter_templates/
    ├── letter_1.txt         # Birthday letter template
    ├── letter_2.txt         # Birthday letter template
    └── letter_3.txt         # Birthday letter template
```

---

## 📦 Libraries Used

### Pandas

Used to read and work with the birthday data stored in the CSV file.

```python
import pandas as pd
```

Pandas is used to:

* Read the CSV file.
* Convert columns into lists.
* Filter birthdays based on the current date.
* Create and save birthday data.

---

### Datetime

Used to get today's date.

```python
import datetime as dt
```

The program uses:

```python
now = dt.datetime.now()
```

to get the current date and then extracts:

```python
day = now.day
month = now.month
```

---

### Random

Used to randomly select one of the birthday letter templates.

```python
import random
```

The program uses:

```python
random.choice(list_of_letters)
```

to select a random letter.

---

### SMTP

Python's built-in `smtplib` module is used to send emails through Gmail's SMTP server.

```python
import smtplib
```

The connection uses:

```python
smtplib.SMTP("smtp.gmail.com", port=587)
```

---

### OS

The `os` module can be used to access environment variables containing sensitive information.

```python
import os
```

For example:

```python
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
```

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the Birthday Wisher project folder.
3. Ensure Python is installed.
4. Install the required dependency:

```bash
pip install -r requirements.txt
```

5. Make sure the `birthdays.csv` file exists.
6. Make sure the `letter_templates` folder contains the letter templates.
7. Configure your email credentials using environment variables.
8. Run the program:

```bash
python main.py
```

---

## 📊 Birthday Data

The birthday information is stored in `birthdays.csv`.

Example:

```csv
name,email,year,month,day
Mum,mum@example.com,1980,8,14
Dad,dad@example.com,1970,9,26
```

The program uses the `day` and `month` columns to determine whether someone has a birthday today.

---

## 📅 1. Checking Today's Birthday

The program first gets the current date:

```python
now = dt.datetime.now()

day = now.day
month = now.month
```

It then compares today's day and month with the birthday data.

```python
birthday_person = data[
    (data.day == day) &
    (data.month == month)
].iloc[0]
```

### What this does:

```text
Today's Day
     +
Today's Month
     ↓
Compare with birthdays.csv
     ↓
Find matching birthday
     ↓
Get the birthday person's information
```

The `&` operator means **AND**, so both the day and month must match.

---

## 📝 2. Selecting a Random Letter

The project contains multiple birthday letter templates:

```python
list_of_letters = [
    "letter_1.txt",
    "letter_2.txt",
    "letter_3.txt"
]
```

A random template is selected using:

```python
random_letter = random.choice(list_of_letters)
```

This means the birthday person can receive a different letter each time.

---

## ✏️ 3. Personalizing the Letter

Each template contains a placeholder:

```text
Dear [NAME],

Happy Birthday!

Wishing you a wonderful day!
```

The program opens the selected template:

```python
with open(
    f"letter_templates/{random_letter}",
    "r"
) as templates:
    content = templates.read()
```

Then `[NAME]` is replaced with the actual person's name:

```python
edited_content = content.replace(
    "[NAME]",
    birthday_person["name"]
)
```

For example:

```text
[NAME]
```

becomes:

```text
Mum
```

Result:

```text
Dear Mum,

Happy Birthday!

Wishing you a wonderful day!
```

---

## 📧 4. Sending the Birthday Email

The project uses Python's `smtplib` module to send the personalized letter.

The basic process is:

```text
Connect to Gmail SMTP
        ↓
Start secure connection
        ↓
Login using email credentials
        ↓
Send email
        ↓
Close connection
```

Example:

```python
connection = smtplib.SMTP(
    "smtp.gmail.com",
    port=587
)

connection.starttls()

connection.login(
    user=my_email,
    password=password
)

connection.sendmail(
    from_addr=my_email,
    to_addrs=birthday_person["email"],
    msg=edited_content
)

connection.close()
```

---

## 🔐 Email Security

Email credentials should **never be hardcoded** directly into the Python program.

Instead of:

```python
my_email = "myemail@gmail.com"
password = "mypassword"
```

environment variables can be used:

```python
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
```

When using GitHub Actions, these values can be stored as **GitHub Secrets**.

Example secrets:

```text
MY_EMAIL
MY_PASSWORD
```

> ⚠️ Gmail requires an **App Password** when using this type of SMTP authentication. Never upload your App Password to GitHub.

---

## 🔄 Application Workflow

```text
                Start Program
                     ↓
              Get Today's Date
                     ↓
              Read birthdays.csv
                     ↓
          Check Day + Month Match
                     ↓
              ┌──────┴──────┐
              ↓             ↓
          Birthday?         No
              ↓             ↓
             Yes           Stop
              ↓
       Find Birthday Person
              ↓
       Select Random Letter
              ↓
       Read Letter Template
              ↓
       Replace [NAME]
              ↓
       Connect to Gmail SMTP
              ↓
           Login Securely
              ↓
          Send Email 📧
              ↓
       Close Connection
```

---

# 🤖 GitHub Actions Automation

The Birthday Wisher can be automated using **GitHub Actions**.

Instead of manually running:

```bash
python main.py
```

every day, GitHub Actions can run the program automatically according to a schedule.

### Basic workflow:

```text
GitHub Actions
      ↓
Runs Python script
      ↓
Checks birthdays.csv
      ↓
Finds today's birthday
      ↓
Creates personalized letter
      ↓
Sends birthday email
```

This allows the Birthday Wisher to run automatically even when the local computer is turned off.

---

## ⏰ Scheduled Runs

GitHub Actions uses a **cron expression** to schedule the program.

For example:

```yaml
cron: "0 9 * * *"
```

This schedules the workflow to run every day at **9:00 AM UTC**.

For India:

```text
IST = UTC + 5:30
```

Therefore, to run at **9:00 AM IST**, the UTC schedule would be:

```yaml
cron: "30 3 * * *"
```

---

## 🔑 GitHub Secrets

Sensitive information should be stored using GitHub Secrets.

Example:

```text
MY_EMAIL
MY_PASSWORD
```

The workflow can provide these secrets to the Python program through environment variables.

This keeps credentials separate from the source code.

---

## 📋 Example

Suppose `birthdays.csv` contains:

```csv
name,email,year,month,day
Mum,mum@example.com,1980,8,14
Dad,dad@example.com,1970,9,26
```

If today is **August 14**, the program finds:

```text
Mum
```

It then selects a random letter template and changes:

```text
Dear [NAME],
```

to:

```text
Dear Mum,
```

The completed birthday message is then sent to:

```text
mum@example.com
```

---

## 🧪 Example Letter

### Template

```text
Dear [NAME],

Happy Birthday!

I hope you have an amazing day filled with happiness and wonderful memories.

Best wishes!
```

### Generated Letter

```text
Dear Mum,

Happy Birthday!

I hope you have an amazing day filled with happiness and wonderful memories.

Best wishes!
```

---

## 📚 Learning Outcome

By completing this project, I learned how to:

* Work with CSV files using Pandas.
* Create and manipulate Pandas DataFrames.
* Filter DataFrames using multiple conditions.
* Use the `&` operator for multiple conditions.
* Understand how `.iloc[0]` retrieves the first matching row.
* Work with Python's `datetime` module.
* Select random items using `random.choice()`.
* Read text files using `open()`.
* Replace placeholders using `.replace()`.
* Automate emails using `smtplib`.
* Connect to Gmail's SMTP server.
* Use `starttls()` for a secure connection.
* Send emails using `sendmail()`.
* Use environment variables for sensitive information.
* Store credentials using GitHub Secrets.
* Schedule Python programs using GitHub Actions.
* Understand basic cron expressions.
* Combine multiple Python concepts into an automated real-world project.

---

## 🚀 Future Improvements

* Add multiple birthday templates with more personalization.
* Add HTML formatting to birthday emails.
* Add birthday reminders before the actual birthday.
* Add support for multiple email providers.
* Add logging to track sent birthday emails.
* Prevent duplicate emails if the workflow runs multiple times.
* Add better error handling for email connection failures.
* Add a web interface for managing birthdays.
* Store birthday information in a database instead of CSV.
* Add timezone-aware scheduling.
* Add automatic testing for the birthday matching logic.
* Improve the GitHub Actions workflow with error notifications.

---

## 🔐 Security Note

This project is created primarily for **learning and automation practice**.

Email credentials and App Passwords should **never be stored directly in the source code or committed to GitHub**.

For a real-world application, credentials should be protected using environment variables or a secure secrets manager.

The project also uses Gmail SMTP and therefore requires appropriate Gmail authentication, such as an App Password where applicable.

---

## 🧠 Key Takeaway

This project helped me understand how Python can be used to create a practical **automation system**.

It combined **Pandas, CSV data, datetime, file handling, random selection, SMTP email automation, environment variables, and GitHub Actions** into one complete project.

The biggest takeaway was learning how a Python script can move from something I run manually to an **automated application that runs on a schedule and performs tasks independently**.
