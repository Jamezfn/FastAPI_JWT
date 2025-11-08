from fastapi import FastAPI

from routers import auth
from dB.base import Base
from dB.session import engine
import models

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
