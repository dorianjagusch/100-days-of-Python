import requests
from datetime import datetime
import smtplib
import dotenv
import time
import os

MY_LAT = 60.197053
MY_LONG = 24.923772

dotenv.load_dotenv()

APP_PW = os.getenv("APP_PW")


def iss_within_n_degrees(limit):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return MY_LAT - limit < iss_latitude < MY_LAT + limit and MY_LONG - limit < iss_longitude < MY_LONG + limit


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    return sunrise >= time_now or time_now >= sunset


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

while True:
    time.sleep(60)
    if iss_within_n_degrees(5) or is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="dudebrodude087@gmail.com",
                             password=APP_PW)
            connection.sendmail("dudebrodude087@gmail.com",
                                "dorian.jagusch@gmail.com",
                                msg="ISS Overhead\n\nThe ISS is above you and should be visible"
                                    " under a clear sky.\n\nBest,\nISS Locator")




