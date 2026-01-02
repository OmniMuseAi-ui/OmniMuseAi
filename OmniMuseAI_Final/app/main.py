
from fastapi import FastAPI

app = FastAPI(title="OmniMuseAI")

@app.get("/")
def root():
    return {"status": "OmniMuseAI backend running"}
