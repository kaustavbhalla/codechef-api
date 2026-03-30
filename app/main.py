from fastapi import FastAPI
from app.routers import users

app = FastAPI(
    title="CodeChef API",
    description="An unofficial REST API for CodeChef, built by scraping the website.",
    version="1.0.0",
)

app.include_router(users.router, prefix="/api/v1", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "CodeChef API is running. Visit /docs for the full API reference."}
