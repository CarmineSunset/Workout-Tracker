import requests
from datetime import datetime as dt

APP_ID = "YOUR APP ID"
API_KEY = "YOUR KEY"
GENDER = "YOUR GENDER"
WEIGHT_KG = 0.0
HEIGHT_CM = 0
AGE = 0
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"

# Enter your exercise information
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, headers=headers, json=parameters)
exercise_data = response.json()
print(exercise_data)

# Save your data to Google Sheet via Sheety API

sheety_endpoint = f"https://api.sheety.co/YOUR DATA HERE"
current_time = dt.now()


request_body = {
    "workout": {
        "date": current_time.strftime("%d/%m/%Y"),
        "time": current_time.strftime("%H:%M:%S	"),
        "exercise": exercise_data['exercises'][0]['name'].title(),
        "duration": exercise_data['exercises'][0]['duration_min'],
        "calories": exercise_data['exercises'][0]['nf_calories']

    }
}

headers = {
    "Authorization": "YOUR AUTHORIZATION"
}

sheety_response = requests.post(sheety_endpoint, json=request_body, auth=(USERNAME, PASSWORD))
print(sheety_response)
