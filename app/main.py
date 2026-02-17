from fastapi import FastAPI
from random import choice

from .models import Quote, QuoteList
from .quotes import QUOTES

app = FastAPI(
    title="Random Quote API ✨",
    description="Free REST API for random motivational & programming quotes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/")
def root():
    return {"message": "Welcome to Random Quote API ✨", "docs": "/docs"}

@app.get("/quote", response_model=Quote)
def get_random_quote():
    if not QUOTES:
        return {"error": "No quotes available"}
    return choice(QUOTES)

@app.get("/quote/{count}", response_model=QuoteList)
def get_multiple_quotes(count: int = 1):
    count = max(1, min(count, 20))
    selected = [choice(QUOTES) for _ in range(count)]
    return {"quotes": selected, "count": len(selected)}