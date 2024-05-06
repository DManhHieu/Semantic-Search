from fastapi import FastAPI, Depends
from routers import article_router
from dotenv import load_dotenv
from auth import checkAPIKey

load_dotenv()
app = FastAPI(
    title="Semantic search",
    description="Using SentenceTransformers and FastAPI for senmatic searching aricles(title and description)",
    version="1.0.0"
)

app.include_router(
    article_router.router,
    prefix="/api/v1",
    dependencies=[Depends(checkAPIKey)]
)