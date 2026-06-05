from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chatbot_service import generate_response

router = APIRouter(
    prefix="/chatbot",
    tags=["Chatbot"]
)

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return generate_response(request.message)