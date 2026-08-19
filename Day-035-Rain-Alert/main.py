import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")

trial_number = "+17372508034"

MY_LAT = 24.203589
MY_LONG = 82.666608

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)

response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="whatsapp:+17372508034",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:+91785643921",
        content_sid="HX25161c213d71bb75e073ead06f38fbbd",
    )

    print(message.sid)
    print(message.status)
