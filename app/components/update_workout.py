import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

def update_workout(workout_id, updated_data):
    update_endpoint = f"{SHEET_ENDPOINT}/{workout_id}"
    response = requests.put(url=update_endpoint, json=updated_data)
    response.raise_for_status()
    return response.json()
