import requests
import dotenv
import os
import datetime as dt

dotenv.load_dotenv()

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
USER_NAME = "dorianinfinland4"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# user_parameters = {
#     "token": PIXELA_TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Coughing graph",
#     "unit": "times",
#     "type": "int",
#     "color": "ajisai",
# }

#headers = {
#    "X-USER-TOKEN": PIXELA_TOKEN
#}

#response = requests.post(graph_endpoint, json=graph_config, headers=headers)
#print(response.text)


date_of_interest = dt.datetime(day=25, month=1, year=2024).strftime("%Y%m%d")

post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date_of_interest}"

data_entry = {
    "quantity": "1057",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.delete(post_pixel_endpoint, headers=headers)
print(response.text)
