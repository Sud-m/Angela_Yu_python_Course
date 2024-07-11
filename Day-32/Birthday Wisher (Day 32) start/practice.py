# import smtplib

# my_email = "sudhanvapython@gmail.com"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password="eodh ydgs xolj rwfo")
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="sudhanvapython@yahoo.com",
#         msg="Subject: Fuck you Sud\n\nHello World!",
#     )
#     connection.close()
# import datetime as dt

# now = dt.datetime.now()
# day = now.weekday()

# birthday = dt.datetime(year = 2003, month = 5, day = 1, hour = 3, minute = 17)
# print(birthday)

import smtplib
import datetime as dt
import random

QUOTES = []
with open(
    "Angela_Yu_python_Course_Git/Day-32/Birthday Wisher (Day 32) start/quotes.txt", "r"
) as file:
    QUOTES = file.read().split("\n")

currentday = dt.datetime.now().weekday()

days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="sudhanvapython@gmail.com", password="eodh ydgs xolj rwfo")
    connection.sendmail(
        from_addr="sudhanvapython@gmail.com",
        to_addrs="sudhanvapython@yahoo.com",
        msg=f"Subject: Happy {days[currentday]}!\n\n{random.choice(QUOTES)}",
    )
    connection.close()
