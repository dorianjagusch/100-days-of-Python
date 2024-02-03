import dotenv, os
from twilio.rest import Client
import datetime as dt
import smtplib

dotenv.load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TO_ME = os.getenv("TO_ME")
HOME_BASE = os.getenv("HOME_BASE")
EMAIL = os.getenv("EMAIL")
EMAIL_PW = os.getenv("EMAIL_PW")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


class NotificationManager:

    def __init__(self):
        self.account_sid = ACCOUNT_SID
        self.auth_token = AUTH_TOKEN
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)
        self.text = None

    def create_message_from_flight(self, flight_data):

        departure_time = flight_data.departure_time.split("T")[0]
        return_time = flight_data.arrival_time.split("T")[0]

        self.text = f"""
            Get ready to pack! A flight from {HOME_BASE} to {flight_data.destination} ({flight_data.dest_code})
            was found!
            Departure: {departure_time}
            Return: {return_time}
            FOR JUST {flight_data.price} EUR!
            """

    def send_emails_to_users(self, users):

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=EMAIL_PW)
            for user in users:
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=user["email"],
                                    msg=f"""Flight Alarm!\n\n
                                        Hey {user['firstName']},\n
                                        {self.text}\n
                                        Don't miss your chance for an exciting getaway!\n\n
                                        Best, 
                                        Your flight management team!
                                        """)

    def send_message(self):
        if self.text is None:
            return
        message = client.messages.create(
            from_='+14788181280',
            to=TO_ME,
            body=self.text
        )
