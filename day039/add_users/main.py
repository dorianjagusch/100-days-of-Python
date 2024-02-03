import dotenv,os
import requests

dotenv.load_dotenv()
FLIGHT_SHEET_ENDPOINT = os.getenv('FLIGHT_SHEET_ENDPOINT')
FLIGHT_SHEET_TOKEN = os.getenv('FLIGHT_SHEET_TOKEN')

headers = {
    "Authorization": FLIGHT_SHEET_TOKEN,
}


def add_user():

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email address: ")
    conf_email = input("Repeat email address: ")

    if email != conf_email:
        print("Email addresses do not match. Reenter your your data.")
        return

    user_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(f"{FLIGHT_SHEET_ENDPOINT}/users",
                             json=user_data,
                             headers=headers)
    response.raise_for_status()
    print(f"{first_name} {last_name} was added to the database.")


if __name__ == "__main__":
    print("Welcome to my flight database! So, you want deals deals deals?\nThen:")
    user_input = "join"
    while user_input == "join":
        add_user()
        user_input = ""
        while user_input not in ["q", "quit", "join"]:
            user_input = input("What do you want to do next? ('q' or 'quit' to quit/ 'join' to add user): ")


