import dotenv, os
import requests
import pprint

dotenv.load_dotenv()

FLIGHT_SHEET_TOKEN = os.getenv("FLIGHT_SHEET_TOKEN")
FLIGHT_SHEET_ENDPOINT = os.getenv("FLIGHT_SHEET_ENDPOINT")


class DataManager:

    def __init__(self):
        self.headers = {
            "Authorization": FLIGHT_SHEET_TOKEN,
        }
        self.flight_data = None
        self.users = None
        

    def show_data(self):
        response = requests.get(f"{FLIGHT_SHEET_ENDPOINT}/prices", headers=self.headers)
        response.raise_for_status()
        self.flight_data = response.json()["prices"]
        return self.flight_data

    def fill_iata(self, entry):

        to_put = {
            "price": entry
        }

        response = requests.put(f"{FLIGHT_SHEET_ENDPOINT}/{entry['id']}",
                                json=to_put,
                                headers=self.headers)
        response.raise_for_status()

    def get_users(self):
        response = requests.get(f"{FLIGHT_SHEET_ENDPOINT}/users",
                                headers=self.headers)
        response.raise_for_status()
        self.users = response.json()["users"]