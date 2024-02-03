from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.show_data()

flight_search = FlightSearch()
for iata in sheet_data:

    if iata["iataCode"] == "":
        iata["iataCode"] = flight_search.get_iata(iata["city"])
        data_manager.fill_iata(iata)

sheet_data = data_manager.show_data()
for destination in sheet_data:
    departure_data = flight_search.find_flights(destination)
    if departure_data:
        notification_manager = NotificationManager()
        notification_manager.create_message_from_flight(departure_data)
        notification_manager.send_message()
        data_manager.get_users()
        notification_manager.send_emails_to_users(data_manager.users)
    else:
        print(f"No flights for {destination['city']} ({destination['iataCode']})")
