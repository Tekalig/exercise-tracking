import requests
from datetime import datetime

NLE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/daff83fbc6d259b51fe1d8967832a618/exerciseTracking/workout"
headers = {
    "x-app-id": "b3a4e181",
    "x-app-key": "00d72269bd5b1d1c1a39c4eaced5ffaa",
}

nle_pram = {"query": input("Tell me what exercise you do: ")}

response = requests.post(url=NLE_ENDPOINT, json=nle_pram, headers=headers)
response.raise_for_status()
data = response.json()["exercises"]
now = datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M:%S")
for exe in data:
    user_data = {"workout": {"date": date, "time": time, "exercise": exe["name"], "duration": exe["duration_min"],
                             "calories": exe["nf_calories"]}}

    response = requests.post(url=SHEET_ENDPOINT, json=user_data)
    response.raise_for_status()
    print(response.json()["workout"])

