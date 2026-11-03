import os
from dotenv import load_dotenv
from datetime import datetime
import requests

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
WEIGHT = 55
HEIGHT = 160.02
AGE = 21
GENDER = "female"
TOKEN = os.getenv("TOKEN")

print(APP_ID)
print(API_KEY)
print(TOKEN)

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = "https://api.sheety.co/d7464e5dd98a954a5043e258665b9ff2/workoutTracking/workouts"

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Get exercise information
exercise_params = {
    "query": input("Tell me which exercise you did: "),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER
}

response = requests.post(
    url=exercise_endpoint,
    json=exercise_params,
    headers=headers
)

result = response.json()

# Get current date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Send each exercise to Google Sheets through Sheety
for exercise in result["exercises"]:

    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=sheety_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
