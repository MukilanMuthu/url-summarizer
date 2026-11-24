import httpx
from dotenv import load_dotenv
from fastapi import FastAPI
from openai import OpenAI

from app.models import Url

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/summarize")
def summarizer(url: Url):
    load_dotenv()
    result = httpx.get(url.url, follow_redirects=True)
    client = OpenAI()
    response = client.responses.create(
        model="gpt-6-luna",
        input=f"Give me the summary of this html content: {result.text}"
    )

    return {"URL": url.url,
        "Status code": result.status_code,
            "summary": response.output_text}
