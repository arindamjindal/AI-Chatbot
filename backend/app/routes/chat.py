from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.openai_service import get_ai_response

router = APIRouter()

chat_history = []

@router.post("/")
def chat(req : ChatRequest):
    chat_history.append({"role": "user", "content": req.message})
    reply = get_ai_response(chat_history)
    chat_history.append({"role":"assistant", "content": reply})
    return {"response":reply}
