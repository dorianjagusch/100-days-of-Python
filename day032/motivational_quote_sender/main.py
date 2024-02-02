import random
import smtplib
import random
import datetime as dt
import dotenv
import os

dotenv.load_dotenv()

EMAIL = "dudebrodude087@gmail.com"
APP_PW = os.getenv("APP_PW")

WEEKDAYS = ["Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]

today = dt.datetime.now().weekday()

if today != 3:
    exit()

try:
    with open("quotes.txt") as data:
        quotes = data.readlines()
except FileNotFoundError:
    print("Create a quotes.txt file with one quote including its author per line")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=APP_PW)
    connection.sendmail(from_addr=EMAIL, to_addrs="dudebrodude087@yahoo.com",
                        msg=f"Subject:Motivational {WEEKDAYS[today]} quote\n\n"
                            f"{random.choice(quotes)}")
