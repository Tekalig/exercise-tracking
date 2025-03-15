import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

NLE_ENDPOINT = os.getenv("NLE_ENDPOINT")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
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

