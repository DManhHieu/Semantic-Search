from fastapi import FastAPI
from model.article_model import ArticleModel
from service.article_service import ArticleService
app = FastAPI()
articleService = ArticleService()

@app.get("/search/")
async def search(query: str, top: int, minScore: float, tags: list):
    return articleService.search(query,minScore,top,tags)

@app.post("/article/")
async def encode(article: ArticleModel):
    return articleService.saveArticleEmbbed(article)

@app.delete("/article/{id}")
async def delete(id: int):
    return articleService.delete(id)