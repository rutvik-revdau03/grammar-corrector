from fastapi import FastAPI
from app.routes.grammar import router as grammar_router

app = FastAPI(
    title="Grammar Correction API",
    description="API for correcting grammar in text",
    version="1.0.0"
)

app.include_router(grammar_router, prefix="/api")
