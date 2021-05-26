import requests
import os
import datetime

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")

pixela_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post("https://pixe.la/v1/users", json = pixela_params)
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Korean Learning",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json = graph_config, headers = headers)
# print(response.text)

today = datetime.datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": str(input("How many hours did you learn the lesson for today?: "))
}

response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1", json = pixel_data, headers = headers)
print(response.text)

# pixel_update = {
#     "quantity": 3
# }

# update_date = datetime.datetime(year = 2020, month = 7, day = 26).strftime("%Y%m%d")
# response = requests.put(f"{graph_endpoint}/graph1/{update_date}", json = pixel_data, headers = headers)