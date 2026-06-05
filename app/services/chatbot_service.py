from app.services.intent_detector import detect_intent
from app.services.search_engine import search_faq

def generate_response(message: str):

    intent = detect_intent(message)

    faq, confidence = search_faq(message)

    return {
        "intent": intent,
        "confidence": confidence,
        "matched_question": faq["question"],
        "answer": faq["answer"]
    }