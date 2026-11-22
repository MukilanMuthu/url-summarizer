import httpx
from fastapi import FastAPI

from app.models import Url

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/summarize")
def summarizer(url: Url):
    result = httpx.get(url.url, follow_redirects=True)
    return {"html": result.text[:500],
        "status_code": result.status_code}
