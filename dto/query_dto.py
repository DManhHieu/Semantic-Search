from pydantic import BaseModel


class QueryDTO(BaseModel):
    query: str
    top: int = 10
    minScore: float = 0.2
    tags: list = None