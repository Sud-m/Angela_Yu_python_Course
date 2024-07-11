##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import csv
import pandas as pd
import random

# 1. Update the birthdays.csv
with open(
    "Angela_Yu_python_Course_Git/Day-32/birthdays.csv", "a", newline=""
) as birthdates:
    people = [
        ["Nanda", "sudhanvapython@yahoo.com", 1974, 5, 27],
        ["Sandhya", "sudhanvapython@yahoo.com", 1977, 10, 7],
        ["Avni", "sudhanvapython@yahoo.com", 2009, 1, 16],
        ["Sudhanva", "sudhanvapython@yahoo.com", 2003, 5, 1],
        ["test", "sudhanvapython@yahoo.com", 2000, 7, 10],
    ]
    writer = csv.writer(birthdates)
    # writer.writerows(people)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
data = pd.read_csv("Angela_Yu_python_Course_Git/Day-32/birthdays.csv")

if data["month"].to_list().index(now.day) == data["day"].to_list().index(now.month):

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(
        f"Angela_Yu_python_Course_Git/Day-32/letter_templates/letter_{random.randint(1,3)}.txt",
        "r",
    ) as file:

        # 4. Send the letter generated in step 3 to that person's email address.
        contents = file.read()
        contents = contents.replace(
            "[NAME]", data["name"][data["month"].to_list().index(now.day)]
        )

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(
                user="sudhanvapython@gmail.com", password="eodh ydgs xolj rwfo"
            )
            connection.sendmail(
                from_addr="sudhanvapython@gmail.com",
                to_addrs="sudhanvapython@yahoo.com",
                msg=f"Subject: Happy Birthday!\n\n{contents}",
            )
            connection.close()
