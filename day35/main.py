import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

API_KEY = os.getenv("API_KEY")
print(API_KEY)
MY_LAT = -42.448300
MY_LONG = 171.214000
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

print(ACCOUNT_SID)
print(AUTH_TOKEN)

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"]

for entry in weather_list:
    weather_id = int(entry["weather"][0]["id"])
    print(weather_id)
    if weather_id < 600:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            body="Pack and umbrella today or you'll get wet!",
            from_='+14788181280',
            to='+358413142220'
        )
        print(message.status)
        break

