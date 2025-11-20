import requests

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 86
HEIGHT_CM = 1.78
AGE = 21

APP_ID = "56a37b86"
API_KEY = "1992b920da0b68d7adde67859e80c5c3"

exercise_text = input("Tell me which exercise you did today?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=url, json=parameters, headers=headers)
result = response.json()
print(result)