from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.utils.init_db import create_tables
from app.routes import auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth.router, tags=["auth"], prefix="/auth")

@app.get("/health")
def health_check():
    return {
        "status": "Running..."
    }