from twilio.rest import Client
import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_AC_SID = os.environ.get("TWILIO_AC_SID")
TWILIO_API_KEY = os.environ.get("TWILIO_API_KEY")
TWILIO_PHONE_NUM = os.environ.get("TWILIO_PHONE_NUM")
RECEIVER_PHONE_NUM = "some valid numbere"


alphavantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": ALPHAVANTAGE_API_KEY
}

response = requests.get("https://www.alphavantage.co/query", params = alphavantage_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

diff_percent = (float(stock_data_list[0]["1. open"]) - float(stock_data_list[1]["4. close"])) / float(stock_data_list[1]["4. close"]) * 100

if abs(diff_percent) > 5.0:
        
    newsapi_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "popularity",
        "pageSize": "3",
        "page": "1"
    }

    response = requests.get("https://newsapi.org/v2/everything", params = newsapi_params)
    response.raise_for_status()
    news_list = response.json()["articles"]
    message_body = f"""{STOCK}: {'🔺' if diff_percent > 0 else '🔻'}{diff_percent}% \
        Headline:{news_list[0]['title']}\n Brief:{news_list[0]['description']} \n\n \
        Headline:{news_list[1]['title']}\n Brief:{news_list[1]['description']} \n\n \
        Headline:{news_list[2]['title']}\n Brief:{news_list[2]['description']}"""


    client = Client(TWILIO_AC_SID, TWILIO_API_KEY)
    message =client.messages.create(
        body = message_body,
        from_ = TWILIO_PHONE_NUM,
        to = RECEIVER_PHONE_NUM
    )
    print(message.status)
