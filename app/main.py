from fastapi import FastAPI
from app.api.routes.chatbot import router as chatbot_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered Medical Chatbot for healthcare assistance and information retrieval.",
)

app.include_router(chatbot_router)

@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "Medical Chatbot API is running successfully",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "health_check": "/health",
        "chat_endpoint": "/chatbot/chat"
    }