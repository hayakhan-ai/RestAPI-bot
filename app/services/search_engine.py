import json
from pathlib import Path
from rapidfuzz import fuzz

BASE_DIR = Path(__file__).resolve().parent.parent
faq_path = BASE_DIR / "data" / "faq_dataset.json"

with open(faq_path, "r", encoding="utf-8") as f:
    FAQS = json.load(f)


def search_faq(user_query: str):

    best_match = None
    best_score = 0

    for faq in FAQS:

        score = fuzz.token_sort_ratio(
            user_query.lower(),
            faq["question"].lower()
        )

        if score > best_score:
            best_score = score
            best_match = faq

    confidence = round(best_score / 100, 2)

    return best_match, confidence