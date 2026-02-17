from pydantic import BaseModel
from typing import Optional, List

class Quote(BaseModel):
    quote: str
    author: Optional[str] = "Anonymous"
    category: Optional[str] = "General"

class QuoteList(BaseModel):
    quotes: List[Quote]
    count: int