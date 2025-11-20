import requests
from twilio.rest import Client

account_sid = "AC6df10d0aab88daf6a09db83f673b5aca"
auth_token = "e5875f7a3da177dfe1a705cb84f0a8b0"

api_key = "48307c2945b23dfb2d5c82c1d768778e"
LAT = -33.924870
LONG = 18.424055

url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt": 3,
}
response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for forecast in weather_data["list"]:
    condition_code = int(forecast["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Bring an umbrella!',
        to='whatsapp:+4916093918341'
    )
    print(message.status)