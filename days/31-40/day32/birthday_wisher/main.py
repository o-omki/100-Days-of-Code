import pandas
import random
import datetime
import os
import smtplib

EMAIL_ADDRESS = "EMAIL"
PASSWORD = "PASSWORD"
letters = []

today = datetime.datetime.now()
today_date = (today.day, today.month)

data = pandas.read_csv(r"days\31-40\day32\birthday_wisher\data\birthdays.csv")
bday_dict = {(row.day, row.month): row for (_, row) in data.iterrows()}

if today_date in bday_dict: 
    bday_person = bday_dict[today_date]
    num_files = len(os.listdir(r"days\31-40\day32\birthday_wisher\data\letter_templates"))
    with open(f"days\\31-40\\day32\\birthday_wisher\data\letter_templates\letter_{random.randint(1, num_files)}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", bday_person.get("name"))

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, PASSWORD)
        connection.sendmail(from_addr = EMAIL_ADDRESS, to_addrs = bday_person.get("email"), msg = f"Subject: Happy Birthday! \n\n {letter}")

        