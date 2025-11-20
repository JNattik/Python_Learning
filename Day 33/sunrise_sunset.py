import requests, datetime as dt

LAT = 49.487457
LONG = 8.466040

parameters = {
    "lat": LAT,
    "lng": LONG,
}

response = requests.get("https://api.sunrise-sunset.org/json?lat=49.487457&lng=8.466040", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunrise = data["results"]["sunset"]

time_now = dt.datetime.now()