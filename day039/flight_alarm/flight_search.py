import dotenv, os
import requests
from flight_data import FlightData
import datetime as dt
import pprint


dotenv.load_dotenv()

HOME_BASE = os.getenv("HOME_BASE")
FLIGHT_API_KEY = os.getenv("FLIGHT_API_KEY")
FLIGHT_SEARCH_ENDPOINT = os.getenv("FLIGHT_SEARCH_ENDPOINT")


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.headers = {
            "apikey": FLIGHT_API_KEY,
        }
        self.endpoint = FLIGHT_SEARCH_ENDPOINT

    def get_iata(self, city):
        params = {
            "term": city,
            "location_types": "city",
        }

        response = requests.get(f"{self.endpoint}/locations/query",
                                params=params,
                                headers=self.headers)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def find_flights(self, destination):
        tomorrow = dt.datetime.now() + dt.timedelta(days=1)
        in_6_months = tomorrow + dt.timedelta(days=(366 / 2))

        search_params = {
            "fly_from": HOME_BASE,
            "fly_to": destination["iataCode"],
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": in_6_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "adults": 1,
            "curr": "EUR",
            "price_to": destination['lowestPrice'],
            "max_stopovers": 0,
            "sort": "price",
        }

        response = requests.get(f"{self.endpoint}/v2/search",
                                headers=self.headers,
                                params=search_params)

        try:
            data = response.json()["data"][0]
        except IndexError:
            ##########################
            search_params["max_stopovers"] = 1
            response = requests.get(
                url=f"{FLIGHT_SEARCH_ENDPOINT}/v2/search",
                headers=self.headers,
                params=search_params,
            )
            try:
                data = response.json()["data"][0]
            except IndexError:
                return
            else:
                pprint.pprint(data)
                flight_data = FlightData(data,
                                         stop_overs=1,
                                         via_city=data["route"][0]["cityTo"])
                return flight_data
        else:
            flight_data = FlightData(data)
            return flight_data
