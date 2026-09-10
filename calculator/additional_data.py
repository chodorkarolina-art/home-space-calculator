import json
from pathlib import Path


DATA_FILE = (
    Path(__file__).resolve().parent
    / "data"
    / "additional_details.json"
)

with open(DATA_FILE, encoding="utf-8") as file:
    ADDITIONAL_DETAILS = json.load(file)