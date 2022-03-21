APP_ID = ""
API_KEY = ""


# Link sheet: https://docs.google.com/spreadsheets/d/1n6wGV6BPqYVhYI0iEVhZ5Y1Gf_1HamJFkpyEJXjp-70/edit#gid=0
import  requests
import os
from datetime import datetime
from dotenv import load_dotenv


load_dotenv("enviromentVariables.env")
APP_ID = os.getenv("My_app_id")
API_KEY = os.getenv("My_api_key")
bearer_code = os.getenv("My_bearer")


headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
     "gender":"male",
     "weight_kg":67,
     "height_cm":171,
     "age":30
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


sheet_endpoint = "https://api.sheety.co/1ef836ca0872f86094ed865f1b74c9c9/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


exercise = result['exercises'][0]['name']
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']

sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise":  exercise.title(),
            "duration": duration,
            "calories": calories
        }
    }

headers = {
    "Authorization" : f"Bearer {bearer_code}",
    "Content-Type": "application/json"
}

sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=headers)

print(sheet_response.text)