
from fastapi import APIRouter

router = APIRouter(prefix="/chat")

@router.post("/")
def chat():
    return {"response": "Standard response (upgrade for high-level reasoning)"}
