from fastapi import FastAPI
from dto.article_dto import ArticleDTO
from service.article_service import ArticleService
from dto.query_dto import QueryDTO
app = FastAPI()
articleService = ArticleService()

@app.post("/search/")
async def search(query : QueryDTO):
    return articleService.search(query.query,query.minScore,query.top,query.tags)

@app.post("/article/")
async def encode(article: ArticleDTO):
    return articleService.saveArticleEmbedded(article.id,article.title,article.description)

@app.delete("/article/{id}")
async def delete(id: int):
    return articleService.delete(id)