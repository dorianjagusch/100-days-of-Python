##################### Extra Hard Starting Project ######################

import pandas as p
import random
import datetime as dt
import smtplib
import sys
import dotenv
import os

dotenv.load_dotenv()

EMAIL = "dudebrodude087@gmail.com"
APP_PW = os.getenv(dotenv)

try:
    birthdays = p.read_csv("birthdays.csv").to_dict(orient="records")
except FileNotFoundError:
    print("You don't have a list of birthdays")
    sys.exit(2)

for entry in birthdays:
    bday = dt.datetime(year=entry["year"], month=entry["month"], day=entry["day"])
    today = dt.datetime.now()

    if bday.month != today.month or bday.day != today.day:
        continue

    index = random.randint(1, 3)

    try:
        with open(f"letter_templates/letter_{index}.txt") as letter:
            content = letter.read().replace("[NAME]", entry["name"])
            content = content.replace("Angela", "Dorian")
    except FileNotFoundError:
        content = f"Happy Birthday, {entry['name']}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=APP_PW)
        connection.sendmail(from_addr=EMAIL, to_addrs=entry["email"],
                            msg="Subject: Happy Birthday!!\n\n"
                                f"{content}")





