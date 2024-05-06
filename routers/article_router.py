from dto.article_dto import ArticleDTO
from dto.query_dto import QueryDTO
from service.article_service import ArticleService
from fastapi import APIRouter
from dto.search_response import SearchResponse
articleService = ArticleService()

router = APIRouter()

@router.post("/article/search/", response_model=list[SearchResponse])
async def search(query : QueryDTO):
    return articleService.search(query.query,query.minScore,query.top,query.tags)

@router.post("/article/")
async def encode(article: ArticleDTO):
    return articleService.saveArticleEmbedded(article.id,article.title,article.description)

@router.delete("/article/{id}")
async def delete(id: int):
    articleService.delete(id)