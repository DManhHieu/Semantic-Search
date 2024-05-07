from pydantic import BaseModel


class ArticleDTO(BaseModel):
    id: int
    title: str 
    description: str 
    tags: list = None