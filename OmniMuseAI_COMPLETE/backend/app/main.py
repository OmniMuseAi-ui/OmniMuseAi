
from fastapi import FastAPI
from app.routers import auth, chat

app = FastAPI(title="OmniMuseAI")

app.include_router(auth.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"status": "OmniMuseAI running"}
