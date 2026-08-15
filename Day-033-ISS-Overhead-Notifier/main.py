import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
MY_EMAIL = "marina5@gmail.com"
MY_PASSWORD = "12345678"

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # #Your position is within +5 or -5 degrees of the ISS position.
    if float(MY_LAT - 5) <= iss_latitude <= float(MY_LAT + 5) and float(MY_LONG - 5) <= iss_longitude <= float(MY_LONG + 5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <=sunrise:
        return True
#If the ISS is close to my current position
# and it is currently dark

while True:
    time.sleep(60) # BONUS: run the code every 60 seconds.
    if is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            # Then send me an email to tell me to look up.
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="alisha@gmail.com",
                                msg="Subject:ISS Location near you!\n\nHurry and go outside to look up for the ISS tracker.")
    else:
        print("Sorry, itsn't the day for you spot the ISS.")




