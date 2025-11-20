import requests
import pandas as pd
from twilio.rest import Client
from newsapi import NewsApiClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = "AC6df10d0aab88daf6a09db83f673b5aca"
auth_token = "e5875f7a3da177dfe1a705cb84f0a8b0"

url = "https://www.alphavantage.co/query"
api_key = "6UF8EE3YNCG8NPDW"
time = "60min"
pre_function = "TIME_SERIES_INTRADAY"

parameters = {
    "apikey": api_key,
    "function": pre_function,
    "symbol": STOCK,
    "interval": time
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_data = requests.get(url=url, params=parameters)
data = stock_data.json()

yesterday = float(data["Time Series (60min)"]["2025-05-09 19:00:00"]["4. close"])
day_before_yesterday = float(data["Time Series (60min)"]["2025-05-08 19:00:00"]["4. close"])
increase = day_before_yesterday*1.05
decrease = day_before_yesterday*0.95

#if yesterday >= increase or yesterday <= decrease:
    #print("Get News")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

url2 = " https://newsapi.org/v2/top-headlines"
api_key2 = "82806c881041412d8b5ff73bc7d3f71e"
q = "Tesla"
news_date = "2025-05-01"

parameters2 = {
    "q": q,
    "from": news_date,
    "sortBy": "popularity",
    "apiKey": api_key2
}

news_data = requests.get(url=url2, params=parameters2)
news_json = news_data.json()
real_news = []
real_news.append(news_json["articles"][:3])

if yesterday >= increase or yesterday <= decrease:
    pass
    #print(real_news[0][0]["content"])
    #print(real_news[0][1]["content"])
    #print(real_news[0][2]["content"])

message1 = real_news[0][0]["title"]
message2 = real_news[0][1]["title"]
message3 = real_news[0][2]["title"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
if yesterday >= increase or yesterday <= decrease:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'{message1} / {message2} / {message3}',
        to='whatsapp:+4916093918341'
    )
    print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""