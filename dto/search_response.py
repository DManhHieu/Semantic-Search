from pydantic import BaseModel

class SearchResponse(BaseModel):
    score: float
    article_id: int