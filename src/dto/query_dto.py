from pydantic import BaseModel


class QueryDTO(BaseModel):
    query: str
    minScore: float = 0.2
    tags: list = None
    page: int = 0
    size: int = 10