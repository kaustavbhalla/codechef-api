from fastapi import FastAPI
from app.routers import users
from app.routers import contests

app = FastAPI(
    title="CodeChef API",
    description="An unofficial REST API for CodeChef, built by scraping the website.",
    version="1.0.0",
)

app.include_router(users.router, prefix="/api/v1", tags=["Users"])
app.include_router(contests.router, prefix="/api/v1/contests", tags=["Contests"])

@app.get("/")
async def root():
    return {"message": "CodeChef API is running. Visit /docs for the full API reference."}
