import os
import httpx
from dotenv import load_dotenv

load_dotenv()

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

async def get_workout():
    async with httpx.AsyncClient() as client:
        response = await client.get(url=SHEET_ENDPOINT)
        response.raise_for_status()
        data = response.json()
    return data.get("workout", [])
