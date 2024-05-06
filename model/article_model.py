from pydantic import BaseModel


class ArticleModel(BaseModel):
    id: int
    title: str | None = None
    description: str | None = None