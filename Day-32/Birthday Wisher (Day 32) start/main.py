import smtplib
import datetime as dt
import csv
import pandas as pd
import random

# 1. Update the birthdays.csv
with open("Angela_Yu_python_Course_Git/Day-32/Birthday Wisher (Day 32) start/birthdays.csv", "a", newline='') as birthdates:
    people = [
        ["Nanda", "sudhanvapython@yahoo.com", 1974, 5, 27],
        ["Sandhya", "sudhanvapython@yahoo.com", 1977, 10, 7],
        ["Avni", "sudhanvapython@yahoo.com", 2009, 1, 16],
        ["Sudhanva", "sudhanvapython@yahoo.com", 2003, 5, 1],
        ["test", "sudhanvapython@yahoo.com", 2000, 7, 10],
    ]
    writer = csv.writer(birthdates)
    writer.writerows(people)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
data = pd.read_csv("Angela_Yu_python_Course_Git/Day-32/Birthday Wisher (Day 32) start/birthdays.csv")

# Find today's birthdays
today_birthdays = data[(data['month'] == now.month) & (data['day'] == now.day)]

if not today_birthdays.empty:
    for index, row in today_birthdays.iterrows():
        name = row['name']
        email = row['email']
        
        # 3. Pick a random letter from letter templates and replace [NAME] with the person's actual name
        letter_path = f"Angela_Yu_python_Course_Git/Day-32/Birthday Wisher (Day 32) start/letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(letter_path, "r") as file:
            contents = file.read()
            contents = contents.replace("[NAME]", name)
        
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="sudhanvapython@gmail.com", password="eodh ydgs xolj rwfo")
            connection.sendmail(
                from_addr="sudhanvapython@gmail.com",
                to_addrs="sudhanvapython@yahoo.com",
                msg=f"Subject: Happy Birthday!\n\n{contents}"
            )
            connection.close()
