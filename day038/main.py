import dotenv
import os
import requests
import datetime as dt

dotenv.load_dotenv()

APP_ENDPOINT = os.getenv("APP_ENDPOINT")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

MY_HEIGHT = os.getenv("MY_HEIGHT")
MY_WEIGHT = os.getenv("MY_WEIGHT")
MY_AGE = os.getenv("MY_AGE")
MY_GENDER = os.getenv("MY_GENDER")


def get_exercise_data():

    exercise_text = input("What exercise(s) have you done?: ")

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }

    parameters = {
        "query": exercise_text,
        "gender": MY_GENDER,
        "height_cm": MY_HEIGHT,
        "weight_kg": MY_WEIGHT,
        "age": MY_AGE,
    }

    response = requests.post(APP_ENDPOINT,
                             json=parameters,
                             headers=headers)
    response.raise_for_status()
    return response.json()["exercises"]


def post_to_google_sheets(exercise_info):

    headers = {
        "Authorization": SHEETY_TOKEN,
        "Content-Type": "application/json",
    }

    print(exercise_info[0]["name"].title())
    print(exercise_info[0]["duration_min"])
    print(exercise_info[0]["nf_calories"])

    for exercises in exercise_info:
        workout_data = {
            "workout": {
                "date": dt.datetime.now().strftime("%d/%m/%Y"),
                "time": dt.datetime.now().strftime("%H:%M:%S"),
                "exercise": exercises["name"].title(),
                "duration": exercises["duration_min"],
                "calories": round(exercises["nf_calories"]),
            }
        }

        response = requests.post(SHEETY_ENDPOINT,
                                 json=workout_data,
                                 headers=headers)
        response.raise_for_status()
        print("Added entry to data")


if __name__ == "__main__":
    post_to_google_sheets(get_exercise_data())
