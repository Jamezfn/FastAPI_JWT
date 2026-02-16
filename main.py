from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager

from app.utils.init_db import create_tables
from app.routes import auth
from app.utils.protectRoute import get_current_user
from app.db.schema.user import UserOutput

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

@app.get("/protected")
def read_protected(user: UserOutput = Depends(get_current_user)):
    return {
        "data": user
    }