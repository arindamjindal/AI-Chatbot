from fastapi import FastAPI
from app.routes import chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(chat.router, prefix="/chat")

@app.get("/")
def home():
    return {"message": "AI Chatbot API is running"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)