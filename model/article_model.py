from pydantic import BaseModel


class ArticleModel(BaseModel):
    id: int
    title: str 
    description: str 