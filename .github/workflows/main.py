##################### Extra Hard Starting Project ######################
import os
import pandas as pd
import smtplib
import datetime as dt
import random

my_email = "marina5@gmail.com"
my_password = "12356"
recipient_email = "alishamarinadsouza@gmail.com"


# 1. Update the birthdays.csv
birthday_dict = {
    'name' : ['Alisha', 'Mum', 'Dad'],
    'email' : [f'{recipient_email}','alisha@gmail.com', 'alishamarina@gmail.com'],
    'day' : [6, 14, 26],
    'month' : [9, 8, 9],
    'year' : [2005, 1980, 1970]
}
df = pd.DataFrame(birthday_dict)
df.to_csv("birthdays.csv", index=False)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

with open("birthdays.csv", "r") as birthday_data:
    data = pd.read_csv(birthday_data)
    day_list = data['day'].to_list()
    month_list = data['month'].to_list()
    list_of_letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
    if day in day_list and month in month_list:
        birthday_person = data[(data.day==day) & (data.month==month)].iloc[0]
        recipient_email = birthday_person['email']
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        random_letter = random.choice(list_of_letters)
        with open(f"letter_templates/{random_letter}", "r") as templates:
            content = templates.read()
            edited_content = content.replace("[NAME]", f"{birthday_person['name']}")

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=recipient_email,
                                msg=f"Subject:Happy Birthday!<3\n\n{edited_content}")



