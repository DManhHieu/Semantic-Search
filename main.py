from fastapi import FastAPI
import os
from model.article_model import ArticleModel
from service.article_service import ArticleService
from sentence_transformers import SentenceTransformer
app = FastAPI()
from dotenv import load_dotenv

load_dotenv()
model_name = os.getenv('SENTENCE_MODEL_NAME')
sentenceModel = SentenceTransformer(model_name)

articleService = ArticleService(sentenceModel)

@app.get("/search/")
async def search(query: str, top: int = 10, minScore: float = 0.2, tags: list = None):
    return articleService.search(query,minScore,top,tags)

@app.post("/article/")
async def encode(article: ArticleModel):
    return articleService.saveArticleEmbbed(article)

@app.delete("/article/{id}")
async def delete(id: int):
    return articleService.delete(id)