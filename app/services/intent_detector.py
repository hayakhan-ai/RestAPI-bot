import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
synonyms_path = BASE_DIR / "data" / "synonyms.json"

with open(synonyms_path, "r", encoding="utf-8") as f:
    SYNONYMS = json.load(f)

def detect_intent(message: str):
    message = message.lower()

    for intent, keywords in SYNONYMS.items():
        for keyword in keywords:
            if keyword in message:
                return intent

    return "unknown"