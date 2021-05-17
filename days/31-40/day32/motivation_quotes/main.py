import smtplib
import datetime
import random

EMAIL_ADDRESS = "something@gmail.com"
PASSWORD = "motivation"

day = datetime.datetime.now().weekday()

if day in [0, 5, 6]:
    try:
        with open(r"days\31-40\day32\motivation_quotes\quotes.txt") as file:
            quotes = file.readlines()
    except FileNotFoundError:
        quotes = ["Stay postive and vibe!"]

    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = EMAIL_ADDRESS, password = PASSWORD)
            connection.sendmail(from_addr = EMAIL_ADDRESS, to_addrs = EMAIL_ADDRESS, msg = f"Subject: Your Weekend Motivation\n\n {random.choice(quotes)}")
    
    except Exception as e:
        print(e)



