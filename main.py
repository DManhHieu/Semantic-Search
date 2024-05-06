from fastapi import FastAPI
from model.article_model import ArticleModel
from service.article_service import ArticleService

app = FastAPI()
articleService = ArticleService()

@app.get("/search/")
async def search(query: str, top: int = 10, minScore: float = 0.2):
    return articleService.search(query,minScore,top)

@app.post("/article/")
async def encode(article: ArticleModel):
    return articleService.saveArticleEmbedded(article)

@app.delete("/article/{id}")
async def delete(id: int):
    return articleService.delete(id)