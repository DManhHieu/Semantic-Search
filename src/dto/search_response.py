from pydantic import BaseModel

class Score(BaseModel):
    score: float
    article_id: int

class SearchResponse(BaseModel):
    scores: list[Score]
    page: int
    size: int
    total: int