import requests
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "KEY"
AC_SID = "ID"
AUTH_TOKEN = "TOKEN"

def send_sms():
    client = Client(AC_SID, AUTH_TOKEN)
    message = client.messages.create(
        body = "It's going to rain today. Carry an umbrella!",
        from_ = "free number",
        to = "your number"
    )
    print(message.status)

params = {"lat": "99.6969", "lon": "69.9696", "appid": API_KEY, "exclude": "current,minutely,daily"}

response = requests.get(ENDPOINT, params = params)
response.raise_for_status()
hourly_weather = response.json()["hourly"][:12]

for _ in range(len(hourly_weather)) :
    if hourly_weather[_]["weather"][0]["id"] < 700:
        send_sms()
        break
        