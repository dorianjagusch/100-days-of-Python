from twilio.rest import Client
import dotenv
import os
import requests
import datetime as dt
import time

dotenv.load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TO_ME = os.getenv("TO_ME")
COMPANY_SHORT = "TLSA"
COMPANY = "Tesla"


def get_news(stock_change_percent):
    parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY,
    }
    response = requests.get("https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    news_data = response.json()["articles"]
    articles = news_data[:3]

    return articles


def send_sms(sms_content):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_='+14788181280',
        to=TO_ME,
        body=sms_content
    )


def check_stock():
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": COMPANY_SHORT,
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]

    flat_data = [value for (key, value) in data.items()]
    yesterday = float(flat_data[0]["4. close"])
    day_before_yesterday = float(flat_data[1]["4. close"])

    change = yesterday - day_before_yesterday
    change /= yesterday
    return change


def compose_sms(news_article, stock_change_percent):
    title = news_article["title"]
    brief = news_article["description"]
    symbol = "🔺" if stock_change_percent > 0 else "🔻"

    sms_content = f"""
                    {COMPANY_SHORT}: {symbol}{round(stock_change_percent * 100, 1)}%
                    Headline: {title}
                    Brief: {brief}
                    """
    return sms_content


def main():
    while True:
        stock_change = check_stock()
        if abs(stock_change) >= 0.1:
            articles = get_news(stock_change)
            for news in articles:
                sms_content = compose_sms(news, stock_change)
                send_sms(sms_content)

        time.sleep(3600)


if __name__ == "__main__":
    main()
