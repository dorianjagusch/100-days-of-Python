import datetime as dt
import dotenv, os
import requests

dotenv.load_dotenv()

HOME_BASE = os.getenv("HOME_BASE")
FLIGHT_SEARCH_ENDPOINT = os.getenv("FLIGHT_SEARCH_ENDPOINT")
FLIGHT_API_KEY = os.getenv("FLIGHT_API_KEY")


class FlightData:

    def __init__(self, flight_data_raw, stop_overs=0,  via_city=""):
        self.home_base = HOME_BASE
        self.destination = flight_data_raw["route"][0]["cityTo"]
        self.dest_code = flight_data_raw["route"][0]["flyTo"]
        self.departure_time = flight_data_raw["route"][0]["local_departure"]
        self.arrival_time = flight_data_raw["route"][1]["local_arrival"]
        self.price = flight_data_raw["price"]


