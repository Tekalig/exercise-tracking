import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

def delete_workout(workout_id):
    delete_endpoint = f"{SHEET_ENDPOINT}/{workout_id}"
    response = requests.delete(url=delete_endpoint)
    response.raise_for_status()
    return response.json()
