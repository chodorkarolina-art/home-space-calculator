import json
from pathlib import Path


DATA_FILE = (
    Path(__file__).resolve().parent
    / "data"
    / "room_details.json"
)

with open(DATA_FILE, encoding="utf-8") as file:
    ROOM_DETAILS = json.load(file)